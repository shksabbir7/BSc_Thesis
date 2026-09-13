# Phase 1 Audit — Addendum: Resolved Gaps and Settled Decisions

**Date:** 2026-08-25
**Companion to:** `docs/thesis_phase1_audit_report.md`
**Status:** closes 11 of the 26 items in Part 4 of that report. Nothing in
`docs/chapters/`, `results/`, `configs/` or either `.bib` file was modified.

Every value below was read from the repository or computed read-only from a file
already in it. Where I computed something rather than reading it, that is stated
explicitly and the number is marked **unregistered** — meaning it must pass
through a proper pipeline step with a lab-notebook entry before it may appear in
the thesis.

---

## Part A — Decisions you settled

| # | Decision | Consequence for the thesis |
|---|---|---|
| 1 | University BSc thesis first; IEEE reference style | Structure follows the 8-chapter recommendation in the Phase 1 report; IEEE numeric citations from `references_ieee.bib` |
| 2 | No university template mandated | I propose the structure; you retain veto |
| 3 | Institutional front matter deferred to LaTeX-writing | Front matter stays a stub through Phase 3; not a defect until then |
| 4 | Figures deferred | Figures 3.1, 3.2, 4.2 remain unbuilt; Chapter 3 stays figure-less for now, and this is now a known deferral rather than an oversight |
| 5 | **English arm out of scope — moves to future work** | See Part C |
| 6 | `references.bib` may be used, but only after the paper is reviewed | See Part D |
| 7 | Base-paper reading status deferred | Chapter 2 rewriting waits on this; noted in Phase 3 sequencing |

---

## Part B — Repository items resolved

### Item 11 — Backbone-sweep hyperparameters ✅ FOUND

`configs/s3_backbone.yaml`, block `training:`

| Setting | Value |
|---|---|
| Seeds | 42, 43, 44, 45, 46 |
| Learning rates | 2.0e-5 and 3.0e-5 |
| Epochs | 4 |
| Batch size | 16 |
| Max sequence length | 128 |
| SetFit pair-sampling iterations | 20 (published default, deliberately not lowered) |
| Decision rule | paired bootstrap, 10,000 resamples, α = 0.05, Benjamini–Hochberg |
| Tie-break (preregistered) | smallest parameter count, then BanglaBERT |

Optimiser, warmup schedule and weight decay are **not** in the config, so they
are Hugging Face `Trainer` defaults. Chapter 4 should state that explicitly
rather than leave them unmentioned — "library defaults, not selected" is a
reportable fact and is consistent with the config's own stance that the 82-row
dev slice is a reporting surface, not a selection surface.

The config also records the seven arms *with the reason each was included*,
including SetFit–LaBSE registered **with a pre-stated expectation of losing**.
That is preregistration of a prediction, and Chapter 4 §4.3 does not currently
mention it. It should — an expected loser that loses is evidence.

### Item 12 — Per-class verifier metrics ✅ COMPUTABLE, and I computed them

The results JSONs carry macro-F1 and an error count only, but
`results/s3c_verifier_a_dev_predictions.csv` and
`results/s3d_verifier_b_dev_predictions.csv` hold per-item `y_true`, `y_pred`
and `p_cluster1` for all 82 dev rows. Confusion matrices are therefore exact,
not estimated:

**Verifier-A** (frozen LaBSE + L2 logistic head) — 1 error in 82

| | pred 0 | pred 1 |
|---|---:|---:|
| **true 0** (n=53) | 53 | 0 |
| **true 1** (n=29) | 1 | 28 |

class 0: P 0.9815, R 1.0000, F1 0.9907 · class 1: P 1.0000, R 0.9655, F1 0.9825
→ macro-F1 **0.9866**, reproducing the reported 0.986555 exactly.

**Verifier-B** (fine-tuned BanglaBERT, seed 42) — 3 errors in 82

| | pred 0 | pred 1 |
|---|---:|---:|
| **true 0** (n=53) | 52 | 1 |
| **true 1** (n=29) | 2 | 27 |

class 0: P 0.9630, R 0.9811, F1 0.9720 · class 1: P 0.9643, R 0.9310, F1 0.9474
→ macro-F1 **0.9597**, reproducing the reported dev value exactly.

**My recommendation: include these, in a small Table 4.x — but not for
completeness.** Include them because they answer a question macro-F1 hides: both
verifiers' errors fall predominantly on true Level-1 items called Level-0
(1 of 1 for A, 2 of 3 for B), i.e. both are conservative about crediting
specificity. **And then say plainly that 1 error and 3 errors cannot support a
claim about error asymmetry.** Reporting the direction while refusing to
interpret it is stronger than omitting it, because a reviewer who computes it
from your published CSVs will otherwise wonder why you did not.

These reproduce published macro-F1 exactly, so no new scientific claim is
introduced — but the table is still a new result file and needs a lab-notebook
entry under the Definition of Done.

### Item 13 — Verbatim two-level operational definition ✅ FOUND — my gap report was wrong

I recorded this as missing. It is not. `docs/axis_definition.md` holds the
definition between parsed markers `<!-- AXIS_DEFINITION_BEGIN -->` and
`<!-- AXIS_DEFINITION_END -->`, and `src/agents/prompts.py` reads it from that
file at render time and **raises if the markers are absent**. The design is
deliberate single-sourcing: the docstring records that this repo had already
logged three incidents of corrected and uncorrected text living in two places
with only one edited.

