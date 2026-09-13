# Chapter 1 — Introduction

This chapter defines the problem: controlling engagement specificity in short
Bangla cinema responses before audience reviews are available. It introduces
the research questions, design, scope, and the separation between
generation-time and outcome verification.

## 1.1 Background

Audience commentary becomes available only after viewers encounter a film.
This thesis asks whether a language model can generate short, plot-based Bangla
responses before such commentary exists. Large language models (LLMs) can
produce plausible responses from a synopsis, and recent work
has evaluated this capability specifically for movie-review generation [@b12].
Fluent review-like text, however, establishes neither control of a requested
characteristic nor credible prediction of real audience reception.
Research on synthetic audiences similarly warns that fluent outputs may
reproduce social and representational biases, respond inconsistently to prompt
wording, hallucinate user characteristics, and encourage anthropomorphic
interpretations beyond the available evidence [@b1].

Producing a fluent Bangla comment is only part of the task. The requested level
of engagement specificity must be recognizable, controllable, and evaluated by
a scorer that did not guide the generation process.
Classifier-guided generation provides a precedent for conditioning text on a
target attribute [@b11]. In this study, the target construct is developed for
Bangla, revision is limited to three attempts, and the final evaluator is kept
outside the generation process.

The study focuses on Bangla text written in Bengali script and on short,
informal cinema commentary in the Bangladeshi research context.
BanglaBERT provides a pretrained encoder for Bangla language understanding
[@b2], while Language-Agnostic BERT Sentence Embedding (LaBSE) provides
multilingual sentence representations [@b3]. The primary review resource is
the 5,000-row *Raw Bangla Movie Review Comment
Dataset for Sentiment Analysis and Natural Language Processing* [@b4]. Its
reviews are short and sentiment-labelled, but the dataset contains no
movie-title field, audience demographic information, or row-level record of the
original collection source. It can therefore support a bounded study of textual
response patterns and controllability, but not film-linked audience modelling,
demographic audience segmentation, or claims that generated responses predict
what actual viewers will say.

## 1.2 Motivation

Prompting alone does not demonstrate control. The target distinction may be
poorly defined, or a model may satisfy it through a shortcut such as response
length. Repeated revision can also raise the score of a visible evaluator by
exploiting its weaknesses. Intrinsic self-correction is unreliable without
dependable external feedback [@b5; @b6].

Controlled-generation methods use discriminators to influence an attribute
[@b11], retrieval-augmented generation supplies contextual evidence [@b8], and
generate–critique–revise procedures attempt to improve initial outputs.
Synthetic-audience research examines risks of generated human proxies [@b1].
It remains unclear whether a response distinction derived from Bangla reviews
can be controlled during generation and evaluated by a verifier that was not
used to optimize the text. The present study combines the existing mechanisms
to examine that question; it does not treat the mechanisms themselves as new.

The generated comments are therefore treated as experimental texts, not as
predictions of audience behaviour. Verifier-A guides revision, whereas
Verifier-B scores the completed outputs and is never shown to the generator.
This separation allows the analysis to detect disagreement between the two
verifiers. Such disagreement matters because optimization against a visible
evaluator can exploit its weaknesses, as evaluator stress tests have shown
[@b7].

## 1.3 Problem Statement

The review corpus does not contain engagement-specificity labels. A usable
distinction must therefore be derived without confusing it with sentiment,
text length, or differences between corpus sources. The generator must then
produce the requested level under a fixed retry policy. Finally, any gain
reported by the in-loop scorer must be checked by an evaluator trained on
disjoint data and excluded from prompt development, acceptance decisions, and
retry routing.

Corpus analysis did not support natural audience categories. Instead, it
supported an operational **engagement-specificity continuum**. At Level 0, a
response is general, formulaic, or only weakly connected to a particular film
detail. At Level 1, it engages with a specific event, character, relationship,
or narrative element. These levels constitute a reproducible cut through a
continuum. They are neither discovered demographic groups nor evidence that the
source reviews contain naturally separated clusters.

The central question is whether a task-trained verifier can improve control of
this distinction when placed inside a generate–verify–refine workflow. The
comparison includes zero-shot generation and the other registered controls,
while Verifier-B remains outside the loop. The study also separates the use of
symbolic rules for acceptance from their use as revision feedback.

## 1.4 Research Aim and Objectives

The aim of this thesis is to design and evaluate an auditable
verifier-in-the-loop framework for controlling engagement specificity in short
Bangla cinema responses while keeping generation guidance separate from final
outcome evaluation.

The specific objectives are to:

1. recover an operational engagement-specificity distinction from the Bangla
   review corpus and determine whether it remains stable and human-recognizable
   after testing corpus-region, sentiment, and length confounds.
