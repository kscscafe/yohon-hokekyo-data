# yohon-hokekyo-data

日蓮宗で読誦される『妙法蓮華経』の要品（ようほん）について、漢字ごとに読み仮名（ルビ）を対応づけた構造化テキストデータです。

各文字に、日蓮宗の読誦で用いられる伝統的な仏教の読み、呉音（ごおん）の読みが付いています。

[English README](README.md)

---

## 収録内容

| ファイル | 品名 | 英語名 | 文字数 |
|----------|------|--------|--------|
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
| `all.json` | 全品 | 全品を結合したもの | 13,852 |

---

## データ形式

各JSONファイルは次の構造です。

```json
{
  "name": "寿量品",
  "name_en": "Juryohon (Chapter 16)",
  "note": "...",
  "source": {
    "repo": "https://github.com/kscscafe/yohon-hokekyo-data",
    "copyright": "© Koryu Sugizaki",
    "license": "CC BY-NC-SA 4.0",
    "version": "v1.1.6",
    "checksum": "e2311122ac0c1a06"
  },
  "text": [
    ["妙", "みょう", "myō"],
    ["法", "ほう", "hō"],
    ["蓮", "れん", "ren"],
    ["華", "げー", "gē"],
    ["経", "きょう", "kyō"]
  ]
}
```

`text` は `[漢字, ルビ, ローマ字]` の3要素の配列です。ルビは日蓮宗の読誦で用いる呉音で、現代日本語の標準的な読みとは異なります。3番目の要素は表示用のローマ字で、かな表記から下記の規則で生成しています。

### 表示用ローマ字

`python3 scripts/normalize_romaji.py` を実行すると、各品のJSONと `all.json` の3番目の要素（表示用ローマ字）を再生成します。このスクリプトは各品のチェックサムも更新します。

長音にはマクロンを使います（`みょう` → `myō`、`ほう` → `hō`）。拗音は `y` を残します（`きょう` → `kyō`、`にょー` → `nyō`）。`sh`、`ch`、`j` はヘボン式に従います。語末の小さい `ッ`/`っ` は、次の文字の頭の子音を担います（`こッ`/`しゅー` → `kos`/`shū`、`せッ`/`ぽう` → `sep`/`pō`）。`sh` の前では `s`、`ch` や `ts` の前では `t` になります。普賢品の位置1014の `薩` は、かなを `さつ`、ローマ字を `satsu` に訂正済みです。

`source` には出典情報とチェックサム（SHA-256を短縮したもの）を記録しています。チェックサムはその品の `text` 配列から計算しており、漢字・ルビ・ローマ字の内容が変わったときにだけ変わります（書式やメタデータの変更では変わりません）。各バージョンの原本どおりのコピーかどうかを確かめるのに使えます。

---

## 稀少字

このデータには、梵語の音写で音を表す要素として使われる稀少なCJK文字 **㝹**（U+3779）が含まれます。

- 序品：阿㝹楼駄（あ**ぬ**るだ）
- 陀羅尼品：那梨㝹那梨（**とー**）、兜醯㝹醯（**とー**）
- 普賢品：阿㝹伽地（**とー**）

標準のフォントでは表示されないことがあります。下の「フォント」を参照してください。

---

## フォント

稀少字や拡張CJK漢字を含め、すべての文字を正しく表示するには、次のオープンソースのフォントを推奨します。

### 花園フォント（Hanazono Font）
CJK統合漢字拡張A〜F以降を含む、最も網羅的なオープンソースの日本語フォントです。
- ダウンロード: https://github.com/cjkvi/HanaMinAFDKO
- ライセンス: SIL Open Font License 1.1

### IPAmj明朝（IPAmj Mincho）
情報処理推進機構（IPA）が開発したフォントで、人名や古典で使われる異体字を含みます。
- ダウンロード: https://moji.or.jp/mojikiban/font/
- ライセンス: IPAフォントライセンス

---

## 誤植について

このデータは、日蓮宗の寺院向けアプリで使われているソースファイルから抽出したものです。正確さには注意を払っていますが、特に次の点で**読みに誤りが残っている可能性があります**。

- 連声（れんじょう）：続く音による音の変化
- 稀少な陀羅尼の音写
- 呉音の異読

**ご指摘を歓迎します。** 次の内容を添えて [GitHub Issue](../../issues) を作成してください。

1. 品名
2. 該当の文字と、現在の（誤っている）読み
3. 正しい読み、あれば根拠

---

## ライセンス

このデータは **クリエイティブ・コモンズ 表示-非営利-継承 4.0 国際（CC BY-NC-SA 4.0）** ライセンスで公開しています。商用利用には、著作者の別途の許可が必要です。

経文そのものはパブリックドメインです。構造化したルビの注釈とデータ形式の著作権は、Koryu Sugizaki に帰属します。

[![CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

> **注:** v1.1.1 までは、商用利用を認める CC BY-SA 4.0 で公開していました。そのライセンスで配布済みのコピーについては、遡って取り消されません。非営利の制限は v1.1.2 以降に適用されます。

---

## クレジット表記

このデータを利用する場合は、次のとおり表記してください。

> yohon-hokekyo-data by Koryu Sugizaki  
> https://github.com/kscscafe/yohon-hokekyo-data  
> Licensed under CC BY-NC-SA 4.0
