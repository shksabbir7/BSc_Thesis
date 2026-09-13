# Thesis table and figure manifest

**Audit date:** 2026-08-26
**Scope:** Bangla cinema response generation. This manifest introduces no
analysis and authorizes no generation rerun.

## Selection rule

A table or figure stays in the main thesis only when it does at least one of
four jobs: defines the research claim, proves an isolation/reproducibility wall,
reports a load-bearing result, or makes a limitation visible beside that result.
Implementation traces, full hyperparameters, per-seed rows and secondary
diagnostics belong in the appendix. The local diagnostic interface is not a
Phase-5 result and receives no main-results figure.

## Main-text tables

| ID | Purpose | Source of truth | State | Required action |
|---|---|---|---|---|
| Table 2.1 | Position against adjacent work | Chapter 2 and cited primary records | Present in Chapter 2 | Outcome isolation is described without implying that any scorer is ground truth. |
| Table 3.1 | Audit and cleaning summary | `s0_data_xray.md`, `s1_cleaning_log.json`, split-map input count | Present in canonical Chapter 3 | Preserves the sequential cleaning cascade from 5,000 raw rows to the 4,625-row split surface. |
| Table 3.2 | Frozen review-data partition | `data/splits/split_map_v1.json`, Region-A K=2 assignments | Present in canonical Chapter 3 | Distinguishes the three disjoint partitions from the 200-row development subset contained within R1. |
| Table 3.3 | Source-region signature in the raw workbook | `s2c_region_split.md` | Present in canonical Chapter 3 | Contrasts Region A and Region B at the raw row-1,999 boundary without assigning an unrecoverable source identity. |
| Table 3.4 | Construct-analysis components and decision roles | registered S2 methods and `docs/protocol.md` | Present in canonical Chapter 3 | Separates stability, clusterability, confound, negative-control and human-validity functions. |
| Table 3.5 | Construct evidence and Region-B negative control | Region-A/B `s2d/s2e/s2f` artifacts | Present in canonical Chapter 3 | Places stability beside silhouette, gap and HDBSCAN evidence that prevents a discrete-persona interpretation. |
| Table 3.6 | Human validation design and evidence | `g300_agreement.md`, `intrusion_agreement.md` | Present in canonical Chapter 3 | Keeps the failed ordinal instrument beside the successful comparative instrument. |
| Table 3.7 | Operational engagement-specificity levels | `docs/axis_definition.md`, RQ1-H validation | Present in canonical Chapter 3 | Defines the levels without presenting them as demographic personas or natural audience segments. |
| Table 4.1 | Registered backbone candidates and their methodological roles | `configs/s3_backbone.yaml`, `docs/protocol.md` S3.2 pre-commitment | Present in Chapter 4 | Pretraining scope, adaptation strategy and role in the ablation. |
| Table 4.2 | Descriptive backbone-ablation performance on dev-82 | `s3_backbone_ablation.*` | Present in Chapter 4 | Mean macro-F1, seed SD, selected learning rate and inferential interpretation; SetFit variability is correctly marked not estimable. |
| Table 4.3 | Reference models used to assess construction circularity | `s3b_baselines.*` | Present in Chapter 4 | Majority, length, frozen-probe and highest fine-tuned reference with their analytical purposes. |
| Table 4.4 | Functional and methodological comparison of the two verifiers | `s3c_verifier_a.*`, `s3d_verifier_b.*` | Present in Chapter 4 | Contrasts function, data, encoder family, adaptation, selection, performance and calibration standing without ranking A against B. |
| Table 4.5 | In-sample calibration before and after temperature scaling | `s3c_verifier_a.json`, `s3d_verifier_b.json` | Present in Chapter 4 | Both verifiers in one table; ECE reduction is reported with its bootstrap CI and descriptive interpretation. |
| Table 4.6 | Design constraints and verification mechanisms for verifier isolation | split map, verifier configs, `tests/` | Present in Chapter 4 | Pairs each isolation dimension with its design constraint and executable verification mechanism. |
| Table 5.1 | Expected bounded-loop cost under a constant pass-rate reference model | `docs/protocol.md` S4 decision 19 cost model; `src/eval/tau_objective.py` | Present in Chapter 5 | Evaluates the registered analytical reference model and shows why cost minimisation without a quality constraint is degenerate. |
| Table 5.2 | Symbolic feature families and their leave-one-family-out contribution | `s35_symbolic.md` | Present in Chapter 5 | Added in the Phase 3 rewrite. Shows the surviving signal concentrated in a family pre-registered as gameable, and that removing length features improves held-out performance. |
| Table 5.3 | Neural/symbolic weight study | `s4_w_sensitivity.*`, `s35_symbolic.*` | Present in Chapter 5 | Was Table 5.2. Reports `w=1` folds and `PRECOMMITMENT_UNRESOLVED`; no hybrid-win language. Length-only probe printed beside the neural column as the real baseline. |
| Table 5.4 | The three registered operating points on the development frontier | `s4_tau_frontier.json` | Present in Chapter 5 | Added in the Phase 3 rewrite. States the forced-three endpoint at five logical calls, not three, and reports both "fraction of gain" denominators with each named. |
| Table 5.5 | Forced-attempt scores and paired transition diagnostics, 60 development cases | `s4_loop_dynamics.json` | Present in Chapter 5 | Two-panel table; every case contributes all three attempts. These are forced-trace diagnostics, not operational continuation subsets and not evidence for an optimal retry ceiling. |
| Table 5.6 | Intervention, computational and isolation contracts for ten experimental conditions | frozen Phase-5 config/runner and Chapter 5 | Present in Chapter 5 | Two-panel table. Static few-shot uses ten same-level examples; blind resampling is explicitly token-budget matched; Verifier-B is absent from every generation condition. |
| Table 6.1 | Complete 20-cell outcome and same-model inference-cost table | `s5_main_bn_master_table.csv` | Present in canonical Chapter 6 | Token note defines provider-reported prompt-plus-completion totals across Writer, Reflector and critique calls; hosted judge tokens remain separate. |
| Table 6.2 | Nine registered paired comparisons against zero-shot and the separate exploratory direct contrast | `s5_main_bn_paired_statistics.csv`, frozen 540-pair hybrid-minus-neural analysis | Present in canonical Chapter 6 | Registered continuous and binary panels remain separate from a clearly labelled exploratory panel; no active-condition ranking is licensed. |
| Table 6.3 | Blinded human-evaluation summary | `s5_human_eval_bn_report.json`, summary CSV | Present in canonical Chapter 6 | Separates per-rater/pooled target-match accuracy from raw agreement and nominal alpha; not system ranking. |
| Table 6.4 | Same-item comparison of the level-measuring instruments, 100 blinded items | `s5_instrument_agreement_bn_v1.json` | Present in canonical Chapter 6 | Split into accuracy/agreement and paired-disagreement panels. Exploratory standing and refusal of per-condition inference are explicit. |
| Table 6.5 | Length-matched sensitivity and coverage | `s5_main_bn_length_matched.*` | Present in canonical Chapter 6 | Coverage appears beside matched accuracy to expose post-treatment selection. |
| Table 6.6 | Rule-selected example outputs, replicate seed 42 | `s5_error_examples_bn_v1.json` | Present in canonical Chapter 6 | Split into selection-metadata and measurement panels; the Bangla texts remain in prose. Each selected stratum carries its size out of 90. |
| Table 7.1 | Validity-threat matrix | Chapter 7 and STATUS verified facts | Present in Chapter 7 | Covers construct/internal/external/statistical/measurement/human/ethics risks. |
| Table 8.1 | Final RQ verdicts and claim boundaries | `docs/thesis_rq_evidence_map.md`, Chapters 6–8 | Present in Chapter 8 | Separates the evidence-bearing conclusion for each active question from the claim that remains unestablished. |

