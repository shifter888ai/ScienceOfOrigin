# Science of Origin — Trilingual Terminology Inventory

**Status:** Expanded source-extraction edition · Version 0.6  
**Languages:** English · 繁體中文 · 日本語  
**Purpose:** Preserve terminology found in original Science of Origin materials, with source traceability and provisional cross-language mappings. This is an internal research inventory, not the published website terminology page.

## 1. Editorial and source rules

1. Preserve the exact original-language form and wording wherever the source is accessible.
2. English and Japanese equivalents in this inventory are editorial translations unless the source itself supplies them.
3. A translation is not proof that two expressions are conceptually identical. Mark uncertain mappings as provisional.
4. Keep historical formulations, later formulations, and current editorial preferences distinguishable.
5. Distinguish a term occurrence, a source explanation, a formula/relation, a title/announcement, and an editorial interpretation.
6. Do not treat keyword counts as definition counts.
7. Preserve source dates, record numbers, page numbers, author roles, and source versions.
8. Do not silently reconcile conflicting source formulations.
9. The internal inventory is trilingual. The published `terminology.html` and `glossary.html` remain English-only unless the project owner later approves a change.
10. This file records successive verified extraction tranches, not the complete terminology of all original materials.

## 2. Language and status labels

- **SRC** — wording directly present in an inspected source.
- **TR-EN / TR-JA** — editorial translation into English / Japanese.
- **REL** — source-stated relationship or formula; not necessarily a dictionary definition.
- **TITLE** — title or announcement only; referenced article/video not present in the inspected record.
- **OPEN** — mapping, meaning, or provenance requires further review.
- **PROVISIONAL** — useful working translation, not yet approved as a canonical equivalent.

## 3. Source register used in this tranche

| Source ID | Source object | What was inspected |
|---|---|---|
| SRC-WB-001 | `materials/weibo-1760432301-combined-originals-2026-11-24T06-35-03-529Z.txt` | Exported original posts, UID 1760432301; selected records 037, 045, 047, 106, 129, 156, 212, 230, 384, 569, 580, 643, 667, 689, 746, 752, 755, 757–759 |
| SRC-WB-IDX-001 | `library/record-index/weibo-originals-record-index.csv` | Record numbers, timestamps, line ranges and extracted post text |
| SRC-WB-AUD-001 | `library/record-index/weibo-origin-context-audit.md` | Manual context classifications for the 45 records containing 本源 |
| SRC-CC-IDX-001 | `library/record-index/chinese-compilation-terminology-candidate-index.csv` | Candidate terms and page/line locators used for discovery; not a substitute for direct passage review |
| SRC-CC-001 | `materials/元吾氏集录20210203.txt` | Original Chinese compilation TXT; directly inspected Pages 264, 300, 306–316, 399 and 1669 in this tranche; Git blob `051b2a12490cacf3dc96e24cb99858ececa6bff0` |
| SRC-RD-001 | `materials/reddit-english-all.txt` | English Reddit archive; directly inspected lines 6432–6483 for Level of Awareness, Lucidity, Strength and Spectrum terminology; Git blob `0452d11a39654864572c0d563667765b5c96da3c` |
| SRC-OR-001 | Current Science of Origin framework pages in the repository | Directly inspected origin.html, zero-origin.html, zero-idle-state-of-origin.html, nature-of-origin.html, infinity-of-imagination.html, imagination.html, origination.html, manifestations.html, origin-models.html, fake-origin-divided-origin.html and oneness-division.html on 2026-11-25 |
| SRC-SOC-001 | `Science-of-Consciousness.txt` (project-supplied file) | Project Description & Research Framework |
| SRC-SOC-002 | `Science-of-Consciousness-—-Research-Architecture.txt` (project-supplied file) | Short research architecture outline |
| SRC-SOC-003 | `materials/awakenology/Science.md` | Current author-framed internal Science of Consciousness framework; directly inspected Sections 1–7, including field/application relationships, Freedomality terminology and Exincarnation terminology |
| SRC-SOC-004 | `TERMINOLOGY-INVENTORY.md` (legacy repository-wide inventory) | Directly reviewed the Freedomality candidate table and its historical note identifying Level of Actualization of Freewill as a previously adopted replacement term for “Freedom of Consciousness”; this is a secondary project record, not the primary defining source |
| SRC-SOC-005 | `library/TERMINOLOGY-CONCEPTUAL-REVIEW-2.md` | Directly reviewed the application terminology review and its explicit statement that the supplied framework documents do not define Level of Actualization of Freewill, Freedomality Index or Freedometry |
| SRC-AW-TERM-001 | `materials/awakenology/Awakenology-Glossary/Terminology.md` | Internal glossary review draft; inspected application and Freedomality rows; treated as a working terminology source, not a final public glossary |
| SRC-ENT-001 | `entropy-of-consciousness.html` | Public research introduction; directly inspected nine-zone architecture, research approach, laboratory/practical distinction and Entropy Particle usage |
| SRC-ENT-IDX-001 | `library/record-index/entropy-rr-assessment-points-index.md` | Derivative structural index of the Entropy assessment source; now links to the RTF text-run transcription, corrected point-level register and layout-verification memo; remains a navigation aid, not a substitute for the original source |
| SRC-ENT-002 | `materials/熵值检测点RR部分.rtf` | Directly retrieved and inspected RTF v1.1 on 2026-11-26; overview, complete TOC (114 top-level headings across nine areas), 2,151 appendix text runs, 224 body headings and 375 assessment blocks extracted; Git blob `4554f3c8fbdf64a76f4fbbfc4a51dac10de05657`; DOCX counterpart not directly inspected |
| SRC-ENT-003 | `library/entropy-assessment-body-transcription-v1.1.md` | Derivative line-numbered transcription of 2,151 visible RTF text runs; all lines independently matched in source order; not a reconstruction of Word paragraphs or visual layout |
| SRC-ENT-004 | `library/entropy-assessment-point-register-v1.1.md` | Derivative first-pass register of 224 body headings and 375 `RR` / `88` / `JJ` blocks; 123 point headings have complete triplets; six blocks are retained as two contextual aggregates; no scoring interpretation or validation |
| SRC-ENT-005 | `library/entropy-assessment-layout-verification-v1.1.md` | RTF text-run and TOC page-locator verification; 113 matched body/TOC headings have matching printed page locators; one TOC/body title difference preserved; DOCX and rendered page images remain uninspected |
| SRC-AW-PAGE-001 | `materials/awakenology/What-Is-Awakenology/index.html`; `materials/awakenology/What-is-SoC-Strength-of-Consciousness/index.html` | Snapshot pages inspected for Awakenology and Strength of Consciousness context; claims remain attributed to the source framework |

**Access and version note:** The Chinese compilation TXT is the canonical source for current research under the completed-library scope. The two PDF volumes are retained as supplemental references; optional OCR/image review is not a completion blocker. The Chinese compilation passages cited in Version 0.2 were read directly from the TXT. For later tranches, each additional source is identified separately in the register; derivative indexes remain discovery aids, not substitutes for original-source review.

## 4. Extracted terminology records

### T-001 — Origin / 本源 / 本源

- **English display term:** Origin
- **繁體中文原詞:** 本源
- **日本語（暫定訳）:** 本源（ほんげん）／根源
- **Source wording (SRC):** Record 106 (2013-11-16): 「本源=一个无限的思想。万物=思想的无限内容。本源之道=一个无限的思想及其无限的內容。」
- **English translation (TR-EN):** “Origin = an infinite thought. All Things = the infinite content of thought. The Way of Origin = an infinite thought and its infinite content.”
- **Japanese translation (TR-JA):** 「本源＝無限の思想。万物＝思想の無限の内容。本源の道＝無限の思想とその無限の内容。」
- **Other source formulations:** Record 569 (2022-04-02) states 「本源=每一个存在的本质。」 (“Origin = the essence of each existence.”) and also states 「万物本源=万物本质=万物整体。」
- **Context / classification:** Direct source formulations in distinct posts and years. Record 384 (2021-05-23) presents an expansive exposition in which opposites and their unity are all described as 本源.
- **Do not collapse:** The 2013 “infinite thought” formulation and the 2022 “essence of each existence” formulation are separate historical formulations. Preserve both.
- **Source:** SRC-WB-001, records 106, 384, 569.
- **Review status:** Extracted; cross-source comparison pending.

