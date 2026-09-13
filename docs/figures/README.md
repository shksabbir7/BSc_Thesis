# Thesis figure source register

This directory contains editable vector figures for the thesis. Schematics do
not introduce computed results; numeric labels reproduce frozen values from the
listed sources.

| Figure | File | Source contract | Numeric standing |
|---|---|---|---|
| 4.1 | `dual_verifier_isolation.svg` | `data/splits/split_map_v1.json`, `results/g300_agreement.md`, Chapters 3--4, frozen verifier/RAG manifests | G=300 and 598/600 Attempt-1 ratings, α=0.497; R1=2,162, R2=2,163; dev-200 is within R1; A train=804, B train=888, RAG=886 |
| 4.2 | `backbone_ablation_circularity.svg` | `results/s3_backbone_ablation.json`, `results/s3b_baselines.json` | Seven descriptive mean macro-F1 values; whiskers are ±1 seed SD, not confidence intervals; SetFit variability omitted because only one effective configuration was produced; frozen-probe reference=0.9866; corrected verdict=`TIE` |
| 5.1 | `../chapters/chapter5/figures/bounded_workflow_state_graph.svg` | implemented controller and Chapter 5 | maximum three Writer attempts; overlap is diagnostic; failed-rule terms augment retrieval only in symbolic-feedback conditions |
| 5.2 | `../chapters/chapter5/figures/development_frontier_forced_trace_diagnostics.svg` | `results/s4_tau_frontier.json`, `results/s4_loop_dynamics.json` | development-only τ=0.4384071; attempt panel contains 60 forced traces at each attempt |

Verifier-B's placement outside Figures 4.1 and 5.1 is a scientific isolation
constraint, not a visual simplification. Figure 5.1 depicts bounded control:
the controller follows fixed retry transitions and may augment the anchored
query with failed symbolic feature names, but it may not change frozen
thresholds, data partitions or attempt ceilings.
