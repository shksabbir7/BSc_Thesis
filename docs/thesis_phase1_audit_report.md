# Phase 1 — Complete Thesis Audit

**Audit date:** 2026-08-25
**Auditor role:** supervisory review (analysis only)
**Scope:** `docs/chapters/*` (7), `docs/appendices/*` (8), `docs/thesis_front_matter.md`,
`docs/thesis_assembly_order.md`, `docs/thesis_table_figure_manifest.md`,
`docs/thesis_rq_evidence_map.md`, `docs/thesis_abbreviations.md`,
`docs/thesis_final_copyedit_checklist.md`, `docs/generative_ai_declaration.md`,
`docs/references_ieee.bib`, `docs/references.bib`.

**No chapter, result, figure, table or bibliography entry was modified during this
audit.** Every number below was counted from the files, not estimated.

---

## 0. Measured inventory (basis for everything that follows)

| Quantity | Measured value |
|---|---:|
| Main-text chapters | 7 |
| Main-text words | 16,239 |
| Appendices | 8 |
| Appendix words | 7,244 |
| Front-matter words | 369 |
| Total repository prose | 23,852 |
| Markdown tables in chapters | 15 |
| Numbered + captioned tables | 14 |
| Figures embedded in chapters | 5 |
| Figures planned but absent | 3 (3.1, 3.2, 4.2) |
| Algorithm / pseudocode listings | **0** |
| Display equations | 2 (Ch. 5 state tuple; Ch. 5 threshold objective) |
| Fenced code blocks in chapters | 0 (6 exist, all in Appendix E) |
| Entries in `references_ieee.bib` | 143 (`b1`–`b143`) |
| Entries in `references.bib` | 129 (semantic author-year keys) |
| Distinct keys cited by chapters | 55 (`b1`–`b55`, contiguous) |
| Cited keys absent from the bibliography | **0** |
| Bibliography entries never cited | **88 of 143 (61.5%)** |
| Citations in appendices | **0 across all eight** |

Per-chapter citation load (distinct keys / total occurrences):
Ch1 8/8 · Ch2 36/44 · Ch3 12/12 · Ch4 11/13 · Ch5 10/10 · Ch6 9/11 · Ch7 10/10.

---

## 1. Overall Thesis Evaluation

### 1.1 Current quality level

**Scientific content: strong — clearly above typical BSc standard, and in the
methodological-discipline dimension competitive with published work.**
**Thesis-document quality: not yet submission-ready.**

These two assessments differ, and the gap is the central finding of this audit.
The research underneath is unusually well governed: preregistered outcome
labels, frozen data walls enforced by executable tests, a genuine negative
result that was kept rather than buried, an inferential family fixed before
analysis, and a discovered circularity that was converted into the study's own
stress test instead of being suppressed. Very few undergraduate theses — and not
all journal papers — hold that line.

What is not yet at that level is the *document*. The chapters read as an
accurate, dense technical record written for someone who already knows the
project. They do not yet read as a thesis that recruits an unfamiliar examiner,
carries them through an argument, and shows them where they are. The defects
below are almost all presentational, structural, or completeness defects — not
scientific ones. That is the good news, because they are cheap to fix relative
to their effect on how the work is judged.

Estimated standing if submitted today: a competent examiner would recognise the
methodological quality but would raise formal objections (missing figures,
uncited tables, no algorithms, contribution inconsistency, an abstract that
under-sells the work). Those objections are all removable.

### 1.2 Strengths

**Methodological integrity is the thesis's real contribution and it is genuine.**
Preregistered three-outcome claims mean negative results were publishable in
advance; `UNRELIABLE`, `PRECOMMITMENT_UNRESOLVED`, `CALIBRATION_NOT_ESTABLISHED`
and `CIRCULARITY_CONFIRMED` all survive into the final text. The failed ordinal
instrument (α = 0.4970) is reported beside the successful comparative one rather
than replaced by it. This is rare and should be foregrounded, not treated as
housekeeping.

**The dual-verifier isolation wall is a real architectural idea, not a label.**
Verifier-A (frozen LaBSE + L2 logistic head, R1, n=804) and Verifier-B
(fine-tuned BanglaBERT, R2, n=888) differ in training data, encoder family,
tokenizer and privilege, and the separation is enforced by an AST scan with a
companion test proving the guard can fail. Most papers asserting an "independent
evaluator" cannot demonstrate independence this concretely.

**Claim discipline is consistently maintained.** Every chapter distinguishes what
was tested from what was observed. Chapter 6 §6.4 explicitly refuses to convert
a descriptive ordering into a tested ranking; Chapter 7 §7.6 refuses to add the
post-hoc hybrid-versus-neural test. The recurring formula — "this is evidence of
X, not proof of Y" — is the correct instinct.

**The experimental surface is large, paired, and complete.** 5,400 cases with
exactly 5,400 unique registered keys, no missing/extra/duplicate cases, a
matching source hash, and byte-identical shared initial RAG drafts across
conditions 3–9. The pairing design (plot × level × seed) is materially stronger
than unpaired condition means.

**Controls are unusually strong for a thesis.** Blind resampling under a matched
token budget and an external hosted judge are exactly the two controls a hostile
reviewer would demand, and both were run rather than argued away.

**Bounded-scope framing is honest and defended.** The thesis repeatedly declines
the "audience simulation" claim its title could have supported. Section 5.1.1
("why this is a multi-agent workflow, not an autonomous-agent claim") is the kind
of paragraph that prevents a reviewer objection before it forms.