### T-002 — All Things / 万物 / 万物

- **English display term:** All Things
- **繁體中文原詞:** 万物（繁體字形：萬物）
- **日本語（暫定訳）:** 万物
- **Source wording (SRC):** Record 106 (2013-11-16): 「万物=思想的无限内容。」
- **English translation (TR-EN):** “All Things = the infinite content of thought.”
- **Japanese translation (TR-JA):** 「万物＝思想の無限の内容。」
- **Related formulation:** Record 569 (2022-04-02): 「万物本源=万物本质=万物整体。」
- **Context:** In record 106, 万物 is related to the content of thought; in record 569, 万物本源 is related to the essence and totality of all things.
- **Source:** SRC-WB-001, records 106 and 569.
- **Review status:** Extracted; scope and capitalization convention pending.

### T-003 — Way of Origin / 本源之道 / 本源の道

- **English display term:** Way of Origin
- **繁體中文原詞:** 本源之道
- **日本語（暫定訳）:** 本源の道
- **Source wording (SRC):** Record 106 (2013-11-16): 「本源之道=一个无限的思想及其无限的內容。」
- **English translation (TR-EN):** “The Way of Origin = an infinite thought and its infinite content.”
- **Japanese translation (TR-JA):** 「本源の道＝無限の思想とその無限の内容。」
- **Context:** This is a source-stated formula in record 106. Other occurrences in the Chinese compilation candidate index include titles and section references; those contexts need direct review before being treated as equivalent definitions.
- **Source:** SRC-WB-001, record 106; SRC-CC-IDX-001, candidate pages 3, 8–10, 484, 654, 1292, 1317–1318 (locators only).
- **Review status:** Extracted from Weibo; compilation context pending.

### T-004 — All-Things Origin / 万物本源 / 万物の本源

- **English display term:** All-Things Origin (provisional)
- **繁體中文原詞:** 万物本源（繁體字形：萬物本源）
- **日本語（暫定訳）:** 万物の本源
- **Source wording (SRC):** Record 156 (2017-07-06): 「万物本源=个体本源+个体本源+个体本源+......」; record 212 (2018-02-21): 「万物本源=万物本质。」
- **English translation (TR-EN):** Record 156: “All-Things Origin = Individual Origin + Individual Origin + Individual Origin + …”; record 212: “All-Things Origin = the essence of all things.”
- **Japanese translation (TR-JA):** 「万物の本源＝個体の本源＋個体の本源＋個体の本源＋……」; 「万物の本源＝万物の本質。」
- **Context / classification:** Two source-stated relations, not one consolidated definition. Record 569 later adds 「万物本源=万物本质=万物整体。」
- **Source:** SRC-WB-001, records 156, 212 and 569.
- **Review status:** Extracted; relation across dates requires conceptual review.

### T-005 — Individual Origin / 个体本源 / 個体の本源

- **English display term:** Individual Origin (provisional)
- **繁體中文原詞:** 个体本源（繁體字形：個體本源）
- **日本語（暫定訳）:** 個体の本源
- **Source wording (SRC):** Record 156 (2017-07-06) includes the repeated term in the relation 「万物本源=个体本源+个体本源+个体本源+......」
- **English translation (TR-EN):** “Individual Origin.”
- **Japanese translation (TR-JA):** 「個体の本源」
- **Context:** The record gives a compositional or additive analogy/formula. It does not independently define the nature or boundaries of an “individual.”
- **Source:** SRC-WB-001, record 156.
- **Review status:** Extracted as a term in a relation; definition OPEN.

### T-006 — Union with Origin / 合一本源 / 本源との合一

- **English display term:** Union with Origin (provisional)
- **繁體中文原詞:** 合一本源
- **日本語（暫定訳）:** 本源との合一
- **Source wording (SRC):** Record 129 (2015-01-11): 「得道=合一本源＋脱离轮回。」
- **English translation (TR-EN):** “Attaining the Way = union with Origin + exiting the reincarnation cycle.”
- **Japanese translation (TR-JA):** 「道を得ること＝本源との合一＋輪廻からの離脱。」
- **Context / classification:** A source-stated relation involving 合一本源; it is not a definition of 本源 itself. Record 580 (2022-05-01) gives the prompt 「如何合一本源：“我是本源”」, but the accompanying video content is not present in the text export.
- **Source:** SRC-WB-001, records 129 and 580; SRC-CC-IDX-001, candidate pages 81, 264, 298, 300, 304, 399 and others (locators only).
- **Review status:** Extracted; operational meaning and Japanese wording provisional.

### T-007 — Consciousness / 意识 / 意識

- **English display term:** Consciousness
- **繁體中文原詞:** 意识（繁體字形：意識）
- **日本語（暫定訳）:** 意識
- **Source evidence in this tranche:** Record 569 uses 「有多大意识，就有多大出息」 and 「意识强度提升点，就是去除肉身与灵魂之间的粘连点。」
- **English translation (TR-EN):** “The greater the consciousness, the greater the prospects”; “A point for increasing consciousness strength is to remove the points of adhesion between the physical body and the soul.”
- **Japanese translation (TR-JA):** 「意識が大きいほど、可能性も大きい。」; 「意識強度を高める一つのポイントは、肉体と魂の間の結合点を取り除くことである。」
- **Important limitation:** These are contextual uses, not a complete definition of 意识. The project framework documents define Science of Consciousness as a research field but do not, in the supplied passages, provide a complete operational definition of Consciousness.
- **Source:** SRC-WB-001, record 569; SRC-SOC-001 and SRC-SOC-002.
- **Review status:** Context extracted; definition OPEN.

### T-008 — Free Consciousness / 自由意识 / 自由意識

- **English display term:** Free Consciousness (literal translation; project mapping requires review)
- **繁體中文原詞:** 自由意识（繁體字形：自由意識）
- **日本語（暫定訳）:** 自由意識
- **Source wording (SRC):** Record 230 (2018-04-12): 「自由意识是唯一的真实存在……自由意识=万物本源。」 Record 689 (2024-10-26): 「自然規律只有一個：自由意識（自由意志Freewill）。」
- **English translation (TR-EN):** “Free Consciousness is the only real existence … Free Consciousness = All-Things Origin.” Record 689 explicitly places “Freewill” in parentheses after 自由意识.
- **Japanese translation (TR-JA):** 「自由意識は唯一の実在である……自由意識＝万物の本源。」; record 689 explicitly pairs 自由意識 with “Freewill.”
- **Distinction:** Preserve 自由意识 and 自由意志 as separate source forms. Record 689 provides an explicit parenthetical pairing in that post; this does not authorize flattening every occurrence across the archive into a universal synonym.
- **Source:** SRC-WB-001, records 230 and 689; SRC-WB-AUD-001.
- **Review status:** Extracted; cross-source mapping OPEN.

### T-009 — Law of Freewill / 自由意志法则 / 自由意志の法則

- **English display term:** Law of Freewill (source translation / working form)
- **繁體中文原詞:** 自由意志法则（繁體字形：自由意志法則）
- **日本語（暫定訳）:** 自由意志の法則
- **Source wording (SRC):** Record 230 (2018-04-12): 「自由意志法则是唯一的真实法则。」
- **English translation (TR-EN):** “The Law of Freewill is the only real law.”
- **Japanese translation (TR-JA):** 「自由意志の法則は唯一の実在する法則である。」
- **Context:** In the same post, 自由意识 is described as the only real existence, while 自由意志法则 is described as the only real law. The source distinguishes the existence term from the law term.
- **Source:** SRC-WB-001, record 230; SRC-WB-AUD-001.
- **Review status:** Extracted; terminology relation to Freewill research field pending.

### T-010 — Strength of Consciousness / 意识强度 / 意識強度

