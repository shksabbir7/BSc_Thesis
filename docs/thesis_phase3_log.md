# Phase 3 — chapter rewrite log

**Purpose.** A chapter rewrite changes tracked prose without producing a file in
`results/`, so the Definition of Done in `CLAUDE.md` does not fire and
`step_close.py` has nothing to scaffold. The rule behind it still applies: a
change whose reasoning was never written down cannot be defended later. This file
is that record, one section per chapter.

**Authorisation.** The structure applied here is §3 of
`docs/thesis_phase1_audit_report.md`, approved by Sabbir on **2026-08-25**
("koro"), together with the two open abstract decisions in Part 9 of
`docs/thesis_abstract_v2.md`.

**Standing constraint for every entry below.** No experimental result may change
without confirmation, and no number may enter a chapter unless it was read out of
a file in this repository during the same session that wrote it. Every figure
added below is listed with its source.

---

## Chapter 1 — Introduction

**Rewritten 2026-08-25.** 1,919 → 2,944 words. Nine sections → eleven.
(Word count re-measured 2026-08-25 after the `b72` removal below; the figure
first recorded here, 2,920, predated the last two edits to the chapter.)

### Structural changes

| Old | New | Change |
|---|---|---|
| 1.1 Background and motivation | 1.1 Background: pre-release audience response and Bangla cinema · 1.2 Motivation and the limits of synthetic audiences | Split. The old §1.1 carried three jobs in three paragraphs: pre-release framing, synthetic-audience risk, and the Bangla setting. The risk paragraph is the motivation and now heads its own section. |
| — | 1.1 ¶3 | **New.** The methodological consequence of low-resource conditions: no external Bangla baseline was available, so every comparison is internal, so credibility rests on auditability. This is the paragraph that makes the rest of the design look necessary rather than elaborate. |
| — | 1.2 ¶2 | **New.** States what narrowing the question does to the success criterion — one declared property, recoverable by an uninformed reader — so §1.9's disclaimers read as a consequence of the design rather than as retreat. |
| 1.2 Research problem | 1.3 Research problem and central question | Renumbered; text unchanged. |
| 1.3 Research questions | 1.4 Research questions | Renumbered; text and Table 1.1 unchanged. |
| 1.4 Research aim and objectives | 1.5 Research aim and objectives | Renumbered. **Text unchanged, deliberately** — the five objectives are Sabbir's and were not touched. |
| — | 1.6 Mapping of objectives, RQs, chapters, contributions | **New, with Table 1.2.** Requested in the approved structure. |
| 1.5 Overview of the research design | 1.7 Overview of the research design | Renumbered; one paragraph revised (see below). |
| 1.6 Contributions (seven) | 1.8 Contributions (six, C1–C6) | Replaced. |
| 1.7 Scope and delimitations | 1.9 Scope and delimitations | Renumbered; text unchanged. |
| 1.8 Organization | 1.10 Organization | Rewritten for eight chapters. |
| 1.9 Chapter summary | 1.11 Chapter summary | Updated to name Table 1.2, six contributions, and blinded human evaluation. |

**Deviation from the approved structure, stated rather than absorbed.** The
approved §3 list for Chapter 1 ends at *1.10 Organisation of the thesis* and
contains no chapter summary, but the current chapter had one and Chapters 2–7 all
end with one. Silently dropping it would have made Chapter 1 the only chapter
without a summary. It is kept as **§1.11**. This is the only departure from the
approved list; it adds a section rather than removing or reordering one.

### The contributions: seven → six

The approved canonical list (C1 verifier isolation and proxy divergence, C2
bounded workflow under matched compute, C3 construct validation that rejected its
own result, C4 circularity, C5 blinded human validation, plus C6 symbolic
diagnosis separated from symbolic adjudication) replaces both the seven in the old
§1.6 and the four in §7.10. Chapter 7 has not yet been updated, so **the two
lists disagree until Phase 3 reaches Chapter 7.** Recorded here so the
inconsistency is a known intermediate state rather than a defect discovered later.

What happened to each of the old seven:

| Old contribution | Disposition |
|---|---|
| 1 — source-aware corpus audit | Absorbed into **C3**, which now carries the 93.3% provenance figure the old item stated without a number. |
| 2 — human-recognizable response construct | Absorbed into **C3**; both instruments, the failed ordinal one and the successful comparative one, are still reported. |
| 3 — dual-verifier isolation design | Became **C1**, extended with the transition figures that make the isolation consequential rather than merely tidy. |
| 4 — auditable neuro-symbolic workflow | Split: the workflow claim is **C2**, the symbolic-placement claim is **C6**. They were one item and they rest on different evidence — one on cost accounting, one on the `w` sensitivity curve. |
| 5 — matched ten-condition experiment | Absorbed into **C2**. A 5,400-case experiment is the apparatus that produces the other findings, not a finding. |
| 6 — held-out-verifier proxy diagnostic | Absorbed into **C1**, which is where isolation and divergence belong together. |
| 7 — blinded human evaluation | Became **C5**, extended with the interval and α. |

Nothing was dropped. The reduction is consolidation, not deletion, and the count
fell because two items were apparatus and two were halves of the same claim.

**Added closing paragraph.** §1.8 now ends by stating that no contribution
establishes multi-agent superiority over a single model, and gives the number that
makes the restraint necessary: the strongest single-model control improved on
zero-shot by +0.2147 against the framework's +0.2570, with no registered contrast
between them. This is the thesis's most attackable claim, and stating it in the
introduction is cheaper than being asked about it in a viva.

### Every number newly added to Chapter 1, with its source

Verified by extracting all numeric tokens from the old and new files and checking
each addition against a file in this repository. Nothing in the old chapter was
dropped.

| Value(s) | Where used | Source |
|---|---|---|
| +0.4835, +0.3006, +0.1828, 147, +0.1415 | C1 | `results/s5_main_bn_goodhart_paired_transitions.csv` — `rag_neural_loop` and `rag_neural_symbolic_feedback`, attempt 1→2 |
| +0.2570, [+0.2151, +0.2987], 1.630, 1.889, 3.000, +0.2147 | C2, closing ¶ | `results/s5_main_bn_reporting_tables_v2.md` |
| 93.3% | C3 | `results/s2b_register_probe.md` |
| 0.78, 0.84, 0.25 | C3 | `docs/STATUS.md` row 10 |
| 0.9866, 82 | C4 | `results/s3b_baselines.json`, `results/s3c_verifier_a.json` |
| 0.8667, 0.9567, 0.8405 | C5 | `results/s5_human_eval_bn_report.json` — `accuracy_ci_low`, `accuracy_ci_high`, `krippendorff_alpha_nominal` |
| 1.0, 0.0000 | C6 | `results/s4_w_sensitivity.json` — `w_chosen_per_fold` and `delta_auc_per_fold`, five folds, both conditions |

All eight citation keys (`b1`–`b8`) resolve against `docs/references_ieee.bib`;
none was lost in the rewrite.

**Correction entered 2026-08-25, after the Chapter 2 rewrite.** The sentence
above originally continued *"No new citation was added, because no literature
search is reachable from this environment and a citation chosen from memory is
worse than no citation."* That was false when written. A recount of `@bN` keys
across `docs/chapters/*.md` returned 61 rather than the expected 60, and the
extra key was `@b72` in §1.3 — added by me during this rewrite, in the clause
*"observed both in evaluator stress tests and in self-play against
reference-free LLM judges."* `git diff` confirms the addition.

The citation has been removed rather than retro-justified, and the clause now
reads *"observed under evaluator stress tests [@b7]"*, which is the literal
subject of `b7` (*Detecting Proxy Gaming in RL and LLM Alignment via Evaluator
Stress Tests*, Findings of ACL 2026). Three reasons for removing rather than
keeping:

- `docs/reference_key_map_full.csv` records `b72` as
  `registry_metadata_preserved` / `metadata_verified_not_full_read`, with a
  one-author entry and no DOI or URL. `docs/STATUS.md` row 49 states the policy
  that applies: *"Metadata-only records remain excluded from load-bearing
  claims."* §1.3 is the problem statement, which is load-bearing by definition.
- The claim imported a specific empirical finding — that reward hacking has been
  *observed* in self-play against reference-free judges — from a title. Chapter 2
  §2.8.2 handles record-level sources by disclosing the depth at the point of use
  before citing them; the introduction has no comparable place to put that
  disclosure without disfiguring it.
- `b7` already carried the proxy-gaming claim. The addition was decorative, and
  a decorative citation to an unread paper is the worst version of the trade.

`b72` is a genuinely relevant record for §2.7 once the paper has actually been
read. It is logged as a candidate there, not carried forward as a citation.

This was found only because the Chapter 2 numbers were recomputed rather than
reused. The recount is the control that caught it, which is the argument for
running it after every chapter rather than at the end of Phase 3.

### Two overclaims caught while sourcing these numbers

Both were mine, both were in my own Phase 2 abstract draft, and both would have
propagated into Chapter 1 had the numbers not been re-read from the result files.

1. **The transition figures were unattributed.** +0.4835 / +0.3006 / +0.1828
   belong to `rag_neural_loop`; the proposed loop reads +0.5381 / +0.3967 /
   +0.1415 on the same 147 cases. The abstract stated them one sentence after
   naming the symbolic-feedback loop as the largest effect, so a reader would
   have attached them to the wrong arm. Both conditions are now named — which
   also improves the finding, since divergence appearing with *and* without
   symbolic feedback makes it a property of verifier-guided iteration rather
   than of one condition.
