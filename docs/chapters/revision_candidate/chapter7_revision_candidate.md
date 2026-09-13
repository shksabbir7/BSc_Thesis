# Chapter 7 — Discussion and Limitations

Chapter 6 showed that generated Bangla cinema responses can be made more
consistent with a requested engagement-specificity level, while also exposing
a gap between successful control and faithful audience modelling. This chapter
interprets that gap and considers the limits of the evidence. Contributions
and future work are reserved for the final chapter.

## 7.1 Main Finding

The evidence shows that conditioning and revision make short Bangla cinema
responses more consistent with a requested engagement-specificity level than
zero-shot prompting. Verifier-B provides consistent coverage of the complete
frozen generation surface, and native Bangla readers usually identify the same
distinction on a smaller blinded subset. Neither result demonstrates that the
system reproduces a real audience. The generated responses were not matched
against reactions to the same films, and the two levels do not represent
demographic or psychological groups. The result is therefore about control
over a textual distinction, not prediction of viewers, sentiment, popularity,
or commercial performance. This boundary is especially important because
synthetic-audience research is vulnerable to prompt sensitivity, hallucination
and anthropomorphic interpretation [@b1]. No single mechanism accounts for the
improvement: static examples, retrieval, blind resampling, self-critique and
verifier-guided revision all improve on zero-shot under the planned
comparisons. The neuro-symbolic condition has the largest observed difference
from zero-shot, but the experiment does not rank the active systems. Its direct
comparison with the neural-only loop was post-hoc and remains exploratory.

### 7.1.1 Engagement Specificity as a Continuum

The early corpus analysis changed the meaning of the target variable. The
Region-A partition was reproducible, yet the geometric evidence did not support
two separated clusters: the silhouette was weak, the gap statistic selected no
value of K, and HDBSCAN treated the points as noise. Human comparative judgment
showed that readers could nevertheless recognize the contrast and its
direction. This combination supports a usable cut through a continuum, not two
naturally occurring audience types.

The framework can therefore request a broader or more specific response without
assigning a person to a fixed category. It controls a property of the generated
text; it does not infer personas within Bangla-speaking audiences.

Length remains part of the construct problem. The corpus, development outputs
and final generations all show that engagement specificity and response length
are related, although the direction is not stable across every setting. The
length-matched analysis retains a Level-0 deficit, so length alone does not
explain the result. At the same time, matching keeps only a selective fraction
of the outputs and cannot establish length-neutral control. The model appears
to manipulate a bundle of cues—detail, reference to plot events, evaluative
specificity and length—rather than an isolated semantic property.

## 7.2 What the Control Mechanisms Add

The ablations separate four functions that would otherwise be hidden inside one
system score:

- **Examples and retrieval.** Static demonstrations and R1 retrieval show the
  two levels in Bangla. They improve the prompt but do not decide when a draft
  has reached its target.

- **Neural verification.** Verifier-A supplies the stopping decision. Revision
  costs additional calls, and later attempts contain only earlier failures, so
  their trajectory describes difficult survivors rather than a fixed population.

- **Symbolic diagnosis.** Symbolic acceptance is weak and inefficient,
  particularly at Level 1. Symbolic feedback is more useful for naming a problem
  while the neural verifier retains the stopping decision. The Level-0 increment
  over neural-only is exploratory, not evidence of general hybrid superiority.

- **Alternative critics.** Self-critique improves control at a fixed three-call
  cost. The hosted judge is a comparator, not an independent outcome authority.
  Evaluator replacement, self-preference and uneven multilingual agreement
  reinforce this restriction [@b22; @b23; @b24; @b25].

### 7.2.1 Why Verifier Separation Matters

Verifier separation becomes most informative during revision. In the
neural-gated loops, drafts selected to satisfy Verifier-A receive progressively
less comparable support from Verifier-B. Because both scores are available on
the same continuing cases, the divergence cannot be attributed to a change in
plot or requested level. Improvement against the in-loop proxy and improvement
under a held-out instrument are not interchangeable.

This pattern is consistent with Goodhart-style pressure, but the evidence does
not identify reward hacking in every revised response. Later attempts are
failure-selected, Verifier-B has its own errors, and its calibration improvement
was not established. Repeated optimization nevertheless changes the
relationship between the two instruments in the direction expected when a proxy
becomes increasingly exploitable. Evaluator stress-testing work
similarly argues that an optimized score needs independent or invariant checks
before it can stand for the intended construct [@b7].