### 1.3 Weaknesses

**No algorithms or pseudocode anywhere.** Zero listings across 16,239 words. A
thesis whose title claims a *framework* and whose Chapter 5 describes a state
machine with routing, thresholds, tie-breaking and a retry ceiling must render
that machine as a numbered algorithm. Currently the loop exists as prose, one
state tuple, and one objective function. This is the single largest formal gap
against the audit checklist.

**Three planned figures do not exist** (3.1 data lineage, 3.2 axis diagnostics,
4.2 calibration). Both `thesis_table_figure_manifest.md` and
`thesis_final_copyedit_checklist.md` already record this. The consequence is that
Chapter 3 — the longest evidence chapter, carrying the corpus audit, the
source-confound rejection, the Region-A/B contrast and two human studies — has
**no figure at all**. It is 2,279 words of tables and prose.

**Cross-referencing is largely absent.** Only 3 of 15 tables (1.1, 2.1, 6.1) are
referred to by number in the body text. The other 11 numbered tables appear with
a caption and no prose pointer — a reader meets Table 3.2 without being told to
look at it. Worse, **Figures 4.1, 5.1 and 5.2 are never mentioned in prose at
all**; they float between paragraphs with an italic caption. Only Figures 6.1 and
6.2 are properly introduced.

**One table is unnumbered and uncaptioned** — the Verifier-A/Verifier-B
comparison in §4.7. Fourteen tables are numbered; this fifteenth is not. It
should become Table 4.2.

**Contribution count is inconsistent between chapters.** §1.6 promises *seven*
contributions; §7.10 delivers *four*. They are reconcilable (Ch1 items 3, 4 and 5
collapse into Ch7 item 2; items 6 and 7 fold into Ch7 items 3 and 4), but an
examiner reading both will read it as carelessness, and the opening and closing
of a thesis are the two places carelessness is least affordable.

**No structure binds objectives to research questions to chapters to
contributions.** There are 5 objectives (§1.4), 4 RQs (§1.3), 7-or-4
contributions, and 7 chapters, with no single table showing how they map.
Objective 3 (develop two verifiers) maps to no research question at all —
**Chapter 4 is the only chapter that answers nothing formally**, despite
containing the circularity finding that reframes the whole verifier design.

**Chapter 4 is under-written relative to its importance.** At 1,397 words it is
the shortest chapter by a wide margin (the next shortest is Ch1 at 1,919; the
longest is Ch6 at 2,901), yet it carries `CIRCULARITY_CONFIRMED` — arguably the
most intellectually interesting result in the thesis, since it explains why the
seven-backbone ablation was near-saturated and why the Goodhart test is
necessary. That finding currently gets 13 lines.

**RQ1 is orphaned in the results chapter.** §6.9 answers RQ2, RQ3 and RQ4. RQ1's
evidence lives in Chapter 3 and its verdict in Chapter 7. A reader arriving at
"Answers to the research questions" and finding three of four will assume an
omission.

**Reporting of the bootstrap p-values invites a false objection.** Table 6.2
prints `0.000200` nine times and BH `q = 0.000200` nine times. §6.4 correctly
explains this is the 10,000-resample resolution floor, but the table as printed
looks like a copy-paste error at first glance. It should be typeset as
`< 2×10⁻⁴ (resampling floor)`.

**No standard classification metrics beyond macro-F1.** Verifier development
reports macro-F1 only. On a 53/29 imbalanced development slice, per-class
precision, recall and a confusion matrix are the conventional minimum, and the
audit checklist explicitly asks for accuracy/precision/recall/F1.

**Chapter 2 has no stated review methodology.** It carries 36 of the thesis's 55
distinct citations (65%) and reads well, but never states how the literature was
identified — which databases, which year windows, which inclusion rule. Given
that this project has an explicit standing instruction to search Consensus with
`year_min` set and to report what the search changed, that methodology exists and
simply is not written down. A Q1 reviewer will ask.

**Bibliography hygiene.** 88 of 143 entries (61.5%) are uncited. The keys `b1`
through `b143` encode bibliography order, so inserting any citation forces a
global renumber of both keys and prose. A second file, `references.bib` (129
entries, semantic keys), is cited by no chapter and uses an incompatible key
scheme. 22 of the 55 cited works (40%) are arXiv/eprint records.

**Terminology and identifier inconsistencies** (from the appendix pass):
Appendix H names the triage model "Gemma-4-31B" while every other file says
`gemma-4-26b-a4b-it`; Appendix A says "maximum three judgments" while Appendix E
says "up to two Writer retries" (reconcilable as 1+2, but stated in two units).
The exact judge model ID never appears in the main text at all.

**Registered verdict labels are never defined for the reader.** `TIE`,
`CIRCULARITY_CONFIRMED`, `CALIBRATION_IMPROVED`, `CALIBRATION_NOT_ESTABLISHED`,
`PRECOMMITMENT_UNRESOLVED`, `RESIDUAL_SURVIVES`, `UNRELIABLE` and
`HUMANLY_PERCEPTIBLE` appear as code-formatted tokens across Chapters 3–5. None
is in `thesis_abbreviations.md` and none is defined on first use. To an examiner
these read as internal jargon; explained properly they are evidence of
preregistration and become a strength.

**Undefined abbreviations in Chapter 2.** Table 2.1 uses KBQA, BM25, BGE-M3 and
LoRA with no expansion in text and no entry in the abbreviations list.