2. **A registered non-result was written as a null.** The draft said the symbolic
   scorer *"carries no independent decision value."* `docs/STATUS.md` row 17e
   registers `PRECOMMITMENT_UNRESOLVED`, explicitly because verdict sensitivity
   across the 21-point grid was 50.8% / 39.2% and therefore not flat — and
   records that the code's catch-all had silently emitted `SYMBOLIC_INERT`, which
   an audit superseded precisely so the null would not be adopted. C6 now states
   the measurement and the unresolved standing, not a null.

Recorded as A2.9 and A2.10 in `docs/thesis_abstract_v2.md`, and both fixed there.

### Still owed on Chapter 1

- §7.10's four-item contribution list must be reconciled with C1–C6 when Phase 3
  reaches Chapter 7.
- `docs/chapters/chapter8_conclusion.md` does not exist yet; §1.10 describes it.
  `docs/thesis_assembly_order.md` now carries the same target state so the two
  files do not contradict each other in the interim.
- Table 1.2 references contributions by number. If the C-list changes, the table
  changes with it.

---

## Chapter 2 — Related Work

**Rewritten 2026-08-25.** 2,655 → 4,337 words. Ten sections → thirteen headings
(eleven numbered sections, two of them with subsections).

### Structural changes

| Old | New | Change |
|---|---|---|
| — | 2.1 Review methodology | **New.** The audit's largest Chapter 2 finding: the chapter carried 36 of 55 citations and never stated how they were found. The methodology existed in `docs/related_work.md` and the lab notebook; it was simply unwritten. |
| 2.1 Synthetic audiences | 2.2 | Renumbered; text unchanged. |
| 2.2 Self-correction and feedback | 2.3 | Renumbered. Two additions: Kamoi's small-training-data sentence, and a new paragraph on trained verifiers (see below). |
| 2.3 Retrieval-augmented generation | 2.4 | Renumbered. KBQA, BM25, BGE-M3 and LoRA now expanded at first use. |
| 2.4 Neural and symbolic validation | 2.5 | Renumbered and **expanded** with the two evidentiary bars, as the approved structure requires. |
| 2.5 Multi-agent workflows | 2.6 | Renumbered. Description tightened to match `src/agents/graph.py`: predefined control flow, not autonomous; Researcher and Critic make no model call. |
| 2.6 Verifiers, judges, proxy optimization | 2.7 | Renumbered. Opening sentence, previously uncited, now cites Cobbe. |
| 2.7 Bangla NLP | 2.8, with 2.8.1 and **2.8.2** | Split. The old section covered classification backbones only, leaving the evaluation half of the low-resource problem unaddressed. |
| 2.8 Human evaluation | 2.9 | Renumbered. New closing paragraph bridges to §2.10 — the audit flagged that §2.8→§2.9 jumped from instrument choice to a comparison table with no transition. |
| 2.9 Comparative position and gap · 2.10 Chapter summary | 2.10 Comparative position and research gap | **Merged**, as recommended. The old §2.10 restated §2.9's enumeration almost item for item. |
| — | 2.11 Chapter summary | Kept as a short forward transition only. |

**Deviation from the approved structure, same shape as §1.11.** The approved list
ends at *2.10 Comparative position and research gap* and the recommendation was
to merge the summary into it. The merge was done — §2.10 now carries the old
summary's substance — but a four-sentence §2.11 is retained so Chapter 2 is not
the only chapter without a summary heading. It restates nothing from §2.10; it
names the constraints the review imposes on the rest of the thesis and hands over
to Chapter 3.

### Why §2.1 is written the way it is

It reports the search practice that actually happened, including the parts that
are unflattering, because the alternative is a methodology section that describes
an idealised search and is therefore false. Three disclosures are deliberate:

- **The index substitution.** Consensus is the standing first-choice index; its
  quota was exhausted by 2026-08-11 with no reset until 2026-09-01, after which
  alphaXiv, Scite and primary records were used. This is recorded per entry
  throughout `docs/related_work.md` and is now stated in the thesis, because
  *"searched a different index"* and *"did not search"* are different facts and
  look identical in a bibliography.
- **Not a systematic review.** No PRISMA flow, no second screener, no screening
  agreement statistic. Stated outright so a reviewer does not have to ask why a
  review with no flow diagram calls itself systematic. It does not.
- **Uneven reading depth.** The sentence *"three were read in full, one
  partially, and two at record level"* is the six Tier-1 base papers, and it is
  the honest version of `docs/STATUS.md`'s highest-risk row.

Two numbers in §2.1 are *not* stated, deliberately. A per-work depth distribution
was attempted and abandoned: 29 of the cited keys are curated entries with no
legacy key in the reading register, so any distribution would have had an unclear
denominator. A screened-versus-retained count was also not stated, because no
screening count was ever recorded and inventing one is exactly what a methodology
section must not do. Both are logged here as owed rather than approximated.

### Citations added, and why each was necessary

Five keys were added. All five already existed in `docs/references_ieee.bib`, so
nothing was renumbered and no reference was chosen from memory.

| Key | Where | Why it belongs there |
|---|---|---|
| `b58` Cobbe et al. 2021 | §2.3 ¶3, §2.7 ¶1, and Chapter 5 §5.7 | **The main repair.** It was in the bibliography and cited in no chapter, while the sentence *"learned verifiers are widely used to score, rank, or select candidate outputs"* carried no citation at all and is that paper's contribution. It is also the ancestor of the `blind_resampling` condition, which is verifier-ranked best-of-N. Huang et al. §6 point at this work as the alternative to intrinsic correction, so omitting it broke the chain from the thesis's own theoretical anchor. |
| `b98` BenHalluEval 2026 | §2.8.2 | Bengali hallucination evaluation; supports treating Bangla generation quality as a documented risk rather than an assumption. |
| `b99` Bangla honorific dataset 2026 | §2.8.2 | Register and honorific failure in Bangla generation — the dimension the failure taxonomy has no category for. |
| `b110` BanglaSocialBench 2026 | §2.8.2 | Sociopragmatic and cultural alignment in Bangladeshi social interaction; *fluency does not guarantee appropriateness*. Its `references.bib` note already flagged it for Chapter 2. |
| `b111` Informal Bangla MT 2025 | §2.8.2 | Informal Bangla is under-resourced relative to formal Bangla, and this corpus is entirely informal comment text. |

**Depth is disclosed at the point of use.** All four §2.8.2 sources were read at
record level, and §2.8.2 says so in its own second paragraph before citing any of
them; they establish that a documented risk exists and no specific finding is
imported from them. Cobbe was also read at record level, which is why the claims
made from it are confined to what its abstract states: verifier-ranked selection
of sampled completions, improvement over the baseline, and better scaling with
data than fine-tuning. **No number from Cobbe is quoted anywhere.**

**Cobbe was deliberately kept out of Table 2.1.** A negative cell in that table is
a claim about what a paper does not report, and an abstract cannot support one.
The table caption now says this, and names Cobbe and Sands as the two record-level
sources discussed in prose instead of tabulated.

### The evidentiary bar added to §2.5

The audit's point was that §2.4 asserted complementarity without saying what would
count as evidence, which made the later `PRECOMMITMENT_UNRESOLVED` read as a
disappointment rather than as a pre-registration failure. Two bars are now stated
before the result: a **predictive** bar (a neural–symbolic mixture must improve
held-out discrimination under cross-validation grouped by `plot_id`, with the
three pre-specified outcomes and their fixed consequences) and a separate, weaker
**diagnostic** bar (naming a failed constraint need only change what the reviser
is told, assessed through loop behaviour and attempt traces). §2.5 then states
that the observed combination fell outside the registered partition, and that the
standing is unresolved rather than null.

The grouping description was verified against `configs/s4_w.yaml`: `group_by:
plot_id`, 5 folds over 30 plots, with the config's own reason — both levels of one
plot share a synopsis and ten retrieved exemplars.

### Numbers in §2.1, with their source

Every one was computed against the repository during this session; none is an
estimate. The first draft of §2.1 asserted the pre-rewrite figures (55 cited, 36
in this chapter, 26 recent) and they were stale within the same edit, because the
rewrite itself added five citations. They were recomputed after the additions.

| Value | Source |
|---|---|
| 60 distinct works cited thesis-wide | `@bN` keys extracted from `docs/chapters/*.md` |
| 41 in this chapter | same extraction, Chapter 2 only |
| 30 of 60 published 2025–2026 | `year` fields in `docs/references_ieee.bib`, intersected with the cited set |
| 6 predate 2013 | same; `b39` 1985, `b43` 1987, `b50` 1995, `b40` 2001, `b38` 2005, `b44` 2008 — each the original statement of a statistic the thesis reports |
| 143 records in the submission bibliography | entry count in `docs/references_ieee.bib` |
| 2026-08-08, 2026-08-11, 2026-09-01 | `docs/lab_notebook.md` and the Tier 9/10 headers of `docs/related_work.md` |

All 41 citation keys resolve against `docs/references_ieee.bib`; **no key from the
old chapter was lost.** Verified by set difference between the old 36 and the new
41.

**Re-verified 2026-08-25 after the `b72` removal described in the Chapter 1
section above.** The full-corpus recount, using `@(b\d+)\b` rather than a
bracket-anchored pattern so that continuation keys inside `[@b7; @b72]` are not
missed, returns: 60 distinct keys cited, 41 of them in Chapter 2, 30 published in
2025–2026, 6 predating 2013, 143 entries in the bibliography, **0 broken
citations**, 83 entries never cited. Every figure printed in §2.1 therefore now
matches a computed value exactly. It did not before: the recount is what exposed
`b72`, and had §2.1's numbers been carried over from the previous session instead
of recomputed, both the stale count and the unlogged citation would have shipped.

