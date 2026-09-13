# Chapter 2 — Related Work

This chapter reviews the work that informs the study: synthetic audiences,
controlled generation, self-correction, retrieval, neural and symbolic
verification, multi-agent workflows, Bangla NLP, and human evaluation. The
review focuses on what each area contributes to controlled Bangla response
generation and where its evidence stops. The final section uses those limits to
define the research gap.

## 2.1 Synthetic Audiences and Response Control

Language models are increasingly used to approximate audiences, users, or
personas before direct human evidence is available. One model can produce many
responses under different conditions, but plausible language is not evidence
of behavioural validity. A generated response may resemble an intended persona
without predicting how any person or population would respond. A recent
systematic review identifies hallucination, bias, prompt sensitivity, limited
ecological validity, and anthropomorphic interpretation as recurring problems
in synthetic-audience studies [@b1]. The risk is greatest when generated text
is presented as evidence about a community rather than as a hypothesis for
later human research.

Mixture-of-Personas illustrates one approach to population-conditioned
generation: latent or synthesized persona representations are used to steer a
common language model toward diverse response distributions [@b9]. SimAB
extends the synthetic-audience idea to persona-conditioned agents for rapid web
A/B-test evaluation and compares simulated decisions with historical outcomes
[@b10]. Both studies show how explicit conditioning can broaden the range of
generated responses. Their aim is population simulation or behavioural
prediction. This thesis asks a narrower question: whether a requested level of
engagement specificity can be expressed and recognized in Bangla comments.

Controlled generation provides a second relevant tradition. FUDGE modifies
token probabilities using a learned future discriminator while leaving the
base generator unchanged [@b11]. This shows that an external classifier can
steer generation without fine-tuning the generator. FUDGE applies its
discriminator during decoding. The system studied here instead scores a
completed draft and may request another attempt. FUDGE also has no separate
outcome evaluator for testing whether optimization has exploited the steering
model. It is a methodological precursor, not the same architecture.

Movie-review generation is the closest application domain. Sands et al.
evaluate reviews written by LLMs and distinguish fluent persona-conditioned
text from evidence of authentic audience response [@b12]. Generated comments
in this thesis are treated as experimental texts, not as predicted reviews of a
film.

## 2.2 Revision with Feedback

Iterative refinement assumes that a language model can inspect a draft, find
its mistakes, and produce a better answer. The evidence is conditional. Huang
et al. find that intrinsic
self-correction—revision without reliable external feedback—does not
consistently improve the reasoning tasks they examine and can alter correct
answers [@b5]. Kamoi et al. similarly distinguish intrinsic feedback from
correction supported by an oracle, tool, environment, or separately trained
model, finding stronger evidence when feedback is externally grounded [@b6].
These findings show that generation ability does not guarantee reliable
self-evaluation.

Self-Refine operationalizes an intrinsic generate–feedback–revise cycle using
the same model [@b13]. Reflexion stores verbal feedback in memory and can draw
that feedback from internal or external signals depending on the task [@b14].
Both systems make intermediate critique explicit. Their results do not show
that self-generated criticism is always accurate, or that reflection rather
than the additional model calls causes the improvement.

External verification provides an alternative. Cobbe et al. train a verifier to
rank sampled completions and report that verifier-based selection improves
performance relative to additional generator fine-tuning [@b58]. The result
supports an independently trained selection signal, but it concerns ranking a
fixed candidate pool rather than revising one draft. The experiment in this
thesis includes both verifier-guided revision and blind resampling.

Role placement is also consequential. Recent evidence shows that the effect of
explicit error feedback can change when identical feedback is assigned to
different conversational roles [@b15]. This motivates comparing intrinsic and
external-role critique while holding the critique content constant.

Compute-aware controls are needed to separate reflection from the benefit of
extra calls. One recent study reports
that repeated sampling can match or exceed Self-Refine and Reflexion under equal
token budgets in its tested settings [@b16]. Other recent reasoning evidence
argues that refinement can outperform resampling under different test-time
conditions [@b17]. The studies use different tasks, models, correction signals,
and definitions of budget, so the findings are not directly contradictory. They
do show why refinement must be compared with resampling under a stated cost
budget.