## Main-text algorithms

Added by the Phase 3 rewrite of Chapter 5, which previously contained none. Both
are transcribed from the implementation rather than paraphrased, and neither
introduces a procedure that is not executed by the frozen run.

| ID | Purpose | Source of truth | State | Required action |
|---|---|---|---|---|
| Algorithm 5.1 | The bounded verifier-in-the-loop generation loop | `src/agents/graph.py`, `src/agents/state.py`, `src/eval/s5_engine.py` | Present in Chapter 5 §5.3 | Records overlap diagnostically; every non-terminal failure re-retrieves, and failed symbolic feature names augment the anchored query only when enabled. |
| Algorithm 5.2 | Blind-resampling selection under a matched token budget | `src/eval/s5_engine.py::run_resampling` | Present in Chapter 5 §5.6.2 | Uses the largest generation-order prefix within the same-case realized generator-token budget and raises if no candidate can be funded. |

## Main-text figures

| ID | Purpose | Source of truth | State | Required action |
|---|---|---|---|---|
| Figure 3.1 | Macro-level research methodology | implemented pipeline, split map and isolation contracts | Placed in canonical Chapter 3 | Shows the staged data, construct, verifier, generation and evaluation flow while keeping Verifier-B outside generation. |
| Figure 3.2 | Micro-level verifier-in-the-loop workflow | implemented agent graph and tool boundaries | Placed in canonical Chapter 3 | Shows one plot–level case, bounded revision and the outcome-only Verifier-B path. |
| Figure 3.3 | K-selection diagnostics across corpus regions | `s2d_ktable_regionA.csv`, `s2d_ktable_regionB.csv` | Placed in canonical Chapter 3 | Shows prediction strength, bootstrap ARI, silhouette and gap for K=2–8; HDBSCAN remains a non-K-dependent diagnostic in Table 3.5. |
| Figure 4.1 | Dual-verifier training and isolation wall | Chapter 4, split map, verifier configs | Placed in Chapter 4 | Shows Gold exclusion, R1/R2 separation, shared-dev qualification and B's outcome-only privilege wall. |
| Figure 4.2 | Backbone ablation and construction-circularity reference | `s3_backbone_ablation.json`, `s3b_baselines.json` | Placed in Chapter 4 | Shows descriptive candidate means with ±1 seed SD and the frozen LaBSE reference; explicitly labels the whiskers as non-CI and the corrected outcome as `TIE`. |
| Figure 4.3 | Shared-development confusion matrices | `s3c_verifier_a_dev_predictions.csv`, `s3d_verifier_b_dev_predictions.csv` | Placed in canonical Chapter 4 | Reports K=2 weak-label reproduction on held-out dev-82 and explicitly refuses a human-gold or final-test interpretation. |
| Figure 5.1 | Bounded four-role workflow state graph | implemented loop and Chapter 5 | Placed in Chapter 5 | Shows fixed Researcher → Writer → Critic → Reflector routing, unconditional re-retrieval after non-terminal failure, optional failed-rule query augmentation, the three-attempt bound and Verifier-B outside the graph. |
| Figure 5.2 | Development quality–cost frontier and forced-trace diagnostics | `s4_tau_frontier.json`, `s4_loop_dynamics.json`, `docs/chapters/chapter5/figures/development_frontier_forced_trace_diagnostics.svg` | Placed in Chapter 5 | Labels the one-call, selected-policy and forced-three endpoints; Panel B explicitly contains all 60 forced traces at every attempt. |
| Figure 6.1 | Preregistered paired effects relative to zero-shot | `s5_main_bn_paired_statistics.csv`; `docs/chapters/chapter6/figures/paired_effects_vs_zero_shot.png` | Placed in canonical Chapter 6 | Shows nine paired mean differences and 95% bootstrap intervals; caption explicitly refuses active-condition ranking. |
| Figure 6.2 | Attempt dynamics and same-case verifier divergence | frozen Goodhart attempt/transition CSVs; `docs/chapters/chapter6/figures/verifier_divergence_diagnostics.png` | Placed in canonical Chapter 6 | Title avoids treating Verifier-B as ground truth; caption distinguishes failure-selected trajectories from paired adjacent transitions. |
| Figure 6.3 | Separate corpus-distribution diagnostics | frozen length-JS, diversity and LaBSE-feature MAUVE tables; `docs/chapters/chapter6/figures/corpus_level_diagnostics.png` | Placed in canonical Chapter 6 | Avoids a composite realism claim and preserves the LaBSE-feature/small-sample limitation. |