### An audit finding of mine that was wrong, and the half of it that was not

The Phase 1 report claimed that *"the keys `b1` through `b143` encode bibliography
order, so inserting any citation forces a global renumber of both keys and
prose."* As a statement about insertion it is false.
`src/common/build_thesis_bibliography.py` writes the header *"Stable source keys
b1, b2, ...; do not renumber existing entries"*, the curated block b1–b29 is
fixed, and later entries are appended in registry order. Display numbers are
assigned at render time by IEEEtran or the IEEE CSL in first-citation order.
**Citing `b58` and `b98`–`b111` therefore renumbered nothing**, and the approval
to "migrate now" that rested on this finding stays withdrawn.

The finding was nevertheless pointing at something real, which the first version
of this entry missed. `src/common/order_thesis_bibliography.py` exists precisely
to renumber: it walks `docs/thesis_front_matter.md`, the chapters, the AI
declaration and the appendices in assembly order, builds
`remap = {old: f"b{i}"}` from first-citation order, and rewrites **both** the
bibliography and every citation in the prose. `docs/STATUS.md` row 37 records
that it was run on 2026-08-23. So the current keys already encode first-citation
order as of that date, the five keys added today sit out of that order, and the
next run of the script will renumber every key in seven chapters at once.

Two consequences, both recorded rather than acted on:

- **The CSV audit map now lags the prose.** `b58`, `b98`, `b99`, `b110` and
  `b111` are cited but are not flagged `chapter_cited` in
  `docs/reference_key_map_full.csv`, so the three-set agreement reported in
  `docs/thesis_citation_apparatus_finding.md` §2 no longer holds for that column.
  Restoring it has exactly two routes: hand-edit five cells of a generated file,
  or re-run the ordering script and accept a global renumber. **That is Sabbir's
  call, not mine** — the first breaks the rule I invoked to withdraw the key
  migration, and the second invalidates every `bN` quoted in the Phase 1 audit
  report, this log and the citation-apparatus finding. Nothing was touched.
- **The renumber has to happen once, late.** It should be the last citation
  operation before rendering, after Chapters 3–8 are rewritten, so it is paid for
  once instead of once per chapter.

The insertion half of the claim remains the ninth false finding of the review,
with the same shape as the other eight: a plausible inference about the
repository, stated without reading the file that settles it. The difference here
is that the inference was aimed at the wrong file rather than at nothing.

### Still owed on Chapter 2

- **Three Chapter 2 works must be re-cited in Chapter 7** so the discussion closes
  the loop. Not done here: Chapter 7 has not been rewritten, and adding forward
  references to a chapter that does not yet contain them would create a dangling
  claim. One such claim was written and removed during this rewrite — §2.8.2
  originally said *"Chapter 7 records this as a limitation of the taxonomy"*, and
  Chapter 7 does not. The sentence now states the limitation in place.
- **`docs/related_work.md`'s gap table has an internal contradiction, not fixed
  here.** It marks Cobbe et al. ✓ under *Refine loop*, while
  `docs/base_papers_brief.md` says the opposite in as many words: *"Their verifier
  ranks; ours gates and refines. Best-of-N versus a verify–refine loop."* The
  register is Sabbir's reading state and this rewrite did not overwrite it; the
  error did not propagate, because Cobbe is not a row in Table 2.1. It should be
  corrected before that table is used for anything.
- A per-work reading-depth audit across all 60 cited works, which is Phase 6 work.
- `KBQA`, `BM25`, `BGE-M3` and `LoRA` were added to `docs/thesis_abbreviations.md`
  in the same edit. The registered verdict labels the audit also flagged
  (`TIE`, `CIRCULARITY_CONFIRMED`, and the rest) are still undefined for the
  reader; §2.5 avoids the problem by using prose instead of the token, but the
  chapters that report them still need a definition on first use.

### Repository housekeeping completed alongside this chapter

**`docs/reference_key_map.md` counts corrected.** This was item 4.1 of
`docs/thesis_citation_apparatus_finding.md`, deferred there so it could ride a
Phase 3 commit rather than a commit of its own. Option (a) of that finding was
applied: the counts were fixed and the historical 29-record table was left in
place under its `SUPERSEDED SNAPSHOT` banner, because the snapshot is the only
readable record of the pre-consolidation bibliography and deleting an audit trail
to remove an already-labelled inconsistency is a poor trade.

| Line | Was | Now | Basis |
|---|---|---|---|
| Banner | *"cite 55 unique sources"* | 60 | recount above |
| Intro ¶ | *"all 141 records (`b1`--`b141`)"* | 143, `b1`--`b143` | `grep -c '^@'` on `docs/references_ieee.bib` |
| Intro ¶ | *"Keys `b30`--`b141`"* | `b30`--`b143` | highest key in the bibliography is `b143` |
| Intro ¶ | *"the earlier 127-entry research registry"* | *"the earlier research registry"* | the 127 figure belongs to the 2026-08-23 state and is preserved in `docs/lab_notebook.md`; repeating it here invited a second stale number |
| §Audit corrections | *"all 112 unique research-registry records as `b30`--`b141`"* | 114, `b30`--`b143` | 143 − 29 = 114, confirmed by counting keys ≥ `b30` |

**`docs/lab_notebook.md` was deliberately not touched.** Its entry at the
consolidation date states *"The canonical total is 141 (`b1`--`b141`)"*, and that
was true on 2026-08-23. A lab notebook is an audit trail; back-dating a number
into a past entry destroys the record of when the count changed, which is the
only thing that entry is for. A later entry already carries the current figure.

**An inconsistency inside `docs/STATUS.md`, flagged and not silently resolved.**
Three rows state three different bibliography sizes: row 29 says **141**, row 37
says **142**, row 49 says **143**. All three are dated 2026-08-23 and they are
almost certainly successive states of the same day's work, with only row 49
current. The true figure is 143, confirmed against the file. `CLAUDE.md` gives
`docs/STATUS.md` precedence *on a number*, so this is exactly the case it warns
about: STATUS cannot arbitrate against itself, and the disagreement is reported
out loud rather than settled by picking the row that suits. **Sabbir's call**
whether the two superseded rows get a "superseded by row 49" marker or stay as
they are; the rows were left untouched.

---

## Chapter 3 — Data, Corpus Audit, and Construct Validation

**Rewritten 2026-08-25.** 2,279 → 8,075 words as measured over the whole file
(6,653 excluding table rows); 10 → 12 sections; 3 → 8 tables; 12 → 15 citation
keys. Retitled from *"Research Methodology, Data, and Construct Validation"*,
which over-promised: the chapter has never contained the framework, the
experimental design or the analysis plan, and the Phase 1 audit flagged the title
as describing a chapter three times its scope.

### Structural changes

| Old | New | Reason |
|---|---|---|
| §3.1 Research design and data roles | §3.1 Research design and the data-privilege contract | S0–S6 arc stated once, whole; audit found the pipeline was never shown end-to-end |
| — | §3.2 Data lineage and the isolation walls | New. Carries Figure 3.1's content as Table 3.1, per the figure deferral |
| §3.2 Primary review corpus and read-only audit | §3.3 (same) | Cleaning material moved out to §3.4; audit had the two mixed |
| §3.3 Cleaning and frozen data partition | §3.4 Cleaning and the frozen partition | Cascade table and threshold sweep added |
| §3.4 Plot corpus | **§3.11**, moved | It interrupted the §3.3 → §3.4 → §3.5 corpus thread |
| §3.5 Why full-corpus clusters were rejected | §3.5, expanded ~4× | Audit: *"decisive for the whole thesis"* yet *"two sentences with no description of what the signature was"* |
| §3.6 Region-A discovery and negative control | §3.6 + §3.7 split | Diagnostics separated from the argument they support |
| §3.7 / §3.8 human validation | §3.8 / §3.9 | Ethics pointer, exact *p*-values and inter-annotator figures added |
| §3.9 Operational definition | §3.10 | Retired-terminology constraint and the generated-text limitation added |
| §3.10 Chapter summary | §3.12 Chapter summary and the RQ1 verdict | Audit: no explicit RQ1 verdict anywhere in the chapter |

Deferred figures: **Figure 3.1** (data lineage) and **Figure 3.2**
(clusterability diagnostics) are not created — Sabbir, 2026-08-25: *"i don't need
the figure for now."* Their content is carried by Tables 3.1, 3.6 and 3.7 and the
deferral is stated in the text at both points, so no sentence depends on a figure
that does not exist.

### 🔴 One experimental number corrected — flagged, not changed quietly

**Table 3.2 of the old chapter gave Region B n = 2,833. The correct figure is
2,728.** `CLAUDE.md` forbids changing an experimental result without
confirmation, so this is surfaced rather than buried. The old figure is
unrecoverable from any result file; it was back-derived as 4,730 − 1,897, which
mixes a *post*-dedup region A with a *pre*-dedup total. Two surfaces exist:

| Surface | Region A | Region B | Total |
|---|---:|---:|---:|
| After rule-based cleaning | 1,910 | 2,820 | 4,730 |
| After near-duplicate removal at 0.95 | 1,897 | 2,728 | 4,625 |

