# Phase 2 — Abstract development

**Status:** proposal. Nothing in `docs/thesis_front_matter.md` has been modified.
Phase 3 applies the replacement after sign-off.

**Correction to my own Phase 1 plan.** I listed Phase 2 as "draft the abstract".
That was wrong: an abstract already exists in `docs/thesis_front_matter.md`
(§Abstract, 268 words) and it is competent. Phase 2 is therefore an audit and a
revision, not a first draft. This is the fifth time in this review that I have
treated something in this repository as absent when it was present, and the
correction is recorded rather than quietly absorbed.

---

## Part 1 — What the existing abstract already gets right

These are not changed, and are listed so the revision is visibly a revision.

1. It leads with the evaluation problem, not with the application. Correct
   ordering for a methods contribution.
2. It states the negative clusterability result **and keeps it** — "does not
   support discrete audience personas" — instead of quietly proceeding to a
   two-level cut as though the cut had been the plan.
3. It already carries the discipline sentence on the largest effect: *"although
   its incremental advantage over neural-only gating was not a registered
   contrast."* That single clause is the difference between a defensible abstract
   and an unpublishable one, and it was already there.
4. It restricts the proxy-divergence finding to the neural loops, which is where
   it occurs; the symbolic loop moves the other way, and the abstract does not
   over-generalise.
5. Its final sentence disclaims audience prediction, personas and film-level
   realism. Consistent with §1.7.

## Part 2 — Defects found

| # | Defect | Why it matters |
|---|---|---|
| A2.1 | **Objectives are never stated.** The reader learns what was done, never what was being attempted. | A required abstract element, and its absence is what makes the abstract read as a report rather than as research. |
| A2.2 | **The human construct validation is numberless.** "Length-matched comparative judgments establish that native-Bangla annotators can recognize the distinction" carries no figure, while the *generation* human study two paragraphs later carries four. | RQ1-H is the study that makes the whole construct legitimate (STATUS: *"the human validation, not the profiling, carries RQ1"*). Presenting the strongest evidence without its numbers, next to weaker evidence with them, inverts the emphasis. |
| A2.2b | **"Length-matched" is left ambiguous.** It is true of RQ1-H (corpus items matched within 2 words). A reader can carry it forward to generation, where `LENGTH_RECOVERS_LEVEL` fired in both arms. | STATUS row 17d: *"no claim of length-neutral axis control may be made anywhere in the thesis."* The current wording does not make that claim, but it does not block the inference either. An abstract must not depend on the reader declining to generalise. |
| A2.3 | **C2 is absent.** No compute figure appears anywhere. The framework's cost — 1.630–1.889 mean generator calls per case, against 3.000 fixed for both self-critique conditions — is not mentioned. | "Bounded workflow under matched compute" is an approved contribution and the abstract does not contain the word compute. `blind_resampling` was explicitly budget-matched per case (`primary_budget: matched_realized_generator_flops_to_row6`); that design fact is invisible. |
| A2.4 | **C6 is half-present.** "Symbolic rules provide diagnostic feedback" states the placement but not the measurement that forced it — `w = 1.0` in all five grouped held-out folds, mean ΔAUC 0.0000, registered as `PRECOMMITMENT_UNRESOLVED`. | The title says *Neuro-Symbolic*. A reader who meets that word in the title and "diagnostic feedback" in the abstract does not learn that the decision-value question was tested and did not resolve in the symbolic scorer's favour. Stating that outcome is what makes the diagnostic placement a result instead of a design preference. See A2.10 for why this must be worded as unresolved rather than as a null. |
| A2.5 | **C4 is absent.** `CIRCULARITY_CONFIRMED` — the in-loop probe reaches 0.9866 because the two-level cut was made in the same LaBSE space the probe reads — appears nowhere. | It is the cheapest credibility the thesis owns: a near-ceiling number, published together with the reason it does not mean what it appears to mean. Omitting it makes 0.9866 look like an achievement claim. |
| A2.6 | **The proxy-divergence sentence can be misread as collapse.** "Same-case revisions also widen the Verifier-A–Verifier-B gap" does not say that *both* verifiers rise. | On the same 147 cases, Verifier-A gains +0.4835 and Verifier-B gains +0.3006 under `rag_neural_loop` (+0.5381 and +0.3967 under the proposed loop). The sealed evaluator agrees that the revisions helped — it just agrees less. "Goodhart" without that sentence reads as "the real metric fell", which would be a fabricated result. |
| A2.7 | **"All nine registered alternatives improve"** gives no inferential quantity. | Every BH-adjusted q = 0.00019998 at 10,000 resamples. One clause converts an assertion into a reported test. |
| A2.8 | Verifier accuracies are given without their evaluation size (82 dev items). | The registered pre-commitment is that **no claim that either verifier is better may be made from dev-82** — one item is 0.0122 macro-F1. Quoting 0.9866 and 0.9597 side by side without n invites exactly the comparison that is forbidden. |
| A2.9 | **Mine, not the original abstract's — introduced by my own Part 3 draft and corrected 2026-08-25.** The +0.4835 / +0.3006 / +0.1828 transition figures were reported without naming their condition, in a paragraph whose previous sentence names the symbolic-feedback loop as the winner. | Those three numbers belong to `rag_neural_loop`, not to `rag_neural_symbolic_feedback`. On the same 147 cases the proposed loop reads +0.5381 / +0.3967 / +0.1415 (`results/s5_main_bn_goodhart_paired_transitions.csv`). An unattributed number beside a named condition is read as belonging to it, which would have put a figure from the wrong arm in the abstract. Now both are named, which also strengthens the finding: divergence appears under neural gating with *and* without symbolic feedback, so it is a property of verifier-guided iteration rather than of one condition. |
| A2.10 | **Mine, and the more serious of the two — corrected 2026-08-25.** My Part 3 draft wrote *"the symbolic scorer carries no independent decision value"*, asserting a null as an established finding. | `docs/STATUS.md` row 17e registers the outcome as **`PRECOMMITMENT_UNRESOLVED`**, not as a null. The supporting numbers are real — `w = 1.0` in all five grouped held-out folds with mean ΔAUC 0.0000, in both the length-controlled and free-length conditions (`results/s4_w_sensitivity.json`) — but verdict sensitivity across the 21-point grid was 50.8% / 39.2%, so the curve was **not** flat, and the registered consequence is that no predictive-value claim is licensed in either direction. Row 17e also records that the code's catch-all silently emitted `SYMBOLIC_INERT` and that this label was superseded by an audit state precisely so the null would not be adopted. Writing the null into the abstract would have re-committed the error that audit exists to prevent. |