Keeping Verifier-B outside generation therefore does more than prevent direct
leakage. It makes disagreement observable. Had the same verifier controlled
revision and supplied the final outcome, the experiment could report rising
scores without showing whether the revisions generalized to another trained
instrument. The separation does not make Verifier-B ground truth, but it turns
proxy dependence into an empirical question.

## 7.3 Human and Automatic Evidence

The blinded study tests the meaning of the output labels rather than providing
another condition leaderboard. Native Bangla readers usually recover the
requested level with strong panel agreement, but five items per condition-level
cell are too few for reliable system ranking.

The same-item comparison reveals an important asymmetry. Human majority labels
perform similarly at both levels, whereas both automatic verifiers are weaker
at Level 0. This makes an instrument-specific Level-0 problem plausible. It
does not prove that the human panel is the definitive oracle: the comparison
contains only 100 items, and within-level agreement statistics are affected by
fixed requested-label marginals [@b36; @b37]. Still, the discrepancy warns
against describing Verifier-B accuracy as human quality.

Annotators selected the requested level; they did not rate fluency, plot
faithfulness, sentiment, usefulness, offensiveness or resemblance to real
audience responses. Human validation therefore supports controllability of the
stated distinction, not overall response quality.

## 7.4 Practical Implications

The evidence supports three practical decisions:

- **Appropriate use:** an inspectable pre-writing aid for comparing both levels,
  reviewing retrieved examples and revision status, and preparing questions for
  direct audience research.

- **Unsupported use:** autonomous marketing, casting, segmentation or commercial
  forecasting. The study learns no film-level response distribution and links no
  generated statement to a demographic group.

- **Deployment choice:** static prompting, retrieval or blind resampling may suit
  inexpensive variety; neural-guided loops add stopping and correction traces.
  The symbolic-only loop is not supported as a default, and cost should not be
  hidden inside one quality score.

## 7.5 Limitations

### 7.5.1 Construct and Measurement

- The axis comes from one Bangla review corpus with unresolved source history;
  region, sentiment and length complicate its geometric origin. Human validation
  supports an operational label, not a natural audience taxonomy.

- Verifier-B is a fixed instrument, not a calibrated probability of human
  acceptance. Its Level-0 mismatch and calibration null remain unresolved.

- The realism measures capture different properties. LaBSE-feature MAUVE is
  small-sample sensitivity evidence [@b55], and sentiment divergence remains
  unmeasured because no independent registered scorer was available.

### 7.5.2 Internal and Statistical Validity

- Verifier-A and Verifier-B use disjoint data and different model families, but
  learn the same operational label; their errors need not be independent. The
  hosted judge is also a same-family treatment, not an external authority.

- Later attempts are failure-selected, and length matching conditions on a
  property changed by generation. Neither analysis supports an unrestricted
  causal reading.

- The primary tests use 540 paired cases, paired bootstrap, McNemar testing and
  Benjamini–Hochberg correction [@b49; @b50]. The three seeds are sensitivity
  blocks, not independent replications, and the direct hybrid contrast remains
  outside the registered comparison family.

### 7.5.3 External Validity, Human Evaluation, and Ethics

- The corpus has no film identifier. The 90 held-out plots separate evaluation
  from development but do not establish generalization to other Bangla
  registers, communities, domains or generator families.

- The three adult native-Bangla evaluators were university batchmates known to
  the researcher. Blinding and coded identities do not remove the limits of a
  convenience sample or possible social pressure. No institutional approval or
  exemption is claimed, and absent fields were not reconstructed [@b32].

- Outputs may contain stereotypes, offensive language or unsupported plot
  details. The interface's source-support diagnostic was not part of the frozen
  experiment or a registered human faithfulness audit; it neither establishes a
  hallucination rate nor certifies safety.

## 7.6 Chapter Summary

The study shows that engagement specificity can be varied in short Bangla
cinema responses, while the verifier and human evidence explains why this
result is not audience simulation. Chapter 8 closes the argument and identifies
the evidence still needed beyond this corpus.