2. implement the bounded verifier-guided workflow and quantify how its
   registered prompting, retrieval, critique, judging, and resampling
   conditions change target-level controllability relative to zero-shot
   generation.
3. determine how symbolic information functions when used for acceptance
   gating and when used as diagnostic feedback alongside neural verification.
4. test whether iterative optimization against the in-loop Verifier-A produces
   measurable divergence from the isolated outcome Verifier-B.

## 1.5 Research Questions

This study addresses the following research questions:

- **RQ1:** Can a meaningful response distinction be recovered from unlabeled
  Bangla reviews and validated as stable and human-recognizable?
- **RQ2:** To what extent do verifier-guided generation and the registered
  prompting, retrieval, self-critique, external-judge, and resampling controls
  improve target-level controllability over zero-shot generation in Bangla?
- **RQ3:** What role does symbolic information play when used for acceptance
  gating and for diagnostic feedback within verifier-guided Bangla response
  generation?
- **RQ4:** Does iterative optimization against Verifier-A produce measurable
  divergence from the independent Verifier-B?

In RQ1, stability refers to reproducibility of the two-level cut; it is not
evidence of natural audience categories. The confirmatory tests for RQ2 compare
each of the nine registered conditions with zero-shot generation. Comparisons
among the active conditions are descriptive or exploratory. RQ3 treats
acceptance rules and diagnostic feedback as different uses of symbolic
information. RQ4 uses Verifier-B as an independent outcome measure, not as
human ground truth.

The four questions address control and evaluation of generated text. Audience
prediction, demographic segmentation, and commercial forecasting fall outside
their scope.

## 1.6 Research Design Overview

The review corpus supports construct development, retrieval, and verifier
training; 120 Bangla Wikipedia film synopses supply separate generation
stimuli. They cannot form film–review pairs because reviews lack movie titles.

Cleaning and near-duplicate control leave 4,625 reviews for the frozen split.
The 300-item Gold partition is reserved for evaluation. R1 supplies retrieval
examples and training data for Verifier-A; R2 is used only to train Verifier-B.
The initial full-corpus partition identified corpus region with 93.3% accuracy,
which points to a source or style difference rather than audience personas. In
Region A, the two-way cut was reproducible, but the silhouette was 0.053, the
gap statistic selected no value of \(K\), and HDBSCAN labelled every review as
noise. These results do not support natural clusters.