**Mixed figure formats and paths.** Chapters 4 and 5 load SVGs from
`../figures/`; Chapter 6 loads PNGs from `../../results/`. Vector and raster
mixed in one document, sourced from two directory trees, is a production risk at
LaTeX assembly.

### 1.4 Major issues affecting thesis quality

In descending order of damage per unit of effort to fix:

1. **Missing algorithms** — a framework thesis with no formal procedure listing.
2. **Missing Figures 3.1, 3.2, 4.2** — leaving the principal evidence chapter
   entirely figure-less.
3. **Abstract does not represent the work** — currently ~280 words in two
   paragraphs, omitting the gap, the objectives, most quantitative results, and
   the contributions. This is the first thing every reader sees.
4. **Contribution inconsistency (7 vs 4)** and the absence of an
   objective↔RQ↔chapter↔contribution map.
5. **Cross-referencing failure** — 11 uncited tables, 3 unreferenced figures.
6. **Chapter 4 under-development** relative to the weight of its finding.
7. **Bibliography state** — 61.5% unused, a redundant second `.bib`, brittle
   ordinal keys.

### 1.5 Is the research contribution clearly presented?

**Partially — and it is currently under-claimed rather than over-claimed.**

The thesis is scrupulous about what it cannot say, which is correct, but it has
not made the positive case with equal force. A reader can finish Chapter 7 and
still be unsure whether the contribution is (a) a Bangla generation system, (b) a
verifier-isolation methodology, or (c) an empirical demonstration that proxy
optimisation is detectable. The evidence best supports (b) and (c), with (a) as
the vehicle — but the document never says that plainly.

The specific failures of presentation are: the two contribution lists disagree;
the abstract does not state a contribution at all; §1.6's seven items mix
methodological contributions with experimental facts (item 5, "a matched
ten-condition experiment containing 5,400 cases", is a description of the method,
not a contribution); and the strongest single result — that a frozen LaBSE probe
reaching 0.9866 exposed the label as near-linear in its own generating
representation, which is *why* the Goodhart test is load-bearing — is buried in
§4.4 and never restated in Chapter 1 or the abstract.

Fixing this does not require new experiments. It requires one canonical
contribution list, stated identically in the abstract, §1.6 and §7.10.

---

## 2. Chapter-by-Chapter Review

### Chapter 1 — Introduction (1,919 words, 8 citations, 1 table, 0 figures)

**Purpose.** Establishes the pre-release audience-response setting, narrows it to
engagement-specificity control, states four RQs and five objectives, previews the
design, and lists contributions and scope.

**Organisation.** Sound and conventional (§1.1 background → §1.9 summary). The
blockquoted central problem statement in §1.2 is effective. Table 1.1 arrives
early and does real work by binding each RQ to its evidential standing before the
reader can over-read the questions.

**Missing sections.** No objective↔RQ mapping. No mention of the plot corpus
licence/ethics posture (deferred entirely to Chapter 3 and Appendix D). No
statement of *why Bangla specifically* beyond resource scarcity — the cultural
and industrial motivation for Bangla cinema is absent, which weakens the
motivation for an examiner outside the field.

**Weak explanations.** §1.5 compresses the entire design into three paragraphs
that assume the reader already accepts terms such as "Region A", "R1/R2" and
"Gold-300" before they are defined (they are defined in Chapter 3). §1.2's third
challenge (proxy gaming) is stated in one sentence and is the thesis's most
distinctive concern — it deserves a paragraph.

**Redundant content.** §1.6 item 5 restates the experimental design already given
in §1.5 and re-labels it a contribution. §1.9 restates §1.1–§1.4 with little new.

**Transitions.** §1.4→§1.5 and §1.7→§1.8 are abrupt. §1.8 is a bare chapter list
rather than an argument for the sequence.

**Technical gaps.** No forward reference to any algorithm, figure or numeric
headline. A reader finishes Chapter 1 without a single result.

**Recommendations.** Add an objectives/RQ/chapter/contribution table. Reduce §1.6
to a single canonical list matching §7.10. Add one or two headline numbers to
§1.5 or §1.6 (for example the +0.2570 registered effect and the 0.9133 human
target match) so the introduction previews outcomes. Add a short paragraph
motivating Bangla cinema as a domain, not only as a low-resource language.
Define, on first use, the registered verdict-label convention.

### Chapter 2 — Related Work (2,655 words, 36 citations, 1 table, 0 figures)

**Purpose.** Thematic synthesis across eight areas and derivation of the research
gap.

**Organisation.** The best-organised chapter. Each section states what a line of
work establishes, what it does not, and what follows for this thesis. Table 2.1
and the six-part gap enumeration in §2.9 are strong.

**Missing sections.** **No review methodology** — no databases, no search terms,
no year window, no inclusion/exclusion rule, no count of screened versus retained
works. Given the project's standing Consensus-first instruction, this is
documented practice that is simply unwritten. No section on Bangla *generation*
evaluation as distinct from Bangla classification; §2.7 covers classification
backbones only, which leaves the evaluation half of the low-resource problem
unaddressed.

**Weak explanations.** §2.4 asserts that neural and symbolic evaluation are
complementary but does not define what would count as evidence for the symbolic
component's value — which matters because the thesis later returns
`PRECOMMITMENT_UNRESOLVED` on exactly that question. Setting the bar in Chapter 2
would make the Chapter 5 non-result legible instead of disappointing.

**Redundant content.** §2.10 largely restates §2.9. The two could merge.

**Transitions.** Good within sections; §2.8→§2.9 jumps from human-evaluation
methodology to a comparison table without a bridge.

