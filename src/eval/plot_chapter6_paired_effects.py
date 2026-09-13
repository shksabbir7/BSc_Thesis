#!/usr/bin/env python3
"""Render the Chapter 6 paired-effect forest plot from the frozen S5 table."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.common.seed import set_seed


LABELS = {
    "static_few_shot": "Static few-shot",
    "rag_only": "RAG only",
    "rag_neural_loop": "RAG + neural loop",
    "rag_symbolic_loop": "RAG + symbolic loop",
    "rag_neural_symbolic_feedback": "RAG + neural + symbolic feedback",
    "intrinsic_self_critique": "Intrinsic self-critique",
    "external_role_self_critique": "External-role self-critique",
    "gemma4_26b_a4b_judge_loop": "Hosted judge loop",
    "blind_resampling": "Blind resampling",
}


def main() -> int:
    set_seed()
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="results/s5_main_bn_paired_statistics.csv")
    parser.add_argument(
        "--output",
        default="docs/chapters/chapter6/figures/paired_effects_vs_zero_shot.png",
    )
    args = parser.parse_args()

    frame = pd.read_csv(args.input)
    if set(frame["condition"]) != set(LABELS) or len(frame) != 9:
        raise RuntimeError("input must contain the exact nine registered comparisons")
    frame = frame.sort_values("b_probability_delta")

    y = list(range(len(frame)))
    effect = frame["b_probability_delta"].to_numpy()
    lower = frame["ci_low"].to_numpy()
    upper = frame["ci_high"].to_numpy()

    fig, ax = plt.subplots(figsize=(9.2, 5.4), constrained_layout=True)
    ax.axvline(0, color="#5f6b7a", linewidth=1.2, linestyle="--")
    ax.errorbar(
        effect, y,
        xerr=[effect - lower, upper - effect],
        fmt="o", color="#246b8e", ecolor="#246b8e",
        markersize=6, elinewidth=2, capsize=4,
    )
    for x, row_y, value in zip(effect, y, effect):
        ax.annotate(f"{value:+.3f}", (x, row_y), xytext=(8, 0),
                    textcoords="offset points", va="center", fontsize=9)
    ax.set_yticks(y, [LABELS[x] for x in frame["condition"]])
    ax.set_xlabel("Paired change in Verifier-B target probability relative to zero-shot")
    ax.set_title("Preregistered Effects Relative to Zero-Shot (95% CIs)",
                 fontweight="bold")
    ax.grid(axis="x", alpha=.22)
    ax.set_xlim(min(0, lower.min() - .02), upper.max() + .055)
    ax.text(.01, -.13,
            "n = 540 paired plot–level–seed cases per condition; BH correction applies to the registered nine-comparison family.",
            transform=ax.transAxes, fontsize=8, color="#4b5563")

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=220, metadata={"Title": "Preregistered paired effects against zero-shot"})
    plt.close(fig)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