Three independent confirmations: (i) `s2d_ktable_regionB.md`,
`s2e_regionB_k2_profile.md` and `s2f_regionB_k2_residual.md` all state n = 2728;
(ii) `data/splits/split_map_v1.json`'s region composition sums to
177 + 1,276 + 1,275 = 2,728; (iii) `s2a_regionA_trapcheck.md` and
`s2b2_regionB_trapcheck.md` show 1910 → 1897 and 2820 → 2728, i.e. 13 + 92 = 105
rows removed, matching the 105 removed on the full corpus. **The old chapter also
contradicted itself:** the contingency table behind its own 93.3% source-recovery
row has marginals 1,897 and 2,728. `docs/thesis_phase1_audit_addendum.md`
propagated 2,833 in a "Bonus resolution" paragraph; that paragraph is now struck
through and corrected in place.

### Four further defects fixed in the old text

1. **§3.6 claimed the richness inversion "holds in all four sentiment/length
   bands."** `s2f_regionA_k2_residual.md`'s Test D uses **length quartiles only**.
   Corrected to "length quartiles", and the separate per-sentiment length AUC test
   (Test A) is now reported as the sentiment control it actually is.
2. **§3.8 and Table 3.3 claimed both intrusion results at *p* < 1×10⁻¹⁵.**
   `results/intrusion_responses.csv` gives *p* = 5.740334×10⁻¹⁵ for annotator A,
   which is **not** below 1e-15. Now reported as 5.7 × 10⁻¹⁵ and 3.0 × 10⁻¹⁸.
   ⚠️ `docs/STATUS.md` row 5m also says "p < 1e-15", so STATUS disagrees with the
   result file it cites. Per `CLAUDE.md` this is stated out loud rather than
   silently resolved; the chapter follows the result file. **STATUS row 5m needs a
   one-character fix and I have not made it — Sabbir's call.**
3. **§3.8 said the intrusion sets used "fresh Region-A R1 material."**
   `configs/intrusion.yaml` sets `exclude_parts: [G]` — only G. The material is
   region A minus Gold-300, spanning R1 and R2. The "R1" narrowing is removed.
4. **§3.9 reported 414 and 269 types per 1,000 tokens as the axis direction
   evidence.** `docs/axis_definition.md` §4 explicitly labels these
   non-reportable — raw TTR over unequal corpora, inflated because TTR falls as
   tokens grow — and says *"S2e's numbers are the reportable ones."* §3.10 now
   leads with the equal-budget 1,913 / 1,623 figures and reports 414 / 269 as
   direction-only, with the reason stated.

### One material addition the old chapter omitted

**The full-corpus trap-check verdict is threshold-dependent, and this was not
disclosed.** `s2_pilot_ari_trapcheck.md` states the rule itself — *"If the
verdict column is not constant across these rows, the trap-check conclusion
depends on an arbitrary choice and must be reported that way"* — and on the full
corpus it is not constant: at 0.90 the ARI reaches 0.2181, crossing the
pre-registered 0.2 boundary, and the verdict changes from
`NOT_SENTIMENT_ALIGNED` to Band 2 `PARTIAL_OVERLAP + RESIDUAL_TEST_REQUIRED`. The
old §3.5 said only that the sweep was "reported ... rather than used to choose
the most favorable result", which is true of the reporting and silent about the
finding. Table 3.4 now shows all ten rows. The consequence is limited — §3.5
rejects the full-corpus partition on independent grounds — but it is a second
reason not to rest anything on it, and within each region the verdict is constant
across all three thresholds.

### Every number newly added to Chapter 3, with its source

| Number | Where | Source file |
|---|---|---|
| Region A/B split of every partition (123/177, 886/1276, 888/1275, 82/118) | Table 3.1 | `data/splits/split_map_v1.json` composition block |
| `input_sha256 = 295c839c…` | §3.2 | same |
| Full 11-row claim/observed audit table | Table 3.2 | `results/s0_data_xray.md` claim verification |
| Union decomposition: 2 + 72 + 204, ∩ = 10, union 268 → 4,732; normalised 270 → 4,730 | §3.3 | same, both decomposition tables |
| `null_rows: 1` is inconsistent with the *claimed* `usable_n` of 4,722, which used 2 | §3.3 | same, lines 39–41 |
| Mean 9.63 words; min 1; 12 reviews ≥ 50 words; 8.19/11.85/8.84 by label; 6 orphan `U+FE0F` rows | §3.3 | same, "Additional observed context" |
| Seven-step cascade with per-step counts and 254 whitespace-modified rows | Table 3.3 | `results/s1_cleaning_log.json` |
| Per-class drops 152/65/52 + 1 unlabelled; the `balance_note` | §3.4 | same |
| `review_id = bn_<row>`, zero-padded to 4 | §3.3 | same, `review_id` block |
| Threshold sweep, all ten rows, both regions and full corpus | Table 3.4 | `s2_pilot_ari_trapcheck.md`, `s2a_regionA_trapcheck.md`, `s2b2_regionB_trapcheck.md` |
| 119 pairs = 13 + 106; 105 removed = 13 + 92 | §3.4 | same three files |
| Keep-first-by-`review_id`, compare-against-kept-only, exhaustive upper triangle | §3.4 | same, "Method notes" |
| Cluster shares 39.2/30.9/29.9%; cluster 0 = 1,814 with 12 class-2 | §3.5 | `s2_pilot_ari_trapcheck.md` |
| ARI(region) 0.4813 vs ARI(sentiment) 0.1793; binary recast 93.3% / 0.7487 / 0.861 | §3.5 | same; recast registered in `docs/STATUS.md` row 5e from `results/s2_cluster_assignments.csv`. Independently recomputed from the 1700/114, 119/1308, 78/1306 crosstab: 93.276%, φ 0.8607, ARI 0.7487 |
| Region profile panel (38.7/99.2% danda, 13.5/0.8% first person, 3.4/0.3% exclaim, 3.3/0.0% comma run, 255.0/127.6 types per 1k) | Table 3.5A | `results/s2c_region_split.md` |
| Structural impossibilities (149.2/0, 38.5/0, 33.3/0, 1005.5/1618; log₁₀ p −68.0, −16.9, −14.6, −334.3) | Table 3.5B | `results/s2b_register_probe.md`. ⚠️ s2b's *interpretation* is superseded by s2c; its measurements are not, and s2c says so explicitly. Reported here as a property of the 1,618 class-2 rows, which is what was measured, with the region reframing supplied by s2c |
| Closed pronoun set আমি/আমার/আমাকে/আমরা/আমাদের/আমায়; verb forms not counted | §3.5 | `s2b_register_probe.md` definition note |
| Rolling danda 29 → 43 → 60 → 100% at rows 1949/1974/1999/2049 | §3.5 | `s2c_region_split.md` seam table |
| Rows 3000–3664 at 96.5%, 3665–4330 at 99.8%, 499–896 at 32.4% | §3.5 | same, per-run breakdown |
| Full K = 2–8 sweep, four criteria, both regions | Table 3.6 | `results/s2d_ktable_regionA.csv`, `s2d_ktable_regionB.csv` |
| HDBSCAN noise 1.0 and 0.966642 | Table 3.6/3.7 | `s2d_ktable_regionA.md`, `s2d_ktable_regionB.md` |
| Types at 4,000 tokens: 1,913.20 ± 19.52 vs 1,623.37 ± 21.35, bootstrapped 30× | §3.6 | `results/s2e_regionA_k2_profile.md` |
| Region B at the same budget: 1,186.33 ± 16.56 vs 1,181.27 ± 16.59 | §3.6 | `results/s2e_regionB_k2_profile.md` |
| First person 17.3% vs 8.8%; 66% positive vs 74% negative | §3.6, §3.10 | `docs/axis_definition.md` §1–§2 |
| Lift decomposition 60.25 / 69.53 / 65.47 / 70.06 → +9.81 pp, cutoff 10.0 | §3.6 | `results/s2f_regionA_k2_residual.md`. Recomputed from `s2e_regionA_k2_assignments.csv` by cell-majority: 60.2530 / 69.5308 / 65.4718 / 70.0580 |
| Test A 0.6115 / 0.6567; Test B \|φ\| 0.3133–0.4112; Test D at 1,100 tokens, 4/4 | §3.6 | same |
| Resubstitution caveat: low lift is strong evidence, high lift is a ceiling | §3.6 | same, verbatim reasoning |
| Region B strongest feature 0.5806 (`mean_word_len`); margin 0.0583; 12.2% within 0.02 | §3.6 | `s2e_regionB_k2_profile.md` |
| Region B residual +7.2 pp; Test A min 0.5276 `ENTANGLED`; Test B min 0.0828; Test D 1/4 | §3.6 | `results/s2f_regionB_k2_residual.md` |
| গল্প vs সিনেমা template families | §3.6 | same file's log-odds table |
| Pinto: k=2, silhouette ≈0.31, ARI 0.999±0.001, 50.6/49.4%, n=8,360, plus two verbatim quotations | §3.6 | `docs/protocol.md` deviations row 2026-08-10; `docs/STATUS.md` row 372 |
| Cornelissen: four-type typology an artefact, centroids near leading principal axes | §3.6 | same |
| Only 123 of Gold-300 are in region A; split map not regenerated | §3.8 | `results/g300_agreement.md` |
| 598 of 600 ratings; 298 doubly rated; 202/298 and 227/298 on the value 2 | §3.8 | same |
| Nominal α 0.4324; linear-weighted Cohen's κ 0.4456 | §3.8 | same |
| Gwet AC1 = 0.8705 | §3.8 | ⚠️ **no result file.** `docs/lab_notebook.md:2231`, corrected at `:2249`. The chapter's *use* of it is a refusal, not a claim, so nothing rests on it — but its provenance is a notebook entry and that is recorded here rather than implied to be a result |
| Wilson intervals [0.648, 0.872], [0.715, 0.917], [0.709, 0.929] | §3.9, Table 3.8 | `results/intrusion_responses.csv` |
| Exact one-sided *p* = 5.7×10⁻¹⁵, 3.0×10⁻¹⁸, 4.2×10⁻⁶ | §3.9, Table 3.8 | same |
| Inter-annotator 70.0% and 75.0%; agreement matches the 0.667 expected under independent errors | §3.9 | `results/intrusion_agreement.md`; the independence reading is `docs/STATUS.md` row 5m |
| Pooled 81/100 is not 100 independent trials | §3.9 | `results/intrusion_agreement.md`, verbatim |
| Both annotators reported the items looked alike | §3.9 | `docs/STATUS.md` row 5m |
| Length-only heuristic 0.16 | §3.9 | ⚠️ **no result file.** `docs/STATUS.md` row 5m, `docs/protocol.md` 2026-08-08 row, lab notebook. Absent from `src/annotate/intrusion_score.py` |
| Length-matching satisfies RQ1-D's binding condition *by construction* | §3.9 | `configs/intrusion.yaml` header, verbatim |
| The two causes of attempt 1's failure, only one diagnosed at the time | §3.8 | same header, verbatim |
| Verbatim Level 0 / Level 1 definition and the two swap tests | §3.10 | `docs/axis_definition.md` `AXIS_DEFINITION_EN_BEGIN` block |
| Generated-text axis recoverable from length at AUC 0.91–0.99 | §3.10 | `docs/protocol.md` deviations row 2026-08-17 |
| 924 API calls; 3,135 candidates; 124 passed; 2,925/65/15/6 rejection reasons; seed categories 66/57/1; sentence min 3 median 9 max 12; harvest 2026-07-31 | §3.11 | `results/plots_harvest_report.md` |
| Ethics: adult volunteers, voluntary consent, no honorarium, coded responses, no institutional review claimed | §3.7 | `docs/appendices/appendix_b_human_evaluation_ethics.md` §B.3–B.4 |