---

## Part 3 — Revised abstract (thesis version, 587 words)

**On the objectives.** The four objectives in the abstract are a **compression of
the five operational objectives Sabbir already wrote** in
`docs/chapters/chapter1/Introduction.md` §1.4 — they are not new objectives, and
the abstract does not get to invent any. The mapping is: §1.4 objectives 1 and 2
→ *"establish a response construct that blinded human readers can recover"*;
objective 4 → *"generate against it under a bounded and auditable control flow"*;
objective 3 → *"measure the result with an evaluator the loop cannot reach"*;
objective 5 → *"compare the mechanism against nine registered alternatives"*.

The first draft of this file compressed to **three**, which silently dropped
objective 5 — the comparison that is the entire content of Chapter 6. Sabbir
approved the correction to four on 2026-08-25. The compression is lossy by
design (an abstract cannot carry five clauses), but it must be lossy *evenly*,
and dropping the objective that owns the largest chapter was not even.

**On length.** 587 words, counted rather than estimated, against the existing
abstract's 268. No university template was supplied, so no cap is known. If one
applies, cut in this order and stop as soon as the limit is met: (i) the
calibration clause, *"and whose calibration error falls from 0.11836 to 0.00537
under temperature scaling"* — a registered result but not one of the six
contributions (−15 words); (ii) the length-heuristic clause, *"and a length
heuristic scoring 0.16, below chance"* (−10); (iii) the symbolic-gating figure,
*"symbolic gating alone gives the smallest, +0.1091 [0.0649, 0.1524]"* (−12).
Do **not** cut the descriptive-orderings sentence or the both-verifiers-rise
clause to save space; those two are what make the remaining numbers honest.