- **English display term:** Strength of Consciousness
- **繁體中文原詞:** 意识强度（繁體字形：意識強度）
- **日本語（暫定訳）:** 意識の強度
- **Weibo source wording (SRC):** Record 569 (2022-04-02) includes 「意识强度提升点，就是去除肉身与灵魂之间的粘连点。」
- **Chinese compilation source context (SRC):** Pages 306–316 (2018–2019, third edition) describe Consciousness Strength assessment points, two functional areas in the inspected passage, paired positive/negative values, and a described testing instrument. Page 399 states that the Consciousness Strength level is a composite value of all assessment points. Page 1669 (2020-10-11) states 「合一本源的比例=意识强度检测值」 and qualifies the relation between a level of 9, a 90% union proportion and level 18 with 「貌似」 and 「理论来说」.
- **English rendering (TR-EN):** The 2022 Weibo sentence is rendered as “A point for increasing Strength of Consciousness is to remove the points of adhesion between the physical body and the soul.” The compilation passages are summarized rather than translated as a single definition.
- **Japanese translation (TR-JA):** 「意識強度」 (working form; operational terminology pending).
- **Context / limitation:** The source describes several distinct layers: assessment points, a testing procedure/instrument, a composite level, and interpretations relating that level to union with Origin and liberation from reincarnation. The inspected passages do not establish that every historical scale, point collection, or numerical model is one unchanged system. Source-reported percentages and levels remain attributed historical claims, not independently validated measurements.
- **Source:** SRC-WB-001, record 569; SRC-CC-001, Pages 306–316, 399 and 1669; SRC-CC-IDX-001, candidate term 意识强度 (144 pages, lexical discovery only).
- **Review status:** Expanded source context; operational definition, scale-version mapping and independent validation OPEN.

### T-011 — Frequency / 频率 / 周波数

- **English display term:** Frequency
- **繁體中文原詞:** 频率（繁體字形：頻率）
- **日本語（暫定訳）:** 周波数
- **Source evidence:** The Chinese compilation candidate index identifies 频率 on 174 pages. The supplied Science of Consciousness framework uses “frequencies” as a defining element of Spectrum / Spectra and the Spectrum of Consciousness / Spectrum of Things.
- **Source wording (SRC):** SRC-SOC-001: Spectrum is intended to represent the entirety of frequencies within the relevant research domain; Spectra refers to multiple spectra or spectral representations.
- **Japanese translation (TR-JA):** 「周波数」
- **Important limitation:** The large Chinese compilation passages were not directly readable in this pass. No claim is made that every occurrence of 频率 in that compilation uses the same technical meaning.
- **Source:** SRC-SOC-001; SRC-CC-IDX-001, candidate term 频率 (174 pages).
- **Review status:** Framework wording extracted; original Chinese passage-level review pending.

### T-012 — Spectrum / 光谱 / スペクトル

- **English display term:** Spectrum
- **繁體中文 candidate form:** 光谱（繁體字形：光譜） — candidate only, not yet established as the canonical translation
- **日本語（暫定訳）:** スペクトル
- **Source wording (SRC):** SRC-SOC-001: “Spectrum is intended to represent the entirety of frequencies within the relevant research domain, rather than merely a limited selection or range.”
- **Japanese translation (TR-JA):** 「Spectrum は、関連する研究領域における周波数の全体を表すことを意図している。」
- **Distinction:** The Chinese compilation candidate index finds 光谱 only on pages 434 and 439, in passages whose excerpts concern aura-related content. This does not establish 光谱 as the Chinese equivalent of the project’s technical term Spectrum.
- **Source:** SRC-SOC-001; SRC-CC-IDX-001, 光谱 pages 434 and 439.
- **Review status:** English source term extracted; Chinese mapping OPEN.

### T-013 — Spectra / 光谱（复数概念待核） / スペクトラ

- **English display term:** Spectra
- **繁體中文:** 暫定譯法待確認
- **日本語（暫定訳）:** スペクトラ
- **Source wording (SRC):** SRC-SOC-001: “Spectra refers to multiple spectra or spectral representations used in comparative and related investigations.”
- **Context:** The source distinguishes singular Spectrum from plural Spectra. Do not merge them in translation or technical writing.
- **Source:** SRC-SOC-001.
- **Review status:** English definition extracted; Chinese and Japanese technical conventions pending.

### T-014 — Science of Consciousness / 意识科学（暫定） / 意識の科学（暫定）

- **English display term:** Science of Consciousness
- **繁體中文（暫定訳）:** 意識科學
- **日本語（暫定訳）:** 意識の科学
- **Source wording (SRC):** SRC-SOC-001 describes the project as investigating the fundamental nature of Life and Things through the scientific study of Consciousness, Freewill and Spectrum.
- **Architecture note:** SRC-SOC-001 lists four core research fields: Science of Consciousness, Science of Freewill, Spectrum of Consciousness, Spectrum of Things. SRC-SOC-002 lists only Science of Consciousness and Science of Freewill as research fields, with Spectrum / Spectra under Core Research Methodology. Preserve this document-level difference.
- **Source:** SRC-SOC-001 and SRC-SOC-002.
- **Review status:** Extracted; architecture discrepancy retained OPEN.

### T-015 — Science of Freewill / 自由意志科学（暫定） / 自由意志の科学（暫定）

- **English display term:** Science of Freewill
- **繁體中文（暫定訳）:** 自由意志科學
- **日本語（暫定訳）:** 自由意志の科学
- **Source wording (SRC):** SRC-SOC-001 describes it as research into the fundamental nature, properties and mechanisms of Freewill.
- **Architecture note:** It appears as a core research field in both supplied framework documents.
- **Source:** SRC-SOC-001 and SRC-SOC-002.
- **Review status:** Extracted; operational definition of Freewill remains separate work.

### T-016 — Nature of Life / 生命的本質（暫定） / 生命の本質（暫定）

- **English display term:** Nature of Life
- **繁體中文（暫定訳）:** 生命的本質
- **日本語（暫定訳）:** 生命の本質
- **Source wording (SRC):** Both supplied framework documents list Nature of Life as a research-scope domain.
- **Source:** SRC-SOC-001 and SRC-SOC-002.
- **Review status:** Framework term extracted; source-language equivalents provisional.

### T-017 — Nature of Things / 事物的本質（暫定） / 物事の本質（暫定）

- **English display term:** Nature of Things
- **繁體中文（暫定訳）:** 事物的本質
- **日本語（暫定訳）:** 物事の本質
- **Source wording (SRC):** Both supplied framework documents list Nature of Things as a research-scope domain.
- **Source:** SRC-SOC-001 and SRC-SOC-002.
- **Review status:** Framework term extracted; source-language equivalents provisional.




### T-018 — Attaining the Way / 得道 / 道を得ること

- **English display term:** Attaining the Way (editorial rendering)
- **繁體中文原詞:** 得道
- **日本語（暫定訳）:** 道を得ること
- **Source wording (SRC):** Chinese compilation Page 264 states 「亲眼见到的是合道（合一本源），亲身认证的是得道/证道（脱离轮回）」 and concludes 「得道=合一本源+脱离轮回。」
- **English rendering (TR-EN):** “What is seen directly is union with the Way (union with Origin); what is personally verified is attaining / realizing the Way (exiting the reincarnation cycle).” The source then states: “Attaining the Way = union with Origin + exiting the reincarnation cycle.”
- **Context / distinction:** The passage separates 合一本源 from 脱离轮回 and treats them as distinct components of 得道. Do not use “Attaining the Way” as a synonym for either component alone.
- **Source:** SRC-CC-001, Page 264, lines 7431–7463.
- **Review status:** Direct passage extracted; English and Japanese renderings provisional.

### T-019 — Exincarnation / 脱离轮回 / 輪廻からの離脱

- **English display term:** Exincarnation (current project term)
- **繁體中文原詞:** 脱离轮回（繁體字形：脫離輪迴）
- **日本語（暫定訳）:** 輪廻からの離脱
- **Source wording (SRC):** Page 264 uses 「脱离轮回」 as a distinct component of 得道 and describes it as returning from the “physical body” to true life, the true self and true freedom. The supplied Science of Consciousness Project Description names “Exincarnation (脱離輪迴)” and Exincarnology as an application field.
- **English mapping:** “Exincarnation” is the current project terminology supplied in the framework document; it is not a literal English word appearing in the Chinese source passage.
- **Context / distinction:** Preserve the source phrase 脱离轮回 and the current English term Exincarnation as a mapped pair with provenance. Page 264 distinguishes it from 合一本源; it is not a synonym for Union with Origin.
- **Source:** SRC-CC-001, Page 264, lines 7431–7463; SRC-SOC-001.
- **Review status:** Project mapping recorded; scope and operational definition OPEN.

### T-020 — Hypnotic Reincarnation / 催眠轮回 / 催眠輪廻