So the `[VERBATIM …]` slot in Appendix E is not a gap — it is a pointer. The fix
is one sentence in Appendix E naming `docs/axis_definition.md` and the marker
pair, plus reproducing the Bangla block itself in the appendix.

The definition's recognition test deserves promotion into Chapter 3 §3.9
verbatim, because it is the clearest statement of the construct anywhere in the
project:

> **Level 0** — এই মন্তব্য প্রায় যেকোনো ছবির নিচে বসিয়ে দেওয়া যায়, আর তাতে কিছুই বদলায় না।
> *(this comment could be pasted under almost any film and nothing would change)*
>
> **Level 1** — এই মন্তব্য অন্য ছবির নিচে বসালে আর খাটে না।
> *(paste this comment under a different film and it no longer fits)*

That swap test is what makes the construct operational rather than impressionistic,
and §3.9 currently paraphrases it instead of quoting it.

### Item 14 — Human item-bootstrap resample count ✅ FOUND

`configs/s5_human_eval_bn.yaml`: `bootstrap_resamples: 10000`, `n_items: 100`,
`seed: 42`. So 10,000 applies uniformly across the paired condition bootstrap,
both verifier calibration bootstraps and the human item bootstrap. Chapter 6 and
Appendix B can state it once for the whole thesis.

### Item 15 — Environment, GPU and index library ✅ FOUND — with one thing to disclose

Main-run runtime, from `results/env_snapshot_s5_bn_kaggle.json` (commit `22124a8`):

Python 3.12.13 · Linux 6.12.90, glibc 2.35 · torch 2.10.0+cu128 · CUDA 12.8 ·
**Tesla T4 ×2** (16 GB each) · chromadb 1.5.9 · hdbscan 0.8.42 · langgraph 1.1.9 ·
numpy 2.0.2 · pandas 2.3.3 · scikit-learn 1.9.0 · scipy 1.16.3 ·
sentence-transformers 5.6.1 · statsmodels 0.14.6 · transformers 5.15.0 ·
umap-learn 0.5.12

**Chroma is confirmed** (`chromadb`), closing the Phase 1 gap where Chapter 5
named it but Appendix G omitted it.

**Disclose this:** the committed `requirements.lock.txt` describes a *different*
environment from the one that produced the results — transformers 4.57.3 vs
5.15.0, chromadb 1.4.1 vs 1.5.9, sentence-transformers 5.2.0 vs 5.6.1, torch
2.9.1+**cpu** vs 2.10.0+cu128. Both are legitimate (lock file = declared local
environment, snapshot = Kaggle runtime, and the snapshot header even says
`"mode": "snapshot_only (requirements.lock.txt NOT modified)"`), but a
reproducibility reviewer comparing the two will find a mismatch. Appendix A
should state in one sentence that the lock file pins the local development
environment while the per-step snapshots record the execution environment, and
that the snapshots are authoritative for every reported number.

### Item 16 — GPU wall-clock hours ❌ NOT RECONSTRUCTIBLE — and the existing disclosure is correct

`results/s5_main_bn_cases.jsonl` carries a `provenance.timestamp_utc` per case,
but the stage field reads `checkpoint_migration` with
`scientific_generation_unchanged: true`. Those timestamps therefore record when
the archive was migrated across commits, not when generation ran. The main-run
per-call log is not in the repository (`data/generated/` contains only
`s4_tau_calls.jsonl` from the S4 threshold work).

**Recommendation: do not attempt reconstruction. Keep the Appendix A.6
disclosure as written.** Deriving an hours figure from migration timestamps
would produce a number that looks authoritative and is wrong, which is worse
than the honest gap you already have. If a venue later demands a scalar, report
the hardware (2× Tesla T4) and the call counts (7,068 local + 654 hosted) and
state that wall-clock was not registered — that is a complete answer.

### Item 17 — "Gemma-4-31B" vs `gemma-4-26b-a4b-it` ✅ NOT A CONFLICT — I was wrong

Both strings are correct and refer to different components:

- `configs/s5_main_bn.yaml` → `gemini_judge.model: gemma-4-26b-a4b-it` — the
  hosted judge in experimental condition 9, `thinking_level: high`,
  `feedback_contract: enum_target_template_v1`, `max_attempts: 3`.
- `configs/demo.yaml` → writer `gemma-4-26b-a4b-it`, second role
  `gemma-4-31b-it` — the **post-run demonstration interface**, which the same
  file marks `backend_disclosure: live_gemma4_not_reported_s5_writer`, i.e.
  explicitly not a reported result.

So Appendix H.3 is describing the demo, not the experiment. The fix is
clarification, not correction: H.3 should name both models and state that the
demo's models are outside the reported experiment. Separately, the main text
should name the judge as `gemma-4-26b-a4b-it` at least once — currently the exact
identifier appears only in appendices.

### Item 18 — Judge and retry budget ✅ CONSISTENT

`configs/s5_main_bn.yaml` sets `max_attempts: 3` identically for the neural loop,
the symbolic loop and the judge loop, each annotated as a deliberately matched
budget. `src/agents/graph.py` confirms the semantics: FAIL with attempt < 3
returns to the Researcher with the query anchored; FAIL at attempt 3 emits
best-of-3 by Verifier-A with `gave_up=True`.

So "maximum three judgments" (Appendix A.4) and "up to two Writer retries"
(Appendix E.5) describe the same contract in different units — 1 initial attempt
plus 2 retries = 3 attempts. State it once, as attempts, and give the retry count
parenthetically.