> Pre-release film planning has no access to authentic audience commentary, and
> unconstrained language-model generation gives no assurance that a requested
> response style is realized rather than merely requested. The evaluation problem
> is prior to the generation problem: where the model that steers generation also
> scores it, improvement cannot be distinguished from adaptation to the scorer.
> This thesis develops and evaluates a neuro-symbolic, verifier-in-the-loop
> framework for controlled Bangla cinema-response generation, pursuing four
> objectives — to establish a response construct that blinded human readers can
> recover, to generate against it under a bounded and auditable control flow, to
> measure the result with an evaluator the loop cannot reach, and to compare the
> mechanism against nine registered alternatives on target-level outcome,
> computational cost and human judgement.
>
> A 5,000-row Bangla review corpus is audited and cleaned to 4,625 usable rows
> under frozen partition rules. Unsupervised structure recovers collection
> provenance at 93.3% accuracy rather than audience identity, so no discrete
> persona claim is made; analysis proceeds on a two-level cut through an
> engagement-specificity continuum. Two annotators blind to the partition recover
> that distinction by comparative judgement on held-out corpus items at 0.780 and
> 0.840 against a 0.25 chance rate, with lengths matched to within two words and
> a length heuristic scoring 0.16, below chance. The framework coordinates four
> components, two of which make no model call: a Researcher retrieving only from
> the R1 partition, a Writer, a deterministic symbolic Critic, and a Reflector
> that verbalises computed rule failures and nothing else. In-loop acceptance uses
> a frozen LaBSE logistic probe whose 0.9866 macro-F1 on 82 development items is
> reported as circular rather than as a modelling result, the cut having been made
> in the same embedding space, and whose calibration error falls from 0.11836 to
> 0.00537 under temperature scaling. Outcome scoring uses a BanglaBERT verifier
> fine-tuned on the disjoint R2 partition and never exposed to the loop.
>
> The completed experiment contains 5,400 outputs over 90 held-out plots, two
> requested levels, ten conditions and three paired generation seeds. All nine
> registered alternatives raise outcome-verifier target probability above
> zero-shot at Benjamini–Hochberg q = 0.0002. Neural gating with symbolic feedback
> gives the largest registered effect, +0.2570 with 95% paired-bootstrap interval
> [0.2151, 0.2987], at 1.63–1.89 generator calls per case, while both
> fixed-iteration self-critique controls spend 3.000; symbolic gating alone gives
> the smallest, +0.1091 [0.0649, 0.1524]. No independent decision value for the
> symbolic scorer is established: every grouped held-out fold selects mixture
> weight 1.0 with mean ΔAUC +0.0000, yet the weight curve is not flat, so the
> pre-registered outcome is recorded as unresolved rather than as a clean null and
> the scorer is retained for diagnosis, not adjudication. On identical
> cases, a first revision under neural gating without symbolic feedback raises the
> in-loop proxy by +0.4835 and the sealed evaluator by +0.3006, widening the gap
> by +0.1828 over 147 cases; the proposed loop moves the same way, +0.1415 over
> the same 147. Both measures agree the revision helped and they disagree about
> how much, which a single evaluator would conceal.
> Three annotators blind to condition, model and requested level recover the
> requested level on a frozen balanced 100-item subset at 0.9133
> [0.8667, 0.9567], nominal Krippendorff
> α 0.8405. Because the registered inferential family contains only
> condition-versus-zero-shot comparisons, orderings among active conditions are
> descriptive.
>
> The framework supports auditable and humanly recoverable control of Bangla
> response style; it does not predict audience reception, recover audience
> segments, or model film-level realism. Its principal contribution is
> methodological — a verifier-isolation protocol under which proxy divergence in
> evaluator–optimizer systems is measurable instead of invisible.

### Notes on three wording choices

- *"reported as circular rather than as a modelling result"* — this deliberately
  spends a clause to disarm the 0.9866. A reviewer who computes the objection
  himself is a hostile reviewer; a reviewer handed it is a persuaded one.
- *"both measures agree the revision helped, and they disagree about how much"* —
  the honest form of the Goodhart finding. This is not hedging: the alternative
  sentence would report a collapse that did not occur.
- *"two of which make no model call"* — the load-bearing half of the
  architectural honesty required by `src/agents/graph.py`. It pre-empts the
  autonomy question in seven words, without the abstract having to use the word
  autonomous at all.

---

## Part 4 — Condensed version (journal submission, 193 words)