- **English display term:** Hypnotic Reincarnation
- **繁體中文原詞:** 催眠轮回（繁體字形：催眠輪迴）
- **日本語（暫定訳）:** 催眠輪廻
- **Source wording (SRC):** Chinese compilation Page 399 describes 「真正觉醒=脱离催眠轮回」.
- **English rendering (TR-EN):** “True awakening = exiting hypnotic reincarnation.”
- **Context:** This is a source-stated relationship in the assessment-point framework. It is not a complete definition of 催眠轮回 or an independently verified account of reincarnation.
- **Source:** SRC-CC-001, Page 399, lines 11136–11155.
- **Review status:** Direct passage extracted; definition OPEN.

### T-021 — Strength of Consciousness Assessment Point / 意识强度检测点 / 意識強度の検査ポイント

- **English display term:** Strength of Consciousness Assessment Point (editorial rendering)
- **繁體中文原詞:** 意识强度检测点（繁體字形：意識強度檢測點）
- **日本語（暫定訳）:** 意識強度の検査ポイント
- **Source wording (SRC):** Page 306 says 「意识强度检测点（=“意识强度练习点”）」 and describes hundreds of major points and tens of thousands of minor points.
- **English rendering (TR-EN):** “Strength of Consciousness assessment point”; the source also equates it parenthetically with a Strength of Consciousness practice point.
- **Context:** The source describes these as items organized by functional areas and used in a testing framework. Counts are source-reported historical claims and should retain their edition/date context.
- **Source:** SRC-CC-001, Pages 306–316, lines 8841–9082.
- **Review status:** Direct passage extracted; complete catalogue and version mapping OPEN.

### T-022 — Strength of Consciousness Practice Point / 意识强度练习点 / 意識強度の実践ポイント

- **English display term:** Strength of Consciousness Practice Point (editorial rendering)
- **繁體中文原詞:** 意识强度练习点（繁體字形：意識強度練習點）
- **日本語（暫定訳）:** 意識強度の実践ポイント
- **Source wording (SRC):** Page 306 explicitly equates 「意识强度检测点」 with 「意识强度练习点」 in that document.
- **English rendering (TR-EN):** “Strength of Consciousness practice point.”
- **Context:** Preserve the source's explicit parenthetical equivalence in this edition. It does not establish that assessment and practice are identical in every later or earlier source context.
- **Source:** SRC-CC-001, Page 306, lines 8841–8860.
- **Review status:** Direct passage extracted; broader usage comparison OPEN.

### T-023 — Mental Control / 心智控制 / 心智制御

- **English display term:** Mental Control (editorial rendering)
- **繁體中文原詞:** 心智控制
- **日本語（暫定訳）:** 心智制御
- **Source wording (SRC):** Page 306 labels the first functional area 「中央区：心智控制区」 and states 「心智控制=机器人心智控制程序模式（AI机器程序）。」
- **English rendering (TR-EN):** “Mental Control = robot-like mental-control program mode (AI machine program).”
- **Context:** This is a source-specific model description, not a general psychological definition of mental control.
- **Source:** SRC-CC-001, Page 306, lines 8841–8880.
- **Review status:** Direct passage extracted; cross-source meaning OPEN.

### T-024 — Mental Control Area / 心智控制区 / 心智制御エリア

- **English display term:** Mental Control Area (editorial rendering)
- **繁體中文原詞:** 心智控制区（繁體字形：心智控制區）
- **日本語（暫定訳）:** 心智制御エリア
- **Source wording (SRC):** Page 306 names 「中央区：心智控制区」 as the first functional area in the described assessment-point framework.
- **English rendering (TR-EN):** “Central Area: Mental Control Area.”
- **Context:** The source places this area within a functional grouping of Consciousness Strength assessment points. Do not treat the label as a general anatomical brain region.
- **Source:** SRC-CC-001, Pages 306–313, lines 8841–8980.
- **Review status:** Direct passage extracted; full architecture review OPEN.

### T-025 — Autonomous Consciousness Area / 自主意识区 / 自主意識エリア

- **English display term:** Autonomous Consciousness Area (editorial rendering)
- **繁體中文原詞:** 自主意识区（繁體字形：自主意識區）
- **日本語（暫定訳）:** 自主意識エリア
- **Source wording (SRC):** Page 314 names 「上方区：自主意识区」 as the second functional area and introduces measures including energy-use rate, composite cooperation, flexible switching, calm handling, resilience, disengagement from addiction, empathy, stillness in solitude and self-release.
- **English rendering (TR-EN):** “Upper Area: Autonomous Consciousness Area.”
- **Context:** This is the source's functional-area label and set of assessment subjects, not a general standardized construct.
- **Source:** SRC-CC-001, Pages 314–316, lines 9010–9082.
- **Review status:** Direct passage extracted; full architecture review OPEN.

### T-026 — Resistance Ratio / 抗性比率 / 抵抗比率

- **English display term:** Resistance Ratio (editorial rendering)
- **繁體中文原詞:** 抗性比率
- **日本語（暫定訳）:** 抵抗比率
- **Source wording (SRC):** Page 306 states that values in the Mental Control Area belong to 「抗性比率」 and are displayed as paired positive and negative percentages.
- **English rendering (TR-EN):** “Resistance ratio.”
- **Context:** Preserve as the source's label for the paired-value structure; do not replace it with a conventional technical term without source support.
- **Source:** SRC-CC-001, Pages 306–307, lines 8841–8910.
- **Review status:** Direct passage extracted; operational interpretation OPEN.

### T-027 — Positive Value / 正值 / 正値

- **English display term:** Positive Value (editorial rendering)
- **繁體中文原詞:** 正值
- **日本語（暫定訳）:** 正値
- **Source wording (SRC):** Page 307 states 「正值=100%-反值%」 and says the positive and negative values are objective experimental quantitative values in the source's framework, with no direct relationship to ordinary human ideas of “good” and “bad”.
- **English rendering (TR-EN):** “Positive value = 100% − negative value.”
- **Context:** “Positive” is a polarity label in this source's measurement display, not a moral evaluation.
- **Source:** SRC-CC-001, Page 307, lines 8875–8910.
- **Review status:** Direct passage extracted; validation OPEN.

### T-028 — Negative Value / 反值 / 反値

- **English display term:** Negative Value (editorial rendering)
- **繁體中文原詞:** 反值
- **日本語（暫定訳）:** 反値
- **Source wording (SRC):** Page 307 states 「反值=100%-正值%」 and distinguishes the display orientation from the positive-value display.
- **English rendering (TR-EN):** “Negative value = 100% − positive value.”
- **Context:** “Negative” is a polarity label in this source's measurement display, not a moral evaluation.
- **Source:** SRC-CC-001, Page 307, lines 8875–8910.
- **Review status:** Direct passage extracted; validation OPEN.

### T-029 — Automation Degree / 自动化程度 / 自動化の程度

- **English display term:** Degree of Automation (editorial rendering)
- **繁體中文原詞:** 自动化程度（繁體字形：自動化程度）
- **日本語（暫定訳）:** 自動化の程度
- **Source wording (SRC):** Page 307 pairs 「自动化程度」 with 「自主化程度」 and describes automation as AI machine-program operation.
- **English rendering (TR-EN):** “Degree of automation.”
- **Context:** The source presents the two as paired percentages within the described Mental Control Area. The source's model-specific meaning should be retained.
- **Source:** SRC-CC-001, Page 307, lines 8890–8930.
- **Review status:** Direct passage extracted; operational mapping OPEN.

### T-030 — Autonomy Degree / 自主化程度 / 自律化の程度

- **English display term:** Degree of Autonomy (editorial rendering)
- **繁體中文原詞:** 自主化程度（繁體字形：自主化程度）
- **日本語（暫定訳）:** 自律化の程度
- **Source wording (SRC):** Page 307 states 「自动化=AI机器程序。自主化=自由意识（freewill）。」
- **English rendering (TR-EN):** “Automation = AI machine program. Autonomy = Free Consciousness (freewill).”
- **Context:** This is an explicit source mapping in this assessment-point passage. Preserve both 自由意识 and the parenthetical English “freewill”; do not generalize it to every historical use of these terms.
- **Source:** SRC-CC-001, Page 307, lines 8890–8930.
- **Review status:** Direct passage extracted; cross-source mapping OPEN.

### T-031 — Freewill Permission / 自由意志权限 / 自由意志の権限