### Item 19 — The §3.5 non-organic signature ✅ FOUND, and it is far stronger than Chapter 3 currently claims

Two results files carry this, one superseding the other. `s2b_register_probe.md`
asked whether `Sentiment == 2` is a different *kind* of text; `s2c_region_split.md`
supersedes it by showing the grouping variable is **raw row position, not the
label**. The superseded file is retained with a ⛔ banner — kept, in its own words,
because "a superseded claim that disappears is one nobody can audit."

**The finding: the source workbook is two corpora concatenated at raw row 1999.**

| Region | n | danda % | first-person % | exclaim % | comma-run % | median words | types / 1k tokens |
|---|---:|---:|---:|---:|---:|---:|---:|
| A_organic | 1,999 | 38.7 | 13.5 | 3.4 | 3.3 | 9 | 255.0 |
| B_uniform | 3,001 | 99.2 | 0.8 | 0.3 | 0.0 | 8 | 127.6 |

3,001 of 5,000 rows = **60.0%**, which is the "60%" Chapter 3 cites without
explanation.

The method matters: **every probe feature is orthographic or structural** —
character counts, punctuation, danda, length, and one closed pronoun set. None can
encode an opinion about a film, which is precisely why separation by these features
proves a difference of *form* rather than of content. A lexical feature would have
been worthless here, and the config says so in advance.

Four structural absolutes, on the class-2 slice (n = 1,618):

| Feature | Rate in others | Expected | Observed | log₁₀ p if same population |
|---|---:|---:|---:|---:|
| first-person pronoun | 9.22% | 149.2 | **0** | −68 |
| exclamation mark | 2.38% | 38.5 | **0** | −16.9 |
| comma run | 2.06% | 33.3 | **0** | −14.6 |
| danda present | 62.15% | 1,005.5 | **1,618** | −334.3 |

And the seam is a step, not a drift — rolling 100-row danda rate goes 29% at row
1949 → 60% at 1999 → 100% at 2049. Meanwhile rows 3000–3664 (label 1) and
3665–4330 (label 0) sit deep in region B and carry **the region's signature rather
than their class's**, which is what rules out sentiment as the grouping variable.
Region A contains zero class-2 rows, all 1,670 neutral rows being nested inside
region B, which is exactly why the first analysis mistook a file-layout artefact
for a semantic property.

**This deserves roughly a page in §3.5, not two sentences.** It is the evidence
that licenses discarding the full-corpus clustering result, and a reader who is
not shown "0 first-person pronouns in 1,618 consecutive rows" has to take the
rejection on trust. It is also, incidentally, a much more interesting finding than
the thing it displaced.

**~~Bonus resolution:~~ WRONG — corrected 2026-08-25.** I wrote: *"Region A
(1,897) + Region B (2,833) = 4,730, so the region analysis ran on the cleaned
corpus, not the 4,625-row deduplicated split surface. The ambiguity I flagged in
Phase 1 is closed — no question needed."* **Region B is 2,728, not 2,833**, and
the conclusion drawn from the false sum is also wrong. 2,833 was back-derived as
4,730 − 1,897, which mixes a *post*-dedup region A with a *pre*-dedup total. The
correct accounting has two rows, not one:

| Surface | Region A | Region B | Total |
|---|---:|---:|---:|
| After rule-based cleaning (`bn_clean.csv`) | 1,910 | 2,820 | 4,730 |
| After near-duplicate removal at 0.95 (split surface) | 1,897 | 2,728 | 4,625 |

Three independent confirmations, any one of which would have caught this:
`s2d_ktable_regionB.md`, `s2e_regionB_k2_profile.md` and
`s2f_regionB_k2_residual.md` all state n = 2728; the frozen split map's own
region composition sums to 177 + 1,276 + 1,275 = 2,728; and the two per-region
trap-check files show 1910 → 1897 (13 removed) and 2820 → 2728 (92 removed),
whose 13 + 92 = 105 matches the full-corpus removal exactly. Chapter 3's
Table 3.2 carried 2,833 and has been corrected in the Phase 3 rewrite, where it
also contradicted Table 3.1's own 93.3% source-recovery row, whose marginals are
1,897 and 2,728. The region analyses ran on the **deduplicated split surface**,
which is the opposite of what the withdrawn sentence concluded.

**A second withdrawal in this item.** Above I wrote that the sentence *"this
profile resembles known automated-production signatures"* is supported by b109.
It should not be cited: `docs/reference_key_map_full.csv` marks b109
`metadata_verified_not_full_read`, and STATUS row 49 excludes metadata-only
records from load-bearing claims. This is the same error as the b72 citation in
Chapter 1. §3.5 as rewritten therefore makes the negative claim only — region B's
register is inconsistent with organic reviewing — which the four structural
impossibilities establish with no citation at all, exactly as this item argued.

### Item 23 — Example generated outputs ✅ AVAILABLE

`results/s5_main_bn_cases.jsonl` — 5,400 lines, 16.4 MB, one JSON record per case
with `result.emitted.text` (the Bangla output), `final_scores.neural_score`,
`final_scores.symbolic_score`, token usage, `logical_generator_calls`, seed,
`finish_reason`, and a provenance block. Qualitative error analysis for Chapter 6
is fully supported, and examples can be selected by a stated rule rather than
hand-picked, matching how the Appendix E.7 trace was chosen.

### Item 24 — Standardised effect sizes ❌ ABSENT, but the better statistic is already there