**Technical gaps.** Citation concentration (36 of 55 distinct keys) means later
chapters rarely re-engage the literature; Chapter 6 in particular cites only
statistical-method references. Findings are therefore never explicitly compared
back to the cited work.

**Recommendations.** Add §2.0 review methodology. Add a subsection on Bangla
generation/evaluation resources. State the evidentiary bar for symbolic value in
§2.4. Merge §2.10 into §2.9. Ensure at least three Chapter 2 works are re-cited
in Chapter 7's discussion so the loop closes.

### Chapter 3 — Research Methodology, Data, and Construct Validation (2,279 words, 12 citations, 3 tables, 0 figures)

**Purpose.** Corpus provenance and audit, cleaning, frozen partition, plot
stimuli, rejection of full-corpus clustering, Region-A discovery with Region-B
negative control, two human validation studies, operational axis definition.

**Organisation.** The chapter title over-promises. It says "Research
Methodology" but contains no methodology for the framework, the experiment, or
the statistics — those live in Chapters 5 and 6. What it actually contains is
data and construct validation, done very well.

**Missing sections.** Figures 3.1 and 3.2, both planned and both absent — leaving
the chapter with zero visual content. No overall research-design overview (the
S0–S6 pipeline is never shown to the reader as a whole). No ethics/consent
statement for the two human validation studies in §3.7–§3.8 (Appendix B has it;
the chapter does not point there). No inter-annotator detail for attempt 2 beyond
raw accuracy.

**Weak explanations.** §3.5's finding that "60% of rows carry a uniform
non-organic signature" is decisive for the whole thesis — it is why full-corpus
clustering was rejected — and receives two sentences with no description of what
the signature was or how it was detected. §3.6's `RESIDUAL_SURVIVES` verdict
notes the result is "only 0.2 points from its cutoff"; the implication (that the
construct is real but marginal) is left for the reader to draw. §3.9's
counter-intuitive shorter-but-richer direction (Level 1 at 8.85 words/414 types
per 1k vs Level 0 at 13.12/269) is correctly retained but not explained.

**Redundant content.** Table 3.1 rows 1–2 restate the §3.2 prose almost exactly.
The data-wall statement appears in §3.1, again in §3.3, and again in §3.5.

**Transitions.** §3.4 (plot corpus) interrupts the review-corpus narrative that
runs §3.2→§3.3→§3.5. Moving §3.4 after §3.9, or into a §3.2.x subsection, would
restore the thread.

**Technical gaps.** No confusion matrix or per-class breakdown for the intrusion
task. The 0.95 near-duplicate threshold's 0.90/0.98 sensitivity results are
mentioned but not reported. No statement of how the two annotators in §3.7–3.8
were recruited (Appendix B has this).

**Recommendations.** Retitle to "Data, Corpus Audit, and Construct Validation" or
add genuine research-design content to justify the current title. Build Figures
3.1 and 3.2 — this chapter needs them most. Expand §3.5 on the source signature.
Relocate §3.4. Add a forward pointer to Appendix B at §3.7.

### Chapter 4 — Verifier Development and Validation (1,397 words, 11 citations, 2 tables, 1 figure)

**Purpose.** Develops Verifier-A and Verifier-B, reports the backbone ablation,
the circularity baseline, calibration, and the isolation wall.

**Organisation.** Logical but compressed. **Shortest chapter in the thesis while
carrying its most reframing finding.**

**Missing sections.** Figure 4.2 (calibration before/after) is planned, its data
exists, and it is absent. No per-class precision/recall or confusion matrix. No
algorithm or procedure listing for verifier training. No statement of what
Chapter 4 contributes to any research question — it is the only chapter that
answers none.

**Weak explanations.** §4.4 is the intellectual core: a frozen LaBSE probe scores
0.9866 against the best fine-tuned arm's 0.9647, and since K=2 was created by
K-means in LaBSE space, a linear probe recovers the generating geometry. This is
explained in nine lines and never connected forward to why the Goodhart test in
Chapter 6 is necessary rather than merely prudent. §4.3's `TIE` verdict is
correct but the reader is not told what practical consequence follows (namely
that fine-tuning bought nothing and the cheap probe was therefore defensible).
§4.5's warning — that Verifier-A's accuracy "is also its risk" — is the thesis's
own thesis and gets one sentence.

**Redundant content.** §4.1 and §4.7 both state the isolation rationale; §4.2 and
§4.3 both describe the seed protocol.

**Transitions.** §4.4→§4.5 is the sharpest break in the thesis: the reader moves
from a finding that undermines the ablation straight into model specification
with no bridging sentence.

**Technical gaps.** Training hyperparameters for the seven-backbone sweep are
absent from the chapter (Appendix F has learning rate and seed only; epochs,
batch size and max sequence length appear in Appendix G for Verifier-B alone).
The §4.7 table is unnumbered and uncaptioned. Dev-82's dual role (model selection
*and* calibration fitting *and* reporting) is disclosed but its consequence for
the reported numbers is not quantified.

**Recommendations.** **Expand this chapter substantially** — target parity with
Chapters 3 and 5. Build Figure 4.2. Number the §4.7 table as Table 4.2. Add
per-class metrics. Add a closing subsection stating what the circularity finding
means for the rest of the thesis. Add a procedure listing for verifier training
and calibration.

### Chapter 5 — Proposed Neuro-Symbolic Multi-Agent Framework (2,268 words, 10 citations, 2 tables, 2 figures)