- **English display term:** Freewill Permission (editorial rendering)
- **繁體中文原詞:** 自由意志权限（繁體字形：自由意志權限）
- **日本語（暫定訳）:** 自由意志の権限
- **Source wording (SRC):** Page 300 defines 「权限」 as the ability to read, execute, master, modify and use Origin's holographic information, and names it 「自由意志权限」.
- **English rendering (TR-EN):** “Permission = the ability to read, execute, master, modify and use Origin's holographic information. I call it ‘Freewill Permission’.”
- **Context:** This is a definition within the source's 18-level / experimental-zone model. It should not be generalized as a standard definition of Freewill or permission.
- **Source:** SRC-CC-001, Page 300, lines 8697–8726.
- **Review status:** Direct passage extracted; model scope OPEN.

### T-032 — 18-Level System / 18级制 / 18段階制

- **English display term:** 18-Level System (editorial rendering)
- **繁體中文原詞:** 18级制（繁體字形：18級制）
- **日本語（暫定訳）:** 18段階制
- **Source wording (SRC):** Page 300 presents levels 1–18, with level 18 labelled 「万物本源」 and described as having unlimited knowledge, energy, frequency and permissions. The source explicitly warns that “无限知无限能” does not mean “全知全能”.
- **English rendering (TR-EN):** “18-level system.”
- **Context / limitation:** Page 1669 later states that Consciousness Strength 18 = Origin is unattainable and that a collective spirit can only approach 17.9999999… Preserve this later qualification rather than merging it into Page 300's model description. The source passages do not establish that this system is validated or numerically identical to every practical Consciousness Strength scale.
- **Source:** SRC-CC-001, Pages 300 and 1669, lines 8697–8726 and 46764–46773.
- **Review status:** Historical model extracted; version and scale relationships OPEN.

### T-033 — Level of Awareness / Level of Awareness / 意識の明晰度レベル（暫定）

- **English source term:** Level of Awareness
- **繁體中文:** 原文段落未提供對應中文詞形；正式對應詞 OPEN
- **日本語（暫定訳）:** 意識の明晰度レベル
- **Source wording (SRC):** The Reddit answer states 「The Level of Awareness = Lucidity of Consciousness.」
- **Context:** Preserve this explicit equation as a statement in this particular answer. It does not by itself establish that Level of Awareness is identical to every use of Consciousness Strength or Spectrum.
- **Source:** SRC-RD-001, lines 6432–6483.
- **Review status:** Direct English source wording extracted; Chinese mapping OPEN.

### T-034 — Lucidity of Consciousness / Lucidity of Consciousness / 意識の明晰さ（暫定）

- **English source term:** Lucidity of Consciousness
- **繁體中文:** 原文段落未提供對應中文詞形；正式對應詞 OPEN
- **日本語（暫定訳）:** 意識の明晰さ
- **Source wording (SRC):** The same Reddit answer equates Lucidity of Consciousness with Level of Awareness and says it can be quantifiably measured through a methodology called Strength of Consciousness (SoC) or Strength of Freewill (SoF).
- **Context:** This records the source's stated measurement relationship, not an independently verified measurement claim.
- **Source:** SRC-RD-001, lines 6432–6483.
- **Review status:** Direct English source wording extracted; operational definition OPEN.

### T-035 — Strength of Freewill / Strength of Freewill / 自由意志の強度（暫定）

- **English source term:** Strength of Freewill (SoF)
- **繁體中文:** 原文段落未提供對應中文詞形；正式對應詞 OPEN
- **日本語（暫定訳）:** 自由意志の強度
- **Source wording (SRC):** The Reddit answer names Strength of Freewill (SoF) as one of several terms used by different groups for the described methodology for quantifiably measuring Lucidity of Consciousness.
- **Context:** The same answer separately lists Strength of Consciousness (SoC) and Spectrum of Consciousness (SoC). The repeated abbreviation SoC does not make the full terms interchangeable.
- **Source:** SRC-RD-001, lines 6432–6483.
- **Review status:** Direct English source wording extracted; relation to Strength of Consciousness OPEN.

### T-036 — Spectrum of Consciousness / Spectrum of Consciousness / 意識のスペクトル（暫定）

- **English source term:** Spectrum of Consciousness (SoC)
- **繁體中文:** 原文段落未提供對應中文詞形；正式對應詞 OPEN
- **日本語（暫定訳）:** 意識のスペクトル
- **Source wording (SRC):** The Reddit answer lists “Spectrum of Consciousness (SoC)” alongside Strength of Freewill and Strength of Consciousness as terms used by different groups.
- **Context:** This entry is Spectrum of Consciousness, not Spectrum of Freewill. Preserve the exact source term and do not infer a Spectrum of Freewill mapping.
- **Source:** SRC-RD-001, lines 6432–6483.
- **Review status:** Direct English source wording extracted; operational relationship OPEN.



### T-037 — Infinity / 无限 / 無限

- **English display term:** Infinity
- **繁體中文原詞:** 无限（繁體字形：無限）
- **日本語（暫定訳）:** 無限
- **Current framework wording (SRC):** origin.html describes Infinity as the closest human-understandable description of Origin, not a definition of Origin. zero-origin.html states: “Infinity is a nature of Origin, not Origin itself.”
- **Historical source wording:** The 2009 First Edition in nature-of-origin.html says “The Source = Infinity” if forced to define it; later clarifications explicitly distinguish Infinity from Origin itself.
- **Context / distinction:** Preserve the historical 2009 formulation and later clarification as separate dated layers. The current account does not treat Infinity as identical to Origin, a numerical quantity, or an exhaustive definition.
- **Source:** SRC-OR-001, nature-of-origin.html (First Edition 2009 and later clarifications), origin.html, zero-origin.html.
- **Review status:** Current distinction recorded; historical wording retained without reconciliation.

### T-038 — Zero / 零 / ゼロ

- **English display term:** Zero
- **繁體中文原詞:** 零
- **日本語:** ゼロ
- **Current framework wording (SRC):** zero-idle-state-of-origin.html states that Zero is not a numerical starting point or a value on a numerical scale; it represents the idle state of Origin.
- **Related wording:** Zero also represents Infinity before manifestation. “Before manifestation” is explicitly not necessarily a chronological time-before.
- **Context / distinction:** Do not interpret Zero as ordinary arithmetic zero, nothingness, a physical vacuum, inactivity within a manifested system, or the first event in a sequence. The historical illustration “0 begets 1…” is not a literal mechanism or chronology.
- **Source:** SRC-OR-001, zero-idle-state-of-origin.html, zero-origin.html, origin.html; library/TERMINOLOGY-CONCEPTUAL-REVIEW.md, Section 2.
- **Review status:** Current working description extracted; exact nature of the idle state remains open.

### T-039 — Idle State of Origin / 本源的静止状态（譯形待核） / 本源のアイドル状態（暫定）

- **English display term:** Idle State of Origin
- **繁體中文:** 本源的靜止狀態（暫定描述，非已核定原詞）
- **日本語（暫定訳）:** 本源のアイドル状態
- **Current framework wording (SRC):** Zero represents the idle state of Origin. “Idle” indicates the state of Origin before manifestation and does not imply absence of capability, Freewill or possibility.
- **Context / distinction:** Origin may be idle, active, or idle in one aspect while active in another. “Idle” is a descriptive state term, not a synonym for nonexistence, nothingness or a measured physical vacuum.
- **Source:** SRC-OR-001, zero-idle-state-of-origin.html, zero-origin.html, origin.html.
- **Review status:** English source term extracted; Chinese and Japanese are editorial renderings.

### T-040 — Spirit / 灵 / 靈

- **English display term:** Spirit
- **繁體中文候選原詞:** 灵（繁體字形：靈）；對應關係仍需原文脈絡核對
- **日本語（暫定訳）:** スピリット
- **Current framework wording (SRC):** origin.html names Spirit as one of five natures or aspects and describes it as the perspective of nature, and the closest description of the Source's nature.
- **Historical wording (SRC):** The 2009 First Edition in nature-of-origin.html, Section E, calls Spirit an approximate description from the perspective of nature and says it is still not accurate.
- **Context / distinction:** The inspected framework pages do not establish a one-to-one identity or translation between Spirit, Soul, 灵魂 or 灵体. Do not merge these terms.
- **Source:** SRC-OR-001, origin.html, zero-origin.html, nature-of-origin.html, Section E; library/TERMINOLOGY-CONCEPTUAL-REVIEW.md, Section 4.
- **Review status:** Current role extracted; Chinese lexical mapping and relation to Soul remain OPEN.

