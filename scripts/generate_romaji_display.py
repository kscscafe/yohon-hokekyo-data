#!/usr/bin/env python3
"""Generate display romaji without altering the legacy three-item text tuples."""

import hashlib
import json
from pathlib import Path

BASE = {
    "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
    "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
    "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
    "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
    "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no",
    "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
    "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",
    "や": "ya", "ゆ": "yu", "よ": "yo",
    "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",
    "わ": "wa", "ん": "n",
    "が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go",
    "ざ": "za", "じ": "ji", "ず": "zu", "ぜ": "ze", "ぞ": "zo",
    "だ": "da", "で": "de", "ど": "do",
    "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo",
    "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぽ": "po",
}
YOON = {"し": "sh", "ち": "ch", "じ": "j"}
MACRON = {"a": "ā", "i": "ī", "u": "ū", "e": "ē", "o": "ō"}
HEADERS = ("文字位置", "漢字", "かなルビ", "ローマ字ルビ")


def romanize(kana):
    if "っ" in kana or "ッ" in kana:
        return ""
    pieces = []
    i = 0
    while i < len(kana):
        char = kana[i]
        if char == "ー":
            if not pieces or pieces[-1][-1] not in MACRON:
                raise ValueError(f"長音記号の位置を解釈できません: {kana}")
            pieces[-1] = pieces[-1][:-1] + MACRON[pieces[-1][-1]]
        elif i + 1 < len(kana) and kana[i + 1] in "ゃゅょ":
            if char not in BASE or not BASE[char].endswith("i"):
                raise ValueError(f"拗音を解釈できません: {kana}")
            stem = YOON.get(char, BASE[char][:-1])
            pieces.append(stem + {"ゃ": "a", "ゅ": "u", "ょ": "o"}[kana[i + 1]])
            i += 1
        else:
            if char not in BASE:
                raise ValueError(f"未対応のかな: {kana} / {char}")
            sound = BASE[char]
            # A following う lengthens an o/u sound; identical vowel kana also lengthen.
            if pieces and ((char == "う" and pieces[-1].endswith(("o", "u")))
                           or (sound in MACRON and pieces[-1].endswith(sound))):
                pieces[-1] = pieces[-1][:-1] + MACRON[pieces[-1][-1]]
            else:
                pieces.append(sound)
        i += 1
    return "".join(pieces)


def romanize_cell(kana, next_kana):
    if "っ" not in kana and "ッ" not in kana:
        return romanize(kana)
    if not next_kana or not kana.endswith(("っ", "ッ")):
        return ""
    following = romanize(next_kana.replace("っ", "").replace("ッ", ""))
    if not following or following[0] in "aiueoāīūēō":
        return ""
    consonant = "t" if following.startswith(("ch", "ts")) else following[0]
    return romanize(kana[:-1]) + consonant




def main():
    root = Path(__file__).resolve().parents[1]
    source = root / "data/all.json"
    raw = source.read_bytes()
    chapters = json.loads(raw)
    if len(chapters) != 12 or sum(len(c["text"]) for c in chapters) != 13852:
        raise ValueError("Expected 12 chapters and 13,852 characters")
    result = {
        "schema_version": 1,
        "source_file": "data/all.json",
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "chapters": [],
    }
    unresolved = []
    for chapter in chapters:
        readings = []
        for index, item in enumerate(chapter["text"]):
            if len(item) != 3:
                raise ValueError(f"Unexpected text entry: {chapter['name']} {index}")
            next_kana = chapter["text"][index + 1][1] if index + 1 < len(chapter["text"]) else None
            value = romanize_cell(item[1], next_kana)
            if not value:
                unresolved.append((chapter["name"], index, item[0], item[1]))
            readings.append(value)
        result["chapters"].append({
            "name": chapter["name"],
            "source_checksum": chapter["source"]["checksum"],
            "romaji": readings,
        })
    if unresolved != [("普賢品", 1014, "薩", "さッ")]:
        raise ValueError(f"Unexpected unresolved readings: {unresolved}")
    target = root / "data/romaji_display.json"
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    check = json.loads(target.read_text(encoding="utf-8"))
    for original, addition in zip(chapters, check["chapters"], strict=True):
        if original["name"] != addition["name"] or len(original["text"]) != len(addition["romaji"]):
            raise AssertionError("Chapter or row count mismatch")
    print(f"Generated {target}: 12 chapters, 13,852 readings, {len(unresolved)} unresolved")


if __name__ == "__main__":
    main()