`results/s5_main_bn_paired_statistics.csv` columns: `condition`, `baseline`,
`n_pairs`, `b_probability_delta`, `ci_low`, `ci_high`, `bootstrap_p`,
`mcnemar_p`, `discordant_condition_only_success`,
`discordant_baseline_only_success`, `bh_q_bootstrap_p`. No Cohen's d, no odds
ratio.

**Recommendation: do not add Cohen's d — add the two discordant-pair counts to
Table 6.2.** They are already computed and provenance-carried, and for paired
binary outcomes they are the natural effect description: for static few-shot,
137 cases succeeded only under the condition against 54 only under zero-shot.
That asymmetry *is* the effect, in units a reader can check by hand. Cohen's d
on a binary outcome would be a weaker summary requiring a new derived quantity.

If a reviewer later demands a single standardised number, the McNemar odds ratio
is a deterministic transform of two integers already in the table, and can be
added then with a one-line derivation.

### Unregistered observation — a realism finding the thesis is missing

Computed by me now, read-only, from `s5_main_bn_cases.jsonl` using **my own**
emoji regex, not the pipeline's registered emoji measurement:

| Condition | Cases with an emoji |
|---|---:|
| zero_shot | 28 / 540 (5.2%) |
| rag_only | 6 / 540 (1.1%) |
| external_role_self_critique | 3 / 540 (0.6%) |
| intrinsic_self_critique | 2 / 540 (0.4%) |
| static_few_shot | 1 / 540 (0.2%) |
| rag_neural_loop | **0 / 540** |
| rag_neural_symbolic_feedback | **0 / 540** |
| rag_symbolic_loop | **0 / 540** |
| blind_resampling | **0 / 540** |
| gemma4_26b_a4b_judge_loop | **0 / 540** |

Chapter 3 §3.2 records **zero emoji rows** in the source corpus under the
registered measurement. So zero-shot generation introduces an out-of-register
artefact at 5.2%, retrieval alone cuts it to 1.1%, and every verifier-mediated
condition eliminates it entirely.

**This is a candidate result, not a result.** It uses an unregistered feature
definition and would need a proper step using the pipeline's own emoji detector,
with a lab-notebook entry, before it could enter §6.8. I am flagging it rather
than using it because it points the same way as the length-JS and MAUVE
diagnostics while being far easier for a reader to grasp: the loop does not only
raise verifier scores, it removes a register violation that the corpus never
contained. If it survives registration, it is one of the more quotable findings
in the thesis.

---

## Part C — English arm: recorded as out of scope

Confirmed against data rather than assumed: **all 5,400 main-run cases carry
`prompt_arm: 'bn'`.** The English rendering exists in `docs/axis_definition.md`
between `AXIS_DEFINITION_EN_BEGIN`/`END` markers, and `src/agents/prompts.py`
supports an `"en"` arm, but it was registered as a *pilot factor* and never run in
the final experiment.

So your instruction matches what the repository already did, and no result changes.
Three consequences for the writing:

1. Chapter 5 should state that prompt language was registered as a pilot factor
   and the final experiment used the Bangla arm only — one sentence, which turns
   an unexplained absence into a deliberate scope decision.
2. Chapter 2's English-instruction citations (English-instruction prompting,
   language confusion, code-switching degradation) move from *method
   justification* to *future-work justification*. They stay cited; their role
   changes.
3. The parallel English capability becomes a concrete future-work item in
   Chapter 8: the arm is implemented and its definition is written, so the future
   work is "run the registered arm", not "build a new system". That is a much
   stronger future-work claim than a generic one, and it is true.

---

## Part D — Answers to your four questions

### 1. What is decision 5?

`docs/STATUS.md` line 370, an open writing decision recorded as yours:

> Frame the register finding in the **stylometry / authorship** literature or the
> **machine-generated-text detection** literature?

Now that Item 19 is resolved, the question is concrete. The "register finding" is
the corpus-seam discovery: 60% of the workbook carries a uniform signature
detected using orthographic and structural features only. Decision 5 asks which
research tradition you cite to establish that this *method of detection* is sound.

- **Stylometry / authorship attribution** — the classic frame. Function words,
  punctuation and character-level statistics distinguishing writers is stylometry's
  core method, so the technique is unimpeachable. The mismatch: stylometry
  *attributes* text to a known author, and you have no author to attribute to.
- **Machine-generated / synthetic text detection** — the modern frame. Your actual
  claim is about *authenticity of provenance*: 0 first-person pronouns and 100%
  danda termination across 1,618 consecutive rows is a template or automation
  signature, not an authorial style. This also matches what you conclude — a
  "Mendeley-hosted Bangla review corpus with unrecoverable row-level provenance",
  not a verified sample of organic opinion.

**My provisional reading: machine-generated-text detection as the primary frame,
with stylometry cited as the methodological ancestor that supplies the feature
family.** It matches the claim you actually make, and it is an active 2023–2026
area, whereas stylometry's canonical citations are older — which matters for the
recency requirement in `CLAUDE.md`.

#### DECIDED 2026-08-25 — and neither of the two options above wins

Sabbir directed a decision without waiting for a literature search. Recorded
honestly: **no literature search was possible.** Consensus quota is exhausted
(`thesis_final_copyedit_checklist.md`); alphaXiv, the arXiv API and every other
paper index are blocked by this session's network allowlist (only
`agentrouter.org` is reachable); the `WebSearch` tool is unsupported for this
model. Verified by attempting each, not assumed. A deviations row is therefore
owed in `docs/protocol.md`.