### T-041 — Void / 虚空（候選；原詞對應待核） / ヴォイド（暫定）

- **English display term:** Void
- **繁體中文:** 虛空（候選翻譯，未核定為原詞對應）
- **日本語（暫定訳）:** ヴォイド
- **Current framework wording (SRC):** Void is named as one of five natures or aspects of Origin in origin.html and zero-origin.html.
- **Context / distinction:** The current pages name Void but do not supply a complete operational definition in the passages reviewed. Do not substitute Voidness or ordinary physical vacuum as its definition.
- **Source:** SRC-OR-001, origin.html, zero-origin.html; library/TERMINOLOGY-CONCEPTUAL-REVIEW.md, Section 4.
- **Review status:** Named aspect extracted; definition and Chinese/Japanese mapping OPEN.

### T-042 — Voidness / 虚无状态（候選） / ヴォイドネス（暫定）

- **English source term:** Voidness
- **繁體中文:** 虛無狀態（候選描述；原詞映射待核）
- **日本語（暫定訳）:** ヴォイドネス
- **Historical source wording (SRC):** nature-of-origin.html, First Edition (2009), Section E, describes Voidness as a visual perspective on the Source. The parenthetical explanation associates it with the Source being still, not in motion and not creating, described as “non-manifestation” or “nothingness.”
- **Current terminology note:** The current five-name list uses Void, while this historical account uses Voidness. The reviewed sources do not establish that the two are identical or that Void replaced Voidness.
- **Source:** SRC-OR-001, nature-of-origin.html, Section E; library/TERMINOLOGY-CONCEPTUAL-REVIEW.md, Section 4.
- **Review status:** Historical usage extracted; relation to current Void remains OPEN.

### T-043 — True Origin / 真本源（候選） / 真の本源（暫定）

- **English display term:** True Origin
- **繁體中文:** 真本源（候選翻譯；未核定）
- **日本語（暫定訳）:** 真の本源
- **Current framework wording (SRC):** origin.html states that True Origin refers to the Oneness Origin and expresses the foundational position that there is one ultimate Origin rather than multiple independent ultimate sources.
- **Context / distinction:** True Origin is not a separate entity alongside Origin; it is a named framing of the Oneness Origin in the current model. Preserve the source's capitalized English term.
- **Source:** SRC-OR-001, origin.html, origin-models.html, fake-origin-divided-origin.html.
- **Review status:** Current framework description extracted; Chinese and Japanese mappings provisional.

### T-044 — Oneness Origin / 一体本源（候選） / 一なる本源（暫定）

- **English display term:** Oneness Origin
- **繁體中文:** 一體本源（候選描述，非已核定原詞）
- **日本語（暫定訳）:** 一なる本源
- **Current framework wording (SRC):** origin.html explicitly glosses True Origin as “the Oneness Origin” and describes it as one ultimate Origin, rather than multiple independent ultimate sources.
- **Context / distinction:** Do not conflate foundational Oneness Origin with structural unity, a system functioning as one, or a collection with shared organization. oneness-division.html explicitly distinguishes these subjects.
- **Source:** SRC-OR-001, origin.html, origin-models.html, oneness-division.html.
- **Review status:** Current framework description extracted; Chinese and Japanese mappings provisional.

### T-045 — Fake Origin / 假本源（候選） / 偽の本源（暫定）

- **English display term:** Fake Origin
- **繁體中文:** 假本源（候選對應，需與原始中文用例核對）
- **日本語（暫定訳）:** 偽の本源
- **Current framework wording (SRC):** origin-models.html and fake-origin-divided-origin.html describe Fake Origin as a manifestation originated from True Origin that imitates Origin and presents relative independence as absolute independence. It is not a second ultimate Origin.
- **Context / distinction:** The model is explicitly conceptual and not presented as independently verified. Do not automatically equate every historical occurrence of 虚拟, 幻相 or 虚假 with this specific current Fake Origin model.
- **Source:** SRC-OR-001, origin-models.html, fake-origin-divided-origin.html; library/TERMINOLOGY-CONCEPTUAL-REVIEW.md, Section 3.
- **Review status:** Current model description extracted; original Chinese mapping and identification criteria OPEN.

### T-046 — Freewill / 自由意志 / 自由意志

- **English display term:** Freewill
- **繁體中文原詞:** 自由意志
- **日本語（暫定訳）:** 自由意志
- **Current framework wording (SRC):** origin.html and zero-origin.html state: “Freewill is the freedom of change itself.” The description includes the freedom to change or not change, originate or not originate, manifest or not manifest, combine or separate, and transform or remain.
- **Perspective distinction:** In origin.html, Consciousness describes Origin from the perspective of attributes; Freewill describes it from the perspective of functionality. The two are related descriptive perspectives, not interchangeable definitions.
- **Historical context:** Weibo records 230 and 242 distinguish 自由意识 (described as existence) from 自由意志法则 (described as law); record 689 later explicitly pairs 自由意识 with “自由意志Freewill” in parentheses. Preserve dated source variation.
- **Source:** SRC-OR-001, origin.html, zero-origin.html, consciousness-freewill.html; SRC-WB-001, records 230, 242 and 689; library/TERMINOLOGY-CONCEPTUAL-REVIEW.md, Section 1.
- **Review status:** Current working description extracted; cross-source mapping with Free Consciousness remains nuanced and context-dependent.

### T-047 — Imagination / 想象 / 想像（用字待統一）

- **English display term:** Imagination
- **繁體中文候選原詞:** 想象／想像（用字依來源保留）
- **日本語（暫定訳）:** 想像
- **Current framework wording (SRC):** origin.html uses imagination in a broad foundational sense: the proposed capacity through which possibilities and manifestations arise from Origin. It is not limited to human fantasy, visualization or mental images.
- **Context / distinction:** The framework distinguishes spontaneous imagination from intentional imagination. It also states that manifestations are imaginations of Origin and that imagination and manifestation are not separate stages in this account. Preserve both the capacity/potential usage and the manifestation-related usage.
- **Source:** SRC-OR-001, origin.html, zero-origin.html, imagination.html, infinity-of-imagination.html; library/TERMINOLOGY-CONCEPTUAL-REVIEW.md, Section 6.
- **Review status:** Current working description extracted; relation between capacity, scope and manifestation remains open.

### T-048 — Origination / 起源过程（描述性译法） / 創出（暫定）

- **English display term:** Origination
- **繁體中文:** 起源過程（描述性譯法；未核定為原詞）
- **日本語（暫定訳）:** 創出
- **Current framework wording (SRC):** origin.html distinguishes Origin (the fundamental source) from origination (the capability and process through which manifestations come about and may give rise to further manifestations).
- **Context / distinction:** Origination is not another name for Origin, and it is not synonymous with a particular manifestation. The source describes spontaneous, deliberate and mixed modes, and says origination and cessation may occur simultaneously.
- **Source:** SRC-OR-001, origin.html, zero-origin.html, origination.html; library/TERMINOLOGY-CONCEPTUAL-REVIEW.md, Section 6.
- **Review status:** Current framework description extracted; Chinese and Japanese renderings provisional.

### T-049 — Manifestation / 显化（候選） / 顕現（暫定）

- **English display term:** Manifestation
- **繁體中文:** 顯化（候選翻譯；需核對來源原詞及語境）
- **日本語（暫定訳）:** 顕現
- **Current framework wording (SRC):** origin.html and zero-origin.html describe manifestations as what comes about through origination, while stating that all manifestations are imaginations of Origin and that imagination and manifestation are not separate stages in this account.
- **Context / distinction:** Manifestation identifies what comes about; origination concerns the capability/process; Origin concerns the fundamental source. Do not collapse these three terms. The framework also distinguishes manifestation from cessation and transformation.
- **Source:** SRC-OR-001, origin.html, zero-origin.html, origination.html, manifestations.html.
- **Review status:** Current framework description extracted; Chinese and Japanese renderings provisional.


### T-050 — Freedomality of Consciousness / 中文對應待核 / 日本語対応待核