### Citations added, and why each was necessary

- **b73 (Pinto et al. 2026)** and **b74 (Cornelissen et al. 2026)** — §3.6 needs
  a defence for treating a stable k = 2 solution as a stratification rather than
  a discovery. Both are `full_or_primary_record` in
  `docs/reference_key_map_full.csv`, so they may carry a load-bearing claim, and
  both were already the registered basis of this framing in `docs/protocol.md`
  (2026-08-10) and `docs/STATUS.md` row 372 — they were cited nowhere in the
  chapters until now.
- **b56 (Monroe, Colaresi & Quinn 2008)** — §3.6 reports the region-B log-odds
  vocabulary contrast, which is that method. `full_or_primary_record`.

**b109 was considered and rejected.** `docs/thesis_phase1_audit_addendum.md` item
19 proposed citing it for *"this profile resembles known automated-production
signatures."* It is marked `metadata_verified_not_full_read`, which STATUS row 49
excludes from load-bearing claims — the same error as the b72 citation in
Chapter 1. §3.5 therefore makes only the negative claim, which the addendum
itself argues needs no citation at all. The addendum has been corrected.

**Mechanical recount after the rewrite**, `@(b\d+)\b` over
`docs/chapters/*.md` and `docs/appendices/*.md`: 63 distinct keys cited (60
before), 143 bibliography entries, 80 never cited (83 before), **zero broken
citations**. Chapter 3 itself went 12 → 15 keys, the three added being exactly
b56, b73, b74 — verified by diffing key sets against `git show HEAD:`, which is
the check that caught b72.

### Still owed on Chapter 3

1. **Chang et al. (2009) word/topic intrusion and Eklund et al. (2025) CIPHE are
   cited by `configs/intrusion.yaml` and `docs/protocol.md` but exist in neither
   `.bib` file** and are absent from `docs/related_work.md`. `docs/lab_notebook.md`
   flags them as owed at `:2456`, `:2460` and `:2609`. §3.9 describes the intrusion
   design without attributing it, which is a real gap: the task is not this
   study's invention. `docs/references_ieee.bib` is generated, so the entries must
   go into `docs/references.bib` and the bibliography be rebuilt — **not** hand-edited.
2. **A per-set or confusion breakdown of the intrusion task**, which the Phase 1
   audit asked for. `results/intrusion_responses.csv` holds six aggregate rows
   only. Computing a breakdown in an ad-hoc shell call would violate *"if logic
   lives in a notebook cell, it cannot enter the paper"*; it needs a registered
   script and a result file.
3. **Result-file backing for AC1 = 0.8705 and for the 0.16 length heuristic.**
   Both are currently notebook/STATUS figures.
4. **`docs/STATUS.md` row 5m says *p* < 1e-15** where the result file says
   5.740×10⁻¹⁵. Sabbir's call.
5. **A template copy-paste defect in three result files**, noted and not
   modified: `s2d_ktable_regionB.md`, `s2e_regionB_k2_profile.md` and
   `s2f_regionB_k2_residual.md` carry "(region A)" in their titles or metadata
   while reporting region B, and `s2f_regionB`'s preamble quotes region A's
   0.1522 / φ 0.3981 / 19.3-point figures. Anyone reading those files for region B
   numbers can be misled; the numbers in their tables are correct.
6. **One `docs/protocol.md` Deviations row** for the Phase 3 framing decisions
   taken without a Consensus search, the index being unreachable until
   1 September 2026.

---

## Chapter 4 — Verifier Development, Circularity, and Isolation

**Rewritten 2026-08-25.** 1,397 → 6,409 words. Eight sections → ten. Two tables
(one of them unnumbered) → seven numbered tables. Retitled from *"Verifier
Development and Validation"*, because "validation" overstates what the chapter
establishes: the verifiers reproduce a label, and §4.4 is the finding that this
is nearly circular.

The Phase 1 audit called this the *"shortest chapter in the thesis while carrying
its most reframing finding"* and asked for five things: substantial expansion to
parity with Chapters 3 and 5, a procedure listing for verifier training and
calibration, per-class metrics, the §4.7 table numbered, and a closing subsection
on what the circularity finding means for the rest of the thesis. Four are done.
The fifth is handled below and not silently dropped.

### Structural changes

| Old | New | Change |
|---|---|---|
| 4.1 Design rationale and verifier roles | 4.1 Design rationale, verifier roles, and what this chapter contributes | Expanded. Adds the statement the audit found missing everywhere: this chapter answers no research question by design, and supplies the instrument RQ2, RQ3 and RQ4 depend on. |
| 4.2 Training and evaluation protocol | 4.2 Training and evaluation protocol | Expanded with **Table 4.1** — all seven arms with model strings, kind, and the reason each was registered — plus the full shared budget and the disclosure that dev-82 carries three roles, quantified at 0.0122 macro-F1 per item. This is the audit's requested procedure listing. |
| 4.3 Backbone ablation | 4.3 Backbone ablation and the registered `TIE` | Expanded. Adds the field's own disagreement as the reason the ablation was necessary, and **Table 4.2** separated from the baselines it was previously mixed with. |
| 4.4 Circularity baseline and revised interpretation | 4.4 The circularity baseline | Split into 4.4 and 4.5. **Table 4.3** now carries the four reference points and the gap in items. |
| — | **4.5 What the circularity finding implies for the rest of the thesis** | **New.** The audit's central request. Four consequences: what a verifier score can mean, why A's cheapness is defensible rather than a compromise, why the Goodhart test is necessary rather than prudent, and how it bounds Chapter 3's stability numbers. |
| 4.5 Verifier-A | 4.6 Verifier-A: the in-loop scorer | Expanded with the full defaults, and the error-location finding described below. |
| 4.6 Verifier-B | 4.7 Verifier-B: the outcome scorer | Expanded with the recipe-versus-checkpoint distinction, the reason its learning rate was never tuned, and **Table 4.4** side by side with A. |
| — | 4.8 Calibration of both verifiers | Promoted from two scattered paragraphs into its own section with **Table 4.5** (T, ECE, Brier, NLL, ΔECE with CI, verdict) and **Table 4.6** (reliability bins). |
| 4.7 Executable isolation wall (unnumbered table) | 4.9 The executable isolation wall (**Table 4.7**) | The audit's request to number the §4.7 table. |
| 4.8 Chapter summary | 4.10 Chapter summary | Rewritten around the circularity finding rather than around a winning backbone. |

### Per-class metrics: what was done instead, and why

The audit asked twice for per-class precision, recall and a confusion matrix for
both verifiers. `results/s3c_verifier_a_dev_predictions.csv` and
`results/s3d_verifier_b_dev_predictions.csv` each hold 82 rows with
`review_id,y_true,y_pred,p_cluster1,correct`, so the material exists. Computing a
confusion matrix from them in an ad-hoc call would violate *"if logic lives in a
notebook cell, it cannot enter the paper"*, and a pending item already specifies
it should arrive as a small numbered table with its own lab-notebook entry. It is
therefore **owed work, listed below, not quietly skipped.**

What the chapter reports instead is entirely file-backed and answers most of the
question the audit was asking: the dev class counts 53/29 that make macro-F1 the
principal metric, error counts rather than decimals (A: 1 of 82; B's persisted
artifact: 3; B across five seeds: 1 to 4), and — from the reliability bins in
`results/s3c_verifier_a.json` and `results/s3d_verifier_b.json` — the asymmetry
in *where* the errors sit. **Verifier-A's single error is its least confident
prediction; two of Verifier-B's three errors are among the 81 items it scores
above 0.8 confidence.** That is not a restatement of the macro-F1 figures, it is
new information read out of the bin tables, and it is also the mechanism behind
B's `CALIBRATION_NOT_ESTABLISHED` verdict.

