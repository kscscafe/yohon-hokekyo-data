# Changelog

## [1.1.6] - 2026-09-22

### Fixed
- User-confirmed readings (2026-09-22, zero-based indices): 序品 171 波 → はー / hā; 属累品 24 大 → だい / dai; 妙荘厳王品 1184 已 → いー / ī; 普賢品 860 賢 → げん / gen.
- Kanji and source positions remain unchanged. Update affected chapter checksums.

## [1.1.5] - 2026-09-20

### Fixed
- Preserve the `y` sound in yōon display romaji (`みょう` → `myō`, `きょう` → `kyō`, `にょー` → `nyō`). Correct 1,107 affected entries across the 12 chapters; kana readings and character positions are unchanged.

## [1.1.4] - 2026-09-20

### Changed
- Correct 普賢品 index 1014 from `さッ` to `さつ` and normalize all 13,852 romaji readings in the third item of the original JSON files.
- Use macrons for long vowels and the following consonant for small `ッ`/`っ`. Update chapter checksums and add a reproducible generator.
- Remove the temporary parallel display-romaji dataset now that all readings are resolved.

## [1.1.3] - 2026-07-05

### Added
- Add a `source` metadata field to each chapter JSON (repo, copyright, license, version, and a content checksum) for provenance tracking

## [1.1.2] - 2026-07-05

### Changed
- **License changed from CC BY-SA 4.0 to CC BY-NC-SA 4.0** — commercial use now requires separate permission from the author. Versions up to and including v1.1.1 remain available under the original CC BY-SA 4.0 terms for copies already distributed under it.

## [1.1.1] - 2026-07-05

### Fixed
- Cross-checked all 12 chapters against the 妙福寺 official yohon PDF (text-layer extraction, no OCR needed) and corrected missing/mistyped kanji found in the OSS transcription
- Restored kanji dropped from the original transcription across all chapters (654 → 13,852 combined characters, up from 13,550)
- Fixed a stray non-kanji character ('z') mistyped in place of 波 in 妙荘厳王品
- Removed a duplicated 彼 in 妙荘厳王品
- Regenerated `all.json` from the corrected per-chapter files
- Documented a newly found 㝹 (U+3779) occurrence in 普賢品 (阿㝹伽地)

## [1.0.0] - 2026-05-26

### Added
- Initial release
- 12 chapters of Yohon (要品) with goon (呉音) ruby readings
- 13,550 kanji-ruby pairs total
- Rare character 㝹 (U+3779) correctly included with readings:
  - 序品 (01_johon): ぬ
  - 陀羅尼品 (10_dharanihon): とー ×2