The number of revisions also matters. Feedback-control analysis describes
self-correction as a dynamic process that may improve initially and then cross
a stability boundary where further revision becomes harmful [@b18]. An
evaluation should report where the loop stops, what changes between attempts,
and how much computation it uses.

## 2.3 Retrieval-Augmented Generation

Retrieval-augmented generation combines a parametric generator with external
non-parametric memory [@b8]. Retrieved material can provide facts, examples, or
domain-specific language that is absent from a prompt. It can also create
leakage, copying, and evaluation circularity when retrieved examples overlap
with training or assessment material. Its value depends not only on retrieval
quality, but also on how the index is built and which data it may contain.

Here, reviews provide examples of register and target level; they are not
factual evidence about a plot. This distinction matters because the
source corpus contains no review-to-film mapping. Retrieval cannot establish
that a generated statement is true of the input film; it can only condition the
style and specificity of the response. The index is restricted to R1, excludes
R2 and Gold-300, retrieves within the
requested level, and retains copy diagnostics. A randomized static few-shot
condition separates the effect of receiving examples from the effect of
semantic retrieval.

HybridRAG-BN is a close recent Bangla-language adjacency. It addresses
knowledge-base question answering (KBQA) by combining BM25 lexical retrieval
with BGE-M3 dense retrieval, Gemma generation, and a verifier and refiner
obtained by low-rank adaptation (LoRA) fine-tuning of Gemma [@b19]. Its
retrieved knowledge base can provide query-relevant facts, and its verifier
participates in answer repair. The index used in this thesis instead provides
response exemplars, not plot facts. No language model is fine-tuned, and
Verifier-B cannot participate in revision. HybridRAG-BN demonstrates retrieval
and verification in Bangla, but it does not address the same data separation or
audience-response task.

## 2.4 Neural and Symbolic Verification

Neural and symbolic evaluators offer complementary properties. Neural
classifiers can learn flexible boundaries from contextual representations, but
their scores rarely identify an actionable reason for failure. Hand-specified
symbolic rules can name observable defects, yet such rules may be incomplete,
brittle, or weakly predictive. A neuro-symbolic design must state whether
symbolic information changes the decision boundary, explains a neural
decision, or guides a subsequent repair; these are different claims and they
carry different evidentiary burdens.

SymDiag provides a recent example in which symbolic verification supports
explainable diagnosis and repair of multi-step reasoning [@b20]. Its
satisfiability-based setting differs from short Bangla comments, for which no
complete formal theory of an acceptable response exists. The useful connection
is architectural: outcome assessment can be separated from a diagnosis that
names the failed constraint.

Prediction and diagnosis require separate evidence. Symbolic information
should affect acceptance only if it
improves held-out discrimination beyond the neural score; otherwise, its role
is limited to naming observable failures and guiding revision. The experiment
tests symbolic gating and symbolic diagnostic feedback separately; the term
*neuro-symbolic* is not treated as evidence of predictive benefit.

## 2.5 Bounded Multi-Agent Workflows

Multi-agent language-model systems divide a task among roles such as planner,
retriever, writer, critic, or reviewer. Role separation can make intermediate
decisions inspectable and can restrict which component may access a particular
tool or dataset. It does not, by itself, guarantee better output. Additional
roles can duplicate work, amplify an early error, or consume more tokens without
adding independent evidence.

A recent controlled comparison of single-agent and multi-agent RAG systems for
repository documentation illustrates this trade-off [@b21]. The multi-agent
workflow achieved strong structural consistency, but a simpler single-agent
pipeline obtained comparable lexical quality with substantially lower token
cost. Developer-guided planning performed best in that study, suggesting that
the value of decomposition depended on where reliable structure entered the
workflow rather than on the number of agents alone. Its software-documentation
task is not directly comparable with Bangla cinema responses, but the result
rules out a generic claim that agentic complexity is inherently beneficial.