### Figure 4.2 — deferred, with its content carried numerically

Figure 4.2 (reliability diagram, both verifiers, before and after scaling) is
**not built**, per Sabbir's standing instruction of 2026-08-25 (*"i don't need
the figure for now"*). The chapter states the deferral in §4.8 rather than
referring to a figure that does not exist, and Tables 4.5 and 4.6 give
numerically every quantity the figure would have plotted — bin populations, mean
confidences and empirical accuracies for both verifiers at both stages. **No
claim in the chapter depends on the figure.** The manifest row stays "Data
present, figure missing".

### Citations

| Key | Work | Where, and why it is load-bearing |
|---|---|---|
| `b69` | Mahmoud et al. 2026, *Reward Hacking in Rubric-Based Reinforcement Learning* | §4.1. The dual-verifier design's external justification: separation between the optimised judge and the evaluating judge is the standard defence. Previously uncited anywhere in the thesis despite being cited by `results/s3d_verifier_b.md` as the basis for decision 16. |
| `b82` | Schneider et al. 2025, *Overtuning in Hyperparameter Optimization* | §4.7. The reason Verifier-B's learning rate was never selected. Its four aggravating conditions — small data, holdout, binary, accuracy-type metric — all describe this run, which is why the finding is quoted rather than a general appeal to overfitting. |
| `b83` | Zhang et al. 2026, *TabPFN beyond Tabular Data* | §4.6 and §4.8. Both directions: why the "natively calibrated" defence of Verifier-A was withdrawn, and why a logistic head is nonetheless right at 768 dimensions and near ceiling. The chapter also states the bound — their grid is ten-class and the gap narrows at two. |
| `b26`, `b27`, `b28` | Mitra 2025; Hassin 2026; Mazumder 2025 | §4.2 Table 4.1 and §4.3. Re-cited from Chapter 2 to carry the argument that the Bangla literature names three different winners, two of them on the same BanglaBlend data at 94.0 and 95.44 per cent. Verified against `docs/related_work.md:427,442,443` and `docs/protocol.md:945,946`, not from memory. |

`b53` (temperature scaling) and `b54` (adaptive scaling in low data) were already
present and are kept where they were, with §4.8 now stating the argument they
support: single-parameter scaling is correct here *because* n is small. Metadata-
only entries were deliberately not cited — the SetFit arm's pre-stated
expectation of losing is reported as a protocol fact without citing Beliveau or
Tunstall, both of which are `metadata_verified_not_full_read` and therefore
barred from carrying a load-bearing claim by STATUS row 49.

### Verification performed

**Numeric tokens.** 83 numeric tokens are new to the chapter relative to
`git show HEAD:`. Every one was located in a source file, with five resolved by
inspection: `0.5435`, `0.7500`, `0.9976`, `0.6430` and `0.6307` are four-decimal
roundings of the full-precision reliability-bin confidences in
`results/s3c_verifier_a.json` and `results/s3d_verifier_b.json`
(0.5434547395517607, 0.7500479578507667, 0.9975933947281775,
0.6429648995399475, 0.6306551154417491), and `0.0349` is the stated arithmetic
0.9647 − 0.9298, the seven-arm spread. **No number in the chapter came from
memory.**

**Two claims corrected against the repository before the chapter was closed.**
The draft asserted *"twelve named tests across seven files enforce inviolable
rule 6"* and that the hybrid-weight fitting module *"and its preflight"* are both
scanned. Grepping the suite returns **seventeen tests naming Verifier-B across
ten files**, and `tests/test_s4_fit_w.py` contains one such test, not two. Both
sentences were rewritten to the measured facts. This is the same failure mode the
memory note records — a plausible count carried forward instead of re-measured.

**Cross-references verified rather than assumed.** §4.5's use of Chapter 3's
prediction strength 0.8605 and bootstrap ARI 0.9399 ± 0.0290 was checked against
`results/s2d_ktable_regionA.md:25`; the intrusion figures 0.780 and 0.840 against
0.25 chance against `results/intrusion_agreement.md`; and §4.9's claim that the
widening of dev-82's registered use is logged as a deviation against
`docs/protocol.md:1932`, which records it verbatim on 2026-08-11 as Sabbir's call.

**Citations recounted** with `@(b\d+)\b`: the chapter went 11 → 17 keys, the six
added being exactly b26, b27, b28, b69, b82, b83, with none dropped, verified by
diffing key sets against `git show HEAD:`. Thesis-wide: **66 distinct keys cited
(63 before), 143 bibliography entries, 77 never cited (80 before), zero broken
citations.**

### Still owed on Chapter 4

1. **A registered script for the per-class confusion tables**, reading the two
   committed dev-prediction CSVs, with its own config, provenance and
   lab-notebook entry. Until it exists no confusion matrix may enter the thesis,
   and the audit's request stays formally open.
2. **Figure 4.2**, deferred by Sabbir, content currently carried by Tables 4.5
   and 4.6.
3. **The SetFit arm's zero seed standard deviation** is reported in §4.3 as an
   implementation defect rather than as stability. The defect itself has not been
   diagnosed, and `results/s3_backbone_ablation.md` does not explain it.
4. **The two missing English verifiers.** Pipeline §3.1 specifies four; two exist.
   §4.10 names this as outstanding and Chapter 8 must place it in future work
   rather than let the count pass unremarked.

---

## Chapter 5 — Proposed Neuro-Symbolic Multi-Agent Framework

Rewritten 2026-08-25. Title unchanged: it matches both the approved structure and
the frozen thesis title, and unlike Chapter 4's "validation" it does not overstate
what the chapter delivers.

**2,268 → 8,025 words. 10 → 11 sections. 2 → 6 numbered tables. 0 → 2 algorithm
listings. 10 → 14 citation keys.**

### Structural change

| Approved section | Source | What changed |
|---|---|---|
| 5.1 Architecture, roles and state | old 5.1 | Kept the state tuple. Added the asymmetry argument (two of four roles make no model call, and the Critic's determinism is what makes Chapter 4's wall enforceable). Added the two implementation defects — shallow-copy snapshots and feedback cleared on advance — because they define what §5.7's dynamics are dynamics *of*. Figure 5.1 now referenced in prose. |
| 5.2 Why this is a bounded workflow | old 5.1.1 | Promoted from a subsection to a section. Added the enumeration of what the controller may and may not do, and named the pattern an evaluator–optimizer workflow with predefined control flow. Kept b21. |
| **5.3 Algorithm 5.1 [NEW]** | `src/agents/graph.py`, `src/agents/state.py` | The audit's first demand. 17-line listing plus five control guarantees, each mapped to a named passing test. Absorbed the decision-19 cost model, which the chapter previously did not contain at all: the two expressions, Table 5.1, and the degeneracy finding that cost minimisation alone selects τ=0 and abolishes the verifier. Added the Appendix E.7 pointer. |
| 5.4 Retrieval and the shared prompt contract | old 5.2 | Added the implementation the chapter was missing: collection `r1_regionA_k2`, LaBSE, cosine via L2-normalised embeddings, k=10, the level filter applied *in-query* and why post-filtering would have varied prompt length with retrieval difficulty, and the row-set digest. |
| 5.5 Neural gating and symbolic diagnosis | old 5.3, expanded | The audit called `PRECOMMITMENT_UNRESOLVED` the most subtle result in the thesis, delivered in one paragraph. Now the section's centre: the three pre-committed outcomes are stated, the observed combination is shown to match none, and "consequential but not predictive" is argued as coherent. New Table 5.2 brings in `s35_symbolic.md`, which the chapter had never used. |
| 5.6 Threshold and stopping-policy selection | old 5.4 | α_lo and α_hi now defined *beside* the equation as the audit asked, not in running prose. Added the candidate-grid repair, the calibrated-scale justification, and Table 5.4. |
| 5.7 Development loop dynamics | old 5.5 **+ absorbed old 5.6** | Failure taxonomy moved in, as approved. Table 5.5 consolidates attempt means and both transitions. Added what the 8-of-50 census costs the analysis, which the audit flagged as disclosed-but-unexplained. |
| 5.8 The ten experimental conditions | old 5.7 | Judge model now named. Byte-identical critique enforcement explained. Cobbe (b58) retained. |
| **5.9 Algorithm 5.2 [NEW]** | `src/eval/s5_contract.py::largest_prefix_within_budget` | The audit's second demand. Listing plus the three properties that make the matched-budget control honest. |
| 5.10 Main-run execution contract | old 5.8 **+ 5.9, reduced** | The two sections restated §5.2/§5.7 and duplicated Appendix A. Merged and cut to a pointer, keeping only seed 42 and the demo-is-not-the-experiment boundary. |
| 5.11 Chapter summary | old 5.10 | Rewritten around the four development results that *shaped* the design, plus three quantities carried into Chapter 6. |

### The number the chapter was getting wrong

The old §5.4 said the operating point "captures 71.63% of the achievable gain".
That figure is real — `s4_tau_frontier.json` records
`fraction_of_achievable: 0.7162937936446756` — but **two different denominators
exist in the result files and the phrase "achievable gain" does not distinguish
them.** Against the frontier's own endpoints the selected point captures 71.63%;
against `s4_loop_dynamics.json`'s post-hoc Verifier-B oracle it captures 69.74%,
and forced-three captures 97.36%. The old text used the first figure and the
oracle sentence in the same chapter without saying they had different bases.
§5.6 now reports both with each denominator named, and argues that the gap between
them measures what the isolation wall costs.

