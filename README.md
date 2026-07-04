# yohon-hokekyo-data

Structured ruby (furigana) text data for the **Yohon** (要品), the essential chapters of the **Myoho Renge Kyo** (Lotus Sutra), as recited in the Nichiren sect.

Each character is paired with its pronunciation reading (呉音 *goon*), the traditional Buddhist reading used in Nichiren sect chanting.

---

## Contents

| File | Chapter (Japanese) | Chapter (English) | Characters |
|------|--------------------|-------------------|-----------|
| `01_johon.json` | 序品 | Johon (Chapter 1) | 713 |
| `02_hobenbon.json` | 方便品 | Hobenpon (Chapter 2) | 302 |
| `03_yokuryoshu.json` | 欲令衆 | Yokuryoshu (Chapter 3 excerpt) | 266 |
| `04_daibadattahon.json` | 提婆達多品 | Daibadattahon (Chapter 12) | 1,753 |
| `05_kanjihon.json` | 勧持品 | Kanjihon (Chapter 13) | 411 |
| `06_juryohon.json` | 寿量品 | Juryohon (Chapter 16) | 2,032 |
| `07_jinrikihon.json` | 神力品 | Jinrikihon (Chapter 21) | 1,138 |
| `08_zokuruihon.json` | 属累品 | Zokuruihon (Chapter 22) | 475 |
| `09_fumonpon.json` | 普門品 | Fumonpon (Chapter 25) | 2,079 |
| `10_dharanihon.json` | 陀羅尼品 | Dharanihon (Chapter 26) | 1,240 |
| `11_myoshogonnohon.json` | 妙荘厳王品 | Myoshogonnohon (Chapter 27) | 1,731 |
| `12_fugenpon.json` | 普賢品 | Fugenpon (Chapter 28) | 1,712 |
| `all.json` | 全品 | All chapters combined | 13,852 |

---

## Data Format

Each JSON file follows this structure:

```json
{
  "name": "寿量品",
  "name_en": "Juryohon (Chapter 16)",
  "note": "...",
  "source": {
    "repo": "https://github.com/kscscafe/yohon-hokekyo-data",
    "copyright": "© Koryu Sugizaki",
    "license": "CC BY-NC-SA 4.0",
    "version": "v1.1.3",
    "checksum": "b56d658983ed7ddf"
  },
  "text": [
    ["妙", "みょう", "myou"],
    ["法", "ほう", "hou"],
    ["蓮", "れん", "ren"],
    ["華", "げー", "gee"],
    ["経", "きょう", "kyou"]
  ]
}
```

`text` is an array of `[kanji, ruby, romaji]` triplets. The ruby represents the *goon* (呉音) pronunciation used in Nichiren sect recitation, which differs from standard modern Japanese readings. Romaji is generated automatically via [pykakasi](https://github.com/miurahr/pykakasi) (Hepburn) and may not perfectly reflect the chanting pronunciation.

`source` records provenance and a checksum (SHA-256, truncated) computed over that chapter's `text` array — it changes if and only if the kanji/ruby/romaji content changes, independent of formatting or metadata edits. Useful for verifying you have an unmodified copy of a given version.

---

## Rare Characters

This dataset includes **㝹** (U+3779), a rare CJK character used as a phonetic component in Sanskrit transliterations:

- 序品: 阿㝹楼駄 (あ**ぬ**るだ)
- 陀羅尼品: 那梨㝹那梨 (**とー**), 兜醯㝹醯 (**とー**)
- 普賢品: 阿㝹伽地 (**とー**)

Standard fonts may not display this character. See the Fonts section below.

---

## Fonts

To display all characters in this dataset correctly, including rare and extended CJK characters, the following open-source fonts are recommended:

### 花園フォント (Hanazono Font)
The most comprehensive open-source Japanese font, covering CJK Unified Ideographs Extensions A–F and beyond.
- Download: https://github.com/cjkvi/HanaMinAFDKO
- License: SIL Open Font License 1.1

### IPAmj明朝 (IPAmj Mincho)
Developed by the Information-technology Promotion Agency (IPA), Japan. Covers variant characters used in personal names and classical texts.
- Download: https://moji.or.jp/mojikiban/font/
- License: IPA Font License

---

## Known Issues / 誤植について

This data was extracted from source files used in a Nichiren sect temple application. While care has been taken to ensure accuracy, **errors in readings may exist**, particularly in:

- Rendaku (連声) — sequential sound changes
- Rare dharani (陀羅尼) transliterations
- Variant goon readings

**Corrections are welcome.** Please open a [GitHub Issue](../../issues) with:
1. The chapter name
2. The character and its current (incorrect) reading
3. The correct reading and, if possible, a reference

---

## License

This data is released under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)** license. Commercial use is not permitted without separate permission from the author.

The sutra text itself is in the public domain. The structured ruby annotations and dataset format are © Koryu Sugizaki.

[![CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

> **Note:** Versions up to and including v1.1.1 were released under CC BY-SA 4.0, which permitted commercial use. That license is not retroactively revoked for copies already distributed under it; this NC restriction applies to v1.1.2 and later.

---

## Attribution

If you use this dataset, please credit:

> yohon-hokekyo-data by Koryu Sugizaki  
> https://github.com/kscscafe/yohon-hokekyo-data  
> Licensed under CC BY-NC-SA 4.0
