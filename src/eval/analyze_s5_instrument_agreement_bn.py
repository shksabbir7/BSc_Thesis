#!/usr/bin/env python3
"""Do the two level-measuring instruments disagree, and does the disagreement
have a level structure?

The main table reports a large asymmetry: every condition scores far lower when
Level 0 is requested than when Level 1 is. That asymmetry is measured entirely
by Verifier-B. The blinded human panel scored a balanced subset of the same
frozen outputs, so for exactly those items two independent instruments answered
the same question, and their disagreement can be read directly instead of
hypothesised.

This is a descriptive, post-hoc comparison. It was written after the registered
nine condition-versus-zero-shot comparisons were known, and it exists because a
thesis audit asked for an explanation of the asymmetry rather than a restatement
of it. It therefore carries the same standing as the other post-hoc contrast in
this repository: reportable, not confirmatory, and never a ranking.

Two things it deliberately does not do. It does not break the comparison down by
condition, because five items per condition-by-level cell cannot support that and
the human study already declined to interpret cells separately. And it does not
treat either instrument as ground truth: the finding is a disagreement, and which
instrument is closer to the construct is a separate question that neither this
analysis nor the frozen data can settle.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.common.provenance import write_result
from src.common.seed import set_seed
from src.eval.analyze_s5_bn import mcnemar_exact
from src.eval.s5_contract import CONDITIONS, REPLICATE_SEEDS

EXPECTED_SCORES = 90 * 2 * len(REPLICATE_SEEDS) * len(CONDITIONS)
EXPECTED_ITEMS = 100
EXPECTED_ANNOTATORS = 3


class InstrumentAgreementError(RuntimeError):
    pass


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def load_scores(path: Path) -> dict[str, dict]:
    rows: dict[str, dict] = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = json.loads(line)
        key = row.get("key")
        if not key or key in rows:
            raise InstrumentAgreementError(f"missing/duplicate key at line {line_number}")
        rows[key] = row
    if len(rows) != EXPECTED_SCORES:
        raise InstrumentAgreementError(
            f"expected the frozen {EXPECTED_SCORES}-score surface, got {len(rows)}"
        )
    return rows


def load_items(key_path: Path, response_path: Path) -> list[dict]:
    """Join the unblinding key to the human judgments, one record per item."""
    key_rows = read_csv(key_path)
    if len(key_rows) != EXPECTED_ITEMS:
        raise InstrumentAgreementError(f"expected {EXPECTED_ITEMS} items, got {len(key_rows)}")
    by_item = {row["item_id"]: row for row in key_rows}
    if len(by_item) != EXPECTED_ITEMS:
        raise InstrumentAgreementError("duplicate item_id in the researcher key")

    judgments: dict[str, list[int]] = {}
    for row in read_csv(response_path):
        item = row["item_id"]
        if item not in by_item:
            raise InstrumentAgreementError(f"judgment references unknown item {item}")
        judgments.setdefault(item, []).append(int(row["response"]))

    items = []
    for item_id, key_row in sorted(by_item.items()):
        responses = judgments.get(item_id, [])
        if len(responses) != EXPECTED_ANNOTATORS:
            raise InstrumentAgreementError(
                f"{item_id}: expected {EXPECTED_ANNOTATORS} judgments, got {len(responses)}"
            )
        counts = Counter(responses)
        # Three annotators and a binary response, so a majority always exists.
        majority, votes = counts.most_common(1)[0]
        items.append({
            "item_id": item_id,
            "case_key": key_row["case_key"],
            "condition": key_row["condition"],
            "target_level": int(key_row["target_level"]),
            "replicate_seed": int(key_row["replicate_seed"]),
            "human_responses": responses,
            "human_majority_label": int(majority),
            "human_majority_votes": int(votes),
            "human_unanimous": votes == EXPECTED_ANNOTATORS,
        })
    return items


def attach_verifiers(items: list[dict], scores: dict[str, dict], b_cut: float,
                     a_cut: float) -> None:
    for item in items:
        score = scores.get(item["case_key"])
        if score is None:
            raise InstrumentAgreementError(f"{item['item_id']}: case key absent from the score file")
        if int(score["target_level"]) != item["target_level"]:
            raise InstrumentAgreementError(f"{item['item_id']}: target level disagrees with the key")
        if score["condition"] != item["condition"]:
            raise InstrumentAgreementError(f"{item['item_id']}: condition disagrees with the key")
        target = item["target_level"]
        p_b = float(score["verifier_b_target_probability"])
        p_a = float(score["verifier_a_target_probability"])
        # A probability is for the TARGET level, so the predicted label is the
        # target when the probability clears the cut and the other level when it
        # does not. Recovering the label this way keeps the comparison on labels
        # rather than on two differently-scaled probabilities.
        item["verifier_b_label"] = target if p_b >= b_cut else 1 - target
        item["verifier_a_label"] = target if p_a >= a_cut else 1 - target
        item["verifier_b_target_probability"] = p_b
        item["verifier_a_target_probability"] = p_a
        # Cross-check against the registered binary column rather than trusting
        # the re-derivation: a silent threshold drift would otherwise be invisible.
        registered = int(score["verifier_b_binary_success"])
        if int(item["verifier_b_label"] == target) != registered:
            raise InstrumentAgreementError(
                f"{item['item_id']}: re-derived Verifier-B decision disagrees with the "
                f"registered verifier_b_binary_success column"
            )


def cohen_kappa(a: list[int], b: list[int]) -> float:
    n = len(a)
    observed = sum(1 for x, y in zip(a, b) if x == y) / n
    expected = sum(
        (sum(1 for x in a if x == label) / n) * (sum(1 for y in b if y == label) / n)
        for label in (0, 1)
    )
    if expected == 1.0:
        return float("nan")
    return (observed - expected) / (1.0 - expected)


def summarize(items: list[dict]) -> dict:
    n = len(items)
    human_right = [int(i["human_majority_label"] == i["target_level"]) for i in items]
    b_right = [int(i["verifier_b_label"] == i["target_level"]) for i in items]
    a_right = [int(i["verifier_a_label"] == i["target_level"]) for i in items]
    human_only = sum(1 for h, b in zip(human_right, b_right) if h == 1 and b == 0)
    b_only = sum(1 for h, b in zip(human_right, b_right) if h == 0 and b == 1)
    return {
        "n_items": n,
        "n_judgments": n * EXPECTED_ANNOTATORS,
        "human_majority_target_match": sum(human_right) / n,
        "verifier_b_target_match_same_items": sum(b_right) / n,
        "verifier_a_target_match_same_items": sum(a_right) / n,
        "human_minus_verifier_b": (sum(human_right) - sum(b_right)) / n,
        "both_correct": sum(1 for h, b in zip(human_right, b_right) if h == 1 and b == 1),
        "human_only_correct": human_only,
        "verifier_b_only_correct": b_only,
        "both_incorrect": sum(1 for h, b in zip(human_right, b_right) if h == 0 and b == 0),
        "descriptive_unadjusted_mcnemar_p": mcnemar_exact(human_only, b_only),
        "human_vs_verifier_b_label_agreement": sum(
            1 for i in items if i["human_majority_label"] == i["verifier_b_label"]
        ) / n,
        "human_vs_verifier_b_cohen_kappa": cohen_kappa(
            [i["human_majority_label"] for i in items],
            [i["verifier_b_label"] for i in items],
        ),
        "n_human_unanimous": sum(1 for i in items if i["human_unanimous"]),
    }


def main() -> int:
    set_seed()
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/s5_instrument_agreement_bn.yaml")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = root / config_path
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))

    score_path = root / config["input"]["verifier_b_scores_jsonl"]
    response_path = root / config["input"]["human_responses_csv"]
    key_path = root / config["input"]["researcher_key_csv"]
    output_path = root / config["output"]["result_json"]
    b_cut = float(config["instruments"]["verifier_b_threshold"])
    a_cut = float(config["instruments"]["verifier_a_threshold"])

    scores = load_scores(score_path)
    items = load_items(key_path, response_path)
    attach_verifiers(items, scores, b_cut, a_cut)

    cells = Counter((i["condition"], i["target_level"]) for i in items)
    if set(cells) != {(c, l) for c in CONDITIONS for l in (0, 1)} or set(cells.values()) != {5}:
        raise InstrumentAgreementError("the human subset is not the registered balanced 5-per-cell subset")

    result = {
        "status": "INSTRUMENT_DIVERGENCE_MEASURED",
        "scientific_standing": config["analysis"]["standing"],
        "selection_disclosure": (
            "This comparison was added after the registered nine condition-versus-zero-shot "
            "results were known, during the thesis rewrite, to test one candidate explanation "
            "of the Level-0 asymmetry. It is not part of the frozen inferential family, and its "
            "p-value is unadjusted and post-selection."
        ),
        "interpretation_rule": (
            "A divergence between the two instruments is evidence that the reported Level-0 "
            "weakness is measured differently by a trained classifier and by blinded readers. "
            "It does not establish which instrument is closer to the construct, and it does not "
            "revise any registered number: the primary outcome remains Verifier-B on all 5,400 "
            "cases. Per-condition breakdown is refused because each cell holds five items."
        ),
        "instruments": {
            "primary_outcome": "verifier_b_binary_target_match",
            "verifier_b_threshold": b_cut,
            "verifier_a_threshold_operating_point": a_cut,
            "human_rule": config["instruments"]["human_rule"],
            "human_panel_size": EXPECTED_ANNOTATORS,
        },
        "overall": summarize(items),
        "by_target_level": {
            str(level): summarize([i for i in items if i["target_level"] == level])
            for level in (0, 1)
        },
        "refused": {
            "per_condition_breakdown": (
                "five items and 15 judgments per condition-by-level cell cannot support it"
            ),
        },
        "input": {
            "scores_path": str(score_path.relative_to(root)).replace("\\", "/"),
            "scores_sha256": hashlib.sha256(score_path.read_bytes()).hexdigest(),
            "human_responses_path": str(response_path.relative_to(root)).replace("\\", "/"),
            "human_responses_sha256": hashlib.sha256(response_path.read_bytes()).hexdigest(),
            "researcher_key_path": str(key_path.relative_to(root)).replace("\\", "/"),
            "researcher_key_sha256": hashlib.sha256(key_path.read_bytes()).hexdigest(),
            "n_items": len(items),
            "generation_rerun": False,
            "verifier_b_rescoring": False,
        },
    }
    write_result(result, output_path, str(config_path.relative_to(root)).replace("\\", "/"))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