For a Q1 submission with a 200-word cap. Not for the thesis.

> Where the model that steers generation also scores it, apparent improvement
> cannot be separated from adaptation to the scorer. We present a
> verifier-in-the-loop framework for controlled Bangla cinema-response generation
> in which the in-loop acceptance model and the outcome evaluator are trained on
> disjoint data partitions and the outcome evaluator is never available to the
> loop. Unsupervised structure in a 5,000-row Bangla review corpus, cleaned to
> 4,625 usable rows, recovers collection provenance (93.3%) rather than audience
> identity, so a two-level
> engagement-specificity cut replaces the persona hypothesis; blinded annotators
> recover it by comparative judgement at 0.780 and 0.840 against 0.25 chance,
> length-matched, where a length heuristic falls below chance. Across 5,400
> generations spanning 90 held-out plots, two levels, ten conditions and three
> paired seeds, all nine registered alternatives exceed zero-shot (q = 0.0002);
> neural gating with symbolic feedback is largest, +0.2570 [0.2151, 0.2987].
> The symbolic scorer has no independent decision value (held-out ΔAUC +0.0000)
> and is retained only for failure diagnosis. On identical cases one revision
> raises the in-loop proxy +0.4835 and the sealed evaluator +0.3006, a +0.1828
> divergence a single evaluator would hide. Blinded human recovery of the
> requested level: 0.9133, α = 0.8405.

---

## Part 5 — Required-element coverage

| Element | Where in the revised abstract | Present before? |
|---|---|---|
| Background | ¶1 s.1 — pre-release access, unconstrained generation | yes |
| Problem | ¶1 s.2 — steering model and scoring model coincide | yes |
| Gap | ¶1 s.2 + ¶2 (persona hypothesis fails; nothing to generate against) | partly, implicit |
| **Objectives** | ¶1 s.3 — three named objectives | **no — added** |
| Methodology | ¶2 — four components, R1-only retrieval, dual verifiers | yes |
| Dataset / setup | ¶2 (corpus) and ¶3 s.1 (5,400-case design) | yes |
| Quantitative results | ¶3 — 12 figures with intervals or q-values | yes, extended |
| Contributions | ¶3 (C1, C4, C6) + ¶4 s.2 (principal contribution named) | partly, implicit |
| Conclusion / significance | ¶4 | yes |

## Part 6 — Every number, and the file it came from

No value below was typed from memory; each was read at the path given during
this session. Two derived values are marked as such.

