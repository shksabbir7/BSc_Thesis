# Thesis structure and end-to-end process audit

**Audit date:** 2026-08-27
**Scope:** eight canonical chapter drafts and their audited source artifacts.

## Structural result

- Every chapter has exactly one level-1 chapter heading.
- Numbered sections are continuous inside Chapters 1--8.
- Level-3 headings are reserved for genuine internal subdivisions, including
  data sources, verifier configurations, pipeline components and the four RQ
  discussions under Section 7.2. Table captions are bold captions, not headings
  or TOC entries.
- All 28 main-text tables are present in their target chapters. Chapter 1 uses
  prose for its research questions, objectives and contributions; the two
  administrative mapping tables from the expanded draft are intentionally not
  part of the concise canonical introduction.
- Chapters 1--7 close with a chapter summary; Chapter 8 closes with the final
  conclusion.

## End-to-end process coverage

| Process stage | Where the method is explained | Where evidence/results appear | Standing |
|---|---|---|---|
| Research problem, construct and four RQs | Chapter 1 §§1.1--1.5 | RQs stated directly in §1.5 | Complete |
| Literature position and research gap | Chapter 2 §§2.1--2.9 | Table 2.1 | Complete; bibliography audit remains separate |
| Research design and data-role separation | Chapter 3 §§3.1--3.3 | frozen pipeline contracts | Complete; review/plot roles and Gold/R1/R2 privileges stated before analysis |
| Raw review audit and cleaning | Chapter 3 §3.4 | Table 3.1; `s0_data_xray`, `s1_cleaning_log` | Complete |
| Near-duplicate removal and frozen Gold/R1/R2 split | Chapter 3 §§3.4--3.5 | Tables 3.1--3.2; frozen split map | Complete; threshold and isolation rules stated |
| Plot harvesting, review, licensing and dev/eval freeze | Chapter 3 §3.3.2 | 120 plots, 30/90 split; harvest report/dataset card; Appendix D | Complete; 120/120 exact revisions attributed |
| Source-confound rejection and axis construction | Chapter 3 §§3.6--3.7 | Tables 3.3--3.5; Region-A/B S2 artifacts | Complete; negative clusterability retained |
| Human construct validation and operational levels | Chapter 3 §§3.8--3.10 | Tables 3.6--3.7; G-300 and intrusion reports | Complete; failed first instrument retained |
| Verifier candidates, circularity baseline and calibration | Chapter 4 §§4.2--4.7 | Tables 4.1--4.5; S3 artifacts | Complete; B calibration null retained |
| Verifier privilege/isolation wall | Chapter 4 §4.8 | Table 4.6 and executable guards | Complete |
| Retrieval, prompting, agents, gates and retry policy | Chapter 5 §§5.2--5.6 | Tables 5.1--5.6; S4 artifacts | Complete |
| Frozen main-run execution and provenance contract | Chapter 5 §5.7 | Case/score manifests and environment snapshot | Complete |
| Full 5,400-case results and registered inference | Chapter 6 §§6.1--6.5 | Tables 6.1--6.2; Figure 6.1 | Complete |
| Generated-output human evaluation | Chapter 6 §6.6 | Tables 6.3--6.4; human report | Complete |
| Length, diversity and corpus-distribution sensitivity | Chapter 6 §§6.7--6.9 | Tables 6.5--6.6; Figures 6.2--6.3 | Complete with stated limitations |
| Four RQ answers and claim boundaries | Chapters 6 §6.11, 7 §7.2 and 8 §8.3 | Table 8.1 | Complete |
| Validity, ethics and practical implications | Chapter 7 §§7.3--7.9 | Table 7.1 | Complete; no institutional approval/exemption claim is made |
| Contributions, future work and conclusion | Chapter 8 §§8.2--8.5 | Table 8.1 | Complete |

## Important non-completions that are not structural gaps

- The institutional ethics determination remains pending and must not be
  represented as approval.
- CC BY-SA attribution is complete in Appendix D; that appendix must remain in
  every distribution containing the plot derivative.
- All eleven manifested main-text figures are placed in Chapters 3--6. Final
  sizing, pagination and print-legibility checks remain template-stage work.
- Verified abstract, keywords, assembly order, reproducibility/ethics/
  responsible-NLP appendices and the generative-AI declaration are complete.
  University-template pagination, institutional fields, table widths,
  automatically generated lists and researcher-authored acknowledgements remain
  final-document assembly tasks.

No item in this audit authorizes rerunning the frozen 5,400 generations.