**Purpose.** Specifies the four-role architecture, retrieval and prompt contract,
neural gating with symbolic diagnosis, threshold selection, loop dynamics, the
ten conditions, and the execution contract.

**Organisation.** Good. §5.1.1 pre-empting the autonomous-agent objection is a
model of anticipatory writing.

**Missing sections.** **No algorithm listing.** A chapter describing a state
machine with acceptance thresholds, query revision, tie-breaking by earliest
attempt, and a retry ceiling must present at least: Algorithm 5.1 (the bounded
generation loop) and Algorithm 5.2 (blind-resampling selection under a matched
budget). Also absent: a cost/complexity model, and a worked end-to-end example
(Appendix E.7 has one and the chapter never points to it).

**Weak explanations.** §5.3's `PRECOMMITMENT_UNRESOLVED` outcome — the 21-point
`w` sweep where every fold selected w=1.0, mean ΔAUC 0.0000, yet 50.8%/39.2% of
generations changed verdict somewhere on the curve — is the most subtle result in
the thesis and is delivered in one paragraph. The reader is not helped to see why
"not inert but not predictive" is a coherent state. §5.4's threshold objective is
given as a formula, but α_lo (one-call RAG) and α_hi (forced-three) are defined in
running prose rather than beside the equation. §5.6's failure taxonomy reports 8
cases where 50 were planned, with no independent coder — correctly disclosed, but
the reader is not told what this costs the analysis.

**Redundant content.** §5.8 restates the execution contract already given in
§5.2 and §5.7. §5.9's reproducibility content substantially duplicates
Appendix A.

**Transitions.** §5.6 (failure taxonomy, 8 development cases) sits between loop
dynamics and the condition matrix and breaks the flow; it belongs adjacent to
§5.5 or in the appendix.

**Technical gaps.** Figures 5.1 and 5.2 are never referenced in prose. Table 6.1
is referenced twice from Chapter 5 before it exists — a forward cross-chapter
reference that should at minimum be signposted. The exact judge model identifier
never appears. Retrieval implementation (Chroma, cosine, k=10) is stated in
Appendix G but only partially in the chapter.

**Recommendations.** Add two algorithm listings. Reference both figures in prose.
Expand §5.3. Move or shorten §5.6. Cut §5.9 down to a pointer to Appendix A. Add
a pointer to the Appendix E.7 worked trace.

### Chapter 6 — Experimental Setup, Results, and Analysis (2,901 words, 9 citations, 4 tables, 2 figures)

**Purpose.** Defines the experimental units and inferential family, verifies
archive integrity, then reports automatic outcomes, planned comparisons, the
Goodhart diagnostic, human validation, the length-controlled slice, and
diversity/realism diagnostics.

**Organisation.** The strongest results chapter structurally. Putting archive
integrity (§6.2) *before* any quality result is exactly right and should be
called out as a deliberate choice rather than left implicit.

**Missing sections.** §6.9 omits RQ1. No comparison against any external
published system, and no statement explaining why none exists (no comparable
Bangla benchmark for this task) — a reviewer will read the absence as an
oversight unless it is addressed. No error analysis of generated outputs: the
thesis reports that Level 0 is harder without showing what Level-0 failures look
like.

**Weak explanations.** The level asymmetry is the most practically important
finding in the chapter — zero-shot reaches 0.8074 at Level 1 but 0.3296 at Level
0 — and §6.3 describes it without explaining it. Why is producing a *general*
response harder than a *specific* one? A hypothesis (instruction-tuned models are
biased toward informativeness; the 20-word ceiling compresses both levels toward
specificity) would cost a paragraph and would substantially raise the analytical
quality. §6.7's length-matched slice correctly warns against post-treatment
selection but then prints matched accuracies of 0.944 and 0.955 on 9 and 11
pairs, which will be quoted out of context.

**Redundant content.** §6.1 re-derives the ten conditions and the 5,400-case
decomposition already specified in §5.7–§5.8. §6.10 restates §6.9.

**Transitions.** Good throughout; §6.7→§6.8 is the weakest.

**Technical gaps.** Table 6.2 prints nine identical p-values and nine identical
q-values. Effect sizes are reported without a standardised effect measure
(Cohen's d or equivalent) alongside the raw deltas. No per-condition variance or
seed-level spread appears in the main text (Appendix F.2 has it). Figure 6.1 and
6.2 captions are embedded in image alt-text rather than typeset as captions,
unlike Figures 4.1/5.1/5.2 — two different conventions in one document.

**Recommendations.** Add RQ1 to §6.9 (even as a pointer to Chapter 3). Typeset
floor-valued p-values as `< 2×10⁻⁴`. Add a paragraph hypothesising the Level-0
asymmetry. Add a short qualitative error analysis with example outputs. State
explicitly why no external baseline exists. Unify figure-caption convention.

### Chapter 7 — Discussion, Limitations, and Conclusion (2,820 words, 10 citations, 2 tables, 0 figures)

**Purpose.** Interprets findings per RQ, works through five validity domains plus
ethics, states practical implications, contributions, future work and conclusion.

**Organisation.** The validity treatment (§7.3–§7.8, organised by construct /
internal / external / statistical-conclusion / measurement / ethical) is textbook
correct and better than most theses attempt. §7.2.1–§7.2.4 are the only genuine
third-level subsections in the document.

**Missing sections.** No engagement with related work as *comparison* — Chapter 7
cites 10 keys but almost entirely for methodological caution, never to say "our
finding agrees/disagrees with X". No separate "Conclusion" chapter; §7.12 carries
the conclusion inside the discussion chapter, which is acceptable but means the
thesis's closing argument occupies 22 lines. No reflection on what the negative
and unresolved results imply for the field.

**Weak explanations.** §7.10's four contributions are stated but not
evidenced — each should point to the specific result that supports it. §7.11's
future work is sound but generic in places ("a larger human sample"); the most
valuable future direction implied by the thesis's own data (a preregistered
neural-plus-symbolic versus neural-only contrast, powered for the observed
+0.0216 descriptive gap) is stated without the power calculation that would make
it actionable.