Length remained a possible shortcut: a length-only classifier achieved AUC
0.6764. The surface and residual profiles are therefore reported as
descriptions, not as independent validation. The first Gold-300 instrument,
which used ordinal ratings, failed its reliability gate
(Krippendorff's \(\alpha=0.4970\)); no downstream validity test was performed.
A second instrument used length-matched comparisons. The two annotators found
the different item in 39/50 and 42/50 intrusion sets and chose the more
engagement-specific response in 34/40 directional pairs. Chance performance was
0.25 and 0.50, respectively, while a length heuristic scored 0.16 on the
intrusion task. The distinction is perceptible to the annotators, but it remains
a cut through a continuum.

Generation proceeds through four functional roles. The Researcher retrieves
same-level examples from the R1 index [@b8], and the Writer produces a response
to the film plot. The Critic applies Verifier-A and the symbolic checks; the
Reflector turns a failed check into revision guidance. These roles form one
controlled workflow rather than four autonomous agents. Neural scores determine
acceptance in the main condition, while symbolic rules identify specific
problems in the draft. Each case permits at most three Writer attempts, and no
LLM is fine-tuned.

Verifier-A uses LaBSE features to reproduce labels that were also derived from
LaBSE space. Its near-perfect label accuracy is therefore partly circular: it
shows that the cut can be learned within the same representation family, but it
does not provide independent human validation. That evidence comes from the
comparative annotation task. Verifier-B instead uses BanglaBERT, is trained on
R2, and remains unavailable until final scoring.

Thirty development plots are used for prompt, threshold, and retry-policy work.
The main experiment uses 90 held-out plots, two levels, ten conditions, and
three paired seeds, producing 5,400 frozen outputs. Zero-shot and nine
registered alternatives include a realized model-token-budget-matched blind
resampling control. Verifier-B is applied only after generation. Seeds are
paired sensitivity blocks, not independent replications.

All nine registered alternatives improved Verifier-B target probability
relative to zero-shot. Neural gating with symbolic diagnostic feedback produced
the largest observed registered zero-shot contrast, +0.2570 with a 95%
paired-bootstrap confidence interval of [0.2151, 0.2987], but this does not
establish superiority over other active conditions. A post-hoc comparison with
neural-only gating remains exploratory. On a frozen balanced 100-item subset,
three blinded
native-Bangla annotators recovered the requested level with pooled accuracy
0.9133 and a 95% item-bootstrap interval of [0.8667, 0.9567]. Same-case
revisions among continuing failed cases also widened the Verifier-A–Verifier-B
gap in the neural-gated loops, consistent with proxy overoptimization but not
proof of reduced human quality.

## 1.7 Scope and Limitations

The study is limited to short Bangla cinema responses at two levels of
engagement specificity. It tests control of those levels and the separation of
the two verifiers; it does not forecast audience opinion.

Source reviews lack film, audience, venue, and row-level provenance. The corpus
has no separated natural clusters; its levels remain a continuum cut. Although
construct-validation items were length-matched, generated length remained
informative about requested level, precluding a length-neutral control claim.
The generation study covers Bangla only; the incomplete English mirror supports
no cross-lingual conclusion. Its three seeds are sensitivity blocks, not
independent replications.

The comparative instrument followed the failed ordinal instrument and departed
from the pipeline's prescribed remedy. Although preregistered before judgment,
it was designed after the first result; this remains a limitation, and a third
instrument was prohibited. The blind-resampling
comparator matches realized total tokens under the same generator rather than
measured FLOPs, latency, hardware utilization, or the functional role of calls.

The human evaluation covers a balanced sample of 100 from the 5,400 outputs. It
shows that readers can recover the requested level in that sample; it does not
rank the ten conditions or assess naturalness, factual support, plot
faithfulness, persuasiveness, or audience preference. Verifier-B is an outcome
proxy, not human ground truth, and temperature scaling did not establish an
improvement in its calibration. A widening gap between the verifiers is evidence
of proxy divergence, not evidence that people would judge the revised text as
worse. The direct comparison of neural-plus-symbolic feedback with neural-only
gating was post-hoc and remains exploratory. The results are also tied to short
cinema responses, Wikipedia film plots, the tested prompts, and the principal
generator family. Chapter 7 discusses these limits in detail.

## 1.8 Contributions

This thesis makes six contributions:

1. A verifier-isolation protocol separates generation control from outcome
   evaluation and measures divergence on revisions of the same case.
2. The neuro-symbolic workflow records every attempt and reports both logical
   calls and token use across a frozen ten-condition experiment.
3. The construct-validation process rejects the initial persona interpretation,
   records the failed ordinal instrument, and retains only the
   human-recognizable engagement-specificity continuum supported by the
   length-matched comparison task.
4. The circularity analysis explains why reproducing LaBSE-derived labels with
   a LaBSE probe is not independent evidence of human validity.
5. A blinded human study tests whether readers can recover the requested level
   from a frozen, balanced sample of generated Bangla responses.
6. The results distinguish symbolic acceptance decisions from symbolic
   diagnostic feedback. Symbolic-only acceptance was weak, while the added
   value of symbolic feedback beside neural gating remains exploratory.

These contributions address controllability, verifier isolation, and the
evidence needed to justify the target construct. They do not establish audience
prediction or general superiority of a multi-role system. The accompanying
[GitHub repository](https://github.com/alphapie77/BSc_Thesis) provides the
complete configurations, attribution records, prompt contracts, supplementary
tables, traces, and interface documentation.

## 1.9 Thesis Structure

The thesis is organized into eight chapters, with each chapter addressing a
distinct part of the research:

- **Chapter 1** introduces the research background, motivation, problem, aim,
  objectives, research questions, research design, scope, limitations, and
  contributions.
- **Chapter 2** reviews synthetic audiences, controllable generation,
  self-correction, evaluator gaming, retrieval-augmented generation,
  neuro-symbolic systems, multi-agent workflows, Bangla NLP, and human
  evaluation, and identifies the research gap.
- **Chapter 3** describes the data resources, preprocessing, frozen partitions,
  corpus diagnostics, development of the engagement-specificity construct,
  and the two-annotator construct-validation study.
- **Chapter 4** develops and evaluates Verifier-A and Verifier-B, reports their
  predictive and calibration properties, and specifies the data-isolation and
  outcome-evaluation wall.
- **Chapter 5** presents the functional
  Researcher–Writer–Critic–Reflector workflow, R1-only retrieval, symbolic
  diagnostics, bounded retry policy, intervention matrix, and experimental
  design.
- **Chapter 6** reports the computational experiment, registered zero-shot
  comparisons, exploratory analyses, verifier-divergence diagnostics,
  diversity and distributional analyses, and the separate three-annotator
  evaluation of generated outputs.
- **Chapter 7** interprets the findings and examines construct, internal,
  external, and statistical-conclusion validity, together with ethical and
  practical implications.
- **Chapter 8** closes the thesis with the conclusion and directions for future
  research.

## 1.10 Chapter Summary

The thesis asks whether short Bangla cinema responses can express a requested
engagement-specificity level without allowing the generation-time verifier to
judge its own outputs. Chapter 2 places that question in the relevant
literature.