What broke the tie instead was a check of the repository. **Neither framing is
citable from this project's bibliography.** Both `.bib` files contain zero
entries matching *stylometry*, *authorship*, *provenance* (as a text-forensics
sense), *datasheet*, *data quality*, or *machine-generated text detection*. So
choosing either would have required importing a literature this project has never
read — exactly what Part D.3 forbids.

Two uncited 2025 entries already in `references_ieee.bib` point at a third
framing that fits the numbers better than either candidate:

- **b109** — Li et al., *Lost in Literalism: How Supervised Training Shapes
  Translationese in LLMs*, arXiv 2503.04369, 2025. Currently uncited.
- **b111** — Roy et al., *Advancing Bangla Machine Translation Through Informal
  Datasets*, arXiv 2512.13487, 2025. Currently uncited.

**Decision: frame §3.5 as a corpus-provenance finding. Characterise Region B's
signature as consistent with automated text production — normalisation plus
lexical simplification, of which translationese is the best-documented case — and
explicitly decline to name the generator.**

Three reasons, in order of weight.

**The numbers match this profile and not the others.** Region B carries 127.6
types per 1,000 tokens against Region A's 255.0 — *half the lexical variety*.
Add 99.2% danda termination, 0.3% exclamation and 0.0% comma runs and the profile
is simplification plus punctuation normalisation plus flattened affect. That is
the signature of text that passed through an automated process, and lexical
variety halving is its single strongest indicator.

**Stylometry is the wrong instrument for the wrong question.** Stylometry
attributes text to a *candidate author set*. There is no candidate set here and
none can be constructed, so adopting the frame invites "attributed to whom?" —
unanswerable. Stylometry still supplies the feature family (punctuation,
function words, character statistics separating text populations), so it belongs
in a methods sentence, not in the framing.

**"Machine-generated" is an overclaim that cannot be defended.** MGT detection
presupposes a *language-model* generator. These eleven orthographic and
structural features cannot distinguish an LLM from a translation system from a
rule-based normaliser from an ingest pipeline that stripped punctuation. The
first reviewer question would be "how do you know it wasn't normalised on
import?" and there is no answer. The corpus is Mendeley-hosted with unrecoverable
row-level provenance and uncertain vintage, so the LLM premise may not even be
chronologically available.

**Why this decision is safe to make without a search.** The claim §3.5 actually
needs is *negative*: Region B's register is inconsistent with organic reviewing,
therefore it cannot ground a claim about audience language, therefore Region A
only. The four structural impossibilities establish that with **no citation at
all** — 0 first-person pronouns where 149.2 were expected is an arithmetic fact.
Literature is required only for the weaker adjacent sentence, "this profile
resembles known automated-production signatures," which b109 supports directly.

So the decision reduces the citation dependency from *a literature this project
does not own* to *one paper it already owns, plus a stated non-claim*. That is
what makes it decidable today rather than blocked.

**Reversal cost and what a later search could change.** The commitment is roughly
one framing paragraph plus two citations — under 300 words, no structural
dependency. If a search later shows the MGT-detection literature has features
that *can* separate LLM output from pipeline normalisation at 8-word lengths, the
frame can strengthen from "consistent with automated production" to a positive
identification. Nothing written under this decision would need retracting,
because "consistent with" does not become false when something more specific
becomes provable.

**Incidental finding: the two-bib-file defect, demonstrated.** b109 and
`references.bib`'s `axiv2503_04369_literalism` are the same paper (arXiv
2503.04369) entered twice under incompatible key schemes — and the
`references.bib` copy reads `author = {AUTHORS UNRESOLVED ...}` while the IEEE
copy carries all eight names. One paper, two keys, one of them unusable. This is
concrete evidence for the migration in Part D.2.

### 2. Item 10 — what I was talking about

Your bibliography keys are literally `b1`, `b2`, … `b143`, and IEEE style numbers
references in order of first citation. Right now those two orderings coincide:
`b1` is cited first, `b2` second, and so on through `b55`. Tidy — and fragile.

Suppose Phase 3 adds one citation in Chapter 2 that should become reference 12.
Then old `b12` must become `b13`, old `b13` becomes `b14`, and so on to `b143` —
in the `.bib` file *and* in every `[@bN]` marker across seven chapter files. One
inserted citation forces a global renumber. Phases 3 and 6 will add several.

This is self-inflicted, because BibTeX assigns the printed numbers itself. If the
key were `huang2024selfcorrect` instead of `b12`, insertion would cost nothing and
the rendered IEEE output would be byte-identical.

**Recommendation: migrate to semantic keys before Phase 3.** It is a scripted,
reversible find-and-replace across 7 chapters and 1 `.bib` file, verifiable by
checking that the compiled reference list is unchanged, and it removes an entire
class of error from the rest of the project. Doing it once now is much cheaper than
renumbering repeatedly under deadline. Say the word and I will script it as its own
commit, touching nothing else.

### 3. Item 8 — `references.bib`, used properly

Understood, and I will hold to the condition: an entry gets cited only after I have
read enough of the actual paper to know it supports the specific sentence citing
it. No title-match citations.

The mechanics, so you know what I am working with. There are two files with
incompatible key schemes: `references_ieee.bib` (143 entries, keys `b1`–`b143`,
the one your chapters cite) and `references.bib` (129 entries, semantic
author-year keys, cited by `docs/protocol.md` and `docs/related_work.md` but by no
chapter). Anything from the second file must be re-keyed into the first to be
citable from a chapter — which is a further argument for the semantic-key
migration in Part D.2, since after it the two files share one scheme and the
duplication problem largely dissolves.