Second correction: **the forced-three endpoint costs five logical calls, not
three**, and the chapter never stated its cost. `forced_3.mean_calls` is 5.0, the
cost model at q=0 gives 1+2+2=5, and
`test_forced_three_continues_after_pass_without_calling_it_gave_up` asserts
`llm_calls == 5`. Three independent sources agree, so Table 5.4 reports calls
rather than attempts.

### Citations

| Key | Work | Where | Reading status | Why load-bearing |
|---|---|---|---|---|
| b88 | Kotte 2026, UCCI: calibrated uncertainty for cost-optimal LLM cascade routing | §5.3, §5.6 | `full_or_primary_record` | The τ objective is adopted from its Thm 1, and its constraint-bounded formulation is *why* α_lo and α_hi exist. The chapter previously presented the objective with no source. Previously uncited anywhere in the thesis. |
| b81 | Kapur 2026, decoupling length and specificity in description evaluation | §5.4 | `full_or_primary_record` | Length and specificity are entangled in the construct, not just the estimator — which is why the 20-word ceiling reduced the confound without removing it. Previously uncited. |
| b87 | Mattei 2026, elementary properties of temperature scaling | §5.6 | `full_or_primary_record` | Justifies reporting τ on the calibrated scale: a monotone single-parameter rescaling cannot move an item across a threshold, so every calibrated τ has an exact raw twin. Previously uncited. |
| b18 | Liu & Meng 2026, self-correction as feedback control | §5.7 | curated b1–b29 | **Nearly dropped.** The old §5.5 cited it for "more iterations cannot be assumed beneficial"; the rewrite restated that argument and lost the citation. Caught by diffing key sets against `git show HEAD:` and restored where the second-revision regression is reported. |

Thesis-wide after Chapter 5: **69 distinct keys cited, 143 entries, 74 uncited,
zero broken.** Per chapter: 8 / 41 / 15 / 17 / 14 / 9 / 10.

### Verification performed

1. **Numeric tokens.** 135 tokens new to the file were extracted and located in
   `results/`, `configs/`, `tests/`, `src/` or an earlier chapter. 14 did not
   match by string search and were each resolved rather than assumed: nine are
   exact roundings of full-precision JSON values (verified by re-rounding the
   source value at the printed precision), four are evaluations of the two
   registered cost-model expressions, and one is a percentage rendering of a JSON
   fraction. Every calls-per-accepted figure computed from the formula reproduced
   decision 19's recorded values exactly (16.310, 5.145, 2.857, 2.032, 1.492,
   1.020), which independently confirms the formula was transcribed correctly.
2. **The 2.000-call figure reconciles.** 39·1 + 12·3 + 1·5 + 8·5 = 120 calls over
   60 cases = 2.000, matching `selection.mean_calls`. The constant-rate model at
   q=0.65 predicts 1.945; the chapter states the discrepancy and attributes it to
   the per-attempt pass rate not being constant, which Table 5.5 shows.
3. **Test-enforcement claims were measured, not asserted.** This is the Chapter 4
   lesson applied. All 16 test names written into Appendix A.7 were checked to
   exist with exact spelling and correct file attribution (zero mismatches), the
   "twenty tests across three files" count was verified, and all three files were
   executed: 7/7, 7/7 and 6/6 pass.
4. **Citation diff against `git show HEAD:`** using `@(b\d+)\b`, which is what
   caught the b18 regression.
5. **Manifest reconciliation.** 30 tables in chapters = 30 rows, zero mismatches
   in either direction; algorithm rows match the listings present in §5.3 and §5.9.

### New this session, and not mine

Two artifacts appeared in the working tree during this session that this review
did not create. Both are flagged rather than absorbed, per the one-writer rule.

1. `results/s5_posthoc_hybrid_vs_neural_bn_v1.json` — a registered post-hoc
   contrast of `rag_neural_symbolic_feedback` against `rag_neural_loop`, with its
   own config and analysis script, run in a clean clone at commit `743d53e`. It is
   an **active-versus-active** comparison, which the frozen inferential family
   excludes; the file labels itself `post_hoc_exploratory_not_in_confirmatory_family`
   and carries its own selection disclosure. **Nothing from it entered Chapter 5**,
   which is the mechanism chapter. It bears on Chapter 6/7 and on Appendix A.5,
   whose flat sentence "No post-hoc active-condition inferential comparison is
   added" will read as false to a reviewer who then meets this result. Sabbir's
   call: keep the sentence and exclude the result, or qualify the sentence.
2. `docs/chapters/chapter1/Introduction.md` — an untracked 1,683-word Chapter 1
   that is neither the pre-rewrite version (1,919 words) nor the rewritten one
   (2,944). Not read into any decision, not modified, not deleted.

### Still owed on Chapter 5

1. **The Appendix E.6 failure census** should state the three limitations §5.7 now
   derives (12.5% resolution floor, no reliability estimate, and five of eight
   cases outside the taxonomy) rather than only the counts.
2. **The two result files disagree about whether the coding deviation is closed.**
   `results/s4_failure_taxonomy.json` records
   `single_coder_user_endorsed_protocol_deviation` — that is, endorsed and closed —
   while `results/s4_loop_dynamics.json` records the same census as
   `pending_independent_double_coding`, that is, still open. §5.7 describes the
   census the way the taxonomy file does, since that is the file that owns it, and
   states that no agreement statistic exists. Not reconciled; neither file touched.
   Sabbir's call, because it turns on whether he considers his review to have
   closed the deviation.
3. **The per-level oracle asymmetry** (82.00% at Level 0 against 39.07% at Level 1)
   is reported descriptively in §5.7 and needs Chapter 7 to say whether sparser
   Level-1 retrieval evidence is the explanation or merely consistent with it.

---

## Chapter 6 — Experimental Setup, Results, and Analysis

Rewritten 2026-08-26. Title unchanged.

**2,943 → 7,004 words. 10 → 12 sections. 4 → 6 numbered tables. 9 → 13 citation
keys.**

### Structural change

| Approved section | Source | What changed |
|---|---|---|
| 6.1 Design, outcomes, frozen family | old 6.1 | Stopped re-enumerating the ten conditions and now points at Table 5.6 and §5.10 for the execution contract, which was the largest duplication in the chapter. Added the four-group grouping so the conditions are still readable without the table. Fixed the broken inline math `(p_B(l\mid y))` → `$p_B(l \mid y)$`. Added an explicit paragraph naming both post-hoc analyses and their standing, and a Bangla-only scope sentence. |
| 6.2 Integrity of the run | old 6.2 | Kept every integrity number. Added the paragraph stating that both post-hoc analyses and the example selection record the same two SHA-256 digests and `generation_rerun: false`, which is what lets a reader check that the exploratory sections read the same bytes as the registered ones. |
| 6.3 Main ablation | old 6.3 | Table 6.1 unchanged. Added the subsection "A hypothesis for the Level-0 deficit" — the audit's main content request. Added a forward pointer to §6.9's symbolic-loop mechanism. |
| 6.4 Planned paired comparisons | old 6.4 | Typeset the nine identical p-values as `2/10001` in a merged "Bootstrap p = BH q" column and said in prose that this is the two-sided resolution floor of 10,000 resamples, not evidence of equal effect strength. Added the two discordant-pair columns and stated that no standardised effect size was registered, so none is introduced. The exploratory hybrid paragraph is retained, with its disclosure strengthened — see below. |
| 6.5 Goodhart diagnostic | old 6.5 | Unchanged except the caption convention. |
| 6.6 Human validation | old 6.6 | Original content unchanged. Added the subsection "The same items, measured twice" with new Table 6.4. |
| 6.7 Length-controlled slice | old 6.7 | Table renumbered 6.4 → **6.5**. Added the closing paragraph stating that the slice does *not* confirm the §6.3 hypothesis, and why the counter-argument is itself weakened by post-treatment selection. |
| 6.8 Diversity and realism | old 6.8 | Two registered corrections, below. |
| 6.9 Qualitative error analysis | **new** | Table 6.6 plus E1–E6 as block quotes. |
| 6.10 No external published baseline | **new** | Four grounded reasons plus an explicit statement that the search was not re-run. |
| 6.11 RQ answers | old 6.9 | Added the RQ1 pointer to §3.12. RQ2/RQ3/RQ4 wording is HEAD's, verbatim — see the correction below. |
| 6.12 Chapter summary | old 6.10 | Rewritten so it argues why the result survives its own controls instead of restating §6.11's four bullets in prose. |

### The two corrections to §6.8, both from result files

1. **The under-four-word rate is not a Level-0 property.** The old text reported it
   as though short degenerate output were a consequence of requesting Level 0.
   `s5_main_bn_diversity.csv` confines it to two cells: external-role critique at
   Level 0 (115/270) and intrinsic critique at Level 0 (84/270). The other 18 cells
   are between 0 and 4. It is a behaviour of the two self-critique arms, not of the
   level.
2. **The length-JS asymmetry runs the other way from the naive reading.**
   `s5_main_bn_length_js.csv` shows the Level-1 cell further from its own reference
   than the Level-0 cell in **nine of ten** conditions (external-role critique the
   exception, 0.3687 against 0.3591). This is the corpus-side counterpart of the
   generated-length inversion, and the old text did not report the direction at all.

### The §6.3 hypothesis, and the evidence for each of its three legs

Every component is file-backed; none of it is inference from memory.

