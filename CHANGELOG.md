# Changelog

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