| Value | Source |
|---|---|
| 5,000 raw rows | `docs/STATUS.md` S0 corrected table |
| 4,730 after rule-based cleaning; 4,625 after near-dup removal at t = 0.95 | `docs/STATUS.md` verified-facts table; decision 1 (closed 2026-08-08) |
| 93.3% provenance-detection accuracy | `docs/STATUS.md` pipeline row 3 |
| RQ1-H 0.780 (39/50), 0.840 (42/50), chance 0.25; Gate B 34/40 both raters; length matched within 2 words; length heuristic 0.16 | `docs/STATUS.md` row 5m → `results/intrusion_agreement.md` |
| Verifier-A macro-F1 0.986555, 1 error in 82 | `docs/STATUS.md` decision 10 / S3.3 row |
| Verifier-A ECE 0.11836 → 0.00537 | `docs/STATUS.md` verified-facts table (measured 2026-08-11) |
| Verifier-B 0.959666 on R2, 888 rows | `docs/STATUS.md` S3.3 row |
| 5,400 = 90 × 2 × 10 × 3 | `results/s5_main_bn_reporting_tables_v2.md`, n = 270 per condition-level cell |
| All nine deltas, CIs, BH q = 0.00019998 | `results/s5_main_bn_reporting_tables_v2.md` §Planned paired statistics |
| Mean generator calls 1.889 / 1.630 (neural+symbolic) and 3.000 / 3.000 (both self-critique) | same file, §Main table, column *Mean calls* |
| `logical_generator_calls` counts Writer **and** Reflector calls | `src/eval/s5_engine.py` lines 112–119 — verified, not assumed, because 3.630 exceeds `max_attempts: 3` |
| Budget matching of `blind_resampling` to row 6 | `configs/s5_main_bn.yaml` §blind_resampling → `src/eval/run_s5_main_bn.py:341` |
| Symbolic mixture w = 1.0 in 5/5 folds, mean ΔAUC +0.0000 | `results/s4_w_sensitivity.md` held-out section; `w_chosen_per_fold` and `delta_auc_per_fold` in the `.json`, five folds in **both** the length-controlled and free-length conditions. Registered standing is `PRECOMMITMENT_UNRESOLVED` (`docs/STATUS.md` row 17e), **not** a null — verdict sensitivity was 50.8% / 39.2%, so the curve was not flat. See A2.10 |
| A-delta +0.4834507, B-delta +0.3006486, gap +0.1828021, n = 147 | `results/s5_main_bn_goodhart_paired_transitions.csv` row 1 — **`rag_neural_loop`**, attempt 1→2. Named in the abstract as of A2.9 |
| Proposed-loop gap +0.1414811 on the same n = 147 | same file, row 3 — `rag_neural_symbolic_feedback`, attempt 1→2 |
| Human eval 0.9133 [0.8667, 0.9567], α 0.8405, per-annotator 0.91/0.93/0.90 | `results/s5_main_bn_reporting_tables_v2.md` §Blinded human validation; `results/s5_human_eval_bn_report.json` (10,000 resamples; both levels exactly 137/150, accuracy 0.9133 in each) |
| Blinding scope — "condition, model and requested level" | `docs/s5_human_eval_heds3.md:33` — *"blinded to condition, model, target, replicate and automatic scores"*; verified rather than assumed from the word "blinded" in the results table |
| *derived* — "1.63–1.89 calls" is the two level-wise means rounded, not a pooled statistic | from the Mean calls column; stated as a range for that reason |
| *derived* — 587 and 193 words, and the existing abstract's 268 | counted programmatically on this file and on `docs/thesis_front_matter.md`. The first draft of this document asserted 412, 198 and 330 from estimate, and all three were wrong. Recorded because it is the same failure mode as the absence claims: a plausible figure produced without measuring. The 587 is the count after three 2026-08-25 revisions: 526 as first drafted, 542 after the fourth objective was added, 562 after A2.9 attributed the transition figures to their conditions, 587 after A2.10 replaced the asserted symbolic null with the registered unresolved outcome |

## Part 7 — What the abstract deliberately does not say

| Not claimed | Registered reason |
|---|---|
| That neural+symbolic beats neural-only | `docs/STATUS.md` row 23: the frozen family contains only comparisons against zero-shot, *"and no post-hoc contrast is invented."* Hence the closing sentence of ¶3. |
| That generation length is controlled independently of level | `docs/STATUS.md` row 17d: `LENGTH_RECOVERS_LEVEL` fired in both arms. "Length-matched" now appears once, explicitly attached to RQ1-H corpus items. |
| That either verifier is more accurate | Pre-committed 2026-08-11: no such claim from dev-82. The abstract gives the two figures in different roles and never adjacent as a comparison. |
| That the system is an autonomous multi-agent system | `src/agents/graph.py`; `src/agents/README.md`. Handled positively — "two of which make no model call" — rather than by a denial. |
| That Verifier-B calibration improved | `CALIBRATION_NOT_ESTABLISHED`; the CI straddles zero. Only Verifier-A's ΔECE appears. |
| That the seeds are replications | They are paired blocking factors; the abstract says "paired generation seeds". |
| That personas or audience segments exist | Decision 12a retired both *persona* and *cluster* as scientific claims. |

## Part 8 — Keywords

Current list names eight terms. Two changes proposed:

- **Remove** *neuro-symbolic AI* as a bare term or keep it — but if kept, the
  abstract must state the null, which the revision now does. Recommend **keep**.
- **Remove** *multi-agent systems*, **add** *compound AI systems* and
  *evaluator–optimizer workflows*. Reason: the title keeps "Multi-Agent
  Framework" for continuity, but the keyword field is where indexing happens, and
  indexing this under multi-agent systems invites reviewers who will look for an
  autonomy claim that the thesis correctly refuses to make.
- **Add** *proxy gaming* alongside *Goodhart effect* — the 2023–2026 literature
  uses both, and the second alone under-retrieves.

Proposed: Bangla natural language processing; controllable text generation;
neuro-symbolic AI; compound AI systems; evaluator–optimizer workflows;
retrieval-augmented generation; verifier-in-the-loop; proxy gaming; Goodhart
effect; human evaluation.