| Leg | Claim | Source |
|---|---|---|
| Corpus | Level 0 is the **longer** half (13.12 vs 8.85 words, gap +4.27) and length is a major component of the cut (AUC 0.6764, `LENGTH_CONFOUNDED`; word-count-only rule 0.6197 vs 0.3926 floor) | §3.6, §4.4, `s2_regionA_*` / `s3_*` as cited there |
| Generation | The polarity **inverts**: 11.47 at Level 0 vs 16.23 at Level 1, gap −4.77, length-only AUC 0.9111, `LENGTH_RECOVERS_LEVEL` | `results/s4_devplot_lenctl_generations.json` |
| Instrument | On identical items the human panel shows **no** level asymmetry (0.92/0.92) where both verifiers do (B 0.60/0.90, A 0.70/0.84) | `results/s5_instrument_agreement_bn_v1.json` |

Three disclosures are written into the chapter rather than left to a reader to
discover: the generation file is flagged `NOT_A_RESULT` and covers 30 development
plots at attempt 1 with no Critic; §6.7's length-matched slice still shows a
Level-0 deficit, which is what the hypothesis would least like to see; and 50
items per level under a forced binary choice bounds rather than resolves the
question. **It licenses no revision of any registered number**, and the chapter
says so.

### Table 6.4 — how it is presented, and the three traps avoided

1. **The 0.9133 vs 0.92 discrepancy is explained, not hidden.** Table 6.3 pools
   300 judgments; a same-item comparison needs one label per item, so Table 6.4
   applies the registered majority-of-three rule. Same data, two aggregations,
   neither superseding the other. Left unexplained this reads as two conflicting
   accuracies for one study.
2. **The κ ordering is explained arithmetically from the table's own numbers**
   (pooled 0.46 > Level 1 0.146 > Level 0 0.038, against raw agreement 0.73 / 0.86
   / 0.60): within a stratum the requested level is constant, so both instruments'
   marginals skew toward it, expected agreement is high and the coefficient
   collapses. No new metric and no citation carrying a claim it was not read for —
   b37 keeps the use it already had in §6.6.
3. **Verifier-A is reported beside Verifier-B without a superiority claim.**
   Chapter 4 §4.9 forbids ranking the two verifiers and states that "RQ4's gap is
   measured on generated text in Chapter 6, not here", which is exactly what this
   is; the chapter still says explicitly that no claim is made that either verifier
   is better.

### Citations

No new keys. Four already-cited keys are re-used in the new material: **b81**
(length/specificity decoupling) for the §6.3 length argument, **b36**
(confidence and stability of scores) twice for the 50-item bound, and
**b98; b110** in §6.10 for what the recent Bangla evaluation resources actually
benchmark. All four were already assessed at a recorded reading depth for
Chapter 2 or Chapter 5, so none needs a new register entry.

Three keys were considered and **rejected**: b133 (interpretable criteria for
subjective NLP tasks), b134 (three-attempt repair loops — which would have been
apposite for §6.9's budget-exhaustion example) and b142 (do automatic factuality
metrics measure factuality). All three are in the bibliography, all three are
currently uncited, and all three are assessable only at title level while
Consensus is quota-exhausted (to 2026-09-01) and alphaXiv is unavailable. §2.1
forbids citing a source without a reading-depth register entry. They are recorded
here as Phase 6 candidates.

### Verification performed

1. **Citation diff against `git show HEAD:`** using `@(b\d+)\b`. All nine
   pre-existing keys survive; the four additions are the intended ones. This is
   the check that caught the b18 regression in Chapter 5.
2. **Every quoted number was re-read from its source file this session** rather
   than carried from a summary: both new result JSONs in full,
   `s5_main_bn_paired_statistics.csv`, `s5_main_bn_diversity.csv`,
   `s5_main_bn_length_js.csv` and `s4_devplot_lenctl_generations.json`. The
   discordant-pair columns of Table 6.2 and the stratum sizes of Table 6.6 are
   transcribed, not recomputed.
3. **The ad-hoc word counts from an earlier session were discarded.** §6.3 uses
   the registered `s4_devplot_lenctl_generations.json` gaps instead. An unregistered
   count must not enter the chapter even when it agrees.
4. **Bangla text was checked byte-for-byte against the result file**, not eyeballed.
   That check is what caught defects 1 and 2 below. After the fix all seven quoted
   strings match exactly, including E1's two emoji, with no transliteration and no
   normalisation.
5. **Manifest reconciled**: two rows added, the length-matched row renumbered, the
   build-order line corrected from 30 to 32 tables and "Tables 6.2--6.4" to
   "6.2--6.6".

### The §6.10 argument, and its stated limit

Chapter 2 carries no ready-made "no external baseline exists" sentence — that was
verified by grep, not assumed — so §6.10 is argued from four things Chapter 2 and
Chapter 3 do say: the outcome construct is corpus-derived and defined in this
thesis; the corpus has no film-title column, so no reference response exists for
any plot and reference-based comparison is impossible by construction; Table 2.1
records no verified adjacent work combining this task, language and instrument,
and Chapter 2's own conclusion is that the gap is an *evaluation* gap; and the
recent Bangla resources are hallucination and sociopragmatic benchmarks, not
controllability benchmarks, assessed at record level.

The section states plainly that the literature search was **not** re-run for it and
that Chapter 2's review is narrative with a quota-exhausted primary index, so the
claim is "no comparable published baseline was identified", not "none exists". It
also states the condition under which one could later be added: same prompt
contract, same 20-word ceiling, same budget accounting, as a new registered
analysis and never as a re-reading of these numbers.

### Four defects the verification caught in my own draft

Recorded because the checks that caught them are the reason to keep running them,
and because two of the four would have been invisible to proofreading.

1. **Two Bangla quotations were not byte-identical to the archive.** E4 and E5 were
   written with base letter plus nukta (`U+09A1 U+09BC`, `U+09AF U+09BC`) where
   `s5_error_examples_bn_v1.json` stores the precomposed forms (`U+09DC`, `U+09DF`).
   The strings are NFC-equivalent and visually identical, so no reader would have
   noticed, but CLAUDE.md forbids normalising Bangla beyond whitespace and the
   archive's own bytes are the reference. Both block quotes were replaced by
   copying the exact bytes out of the result file programmatically rather than
   retyping them; all seven quoted strings (six examples plus E5's comparator) now
   match byte-for-byte. The file is internally inconsistent about this — E1, E3 and
   E6 use base+nukta — which is a property of the original text and was preserved,
   not repaired.
2. **E2 appeared in Table 6.6 but its text was never shown.** The section promises
   six outputs and displayed five. E2's block quote was inserted with its analysis,
   and the observation that it sits exactly at the 20-word prompt ceiling.
3. **Two disclosures drifted weaker than HEAD's and were restored.** My RQ3 bullet
   had compressed "Because the contrast was selected after inspecting the
   registered results, it is exploratory" into "The comparison does not establish
   overall hybrid superiority", and my §6.12 dropped the 91.33% human accuracy that
   HEAD's summary carried. HEAD's RQ3 sentence is restored verbatim, the figure is
   back in §6.12, and §6.4's paragraph now also states that the interval is a naive
   post-selection interval — which the result file says and the prose did not.
   **The general point: the hybrid paragraph does not exist in HEAD at all.** It was
   in the uncommitted working tree, so "carries over verbatim" was unverifiable
   the moment the file was overwritten. The claim has been corrected above to say
   the numbers were re-verified against
   `results/s5_posthoc_hybrid_vs_neural_bn_v1.json` — all six of them match — rather
   than that the wording was preserved, which cannot now be checked.
4. **One rounding tie, left as it was.** Table 6.5's blind-resampling row shows
   1.088 and 0.8188 where the raw values are exactly 1.0875 and 0.81875. Half-up
   gives the draft's values, half-even gives 1.087 and 0.8187. Both are correct
   roundings of an exact tie; the draft's values were kept and are noted here so a
   later checker does not file it as an error. It is the only tie in the table.

### Still owed on Chapter 6

1. **Definition of Done for the two new registered analyses.** Lab-notebook
   entries via `src/common/step_close.py`, a `docs/protocol.md` Deviations row for
   the post-hoc instrument-agreement analysis, a STATUS row and verified fact, and
   `step_close.py --check` exiting 0. Not done in this session.
2. **`docs/appendices/appendix_a_reproducibility.md:63`** — "No post-hoc
   active-condition inferential comparison is added" was already false once
   (the hybrid-vs-neural contrast) and is now false twice. Sabbir's call: qualify
   the sentence or exclude the results.
3. **Three documents still name "Table 6.4" as the length-matched slice** and were
   deliberately not edited, because they are dated records rather than thesis
   deliverables: `docs/lab_notebook.md` (5484–5485),
   `docs/thesis_rq_evidence_map.md` (116–118, 173) and
   `docs/thesis_structure_process_audit.md` (31–33). The evidence map is the one
   most likely to want updating, since it is read as current.
4. **Chapter 7 inherits new material**: the instrument-divergence finding bears
   directly on its measurement-validity row, and §6.9's symbolic-gate mechanism
   explains a cost result Chapter 7 currently only reports.
5. **`docs/chapters/references.bib` will need four keys when the per-chapter
   extractor reaches Chapter 6.** All 13 of the chapter's keys resolve in
   `docs/references_ieee.bib` (the correct target — `docs/references.bib` uses
   semantic keys by design and resolves none of them, which is not a defect). The
   chapter-scoped bib holds 50 entries, last generated for Chapters 1–3, and is
   missing **b49, b50, b55** — all three already cited by the pre-rewrite Chapter 6
   — plus **b81** from this rewrite. Not edited: that file is generated by
   `src/common/extract_chapter_bibliography.py`, is modified in the working tree by
   the other writer, and hand-editing a generated bibliography is the same class of
   error as hand-editing `references_ieee.bib`.

---

## Chapters 7–8

Not yet rewritten. Chapter 8 does not exist yet.
