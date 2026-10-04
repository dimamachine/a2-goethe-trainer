#!/usr/bin/env python3
"""Reshape Lesen T1/T3 texts toward official Goethe A2 paragraph style.

- Join telegraphic sentences (≤6 words) onto the previous sentence.
- Pack body text into 4 (T1) / 5 (T3) denser paragraphs.
- Reorder scored questions to follow the text (T1 Q5 stays last / global).
- Remap question hints after joins.

Does not touch T2 (boards) or T4 (ads). Run from repo root:
  python3 tools/_reparagraph_lesen.py          # write
  python3 tools/_reparagraph_lesen.py --dry    # report only
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
FILE = ROOT / "assets/data/lesen-tests.js"

FUNC_FIRST = {
    "der", "die", "das", "den", "dem", "des",
    "ein", "eine", "einer", "eines", "einen", "einem",
    "er", "sie", "es", "wir", "ihr", "man", "ich", "du",
    "mein", "meine", "meiner", "meinem", "meinen", "meines",
    "dein", "deine", "sein", "seine", "ihre", "ihr", "unser", "unsere",
    "viele", "manche", "einige", "alle", "beide", "andere",
    "auch", "so", "dann", "dort", "hier", "heute", "damals", "jetzt",
    "bald", "später", "danach", "deshalb", "trotzdem",
    "aber", "und", "oder", "denn", "weil", "wenn", "als",
    "am", "im", "zum", "zur", "beim", "vom",
    "nach", "vor", "für", "mit", "von", "aus", "auf", "über", "unter",
    "zwischen", "ohne", "bis", "seit",
    "nicht", "nur", "noch", "schon", "sehr", "ganz",
    "was", "wie", "wo", "wer", "wann",
    "das", "dies", "dieser", "diese", "dieses",
}


def extract_pools(src: str) -> tuple[str, dict]:
    header = src[: src.index("window.")]
    pools = {}
    for name in ("LESEN_T1_SETS", "LESEN_T2_SETS", "LESEN_T3_SETS", "LESEN_T4_SETS"):
        m = re.search(rf"window\.{name}\s*=\s*", src)
        i = m.end()
        while src[i] not in "[{":
            i += 1
        opener = src[i]
        closer = "]" if opener == "[" else "}"
        depth = 0
        in_str = None
        esc = False
        for j in range(i, len(src)):
            c = src[j]
            if in_str:
                if esc:
                    esc = False
                elif c == "\\":
                    esc = True
                elif c == in_str:
                    in_str = None
                continue
            if c in "\"'":
                in_str = c
                continue
            if c == opener:
                depth += 1
            elif c == closer:
                depth -= 1
                if depth == 0:
                    pools[name] = json.loads(src[i : j + 1])
                    break
    return header, pools


def words(s: str) -> int:
    return len(re.findall(r"[A-Za-zÄÖÜäöüß0-9']+", s))


def first_word(s: str) -> str:
    m = re.match(r"[„\"'\(\[]*([A-Za-zÄÖÜäöüß\-]+)", s)
    return m.group(1) if m else ""


def join_onto(prev: str, nxt: str) -> str:
    core = prev.rstrip()
    if core.endswith("."):
        core = core[:-1]
    add = nxt.lstrip()
    fw = first_word(add)
    if fw and fw.lower() in FUNC_FIRST and add[0].isupper() and add[0] not in "„\"'":
        # lowercase the first letter only
        add = add[0].lower() + add[1:]
    sep = " — " if core.endswith(("!", "?", ":", "…")) else ", "
    if core.endswith(("—", "-")):
        sep = " "
    return core + sep + add


def join_short(
    sentences: list[str],
    protected: set[int],
    max_short: int = 6,
    prev_cap: int = 24,
) -> tuple[list[str], list[int]]:
    """Join tiny non-evidence sentences onto the previous one.

    Evidence sentences (question hints) stay standalone so each question
    still highlights a distinct span. Returns (new_sentences, old_to_new).
    """
    new: list[str] = []
    mapping: list[int] = []
    joins_into_current = 0
    for i, sent in enumerate(sentences):
        w = words(sent)
        starts_quote = sent.lstrip()[:1] in "„\"'"
        can_join = (
            new
            and i not in protected
            and w <= max_short
            and words(new[-1]) <= prev_cap
            and joins_into_current < 1
            and not starts_quote
            and not new[-1].rstrip().endswith(("?", "!"))
        )
        if can_join:
            new[-1] = join_onto(new[-1], sent)
            mapping.append(len(new) - 1)
            joins_into_current += 1
        else:
            mapping.append(len(new))
            new.append(sent)
            joins_into_current = 0
    return new, mapping


def pack_paragraphs(sentences: list[str], target_n: int, min_words: int, floor: int = 3) -> list[list[int]]:
    """Split the text into ~target_n contiguous paragraphs of similar size.

    Keeps reading order. Matches official papers: 3–5 dense paragraphs,
    not one question per paragraph.
    """
    n = len(sentences)
    if n == 0:
        return []
    weights = [words(s) for s in sentences]
    total = sum(weights)
    target_n = min(target_n, n)
    while target_n > 3 and total / target_n < min_words:
        target_n -= 1
    if target_n <= 1:
        return [list(range(n))]
    cuts = []
    acc = 0
    k = 1
    for i, w in enumerate(weights):
        acc += w
        if k < target_n and i < n - 1 and acc >= (total * k) / target_n:
            cuts.append(i + 1)
            k += 1
    bounds = [0] + cuts + [n]
    clean = [bounds[0]]
    for b in bounds[1:]:
        if b > clean[-1]:
            clean.append(b)
    if clean[-1] != n:
        clean.append(n)
    paras = [list(range(clean[j], clean[j + 1])) for j in range(len(clean) - 1)]

    def pw(p):
        return sum(weights[i] for i in p)

    floor = min(floor, target_n)
    changed = True
    while changed and len(paras) > floor:
        changed = False
        for k, p in enumerate(paras):
            if pw(p) < min_words:
                if k == 0:
                    paras[1] = p + paras[1]
                    del paras[0]
                else:
                    paras[k - 1] = paras[k - 1] + p
                    del paras[k]
                changed = True
                break
    return paras


def smooth_breaks(sentences: list[str], paras: list[list[int]]) -> list[list[int]]:
    """Don't start a paragraph with a tiny leftover fragment."""
    if len(paras) < 2:
        return paras
    out = [list(p) for p in paras]
    k = 1
    while k < len(out):
        if not out[k]:
            del out[k]
            continue
        first = sentences[out[k][0]]
        if words(first) <= 6 and len(out[k]) > 1 and out[k - 1]:
            out[k - 1].append(out[k].pop(0))
            continue
        k += 1
    return [p for p in out if p]


