#!/usr/bin/env python3
"""Regenerate normalized romaji in all chapter JSON files and all.json."""

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
            stem = YOON.get(char, BASE[char][:-1] + "y")
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




def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    root = Path(__file__).resolve().parents[1]
    source = root / "data/all.json"
    chapters = json.loads(source.read_text(encoding="utf-8"))
    files = sorted((root / "data").glob("[0-9][0-9]_*.json"))
    if len(chapters) != 12 or len(files) != 12:
        raise ValueError("Expected 12 chapters")
    if sum(len(c["text"]) for c in chapters) != 13852:
        raise ValueError("Expected 13,852 characters")
    for chapter, path in zip(chapters, files, strict=True):
        individual = json.loads(path.read_text(encoding="utf-8"))
        if individual != chapter:
            raise ValueError(f"Chapter mismatch: {path}")
        for index, item in enumerate(chapter["text"]):
            if len(item) != 3:
                raise ValueError(f"Unexpected entry: {chapter['name']} {index}")
            if chapter["name"] == "普賢品" and index == 1014:
                if item[0] != "薩" or item[1] not in ("さッ", "さつ"):
                    raise ValueError("Unexpected 普賢品 index 1014")
                item[1] = "さつ"
            next_kana = chapter["text"][index + 1][1] if index + 1 < len(chapter["text"]) else None
            item[2] = romanize_cell(item[1], next_kana)
            if not item[2]:
                raise ValueError(f"Unresolved romaji: {chapter['name']} {index}")
        chapter["note"] = "Readings follow Nichiren sect goon (呉音) pronunciation. Display romaji uses macrons for long vowels and context-aware consonants for small tsu; corrections are welcome via GitHub Issues."
        chapter["source"]["version"] = "v1.1.5"
        chapter["source"]["checksum"] = hashlib.sha256(
            json.dumps(chapter["text"], ensure_ascii=False).encode("utf-8")
        ).hexdigest()[:16]
        write_json(path, chapter)
    write_json(source, chapters)
    print("Updated 12 chapters and all.json: 13,852 complete readings")


if __name__ == "__main__":
    main()