The architecture is described as a **bounded multi-agent workflow** with a
predefined control flow, not as an autonomous system.
Writer and Reflector are model-calling roles; Researcher is a retrieval and tool
role that makes no model call; Critic is a deterministic neural–symbolic
evaluation role that also makes no model call. Their privileges and transitions
are fixed rather than negotiated at run time. The ten-condition experiment tests
retrieval, verification, feedback, judging, and resampling mechanisms. It does
not include a direct single-agent-versus-multi-agent architecture ablation and
cannot establish that a multi-agent architecture is better than a single-agent
alternative.

## 2.6 Verifier Reliability and Proxy Gaming

Learned verifiers can make generation control inexpensive, but they also create
a proxy: the system optimizes what the verifier recognizes rather than the
intended construct itself. Evaluator Stress Tests formalize this concern
through perturbations that separate proxy improvement from performance under an
independent criterion [@b7]. Large language model (LLM) judges introduce related
risks, including rubric sensitivity, position effects, and self-preference when
evaluator and generator share model families. Fixed responses can receive
different measurements after a judge change [@b22], and rubric-based judges can
prefer outputs from their own model family [@b23]. Multilingual evidence also
finds uneven judge reliability across languages [@b24], while a low-resource
Basque study reports weak agreement both with humans and across judges [@b25].
These findings prevent the hosted same-family Gemma judge from serving as the
final Bangla outcome evaluator.

An outcome evaluator must be kept outside the procedure it assesses. Verifier-A
is deliberately available during generation, whereas
Verifier-B is trained on disjoint data with a different pretrained model and
tokenizer and is never allowed to gate, select, critique, or rewrite an output.
A widening A–B gap is interpreted as evidence consistent with proxy
overoptimization. It is not proof that Verifier-B represents human truth or
that human-perceived quality has declined.

## 2.7 Bangla NLP for This Study

### 2.7.1 Classification Backbones

Bangla NLP systems vary in pretraining corpus, tokenizer, script coverage, and
register. BanglaBERT provides a Bangla-specific pretrained language model and
evaluation benchmarks [@b2], while LaBSE provides language-agnostic sentence
embeddings suitable for multilingual semantic comparison [@b3]. These
resources enable controlled studies in Bangla, but model identity alone does
not determine which representation will best reproduce a constructed label.

Recent Bangla classification studies reinforce that caution. MuRIL performs
strongly on Bangla emotion detection [@b26], whereas studies on BanglaBlend and
Bangla form classification report advantages for XLM-R or IndicBERTv2 over
BanglaBERT in their respective settings [@b27; @b28]. Their tasks and datasets
do not settle the verifier choice for this thesis. They show why a
Bangla-specific backbone cannot be assumed to be superior from its name alone.

This is especially relevant for short reviews. Sentiment, length, punctuation,
and source register may dominate a representation that is later interpreted as
engagement or persona. These factors are audited before the construct is named,
and the verifier backbones are compared on the task rather than selected from
model identity.

### 2.7.2 Generation and Evaluation Resources

Classification backbones address only half of the low-resource problem. A study
that generates Bangla text also depends on what is known about Bangla generation
quality and on which instruments exist to evaluate it, and that literature is
both thinner and more recent.

Three 2026 resources are directly relevant. A multi-task hallucination
evaluation framework for Bengali reports that no prior work had systematically
evaluated hallucination in large language models for the language, despite its
speaker population [@b98]. A curated dataset on honorific failures in
multilingual Bangla generation targets a failure mode in which output is
superficially polite but pragmatically wrong [@b99]. A benchmark for
sociopragmatic and cultural alignment in Bangladeshi social interaction reports
that fluency alone does not guarantee socially appropriate language use in a
high-context language [@b110]. Alongside these, work on informal Bangla machine
translation documents that informal Bangla is under-resourced relative to
formal Bangla [@b111]. This matters because the review corpus consists of
informal comments.

Apparent Bangla fluency cannot replace evaluation by a separately trained
verifier and native readers. Register and honorific use also remain possible
failure dimensions outside the symbolic checks used in this study. They are
reported as limitations of the evaluation.

## 2.8 Human Evaluation of Controlled Generation

Human evaluation serves two distinct purposes in this thesis: validating the
corpus-derived construct and assessing whether generated outputs express the
requested level. These purposes require different instruments. Comparative
judgments can be more reliable than rating scales for subjective intensity
annotation [@b29], while recent work shows that ratings and comparisons may
provide complementary information rather than interchangeable measurements
[@b30]. The elicitation format must therefore match the construct, and the
instrument must be tested rather than assumed to be reliable.