## Appendix-only material

| Artifact | Why it is not in the main narrative |
|---|---|
| Complete configs, hyperparameters and environment-to-result mapping | Present in Appendices A and G. |
| Per-seed verifier and Phase-5 supplementary rows | Present in Appendix F; seeds are sensitivity/pairing blocks, not independent studies. |
| Exact symbolic rule catalogue and failure taxonomy | Present in Appendix E; the eight-case single-coder deviation remains visible. |
| Exact Goodhart adjacent-transition rows and sample sizes | Present in Appendix F; the main figure carries the interpretation. |
| Diversity, length-JS and LaBSE-MAUVE numeric tables | Present in Appendix F with the MAUVE standing retained. |
| Prompt templates and trace policy | Present in Appendix E; complete sealed traces remain the authority rather than a favourable hand-picked example. |
| Full bibliography audit map | Appendix G points to the 143-entry audit map; metadata provenance is not a thesis result. |
| Post-run local interface | Present in Appendix H and explicitly excluded from experimental evidence. |

## Explicit exclusions

- No audience-demographic, persona, cluster-type or box-office figure.
- No sentiment-JS panel: an independent registered generated-text sentiment
  scorer does not exist.
- No film-level realism plot: reviews cannot be mapped to films.
- No interface screenshot in the main experimental results. If retained, the
  diagnostic demo belongs in an implementation appendix and must be labelled
  as post-run software using a different live model path.
- No new composite score or post-hoc ranking of the ten conditions.

## Build order

1. ✅ Insert the two already-final Phase-5 PNGs and replace Chapter 6 placeholder
   wording.
2. ✅ Render Tables 6.2--6.6 directly from their audited result files.
3. ✅ Build and place Figures 4.1 and 5.1, because the verifier wall and
   multi-agent routing are central to the title and defence.
4. ✅ Build and place the three Chapter 3 methodology figures and the Chapter 4
   ablation/circularity and confusion-matrix figures. A calibration reliability diagram was not
   retained because the 82-row in-sample surface is too sparse for that figure
   to add evidence beyond Table 4.5.
5. ✅ All **28** canonical main-text tables are placed and listed above.
   The two administrative Chapter 1 mapping tables introduced in the expanded
   flat draft were retired when the concise academic introduction was restored;
   the detailed RQ evidence map remains an audit artifact, and the final RQ
   verdicts remain in Table 8.1. Chapter 5 also contains two algorithm listings,
   recorded separately above. Final pagination and formatting wait for the
   university thesis template.

Every numeric rendering must retain its source artifact and rounding rule in a
manifest. Existing 5,400 generations are frozen and must not be rerun.