- **English display term:** Freedomality of Consciousness
- **繁體中文:** 尚無已核定對應詞；保留英文原詞
- **日本語:** 確認済みの対応語なし；英語原語を保持
- **Current framework wording (SRC):** The internal Science of Consciousness framework describes Freedomality of Consciousness as the concept/property describing the degree to which an individual's inherent free will is actually expressed through their Soul Characteristics.
- **Related framework statement:** The same source describes Soul Nature as inherently 100% free will, while Soul Characteristics may express only a portion of that free will. These are framework statements, not independently validated scientific findings.
- **Context / distinction:** The supplied Science of Consciousness Project Description describes Freedomality as a property of consciousness and a possible subject of measurement and quantification. The internal framework gives a more specific working description but says its operational definition and measurement still require development and validation.
- **Architecture note:** The supplied Project Description lists Science of Freewill among its four core fields; the internal `materials/awakenology/Science.md` instead lists Frequency of Consciousness, Spectrum of Consciousness, Entropy of Consciousness and Freedom of Consciousness as its four fields. Preserve this document-level difference. Freedomality of Consciousness is listed as an application in both sources.
- **Source:** SRC-SOC-001; SRC-SOC-003, Sections 1 and 5; SRC-AW-TERM-001.
- **Review status:** Current framework working description extracted; operational definition, measurement validity and cross-language mappings OPEN.

### T-051 — Freedomality Index (FI) / 中文對應待核 / 日本語対応待核

- **English display term:** Freedomality Index (FI)
- **繁體中文:** 尚無已核定對應詞；保留英文原詞
- **日本語:** 確認済みの対応語なし；英語原語を保持
- **Current framework wording (SRC):** The internal Science of Consciousness framework describes the Freedomality Index (FI) as the quantified representation or estimate of Freedomality of Consciousness.
- **Context / limitation:** Its scale, calculation, aggregation rules and interpretation remain to be operationally defined and validated. The source assumes no fixed numerical scale. Do not invent a range, unit, formula or conversion rule.
- **Source:** SRC-SOC-003, Section 5; SRC-AW-TERM-001.
- **Review status:** Working description extracted; operational specification and validation OPEN.

### T-052 — Freedometry / 中文對應待核 / 日本語対応待核

- **English display term:** Freedometry
- **繁體中文:** 尚無已核定對應詞；保留英文原詞
- **日本語:** 確認済みの対応語なし；英語原語を保持
- **Current framework wording (SRC):** The internal Science of Consciousness framework describes Freedometry as a proposed measurement methodology for operationalizing and estimating Freedomality of Consciousness and its Freedomality Index (FI).
- **Context / limitation:** The source explicitly says this is a proposed methodology, not an established or validated measurement method. Possible use of Spectrum of Consciousness assessment or sensor systems is presented as a research direction, not a completed measurement protocol. Direct observations must remain distinct from derived estimates and interpretations.
- **Source:** SRC-SOC-003, Section 5; SRC-AW-TERM-001.
- **Review status:** Proposed methodology name extracted; protocol, calibration, uncertainty, inference limits and independent validation OPEN.

### T-053 — Entropy of Consciousness / 意識熵（工作對應） / 日本語対応待核

- **English display term:** Entropy of Consciousness
- **繁體中文（工作對應）:** 意識熵（出現在 Awakenology glossary working draft；尚非原始中文定義）
- **日本語:** 確認済みの対応語なし；英語原語を保持
- **Project Description wording (SRC):** Entropy of Consciousness is an application research field concerning entropy in relation to consciousness, including its properties, characteristics and measurable aspects.
- **Internal framework wording (SRC):** `materials/awakenology/Science.md` lists Entropy of Consciousness as the third field of Science of Consciousness. This field classification differs from the supplied Project Description, which lists it as an application.
- **Current public research page:** `entropy-of-consciousness.html` presents a nine-zone research architecture covering multidimensional capabilities, foundational characteristics, entropy dynamics, flexibility, integration and collaboration, three laboratory-testing zones, and practical application. It explicitly avoids reducing Entropy to a single numerical value and distinguishes laboratory reference assessments from practical performance.
- **Context / limitation:** The reviewed sources do not provide a single operational definition of Entropy of Consciousness. Do not silently import a conventional thermodynamic definition or assume the framework's use is identical to it.
- **Source:** SRC-SOC-001; SRC-SOC-003, Section 1; SRC-AW-TERM-001; SRC-ENT-001.
- **Review status:** Application/field descriptions and public research architecture extracted; operational definition, measurement and cross-document classification OPEN.

### T-054 — Entropy Particle / 中文對應待核 / 日本語対応待核

- **English source term:** Entropy Particle
- **繁體中文:** 原始對應詞待核；保留英文原詞
- **日本語:** 原始對應詞待核；保留英文原詞
- **Current public research-page wording (SRC):** `entropy-of-consciousness.html` uses the term Entropy Particle for structures whose characteristics are examined in the framework. Its Zone 6 examples include oscillation, energy accumulation, elasticity, resistance, controlled movement, weighting and self-balancing.
- **Context / limitation:** The public page says detailed definitions and operational treatment are outside its scope. The RTF v1.1 assessment source has now been directly inspected and provides further source-specific descriptions and assessment points, recorded in the text-run transcription and first-pass point-level register. These passages remain source-contextual and do not establish a complete ontology or operational definition. The DOCX counterpart has not been directly inspected. Do not treat the listed examples as a complete definition or assume the particle terminology is equivalent to a conventional physical particle.
- **Source:** SRC-ENT-001; SRC-ENT-002; SRC-ENT-003; SRC-ENT-004; SRC-ENT-005; SRC-ENT-IDX-001.
- **Review status:** English occurrence and RTF source context extracted; original-language mapping, complete source-level definition and measurement protocol OPEN.

### T-055 — Strength of Consciousness of Things / 中文對應待核 / 日本語対応待核

- **English display term:** Strength of Consciousness of Things
- **繁體中文:** 尚無已核定對應詞；保留英文原詞
- **日本語:** 確認済みの対応語なし；英語原語を保持
- **Project Description wording (SRC):** This is an application research field concerning the strength of consciousness in relation to things, including its properties and potential measurement.
- **Context / distinction:** Keep this exact application name distinct from **Strength of Consciousness**, which appears separately in the Awakenology internal framework as an application of both Awakenology and Spectrum of Consciousness, and has a historical assessment-point framework. The sources reviewed do not establish that Strength of Consciousness of Things is the same construct, a renamed version, or a direct extension of Strength of Consciousness.
- **Related research objective:** Spectrum of Things = Spectrum of Consciousness remains an objective for investigation, not an established conclusion. Do not infer the relationship from the shared word “Things.”
- **Source:** SRC-SOC-001; SRC-SOC-002; SRC-SOC-003, Sections 2–3; SRC-AW-TERM-001; library/TERMINOLOGY-CONCEPTUAL-REVIEW-2.md.
- **Review status:** Application scope extracted; construct definition, measurement and relationship to Strength of Consciousness / Spectrum of Things OPEN.

### T-056 — Awakenology / 催醒法＋催醒學（工作對應） / 催醒法・催醒学（暫定）

- **English display term:** Awakenology
- **繁體中文（工作對應）:** 催醒法＋催醒學
- **日本語（暫定訳）:** 催醒法・催醒学（原語表記を保持した作業上の対応）
- **Current internal framework wording (SRC):** `materials/awakenology/Science.md` describes Awakenology as an application of Science of Consciousness and as an umbrella framework encompassing both 催醒法 (methods/practice) and 催醒學 (knowledge/principles).
- **Project Description wording (SRC):** The supplied Project Description describes Awakenology as applied research into methods of awakening humanity and the development of consciousness.
- **Context / distinction:** Awakenology is not restricted to 催醒法 alone in the current internal framework. The method/practice and knowledge/principles components are both retained. The precise relation between this application and the other application fields must follow the dated source version rather than be assumed.
- **Source:** SRC-SOC-001; SRC-SOC-003, Sections 2–3; SRC-AW-TERM-001; SRC-AW-PAGE-001.
- **Review status:** Umbrella/application description extracted; source-history comparison and Japanese terminology review OPEN.

### T-057 — Exincarnology / 脫離輪迴法（脫離輪迴學） / エクスインカルノロジー（暫定）