The generated-output study uses a forced binary target-level judgment rather
than a general quality rating. Agreement is reported through raw three-way
agreement and nominal Krippendorff alpha [@b31], with item-level bootstrap
uncertainty. HEDS 3.0 guides transparent reporting of recruitment, evaluated
systems, allocation, criteria, ethics, and analysis decisions [@b32]. Agreement
is not treated as validity on its own, and the human study is not used to rank
conditions whose per-cell sample is too small.

The composition of the evaluation set also matters. Outcome-blind balanced
selection avoids conditioning the human sample on either verifier, a risk noted
for metric-guided NLG evaluation sampling [@b33]. Replicable evaluation depends
jointly on item allocation and ratings per item [@b34], and persistent rater
identifiers are needed to represent annotator variation [@b35]. Work on global
and pairwise scoring likewise supports matching the elicitation form to the
estimand instead of treating one format as universally best [@b36]. For three
nominal raters, metric-selection guidance further supports reporting
Krippendorff alpha with uncertainty and disagreement patterns instead of a
universal agreement cutoff [@b37].

The preceding sections identify the methods used in this thesis and the limits
of the evidence behind them. The remaining gap lies in testing those methods
under the same data and evaluation constraints. The following section states
that gap directly.

## 2.9 Research Gap

Table 2.1 summarizes how selected adjacent studies differ from the design used
in this thesis.

**Table 2.1. How the present study differs from adjacent work**

| Work | Task | Retrieval | Feedback | Symbolic diagnosis | Isolated outcome scorer | Human evidence |
|---|---|---:|---|---:|---:|---:|
| Mixture-of-Personas [@b9] | Population-conditioned text generation | No | Persona conditioning | No | No | Study-specific evaluation |
| SimAB [@b10] | Persona-conditioned web A/B prediction | Context documents | Agent interaction | No | No | Historical outcomes and practitioner study |
| FUDGE [@b11] | Controlled text generation | No | Learned discriminator during decoding | No | No | Task metrics |
| Self-Refine [@b13] | Multi-task refinement | No | Same-model self-feedback | No | No | Task-dependent human and automatic evaluation |
| Reflexion [@b14] | Reasoning, coding, and decision tasks | Task-dependent | Verbal feedback or memory | Verbal or heuristic | No | Benchmark outcomes |
| HybridRAG-BN [@b19] | Bangla knowledge-base question answering | BM25 and BGE-M3 | Fine-tuned verifier and refiner | No | No | Competition token-F1 |
| SymDiag [@b20] | Multi-step reasoning | No | Symbolic diagnosis supports repair | Yes | No isolated A/B wall | Manually audited diagnosis |
| Saleh et al. [@b21] | Repository documentation | Repository retrieval | Reviewer-mediated rewriting | No | No | Manual structural analysis and automatic metrics |
| Present study | Bangla cinema-response generation | R1 level-specific exemplars | Verifier-A and bounded feedback | Deterministic diagnostic rules | Verifier-B outside the loop | Construct study and blinded output study |

*Note.* The table is selective rather than exhaustive and does not rank study
quality. A negative entry indicates only that the paper does not report that
component. Evaluation approaches differ across tasks and should not be
interpreted as equivalent instruments.

None of the selected studies combines R1-based retrieval, bounded revision with
Verifier-A, an isolated Verifier-B, deterministic diagnosis, and blinded
assessment for short Bangla cinema responses. The resulting gap is evaluative
rather than algorithmic: whether this combination works when data access,
computational cost, negative results, and possible proxy optimization are
recorded. This thesis tests that combination without presenting retrieval,
verification, symbolic diagnosis, or multi-agent roles as new inventions.

## 2.10 Chapter Summary

Prior work supplies the mechanisms used here, but also shows where they fail:
self-correction can be unreliable, retrieval can leak information, and repeated
optimization can exploit an evaluator. These risks motivate the data
boundaries, matched controls, and separate human and model-based evidence
developed in Chapter 3.