def reorder_questions(set_, keep_last_global: bool) -> None:
    qs = set_["questions"]
    if keep_last_global:
        head, last = qs[:-1], qs[-1:]
        head.sort(key=lambda q: q["hint"])
        set_["questions"] = head + last
    else:
        qs.sort(key=lambda q: q["hint"])


def apply_set(set_, target_n: int, min_words: int, keep_last_global: bool) -> dict:
    old_n_sent = len(set_["sentences"])
    old_n_para = len(set_["paragraphs"])
    nq = len(set_["questions"]) - (1 if keep_last_global else 0)
    protected = {q["hint"] for q in set_["questions"][:nq]}
    new_sents, mapping = join_short(set_["sentences"], protected)
    for q in set_["questions"]:
        q["hint"] = mapping[q["hint"]]
    set_["sentences"] = new_sents
    set_["paragraphs"] = smooth_breaks(
        new_sents,
        pack_paragraphs(new_sents, target_n, min_words, floor=4 if target_n >= 5 else 3),
    )
    reorder_questions(set_, keep_last_global)
    # sanity: every sentence in exactly one paragraph, hints in range
    flat = [i for p in set_["paragraphs"] for i in p]
    if flat != list(range(len(new_sents))):
        raise RuntimeError("paragraphs do not partition sentences")
    for q in set_["questions"]:
        if not (0 <= q["hint"] < len(new_sents)):
            raise RuntimeError(f"hint {q['hint']} out of range {len(new_sents)}")
        if "correct" not in q or q["correct"] not in (0, 1, 2):
            raise RuntimeError("bad correct")
        if len(q.get("opts") or []) != 3:
            raise RuntimeError("need 3 opts")
    new_pw = [
        sum(words(new_sents[i]) for i in para) for para in set_["paragraphs"]
    ]
    return {
        "old_sent": old_n_sent,
        "new_sent": len(new_sents),
        "old_para": old_n_para,
        "new_para": len(set_["paragraphs"]),
        "para_words": new_pw,
        "joined": old_n_sent - len(new_sents),
    }


def main():
    dry = "--dry" in sys.argv
    src = FILE.read_text()
    header, pools = extract_pools(src)

    stats_t1 = []
    for s in pools["LESEN_T1_SETS"]:
        stats_t1.append(apply_set(s, target_n=4, min_words=40, keep_last_global=True))
    stats_t3 = []
    for s in pools["LESEN_T3_SETS"]:
        stats_t3.append(apply_set(s, target_n=5, min_words=30, keep_last_global=False))

    def summarize(label, st):
        tiny = sum(1 for x in st if min(x["para_words"] or [0]) < 30)
        npara = sorted(x["new_para"] for x in st)
        joined = sum(x["joined"] for x in st)
        print(
            f"{label}: joined {joined} short sents; "
            f"paras now {min(npara)}–{max(npara)} (median {npara[len(npara)//2]}); "
            f"sets with a para <30w: {tiny}/{len(st)}"
        )

    summarize("T1", stats_t1)
    summarize("T3", stats_t3)

    # Show a few samples
    def show(tag, s, nq):
        print(f"\n--- {tag} {s.get('title') or s.get('subject')} ---")
        print("paras", [sum(words(s["sentences"][i]) for i in p) for p in s["paragraphs"]])
        print("hints", [q["hint"] for q in s["questions"]])
        for pi, p in enumerate(s["paragraphs"]):
            body = " ".join(s["sentences"][i] for i in p)
            print(f"P{pi+1}: {body[:180]}{'...' if len(body)>180 else ''}")

    show("T1[0]", pools["LESEN_T1_SETS"][0], 4)
    show("T1[65]", pools["LESEN_T1_SETS"][65], 4)
    show("T1[93]", pools["LESEN_T1_SETS"][93], 4)
    show("T3[0]", pools["LESEN_T3_SETS"][0], 5)
    show("T3[7]", pools["LESEN_T3_SETS"][7], 5)
    show("T3[65]", pools["LESEN_T3_SETS"][65], 5)

    if dry:
        print("\nDRY RUN — file not written")
        return
    out = header
    for name, arr in pools.items():
        out += f"window.{name} = {json.dumps(arr, ensure_ascii=False, indent=2)};\n\n"
    FILE.write_text(out)
    print(f"\nWrote {FILE}")


if __name__ == "__main__":
    main()
