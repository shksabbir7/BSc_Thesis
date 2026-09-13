#!/usr/bin/env python3
"""Select qualitative example outputs for Chapter 6 by a registered rule.

An error analysis that quotes hand-picked outputs is an advertisement, not
evidence: the reader cannot tell whether the example was typical or whether it
was the fifth one looked at. This script therefore fixes the strata and the
tie-break in a config, applies them to the sealed 5,400-case surface, and
reports each selected case beside the size of the stratum it came from, so the
example arrives with its own representativeness attached.

It reads the frozen archive and the frozen score file. It generates nothing,
rescores nothing, and defines no new evaluation metric.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.common.provenance import write_result
from src.common.seed import set_seed
from src.eval.s5_contract import CONDITIONS, REPLICATE_SEEDS

EXPECTED_CASES = 90 * 2 * len(REPLICATE_SEEDS) * len(CONDITIONS)


class ErrorExampleError(RuntimeError):
    pass


def load_jsonl(path: Path, label: str) -> dict[str, dict]:
    rows: dict[str, dict] = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        key = row.get("key")
        if not key:
            raise ErrorExampleError(f"{label}: missing key at line {line_number}")
        if key in rows:
            raise ErrorExampleError(f"{label}: duplicate key {key} at line {line_number}")
        rows[key] = row
    if len(rows) != EXPECTED_CASES:
        raise ErrorExampleError(
            f"{label}: expected the frozen {EXPECTED_CASES}-case surface, got {len(rows)}"
        )
    return rows


#: Fields the emitted record carries only for the conditions that ran a loop or a
#: selector. Reported when present because they show *why* the emitted attempt
#: was the one emitted; absent for the five single-pass conditions.
LOOP_FIELDS = (
    "attempt", "index", "verdict", "gate", "gate_score",
    "neural_score", "symbolic_score", "feedback",
)


def emitted_generation(emitted: dict, key: str) -> tuple[dict, dict]:
    """Return (generation_record, loop_metadata) for any of the four shapes.

    The archive stores `emitted` four different ways: the five single-pass
    conditions inline the generation, while the three gated loops, the hosted
    judge loop and blind resampling wrap it under `generation` and add the
    bookkeeping that decided which attempt survived. Reading only the inline
    shape silently drops half the surface, so both are resolved here.
    """
    if "text" in emitted:
        generation = emitted
    elif isinstance(emitted.get("generation"), dict) and "text" in emitted["generation"]:
        generation = emitted["generation"]
    else:
        raise ErrorExampleError(f"{key}: emitted record carries no generated text")
    metadata = {field: emitted[field] for field in LOOP_FIELDS if field in emitted}
    return generation, metadata


def join(cases: dict[str, dict], scores: dict[str, dict]) -> dict[str, dict]:
    if set(cases) != set(scores):
        raise ErrorExampleError("case archive and score file do not cover the same keys")
    joined = {}
    for key, case in cases.items():
        score = scores[key]
        for field in ("plot_id", "condition", "target_level", "replicate_seed"):
            if str(case[field]) != str(score[field]):
                raise ErrorExampleError(f"{key}: {field} disagrees between archive and scores")
        emitted, loop_metadata = emitted_generation(case["result"]["emitted"], key)
        joined[key] = {
            "key": key,
            "plot_id": case["plot_id"],
            "condition": case["condition"],
            "target_level": int(case["target_level"]),
            "replicate_seed": int(case["replicate_seed"]),
            "text": emitted["text"],
            "finish_reason": emitted.get("finish_reason"),
            "completion_tokens": (emitted.get("usage") or {}).get("completion_tokens"),
            "emitted_selection_metadata": loop_metadata,
            "verifier_b_target_probability": float(score["verifier_b_target_probability"]),
            "verifier_b_binary_success": int(score["verifier_b_binary_success"]),
            "verifier_a_target_probability": (
                None if score.get("verifier_a_target_probability") is None
                else float(score["verifier_a_target_probability"])
            ),
            "gave_up": bool(score["gave_up"]),
            "logical_generator_calls": int(score["logical_generator_calls"]),
            "attempt_scores": score.get("attempt_scores", []),
        }
    return joined


def word_count(text: str) -> int:
    return len(text.split())


def report_case(record: dict) -> dict:
    keep = (
        "key", "plot_id", "condition", "target_level", "replicate_seed", "text",
        "finish_reason", "completion_tokens", "verifier_b_target_probability",
        "verifier_b_binary_success", "verifier_a_target_probability", "gave_up",
        "logical_generator_calls", "attempt_scores",
    )
    out = {field: record[field] for field in keep}
    out["word_count"] = word_count(record["text"])
    return out


def select_single(records: list[dict], stratum: dict, seed: int) -> dict:
    condition = stratum["condition"]
    if condition not in CONDITIONS:
        raise ErrorExampleError(f"{stratum['id']}: {condition} is not a frozen condition")
    pool = [
        r for r in records
        if r["condition"] == condition
        and r["replicate_seed"] == seed
        and r["target_level"] == int(stratum["target_level"])
        and r["verifier_b_binary_success"] == int(stratum["binary_success"])
        and (("gave_up" not in stratum) or r["gave_up"] is bool(stratum["gave_up"]))
    ]
    if not pool:
        raise ErrorExampleError(f"{stratum['id']}: stratum is empty, no example can be selected")
    pool.sort(key=lambda r: r["key"])
    return {
        "id": stratum["id"],
        "kind": "single_condition",
        "description": stratum["description"].strip(),
        "stratum_size": len(pool),
        "stratum_denominator": 90,
        "selected": report_case(pool[0]),
    }


def select_repair(records: list[dict], stratum: dict, seed: int) -> dict:
    treatment, comparator = stratum["treatment"], stratum["comparator"]
    if treatment not in CONDITIONS or comparator not in CONDITIONS or treatment == comparator:
        raise ErrorExampleError(f"{stratum['id']}: strata must name two distinct frozen conditions")
    level = int(stratum["target_level"])
    indexed = {r["key"]: r for r in records}
    pool = []
    for record in records:
        if (record["condition"] != treatment or record["replicate_seed"] != seed
                or record["target_level"] != level
                or record["verifier_b_binary_success"] != 1):
            continue
        comparator_key = record["key"].rsplit("|", 1)[0] + "|" + comparator
        other = indexed.get(comparator_key)
        if other is None:
            raise ErrorExampleError(f"{record['key']}: comparator case is missing")
        if other["verifier_b_binary_success"] == 0:
            pool.append((record, other))
    if not pool:
        raise ErrorExampleError(f"{stratum['id']}: no discordant pair in the requested direction")
    pool.sort(key=lambda pair: pair[0]["key"])
    treatment_case, comparator_case = pool[0]
    return {
        "id": stratum["id"],
        "kind": "repair_pair",
        "description": stratum["description"].strip(),
        "stratum_size": len(pool),
        "stratum_denominator": 90,
        "selected": report_case(treatment_case),
        "comparator": report_case(comparator_case),
    }


def give_up_census(records: list[dict], seed: int) -> dict:
    """How often each loop condition exhausted its attempt budget.

    Reported so that E6 is read as an instance of a counted event rather than as
    an isolated anecdote. Counts only; no rate is compared across conditions.
    """
    census: dict[str, dict[str, int]] = {}
    for condition in CONDITIONS:
        for level in (0, 1):
            pool = [
                r for r in records
                if r["condition"] == condition and r["replicate_seed"] == seed
                and r["target_level"] == level
            ]
            gave_up = sum(1 for r in pool if r["gave_up"])
            if gave_up:
                census.setdefault(condition, {})[f"L{level}"] = gave_up
    return census


def main() -> int:
    set_seed()
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/s5_error_examples_bn.yaml")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = root / config_path
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))

    cases_path = root / config["input"]["cases_jsonl"]
    scores_path = root / config["input"]["scores_jsonl"]
    output_path = root / config["output"]["result_json"]
    seed = int(config["selection"]["replicate_seed"])
    if seed not in REPLICATE_SEEDS:
        raise ErrorExampleError(f"{seed} is not one of the frozen replicates {REPLICATE_SEEDS}")

    joined = join(
        load_jsonl(cases_path, "cases"),
        load_jsonl(scores_path, "scores"),
    )
    records = list(joined.values())

    examples = []
    for stratum in config["selection"]["strata"]:
        kind = stratum["kind"]
        if kind == "single_condition":
            examples.append(select_single(records, stratum, seed))
        elif kind == "repair_pair":
            examples.append(select_repair(records, stratum, seed))
        else:
            raise ErrorExampleError(f"{stratum['id']}: unknown stratum kind {kind}")

    result = {
        "status": "EXAMPLES_SELECTED",
        "scientific_standing": (
            "illustrative_only_selected_by_registered_rule; stratum sizes are counts over "
            "the frozen surface and are not a new evaluation metric"
        ),
        "selection_rule": (
            "Fix replicate seed 42, filter to the stratum stated in the config, order by case "
            "key and take the first. No text was read before the strata were registered."
        ),
        "interpretation_rule": (
            "Each example illustrates a failure mode whose frequency is given by its stratum "
            "size out of 90 evaluation plots at that condition and level. Verifier-B is the "
            "registered outcome measure, not ground truth, so a case it marks as failing is "
            "evidence about the measured outcome and not proof that a human would agree."
        ),
        "replicate_seed": seed,
        "tie_break": config["selection"]["tie_break"],
        "examples": examples,
        "give_up_census_seed42_counts_out_of_90": give_up_census(records, seed),
        "input": {
            "cases_path": str(cases_path.relative_to(root)).replace("\\", "/"),
            "cases_sha256": hashlib.sha256(cases_path.read_bytes()).hexdigest(),
            "scores_path": str(scores_path.relative_to(root)).replace("\\", "/"),
            "scores_sha256": hashlib.sha256(scores_path.read_bytes()).hexdigest(),
            "n_frozen_cases": len(records),
            "generation_rerun": False,
            "verifier_b_rescoring": False,
        },
    }
    write_result(result, output_path, str(config_path.relative_to(root)).replace("\\", "/"))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
