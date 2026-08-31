---
name: primary-source-analysis
description: Analyze primary historical sources such as inscriptions, manuscripts, official records, letters, legal documents, maps, images, artifacts, and archaeological reports. Use when extracting, transcribing, contextualizing, or interpreting a primary source while preserving the distinction between source evidence and later explanation.
---

# Primary Source Analysis

## Processing order

1. Identify the source and its physical or digital carrier.
2. Record the exact source location, page, folio, item number, image identifier, edition and access date.
3. Separate original text, diplomatic transcription, normalized transcription, translation, editorial note and interpretation.
4. Describe visible omissions, damage, illegible characters, lacunae, layout, seals, marginalia, diagrams and captions.
5. Establish genre, date range, provenance, audience and institutional context.
6. Extract claims and classify each as descriptive, normative, administrative, commemorative, polemical or symbolic.
7. Compare with independent sources and relevant scholarship.
8. State what the source can answer, cannot answer, and only suggests.

## Transcription rules

- Preserve original spelling, script, punctuation, lineation and brackets when the task is diplomatic transcription.
- Use `[缺字]`, `[漫漶]`, `[无法辨认]` or `[疑]` rather than guessing.
- Keep editorial supplements in `< >` or another explicitly declared convention; never mix them into the original text.
- Record variant readings separately.
- Do not modernize names, institutions or place names without labeling the normalization.

## Image and artifact rules

- Describe the object before interpreting its meaning.
- Keep image labels, captions, catalog numbers and modern释文 separate from text on the original object.
- Do not infer an object identity solely from visual resemblance.
- For unclear images, preserve the image reference and report only visible external information.

## Output structure

```text
来源信息：
载体与版本：
原始文字/图像描述：
忠实转录：
规范化转录：
译文：
编辑说明：
历史语境：
可直接支持的事实：
解释性推论：
不能确定的内容：
参照文献：
```