**Redundant content.** §7.1 substantially restates §6.10. §7.3's construct
discussion repeats §3.6 and §3.10. Table 7.2 repeats Table 1.1 with different
wording — deliberate bookending, but the wording differences should be
eliminated so the two tables are visibly the same claims.

**Transitions.** §7.8→§7.9 (ethics to practical implications) is abrupt.

**Technical gaps.** Contribution list conflicts with §1.6. No figure. The
conclusion does not restate a single number, so a reader who skips to the end
learns nothing quantitative.

**Recommendations.** Reconcile contributions with §1.6 to one canonical list.
Attach each contribution to its supporting result. Add a comparison-to-literature
subsection. Consider promoting §7.12 to a short Chapter 8 (Conclusion) if the
university template expects a separate conclusion chapter. Add two or three
headline numbers to the closing paragraphs.

### Appendices A–H (7,244 words, 0 citations)

**Standing.** Substantially better than typical thesis appendices. Appendix E
(verbatim prompts, symbolic feature catalogue, a rule-selected correction trace)
and Appendix G (canonical configuration and provenance) are genuinely reusable.
Appendix D discharges a real licensing obligation with per-row Wikipedia revision
IDs.

**Issues.**
- **No appendix cites anything.** Method choices described there (temperature
  scaling, logistic regression, MAUVE) inherit citations from chapters but the
  appendices themselves are citation-free, which is unusual for material intended
  as a standalone artifact record.
- **Substantial A↔G duplication.** A.4 ≈ G.2, A.3 ≈ G.3, A.1 ≈ G.4. One should
  become canonical and the other a cross-reference.
- **Compute hours are explicitly unreported** and flagged in three separate
  places (A.6, C, G.3) as pending.
- **Appendix F.1's 70-row table has no summary statistics** — no per-backbone
  mean or SD, forcing the reader to aggregate by hand.
- **Appendix E's prompt cannot be reconstructed** because the two-level
  operational definition is a `[VERBATIM ...]` slot rather than the actual text.
- **Naming conflicts**: "Gemma-4-31B" (H.3) vs `gemma-4-26b-a4b-it` (everywhere
  else); "maximum three judgments" (A.4) vs "up to two Writer retries" (E.5).
- **Human item-bootstrap resample count is never stated** (B.2 gives CIs; A.5
  gives 10,000 for the paired bootstrap only).

---

## 3. Thesis Structure Recommendation

The existing seven-chapter architecture is sound and should be **refined, not
rebuilt**. The recommendation below preserves every existing result and section,
adds what is missing, and fixes the mapping problems. Changes from the current
state are marked **[NEW]**, **[MOVE]**, **[RENAME]** or **[EXPAND]**.

### Front matter

Title page · Declaration · Certificate/Approval · Acknowledgements ·
**Abstract [EXPAND — Phase 2]** · Keywords · Table of Contents ·
**List of Figures [NEW]** · **List of Tables [NEW]** ·
**List of Algorithms [NEW]** · List of Abbreviations and Symbols
**[EXPAND: add registered verdict labels, KBQA, BM25, BGE-M3, LoRA]**

### Chapter 1 — Introduction
*Purpose: establish the problem, bound the claim, and give the reader the map.*
Serves all objectives; owns none.

1.1 Background: pre-release audience response and Bangla cinema **[EXPAND]**
1.2 Motivation and the limits of synthetic audiences
1.3 Research problem and central question
1.4 Research questions
1.5 Research aim and objectives
1.6 **Mapping of objectives, research questions, chapters and contributions [NEW — Table 1.2]**
1.7 Overview of the research design
1.8 Contributions **[RENAME/reduce to canonical list matching §7.10]**
1.9 Scope and delimitations
1.10 Organisation of the thesis

### Chapter 2 — Related Work
*Purpose: derive the gap from evidence, not from assertion.* Supports the novelty
claim underlying all four RQs.

2.1 **Review methodology: sources, search strategy, year window, inclusion criteria [NEW]**
2.2 Synthetic audiences and controlled response generation
2.3 Self-correction and feedback
2.4 Retrieval-augmented generation
2.5 Neural and symbolic validation **[EXPAND: state the evidentiary bar for symbolic value]**
2.6 Multi-agent workflows and architectural complexity
2.7 Verifiers, judges and proxy optimisation
2.8 Bangla NLP: classification backbones and **generation/evaluation resources [NEW subsection]**
2.9 Human evaluation methodology
2.10 Comparative position and research gap **[merge current §2.10 in]**

### Chapter 3 — Data, Corpus Audit, and Construct Validation **[RENAME]**
*Purpose: prove the target construct exists and is human-recognisable before any
generator is built.* Objectives 1–2; answers RQ1.

