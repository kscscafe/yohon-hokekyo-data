# yohon-hokekyo-data

Structured ruby (furigana) text data for the **Yohon** (要品), the essential chapters of the **Myoho Renge Kyo** (Lotus Sutra), as recited in the Nichiren sect.

Each character is paired with its pronunciation reading (呉音 *goon*), the traditional Buddhist reading used in Nichiren sect chanting.

---

## Contents

| File | Chapter (Japanese) | Chapter (English) | Characters |
|------|--------------------|-------------------|-----------|
| `01_johon.json` | 序品 | Jobon (Chapter 1) | 654 |
| `02_hobenbon.json` | 方便品 | Hobenpon (Chapter 2) | 294 |
| `03_yokuryoshu.json` | 欲令衆 | Yokuryoshu (Chapter 3 excerpt) | 255 |
| `04_daibadattahon.json` | 提婆達多品 | Daibadattahon (Chapter 12) | 1,736 |
| `05_kanjihon.json` | 勧持品 | Kanjihon (Chapter 13) | 409 |
| `06_juryohon.json` | 寿量品 | Juryohon (Chapter 16) | 2,027 |
| `07_jinrikihon.json` | 神力品 | Jinrikihon (Chapter 21) | 1,097 |
| `08_zokuruihon.json` | 属累品 | Zokuruihon (Chapter 22) | 468 |
| `09_fumonpon.json` | 普門品 | Fumonpon (Chapter 25) | 2,046 |
| `10_dharanihon.json` | 陀羅尼品 | Dharanihon (Chapter 26) | 1,208 |
| `11_myoshogonnohon.json` | 妙荘厳王品 | Myoshogonnohon (Chapter 27) | 1,704 |
| `12_fugenpon.json` | 普賢品 | Fugenpon (Chapter 28) | 1,652 |
| `all.json` | 全品 | All chapters combined | 13,550 |

---

## Data Format

Each JSON file follows this structure:

```json
{
  "name": "寿量品",
  "name_en": "Juryohon (Chapter 16)",
  "note": "...",
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

---

## Rare Characters

This dataset includes **㝹** (U+3779), a rare CJK character used as a phonetic component in Sanskrit transliterations:

- 序品: 阿㝹楼駄 (あ**ぬ**るだ)
- 陀羅尼品: 那梨㝹那梨 (**とー**), 兜醯㝹醯 (**とー**)

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

This data is released under the **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** license.

The sutra text itself is in the public domain. The structured ruby annotations and dataset format are © OFFICE ES LLC.

[![CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-sa/4.0/)

---

## Attribution

If you use this dataset, please credit:

> yohon-hokekyo-data by OFFICE ES LLC  
> https://github.com/kscscafe/yohon-hokekyo-data  
> Licensed under CC BY-SA 4.0