Separately, **88 of the 143 entries in `references_ieee.bib` are already uncited**,
and they are not junk: they cluster tightly around reward hacking, self-correction,
clustering validity, calibration and conformal prediction, Bangla NLP, multilingual
model internals, decoding, in-context learning, and RAG faithfulness. That is a
deliberately collected 2025–2026 corpus which never reached the prose. So the first
place I will look for a needed citation is that unused set, before touching
`references.bib` at all. I will report in Phase 6 which of the 88 earned a citation,
which stayed out, and why.

### 4. Primary contribution — what I actually find

You said your domain is multi-agent systems. I have to tell you something
uncomfortable first, because it is better heard from me now than from an examiner
later.

**The thesis does not support a claim that multi-agent architecture is what
worked.** Three reasons, all from your own artifacts:

- The frozen inferential family is nine condition-vs-zero-shot comparisons and
  contains **no active-vs-active contrast**. So the loop was never tested against
  self-critique.
- The numbers make that gap conspicuous. Your best loop is +0.2570; **intrinsic
  self-critique — one model, no agents, no retrieval — is +0.2147**, and blind
  resampling is +0.2087. The architecture's apparent margin is about 4 points and
  is statistically untested.
- `src/agents/graph.py` says it outright: *"Never describe this as an autonomous
  multi-agent system … Two of the four components make no LLM call at all."* And
  Chapter 2 §2.5 already concedes the study "does not constitute a direct
  single-agent-versus-multi-agent architecture ablation."

If Chapter 1 claims architectural superiority, that is the sentence a reviewer
attacks, and they will win. Do not write it.

**Here is what you do have, and it is a multi-agent-systems contribution.**

Your code names its own identity precisely: *a compound AI system implementing the
evaluator–optimizer workflow, with predefined control flow.* The hard, unsolved
problem for such systems is not building them — it is **evaluating them honestly**,
because the verifier that drives the loop is also the thing you would naturally
measure success with, and that makes every reported improvement partly
self-congratulation.

You solved that, and you solved it structurally rather than rhetorically:

> **Primary contribution.** A verifier-isolation protocol for evaluator–optimizer
> systems — an in-loop verifier the system may optimise against, and an outcome
> verifier made independent by construction (disjoint training rows, a different
> pretraining family, a different tokenizer) and sealed from the loop by an
> executable guard — together with evidence that the protocol *detects* proxy
> overoptimisation: on continuing neural-loop cases the in-loop score improves
> while the same-case gap to the held-out verifier widens by +0.182802 (n = 147).

Three things make that a real contribution rather than good hygiene. The
independence is *architectural*, not asserted — different data, different encoder
family, different tokenizer, and an AST scan of `src/agents/` with a companion test
proving the guard can fail. The diagnostic *fired*, so you are not proposing an
untested safeguard. And it is transferable: nothing in it is specific to Bangla, to
cinema, or to this label.

The Bangla low-resource setting is what makes it *credible* — 804 and 888 training
rows, 8-word texts, no benchmark to hide behind — rather than what the contribution
is about. Frame Bangla as the stress test, not the subject.

There is a second finding I would push almost as hard, because it is a warning the
field needs: a **frozen** LaBSE linear probe scored 0.9866 against the best of
seven fine-tuned transformer arms at 0.9647, registered `TIE`. The reason is that
the label was created by K-means *in the probe's own representation space*. Anyone
who clusters embeddings and then trains a verifier on those clusters will get a
spectacular verifier that measures its own geometry. You found that in your own
pipeline and reported it instead of banking the 0.9866. That transfers far beyond
this thesis.

**What I would not claim:** *predictive* value for the symbolic scorer. That is
registered as unavailable and the numbers are unambiguous — every grouped held-out
fold selected w = 1.0, mean ΔAUC against neural-only was 0.0000, and symbolic-only
AUC was 0.3417 (length-controlled) and 0.0656 (free length) against neural-only's
0.8333 and 0.8658. An AUC of 0.0656 is far worse than chance. So no hybrid-accuracy
claim, no decision-boundary claim, no selected w.

**RETRACTED 2026-08-25 — my claim that this leaves "Neuro-Symbolic" unsupported.**
I wrote that and it is wrong. Sabbir challenged it; the repository does not support
me. Three things I failed to check before writing it:

1. **`docs/protocol.md:1929` preserves the symbolic role explicitly** while
   retiring the predictive claim: *"The symbolic component remains available only
   for its separately registered failed-rule-naming role."* `STATUS.md:175` and
   `chapter5_multi_agent_system.md:113` say the same. The role was retained by
   registered decision, not left over by neglect.
2. **That role is load-bearing, not decorative.** `reflector.py`'s `failed_rules()`
   decomposes the symbolic logistic into exact per-feature signed contributions —
   `coef × z` is the contribution, nothing estimated, nothing re-fitted — and
   returns the three pushing hardest away from the target level. It is the *only*
   source of error-localised feedback in the loop; remove it and the Reflector has
   nothing specific to say. Its docstring registers the reason as **interpretability,
   not accuracy**, and cites Tyen et al. 2024 plus the Self-Refine ablation for why
   localised feedback beats generic.
3. **§1.6 contribution 4 already claims exactly this** — *"an auditable
   neuro-symbolic workflow combining R1-only retrieval, neural acceptance,
   **symbolic failure descriptions**, bounded feedback, and persistent attempt
   traces."* And **§2.4 already draws the distinction I accused the thesis of
   missing**: *"A neuro-symbolic design must therefore state whether symbolic
   information changes the decision boundary, explains a neural decision, or guides
   a subsequent repair; these are different claims."* The thesis claims the third
   and disclaims the first, in advance, in the literature chapter.