3.1 Research design and data-privilege contract
3.2 **Figure 3.1 — frozen data lineage and isolation walls [NEW FIGURE]**
3.3 Primary review corpus and read-only audit
3.4 Cleaning and the frozen partition
3.5 Why full-corpus clustering was rejected **[EXPAND: describe the source signature]**
3.6 Region-A construct discovery and the Region-B negative control
3.7 **Figure 3.2 — clusterability, stability and confound diagnostics [NEW FIGURE]**
3.8 Human validation attempt 1: ordinal ratings (failed gate)
3.9 Human validation attempt 2: comparative intrusion judgments
3.10 Operational definition of the engagement-specificity axis
3.11 Plot corpus and experimental stimuli **[MOVE from current §3.4]**
3.12 Chapter summary and RQ1 verdict **[NEW]**

### Chapter 4 — Verifier Development, Circularity, and Isolation **[RENAME, EXPAND]**
*Purpose: build the measurement instruments and expose their limits.* Objective 3;
supplies the instruments RQ2 and RQ4 depend on.

4.1 Design rationale and verifier roles
4.2 Training and evaluation protocol **[ADD: full hyperparameters for all seven arms]**
4.3 Backbone ablation and the registered `TIE`
4.4 The circularity baseline **[EXPAND — this is the chapter's core]**
4.5 **What circularity implies for the rest of the thesis [NEW]**
4.6 Verifier-A: the in-loop scorer **[ADD: per-class precision/recall/confusion matrix]**
4.7 Verifier-B: the outcome scorer **[ADD: same]**
4.8 **Figure 4.2 — calibration before and after temperature scaling [NEW FIGURE]**
4.9 The executable isolation wall **[ADD: number as Table 4.2]**
4.10 Chapter summary

### Chapter 5 — Proposed Neuro-Symbolic Multi-Agent Framework
*Purpose: specify the framework as an executable, inspectable procedure.*
Objective 4; the mechanism under test in RQ2 and RQ3.

5.1 Architecture, roles and state
5.2 Why this is a bounded workflow, not an autonomous agent
5.3 **Algorithm 5.1 — the bounded generation loop [NEW]**
5.4 Retrieval and the shared prompt contract
5.5 Neural gating and symbolic diagnosis **[EXPAND §5.3 material]**
5.6 Threshold and stopping-policy selection
5.7 Development loop dynamics **[absorb current §5.6 failure taxonomy]**
5.8 The ten experimental conditions
5.9 **Algorithm 5.2 — blind-resampling selection under a matched budget [NEW]**
5.10 Main-run execution contract **[reduce; point to Appendix A]**
5.11 Chapter summary

### Chapter 6 — Experimental Setup, Results, and Analysis
*Purpose: report what happened, in the order that prevents over-reading.*
Objective 5; answers RQ2, RQ3, RQ4.

6.1 Experimental design, outcomes and the frozen inferential family **[reduce duplication with §5.8]**
6.2 Integrity of the completed run
6.3 Main ablation results **[ADD: hypothesis for the Level-0 asymmetry]**
6.4 Planned paired comparisons **[fix p-value typesetting; add standardised effect sizes]**
6.5 Verifier-in-the-loop dynamics and the Goodhart diagnostic
6.6 Blinded human validation of requested level
6.7 Length-controlled sensitivity analysis
6.8 Diversity and corpus-level realism
6.9 **Qualitative error analysis with example outputs [NEW]**
6.10 **Why no external published baseline is available [NEW]**
6.11 Answers to the research questions **[ADD RQ1 pointer]**
6.12 Chapter summary

### Chapter 7 — Discussion and Limitations
*Purpose: interpret, bound, and situate.* Serves all RQs.

7.1 What the experiment establishes
7.2 Interpretation by research question (7.2.1–7.2.4)
7.3 **Relation to prior work [NEW — close the Chapter 2 loop]**
7.4 Construct validity
7.5 Internal validity
7.6 External validity
7.7 Statistical-conclusion validity
7.8 Measurement limitations
7.9 Ethical and practical limitations
7.10 Practical implications

### Chapter 8 — Conclusion and Future Work **[NEW — promoted from §7.10–§7.12]**
*Purpose: state the contribution and the next experiment plainly.*

8.1 Summary of findings **[with headline numbers]**
8.2 Contributions **[canonical list, each attached to its supporting result]**
8.3 Limitations in brief
8.4 Future work **[with the power calculation for the hybrid-vs-neural contrast]**
8.5 Concluding remarks

*If the university template requires exactly seven chapters, keep §7.11–§7.12 in
place and apply only the content fixes.*

### End matter
Generative-AI declaration · References (IEEE, from `references_ieee.bib`) ·
Appendices A–H **[with A↔G duplication resolved]**

---

## 4. Missing Information Required From You

I will not guess at any of these. Items marked 🔴 block Phase 2 or Phase 3.

### A. Target and template

1. 🔴 **What is the immediate deliverable** — the university BSc thesis, the Q1
   journal submission, or both in sequence? They imply different structures
   (8 chapters vs 7), different lengths, and different appendix handling.
2. 🔴 **Which journal or venue**, if known? Word/page limit, reference style, and
   whether appendices ship as supplementary material.
3. Does your university mandate a chapter structure or template? If a template
   exists, send it and I will conform the structure to it rather than proposing
   my own.
4. 🔴 Institutional front-matter fields, currently listed as deliberately pending
   in `docs/thesis_front_matter.md`: legal name, student ID, department, faculty,
   university, degree title, submission date, supervisor name/title/affiliation,
   required declaration wording, and whether you want acknowledgements.

### B. Contributions and framing (blocks the abstract)

5. 🔴 **Which contribution list is canonical — the seven in §1.6 or the four in
   §7.10?** I can propose a reconciled list, but the choice of what you want to
   claim is yours, not mine.
6. 🔴 **What do you consider the primary contribution?** My reading of the
   evidence is that it is the verifier-isolation methodology plus the
   demonstrated proxy divergence, with the Bangla system as the vehicle. If you
   intend the Bangla framework itself as the headline, the abstract and Chapter 1
   need to be framed differently.
7. Open decision 5 in `STATUS.md` is still yours: should the register/source
   finding in §3.5 be framed in the **stylometry/authorship** literature or the
   **machine-generated-text detection** literature? This affects Chapter 2 and
   Chapter 3 wording.

### C. Bibliography decisions

8. 🔴 **`docs/references.bib` (129 entries, semantic keys) is cited by no
   chapter.** Should it be archived out of the thesis build, merged into
   `references_ieee.bib`, or retained for `protocol.md` / `related_work.md` only?
9. 🔴 **88 of 143 entries in `references_ieee.bib` are uncited.** Prune them,
   retain them for a future paper, or use some of them to fill the citation gaps
   I will identify in Phase 6?
10. The keys `b1`–`b143` encode bibliography order, so any inserted citation
    forces a global renumber. Do you want to migrate to stable semantic keys
    before Phase 3 rewriting, or accept renumbering at the end?

### D. Experimental and model details not in any file

11. 🔴 **Training hyperparameters for the seven-backbone ablation** beyond
    learning rate (2e-05 / 3e-05) and seeds (42–46): epochs, batch size, max
    sequence length, optimiser, warmup, weight decay. Appendix G gives these for
    Verifier-B only (LR 2e-05, 4 epochs, batch 16, max len 128).
12. 🔴 **Per-class precision, recall, F1 and confusion matrices** for Verifier-A
    and Verifier-B on dev-82. Do these exist in `results/`? If they do, tell me
    the filenames and I will surface them; if they do not, say so and I will
    report macro-F1 only rather than invent them.
13. **The verbatim two-level operational definition string** used in the prompt.
    Appendix E.2 slots it as `[VERBATIM TWO-LEVEL OPERATIONAL DEFINITION]`, so
    the prompt cannot currently be reconstructed from the thesis.
14. **The number of bootstrap resamples used for the human item-bootstrap CIs**
    in §6.6 / Appendix B.2. The paired bootstrap is documented at 10,000; the
    human one is not stated.
15. **Environment detail**: Python version, torch version, CUDA version, VRAM,
    and the vector-index library/version. Appendix A/G give transformers 5.15.0
    and scikit-learn 1.9.0 only.
16. **Consolidated GPU wall-clock hours** — flagged as pending in A.6, C and G.3.
    If your venue requires a compute figure, this must be derived from archived
    timestamps by a script. Do you want me to write that script, or should the
    figure be omitted with the existing disclosure?
17. **Model identifier conflict**: Appendix H.3 says "Gemma-4-31B"; every other
    file says `gemma-4-26b-a4b-it`. Which is correct? The main text never names
    the judge model at all and should.
18. **Judge-call accounting**: Appendix A.4 says "maximum three judgments";
    Appendix E.5 says "up to two Writer retries". Confirm these describe the same
    budget so I can state it once, consistently.
19. **The §3.5 source signature.** What exactly was the "uniform non-organic
    signature" carried by 60% of rows, and how was it detected? This finding
    justifies rejecting full-corpus clustering and currently gets two sentences.

### E. Figures and visual material

20. 🔴 **Figures 3.1, 3.2 and 4.2 do not exist.** Do you want me to generate them
    from the existing audited artifacts? All three have their data present.
    Chapter 3 currently has no figure at all.
21. Do you want the two Chapter 6 PNGs regenerated as vector (SVG/PDF) for print
    quality, or is the existing raster acceptable? Mixing formats is a production
    risk but regenerating means touching frozen figure artifacts, which I will
    not do without instruction.
22. Should the Appendix E.7 worked correction trace be promoted into Chapter 5 as
    a figure or worked example? It would materially help the reader.

### F. Additional results and analysis

23. **Qualitative examples.** May I include example generated outputs (Bangla with
    English gloss) in Chapter 6 for error analysis? If yes, should they be
    selected by a stated rule (as Appendix E.7 was) rather than hand-picked?
24. **Standardised effect sizes** for Table 6.2 — do these exist in
    `s5_main_bn_paired_statistics.csv`, or should the table report raw deltas and
    CIs only?
25. **External baseline.** Is there any published Bangla system on a comparable
    task you want positioned quantitatively, or is the correct statement that no
    comparable benchmark exists?

### G. Research-integrity item

26. `STATUS.md` records that the six Tier-1 base papers are **"6 briefed, 0 read
    by Sabbir"**, and flags this as the project's highest risk. Chapter 2 rests
    on those readings. Before Phase 3 rewriting hardens that chapter, do you want
    to read them, or should Chapter 2 be written to claim only what the briefs
    verifiably support?

---

## Recommended sequence from here

1. You answer Section 4 (at minimum the 🔴 items).
2. **Phase 2** — abstract, written only from confirmed numbers.
3. You approve or amend the Section 3 structure.
4. **Phase 3** — chapter-by-chapter rewriting, in dependency order:
   Ch1 → Ch4 (largest gap) → Ch3 → Ch5 → Ch6 → Ch7/8 → Ch2.
5. **Phases 4–7** — technical verification, quantitative gap check, full citation
   audit with the four required lists, and the final reviewer evaluation.