- **English display term:** Exincarnology
- **繁體中文（工作對應）:** 脫離輪迴法（脫離輪迴學）
- **日本語（暫定訳）:** エクスインカルノロジー（internal glossary working form）
- **Current internal framework wording (SRC):** `materials/awakenology/Science.md` identifies Exincarnology as the first application of Awakenology and describes it as the specialized discipline and practical framework concerning 脫離輪迴, encompassing the practical method and its knowledge/principles.
- **Project Description wording (SRC):** The supplied Science of Consciousness Project Description lists Exincarnology among the five applications and describes it as applied research into methods of Exincarnation, focusing on liberation from the reincarnation cycle. The short Research Architecture lists it alongside Awakenology without stating a parent/child relationship.
- **Context / distinction:** Preserve the source-version difference: one document lists the application fields together, while the internal framework nests Exincarnology under Awakenology. This tranche records both and does not silently reconcile them.
- **Source:** SRC-SOC-001; SRC-SOC-002; SRC-SOC-003, Sections 2–4; SRC-AW-TERM-001.
- **Review status:** Current internal hierarchy and project-description classification extracted; full source history and Japanese mapping OPEN.

### T-058 — Exincarnation / 脫離輪迴 / 輪廻からの離脱（暫定）

- **English display term:** Exincarnation
- **繁體中文原詞:** 脫離輪迴
- **日本語（暫定訳）:** 輪廻からの離脱
- **Current internal framework wording (SRC):** Exincarnation is described as the process or achievement that Exincarnology aims at.
- **Chinese compilation source wording (SRC):** Page 264 uses 「脱离轮回」 and states 「得道=合一本源+脱离轮回」. The passage distinguishes union with Origin from exiting the reincarnation cycle as two components of 得道.
- **Context / distinction:** Preserve the source phrase 脫離輪迴 and the current project term Exincarnation as a mapped pair with provenance. Exincarnation is not a synonym for Union with Origin. The source's claimed outcome and mechanism are not independently verified by this inventory.
- **Source:** SRC-SOC-001; SRC-SOC-003, Sections 3–4; SRC-CC-001, Page 264, lines 7431–7463.
- **Review status:** Project mapping and historical source relation extracted; operational scope and independent verification OPEN.

### T-059 — Level of Actualization of Freewill / 中文對應待核 / 日本語対応待核

- **English project term:** Level of Actualization of Freewill
- **繁體中文:** 尚無已核定對應詞；保留英文原詞
- **日本語:** 確認済みの対応語なし；英語原語を保持
- **Legacy project record (SRC):** The repository-wide legacy `TERMINOLOGY-INVENTORY.md` records this as a previously adopted replacement term for “Freedom of Consciousness.”
- **Current-source comparison:** The current internal `materials/awakenology/Science.md` uses the phrase “actualization of free will” when describing a research relationship that must be explicitly defined, tested and independently validated. It separately defines Freedomality of Consciousness as the degree to which inherent free will is actually expressed through Soul Characteristics.
- **Related current terminology:** Freedomality of Consciousness (T-050), Freedomality Index (FI) (T-051), and Freedometry (T-052).
- **Context / limitation:** The reviewed primary/current framework sources do not provide a complete definition of the exact title “Level of Actualization of Freewill,” nor a scale, unit, formula, or explicit equivalence with Freedomality of Consciousness or FI. The legacy inventory establishes that the term was previously adopted in project terminology, but does not supply its original defining passage. Do not infer that it is identical to Freedomality, FI, or the actualization of a manifestation.
- **Source:** `TERMINOLOGY-INVENTORY.md` (legacy candidate table); `library/TERMINOLOGY-CONCEPTUAL-REVIEW-2.md`; `materials/awakenology/Science.md`, Section 5; `consciousness-freewill.html`; `what-is-freewill.html`.
- **Review status:** Historical project-term usage located; primary definition, source history, operational meaning, measurement relation and cross-language mappings OPEN.

## 5. Candidate terms and unresolved source families

The following still require additional direct source review before a fuller history or operational definition can be recorded:

- 本源意识
- 万物本质
- 虚拟存在
- 虚拟现实
- 自由意志
- 意识频率
- 意识光谱
- 自由度 / 自由意识的自由强度
- Level of Actualization of Freewill — the legacy repository inventory records it as a previously adopted replacement term for “Freedom of Consciousness” (T-059). Its primary defining passage, operational meaning and relationship to Freedomality of Consciousness / FI remain unverified.
- Hypnotic Reincarnation — a source-stated relation is recorded in T-020, but a fuller definition and source history remain open.
- Soul Nature / Soul Characteristics — used as related concepts in the Freedomality framework; their independent definitions and source history require extraction before further operational interpretation.

Freedomality of Consciousness, Freedomality Index, Freedometry, Entropy of Consciousness, Strength of Consciousness of Things, Awakenology, Exincarnology and Exincarnation now have working records based on the inspected project sources. Their operational definitions, historical source coverage, translations or interrelationships remain open as specified in each record.

## 6. Next extraction priorities

1. Review the remaining original-source families for 本源意识, 万物本质, 虚拟存在 and 虚拟现实, separating definitions from examples, titles and contextual uses.
2. Locate and directly verify the primary source history and defining passage for **Level of Actualization of Freewill** (T-059); establish its intended scope and relationship to Freedomality of Consciousness / FI before defining it.
3. Inspect the Entropy DOCX counterpart directly (still uninspected) and compare its visible content/layout with the reviewed RTF. The RTF v1.1 now has a 2,151-text-run transcription, a first-pass 224-heading / 375-assessment-block register and an RTF text-run/TOC verification memo. Complete semantic classification of individual point qualifications and scoring interpretation remain open; do not treat the register as a count of all source-reported 1,800 points.
4. Review the source history and intended relationship among Freedomality of Consciousness, Freedomality Index (FI), Freedometry and any Level of Actualization of Freewill terminology.
5. Compare Strength of Consciousness of Things with Strength of Consciousness and Spectrum of Things without assuming identity or a parent/child relationship.
6. Continue Awakenology / Exincarnology source-history review and preserve the different organizational descriptions across document versions.
7. Continue Japanese-source verification where original Japanese material exists; provisional translations must remain visibly provisional.

## 7. Change history

- **2026-11-26 — Version 0.7:** Added the RTF v1.1 appendix text-run transcription, corrected point-level assessment register and independent RTF text-run/TOC verification. Recorded 224 body headings and 375 assessment blocks without validating score meaning or the source-reported point totals. DOCX counterpart remains uninspected. No public HTML was changed.
- **2026-11-26 — Version 0.6:** Added direct-source tracking for the Entropy assessment RTF v1.1, including its 114 top-level TOC headings across nine areas and selected detailed passages. Updated the source status without promoting the reported point totals or scoring scheme to independently verified facts.
- **2026-11-26 — Version 0.5:** Added T-059 for Level of Actualization of Freewill after locating its historical project-term record in the legacy terminology inventory. Preserved that historical usage while keeping the primary definition, operational meaning and relationship to Freedomality / FI open. Added a source-attributed Freedomality–actualization conceptual review. No public HTML was changed.
- **2026-11-25 — Version 0.4:** Added T-050–T-058 for Freedomality of Consciousness, Freedomality Index, Freedometry, Entropy of Consciousness, Entropy Particle, Strength of Consciousness of Things, Awakenology, Exincarnology and Exincarnation. Added direct review of the current internal Science.md framework, Awakenology terminology review draft, Entropy public research page and Entropy assessment-point index. Preserved conflicting field/application classifications and the different Awakenology / Exincarnology hierarchies by source version. Left Level of Actualization of Freewill unresolved because the exact term and definition were not present in the reviewed current source files. No public HTML was changed.
- **2026-11-25 — Version 0.3:** Added 13 terminology records (T-037–T-049) from direct review of current Science of Origin framework pages and preserved historical First Edition wording. Recorded Infinity, Zero, Idle State, Spirit, Void, Voidness, True Origin, Oneness Origin, Fake Origin, Freewill, Imagination, Origination and Manifestation. Explicitly retained unresolved Void/Voidness, Spirit/Soul, historical Infinity/Origin and cross-language mappings. No public HTML was changed.
- **2026-11-25 — Version 0.2:** Added direct passage extraction from the completed Chinese compilation TXT (Pages 264, 300, 306–316, 399 and 1669) and the English Reddit archive (lines 6432–6483). Expanded the Consciousness Strength assessment vocabulary and recorded the source's distinctions between union with Origin, liberation from reincarnation, assessment points, practice points, and the historical 18-level model. No published HTML was changed.
- **2026-11-25 — Version 0.1:** Created the first source-traceable trilingual extraction tranche from selected Weibo records, the Weibo context audit, source indexes, and the two supplied Science of Consciousness framework documents. No published HTML was changed.