So "Neuro-Symbolic" in the title is supported, as an architectural descriptor and
as repair guidance. What is unsupported is a decision-boundary claim the thesis
never makes.

**Also retracted: the recommended §1.7 fix.** §1.7 already defines *pre-release*
("using plot synopses before authentic post-release comments are available") and
disclaims named individuals, demographics, psychological profiles, naturally
occurring audience segments, film-level realism, audience composition, box-office
performance and individual preference. It does the work I proposed adding. There is
no title-versus-body gap to close.

**The one residual, and it is polish rather than a defect.** §1.7 is the only place
that never mentions the symbolic component, so a reader checking the title against
the scope section finds three of four terms addressed there and the fourth
addressed in §2.4 and §5.3. One clause in §1.7 — symbolic evidence guides repair
and does not move the accept/reject boundary, see §5.3 — would make the scope
section self-contained. A clause, not a paragraph, and optional.

**What survives from the original concern, reframed.** The 50.8% and 39.2%
verdict-sensitivity figures mean symbolic weight *would* have moved PASS/FAIL
decisions had it been given any. That is the argument for why w = 1.0 was
necessary rather than merely cautious, and §5.3 currently reports the number
without drawing that conclusion. Worth one sentence in Phase 3.

---

## Part E — Canonical contribution list (approved 2026-08-25; C6 added same day)

Six contributions, replacing both the seven in §1.6 and the four in §7.10 — so
neither existing list survives, which is the honest outcome. Ordered by strength of
evidence. Each is stated so it can be defended in a viva with one number, and each
is deliberately bounded, because at BSc level a modest claim you can prove beats an
ambitious one you cannot.

Sabbir approved the first five on 2026-08-25. **C6 was added later the same day
after he challenged my claim that "Neuro-Symbolic" was unsupported and the
repository proved him right** — so the approved list is five items plus one
correction, and C6 needs his sign-off separately.

**C1 — A verifier-isolation protocol with a working proxy-divergence diagnostic.**
Verifier-A (804 R1 rows, frozen LaBSE + L2 logistic head) and Verifier-B (888
disjoint R2 rows, fine-tuned BanglaBERT), independent by construction and separated
by an AST-enforced wall with a test proving the guard can fail. Neural-loop
revisions widen the same-case A–B gap by +0.182802 (n = 147) in the direction
predicted under overoptimisation. → RQ4, Chapters 4 and 6.

**C2 — A bounded evaluator–optimizer workflow for Bangla, evaluated against a
compute-matched control set.** 5,400 frozen cases (90 held-out plots × 2 levels ×
10 conditions × 3 paired seeds), verified as 5,400 unique keys with no missing or
duplicate case. All nine active conditions exceed zero-shot, the largest at +0.2570
[0.2151, 0.2987]; the controls include blind resampling under a matched token budget
and an external hosted judge. Claim is *controllability under matched cost*, not
architectural superiority. → RQ2, Chapters 5 and 6.

**C3 — A construct-validation methodology that rejected its own first result.**
Full-corpus clusters were discarded on evidence that they identify corpus source at
93.3% accuracy (ARI 0.7487, φ 0.861); the surviving Region-A cut is reported with a
Region-B negative control that passes stability while failing content replication;
a failed ordinal instrument (α = 0.4970) is retained alongside the successful
comparative intrusion task (0.780 and 0.840 against 0.25 chance). → RQ1, Chapter 3.

**C4 — A transferable circularity warning for cluster-derived labels.** A frozen
linear probe on the label-generating encoder reached macro-F1 0.9866 against 0.9647
for the best of seven fine-tuned backbones, registered `TIE` (minimum unadjusted
p = 0.096). Cluster-derived labels are near-linear in the representation that
produced them, so verifier accuracy on such labels is not evidence of construct
learning. → Chapter 4.

**C5 — Blinded human validation of requested-level recovery.** Three native-Bangla
annotators, 300 judgments on an outcome-blind balanced 100-item subset: 0.9133
pooled target-level match [0.8667, 0.9567], raw three-way agreement 0.8800,
nominal Krippendorff α 0.8405 [0.7473, 0.9200]. → RQ2, Chapter 6.

**C6 — Placement, not presence, is what determines whether symbolic evidence
helps.** *Added 2026-08-25 correcting my erroneous exclusion (Part D.4), then
restated the same day after Sabbir asked whether I had actually checked it. I had
not. The restatement below is what the evidence supports; my first version
asserted "guides repair" from the code's design intent, which is not a result.*

Verified from primary sources, in the order that matters:

1. **No predictive value as a decision component** — `results/s4_w_sensitivity.md`:
   every one of five grouped held-out folds selected w = 1.0, mean ΔAUC +0.0000,
   symbolic-only AUC 0.3417 (length-controlled) and 0.0656 (free length) against
   neural-only 0.8333 and 0.8658. Audit state `PRECOMMITMENT_UNRESOLVED`.
2. **The two gates were matched on first-pass rate, so the comparison is not
   confounded by strictness** — `configs/s5_main_bn.yaml` sets
   `symbolic_gate.target_first_pass_rate: 0.65` explicitly "matches S4 neural
   first-pass 39/60", giving τ = 0.1816651 against the neural gate's 0.4384071.
