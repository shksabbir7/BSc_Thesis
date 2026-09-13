# Citation apparatus — verification, and a withdrawn recommendation

**Date:** 2026-08-25. **Status:** finding. No tracked file was modified to produce
it; the checks below are read-only and reproducible.

---

## 1. The recommendation I made in Phase 1 is withdrawn

**Withdrawn: "migrate the bibliography keys from positional `b1`–`b143` to
semantic keys."** You approved it ("migrate now"). It should not be done, and I
should not have proposed it. Flagged rather than executed, per `CLAUDE.md`:
*"if it differs from what the proposal assumes, flag the conflict and stop."*

Four reasons, in descending order of how badly the migration would have gone.

**1.1 `docs/references_ieee.bib` is a generated file.** It is produced by
`src/common/build_thesis_bibliography.py` from `docs/references.bib` plus a
frozen `b1`–`b29` core. Hand-editing its keys puts it in the same category as
hand-editing `requirements.lock.txt`, which `CLAUDE.md` forbids by name — and the
edit would be silently reverted by the next rebuild. The script's own docstring
states the design: *"The curated b1--b29 entries are stable. Research-registry
entries are appended after metadata-based deduplication."*

**1.2 The migration I proposed is the reverse of one already completed.** It ran
on 2026-08-23 and is logged in `docs/lab_notebook.md` (*"Correction: full
literature-registry consolidation"*). It went **semantic → positional**, and the
old semantic keys were not discarded: `docs/reference_key_map_full.csv` preserves
them in a `legacy_key` column for **114 of 143** entries (`b4` ←
`hossain2026banglamoviereviews`, `b12` ← `sands2026`, and so on). I proposed
undoing a two-day-old audited migration whose audit trail was sitting in the file
I had already read.

**1.3 The convention is documented, not accidental.**
`docs/reference_key_map.md`: *"Source prose uses `b1`, `b2`, ... as stable BibTeX
keys. IEEE rendering converts these to numeric citations such as `[1]` and `[2]`;
the letter `b` is not printed."*

**1.4 The concrete defect I cited as justification is not a defect.** I reported
that arXiv 2503.04369 exists twice — as `b109` and as
`axiv2503_04369_literalism`, the latter with `author = {AUTHORS UNRESOLVED ...}`.
Both halves are wrong as stated:

- The two files have **different jobs**, so the paper appearing in both is by
  design, not duplication. `CLAUDE.md`'s Definition of Done step (c) requires new
  method references to go into `docs/related_work.md` *and*
  `docs/references.bib` — that pair is the working research registry. The
  lab notebook states the other half: *"The older `docs/references.bib` is a
  research registry, not a submission bibliography."*
- The unresolved author list **is already repaired at build time**.
  `build_thesis_bibliography.py` line 40 carries
  `AUTHOR_FIXES["2503.04369"]` with the full eight-author list, and the generated
  `b109` entry reads `author = {Yafu Li and Ronghao Zhang and Zhilin Wang and
  Huajian Zhang and Leyang Cui and Yongjing Yin and Tong Xiao and Yue Zhang}`.
  The `AUTHORS UNRESOLVED` string exists only in the registry, which is the file
  that is *allowed* to hold discovery-state metadata.

This is the sixth item in this review that I reported as broken or missing and
that the repository had already handled. The pattern is recorded in memory; it is
noted here too, because this one came with an approval attached and would have
damaged a tracked artifact.

---

## 2. What the citation apparatus actually looks like

Reproducible check, run 2026-08-25 against `docs/chapters/*.md`,
`docs/appendices/*.md`, `docs/references_ieee.bib` and
`docs/reference_key_map_full.csv`:

```python
import re, csv, glob
cited = set()
for f in glob.glob('docs/chapters/*.md') + glob.glob('docs/appendices/*.md'):
    cited |= set(re.findall(r'@(b\d+)\b', open(f, encoding='utf-8').read()))
bib = set(re.findall(r'^@[A-Za-z]+\{(b\d+),',
                     open('docs/references_ieee.bib', encoding='utf-8').read(), re.M))
rows = list(csv.DictReader(open('docs/reference_key_map_full.csv', encoding='utf-8')))
flagged = {r['b_key'] for r in rows if r['reading_status'] == 'chapter_cited'}
```

| Check | Result |
|---|---|
| Unique keys cited by the 7 chapters and 8 appendices | **55** |
| Entries in `docs/references_ieee.bib` | **143** |
| Rows in `docs/reference_key_map_full.csv` | **143** |
| CSV rows flagged `chapter_cited` | **55** |
| Cited but absent from the bibliography (broken citations) | **none** |
| Cited but not flagged in the CSV | **none** |
| Flagged in the CSV but not actually cited | **none** |
| In the bibliography, never cited | **88** |

The three sets agree exactly, not merely in count. There are **zero broken
citations** in the thesis.

> **Recount 2026-08-25, after the Chapter 1 and Chapter 2 rewrites.** Unique keys
> cited rose 55 → **60** and never-cited entries fell 88 → **83**; the
> bibliography and CSV are unchanged at 143, and broken citations remain at
> **zero**. The 55 above was correct when written — re-running the snippet against
> `git show HEAD:` for all seventeen assembled documents reproduces it exactly.
> One row of the table no longer holds: the CSV's `chapter_cited` column is still
> 55, because `b58`, `b98`, `b99`, `b110` and `b111` were cited without the flags
> being refreshed, so *"cited but not flagged"* is now five rather than none. The
> refresh is blocked on a decision recorded in `docs/thesis_phase3_log.md`:
> `src/common/order_thesis_bibliography.py` restores the column, but it also
> renumbers every key in every chapter.
>
> **A hazard worth naming for Phase 6, since it did not bite here but nearly
> did.** Any citation count must use `@(b\d+)\b`, as the snippet above does, and
> never a bracket-anchored `\[@(b\d+)`. The latter silently drops continuation keys
> in multi-key citations such as `[@b5; @b6]` — on the current corpus it
> undercounts by four (`b28`, `b42`, `b47`, `b72`) and on the HEAD corpus by three.
> A count that is wrong in this particular way looks plausible, because it is
> wrong by a small margin and always downward.

### 2.1 The 88 uncited entries are not an error

You wrote that many references may exist in the `.bib` files without being cited.
That is true — 88 of 143 — and it is harmless. Under pandoc with an IEEE CSL, or
under `IEEEtran` with BibTeX, an entry that is never cited is never rendered. The
bibliography that reaches the page will contain 55 entries unless a `nocite`
directive is added, and none exists. The 88 are the research registry's reach,
carried in the same file for auditability.

⚠️ One consequence to keep in view for Phase 6: because uncited entries are
invisible in the output, a *wrong* key in prose fails loudly (missing citation)
but a *missing* citation fails silently — the sentence simply carries no
reference. Phase 6 therefore has to read for uncited claims, which the mechanical
check above cannot detect.

### 2.2 Four semantic keys appear in prose — and they are fine

`@papageorgiou2025agenticfaithfulness`, `@rahman2025hallucination`,
`@ramprasad2024factualitymetrics`, `@zhu2024rageval` occur in
`docs/related_work.md` and resolve against `docs/references.bib`, not against the
IEEE file. `docs/related_work.md` is **not** in `docs/thesis_assembly_order.md`;
it is the working method-reference ledger that the Definition of Done maintains.
No thesis chapter or appendix contains a non-`bN` citation key.

---

## 3. The one real defect found

**`docs/reference_key_map.md` states the wrong record count.** It says **141** in
four places, and `b1`--`b141`, where the true figure is **143** in both the
generated bibliography and the CSV map. The file already carries a
`> **SUPERSEDED SNAPSHOT**` banner directing readers to the CSV, so nothing
downstream depends on it — but a stale count inside a file that also *documents*
the key convention is worth two minutes.

Its readable table is stale in a second way, and more sharply: it lists
`b14` = BanglaBERT and `b15` = LaBSE, while the CSV (the stated authority) has
`b2` = BanglaBERT and `b3` = LaBSE. The consolidation renumbered, and the
snapshot table was not regenerated. The banner covers this honestly. Two options:

- **(a)** Fix the four counts, leave the table under its banner. Cheap, keeps the
  historical 29-record view intact as an audit trail.
- **(b)** Replace the table with a generated view from the CSV. Removes the
  stale-key hazard entirely at the cost of the historical snapshot.

**Recommendation: (a).** The banner is doing its job, and the 29-record snapshot
is the only readable record of what the bibliography looked like before
consolidation. Deleting an audit trail to remove an inconsistency that is already
labelled is a poor trade.

Neither option is applied here. This is a finding, not an edit.

> **Resolved 2026-08-25.** Option (a) was applied during the Chapter 2 rewrite,
> batched into Phase 3 as item 4.1 below prescribes. Five stale strings were
> corrected — the banner's cited-source count, three `141`/`b141` references and
> one `112`. The historical table stays under its banner. The change table is in
> `docs/thesis_phase3_log.md` under *Repository housekeeping completed alongside
> this chapter*, which also records a related defect this finding did not reach:
> `docs/STATUS.md` states the bibliography size three times, as 141 (row 29),
> 142 (row 37) and 143 (row 49). Only row 49 is current.

---

## 4. What remains genuinely owed on citations

1. ~~**Fix the 141 → 143 counts** in `docs/reference_key_map.md` (option (a)
   above), batched into the Phase 3 commit rather than committed alone.~~
   **Done 2026-08-25**, batched as intended. Superseded by a new item: decide
   whether the `chapter_cited` column is refreshed by hand or by re-running
   `src/common/order_thesis_bibliography.py`, and if the latter, run it once after
   Chapter 8 rather than once per chapter.
2. **Phase 6 proper**, which this document does not attempt: whether each cited
   source actually supports the sentence citing it. The mechanical apparatus is
   clean; that says nothing about whether `[@b20]` is the right paper for the
   claim beside it. That check requires reading, and for the ~40 entries marked
   `metadata_verified_not_full_read` in the CSV it requires reading the papers —
   which is also why `docs/references.bib` may be drawn on only after the paper
   has actually been reviewed, per your own instruction.
3. **Consensus quota returns 1 September 2026.** Literature completeness is not
   represented as closed until then; the lab notebook already says so.