## Part 9 — The two decisions, both now resolved

Both were answered by Sabbir on **2026-08-25** ("koro"), together with approval of
the Phase 1 structure recommendation. Recorded here rather than deleted, because
the reasoning is what makes the resulting wording defensible.

1. **Objectives wording — RESOLVED, and my question was malformed.** I asked him
   to "confirm or replace the three objectives" as though the thesis had none.
   `docs/chapters/chapter1/Introduction.md` §1.4 already contains **five
   operational objectives in his words**, and §1.9 says so explicitly
   (*"four research questions and five operational objectives"*). The real
   question was only how to compress five into an abstract, and the answer was
   four rather than three — see *On the objectives* in Part 3 for the mapping.
   This was the eighth absence claim in this review that the repository had
   already answered; the pattern is recorded in memory and is the reason the
   mapping is now written down instead of assumed.
2. **The 3.000-call comparison in ¶3 — RESOLVED: keep.** Sharpened since the
   original recommendation. The decisive argument is not that the matching was
   pre-registered (true, `primary_budget: matched_realized_generator_flops_to_row6`
   in `configs/s5_main_bn.yaml`, wired at `run_s5_main_bn.py:341`) but that
   **`docs/STATUS.md` row 23 restricts the inferential family, and a call count is
   not an inference.** 1.63–1.89 against 3.000 is arithmetic over a logged
   counter, in the same category as a token count; what must stay descriptive is
   the word *therefore*, and the abstract never uses it. Independently, his own
   §1.4 objective 5 names **computational cost** as a registered comparison
   dimension, so the figure is inside the registered design rather than an
   addition to it.

**Provenance of this document.** Written under the standing delegation *"jeta
valo hoy koro"*. The defect list, the revised wording and both keyword changes
are mine, endorsed not authored, following the convention `docs/protocol.md`
already uses for delegated decisions. No literature search supports the keyword
recommendation: no search index is reachable from this environment (alphaXiv and
arXiv blocked by the network allowlist, `WebSearch` unsupported for this model,
Consensus quota exhausted until 1 September 2026). That gap is owed a
`docs/protocol.md` deviations row, to be committed with the Phase 3 rewrite.

---

## Part 10 — Should the abstract live in `docs/chapters/`?

**Recommendation: no. Keep it in `docs/thesis_front_matter.md`.** Checked before
answering, because the question is about a convention and the convention is
written down.

What the repository already says:

- `docs/thesis_assembly_order.md` item 5 of **Front matter** is *"Abstract and
  keywords — `docs/thesis_front_matter.md`"*. The abstract is front matter in the
  assembly order, not main text.
- `docs/chapters/` contains exactly the seven main-text chapters, and the
  assembly order's **Main text** section lists exactly those seven files in
  order. The folder currently maps one-to-one onto that list. Adding an
  eighth, non-chapter file breaks that mapping, and the file would then need a
  name that lies — `chapter0_abstract.md` would be the obvious choice and the
  abstract is not chapter zero.
- Nothing would *break*. No script reads `docs/thesis_front_matter.md`; only
  `thesis_assembly_order.md` and `docs/lab_notebook.md` reference the path. So
  this is a convention cost, not a build failure — which is why it is a
  recommendation and not a refusal.

**The reason worth more than the convention.** Front matter is where the
institutional fields go — legal name, student ID, department, supervisor,
declaration wording — and those are still pending. Title, abstract, keywords and
those pending fields are one unit of work, filled in at LaTeX time in one pass.
Splitting the abstract away from them creates two places to remember instead of
one.

**What I will do at Phase 3 instead**, once the revision is approved: replace the
§Abstract section inside `docs/thesis_front_matter.md`, and move
`docs/thesis_abstract_v2.md` to `docs/legacy/` in the same commit. Two abstracts
on disk means one of them is stale, and that is the failure `CLAUDE.md` warns
about for "where are we" — it applies just as well to "what does the abstract
say".

**If you want it in `chapters/` anyway,** say so and I will do it, but then
`docs/thesis_assembly_order.md` must be edited in the same commit so the two
files do not disagree. A pointer that points at the wrong place is worse than an
inconvenient pointer.