3. **The same component sits at both ends of the nine-condition ranking**
   (`results/s5_main_bn_paired_statistics.csv`, deltas in Verifier-B target
   probability against zero-shot):

   | Placement of the symbolic scorer | Condition | Δ vs zero-shot | 95% CI | BH q |
   |---|---|---:|---|---:|
   | guides repair (with neural gate) | `rag_neural_symbolic_feedback` | **+0.2570** | [0.2151, 0.2987] | 0.0002 |
   | absent (neural gate only) | `rag_neural_loop` | +0.2354 | [0.1934, 0.2772] | 0.0002 |
   | **is** the gate | `rag_symbolic_loop` | **+0.1091** | [0.0649, 0.1524] | 0.0002 |

   Symbolic-as-feedback is the **largest** of the nine deltas; symbolic-as-gate is
   the **smallest**, below `rag_only` at +0.1182 — i.e. gating on symbolic evidence
   scored worse than doing no repair at all. A spread of 0.1479 across two
   placements of one component.
4. **The Goodhart trajectories separate the same way** (`STATUS.md` row 21,
   same-case adjacent transitions among continuing failures): neural loop
   +0.182802 (n=147) and +0.114836 (n=67); neural+symbolic feedback +0.141481
   (n=147) and +0.145979 (n=58); symbolic loop **−0.042224** (n=193) and
   +0.001396 (n=165). Proxy divergence is specific to optimising against the
   *neural* gate — the symbolic-gated loop barely drifts, because it is not
   pushing on Verifier-A at all.
5. **The design decision preceded the outcome.** The w-audit registering symbolic
   as available "only for its separately registered failed-rule-naming role" is
   dated 2026-08-18 (`protocol.md`); S5 generation completed 2026-08-22
   (`STATUS.md` row 18). Four days. So the ranking is consistent with a decision
   already on record, not a story fitted to it afterwards.

⛔ **What this contribution must not say, and what I nearly wrote.**
`STATUS.md` row 23 states it directly: *"This does not test neural+symbolic versus
neural-only: the frozen family contains only comparisons against zero-shot, and no
post-hoc contrast is invented."* The +0.2570-versus-+0.2354 difference and the
+0.2570-versus-+0.1091 spread are **descriptive orderings, not tested contrasts.**
Every claim above is either a registered vs-zero-shot result or explicitly labelled
descriptive. No causal claim that symbolic feedback produced the improvement.

**Why it is still a contribution under that constraint.** The registered result
(no predictive value) and the descriptive ranking (best when advisory, worst when
authoritative) point the same way, and §2.4 committed in advance to distinguishing
these exact three roles — moving the boundary, explaining a decision, guiding a
repair. The thesis claims the third, disclaims the first, and the data are
consistent with both. That is what supports "Neuro-Symbolic" in the title.
→ RQ3, Chapters 2 and 5.

**Open question this surfaced, not yet resolved.** `s4_w_sensitivity.md` prints a
length-only probe at AUC 0.9111 (bn, length-controlled) and 0.9894 (bn, free) and
calls it "the real baseline" — above neural-only's 0.8333 and 0.8658. A word count
recovers the requested level better than Verifier-A does. There is a registered
verdict label `LENGTH_RECOVERS_LEVEL` for this, so it is anticipated somewhere; I
have not yet checked whether Chapter 4 or 5 confronts it. It needs checking before
Phase 3, because a reviewer who reads that table will ask.

**Deliberately excluded:** the old §1.6 item 5 ("a matched ten-condition
experiment containing 5,400 cases"), which describes the method and is now the
evidence for C2 rather than a contribution in its own right. Nothing else is
excluded — my earlier exclusion of symbolic diagnosis was an error, not a
judgment.

---

## What is now unblocked, and what still blocks

**Phase 2 (abstract) can proceed** once you accept or amend Part E, since the
abstract must state the contributions and there is no point drafting it twice. Every
other input it needs — dataset statistics, experimental setup, quantitative results
— is confirmed and in hand.

**Closed 2026-08-25:**

- **Decision 5** — decided (Part D.1): corpus-provenance framing, register
  characterised as consistent with automated production, generator not named.
  Cites b109 and b111, both already owned and previously uncited.
- **The autonomy question** — decided: the system is not an autonomous multi-agent
  system and will not be made one. The determinism of the Critic is the measuring
  instrument for the primary contribution, so adding discretion would delete the
  finding rather than upgrade the architecture. Consequence for the writing: the
  thesis makes **no comparative claim about predefined control flow versus
  autonomous agents** — that would be a claim about the field, requiring a search
  I cannot run. It argues instead from its own instrument: a proxy that moves
  cannot measure drift against itself. That claim is provable from the code and
  the linear decomposition in `reflector.py`, needs no citation, and therefore
  removes the blocked dependency rather than waiting on it.

**Still open, and each of these is yours:**

1. Accept, amend or reject the five contributions in Part E.
2. Semantic-key migration before Phase 3 — yes or no (Part D.2).
3. The title-versus-body gap — whether the §1.7 clarifying paragraph is the fix
   you want (Part D.4).
4. Base-paper reading, deferred by you, which gates Chapter 2 in Phase 3.

**Owed to `docs/protocol.md`** — one Deviations row, dated 2026-08-25: two
framing decisions were made without the literature search that `CLAUDE.md`
requires, because no search tool was reachable. Reason and reversal cost recorded
above. Not written yet; it touches a tracked normative document and should be
committed alongside the Chapter 3 rewrite rather than on its own.
