#!/usr/bin/env python3
"""Two audio-neutral key improvements across all tests:

1. Teil 2 (match): currently the 5 correct answers are almost always a-b-c-d-e
   (distractors f-i never used). Re-order the 9 option texts under the fixed
   letters a-i so the correct answers spread across the whole range and the
   distractors become plausible. The spoken conversation is unchanged.

2. Teil 4 (ja/nein): the first statement is "ja" in 80/100 tests. Re-order the
   5 independent statements so the first answer is balanced ~50/50 across the
   bank. Each statement keeps its own correct answer; only display order moves.
   The interview audio is unchanged.
"""

import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / 'tools'
LETTERS = 'abcdefghi'


def shuffle_teil2(test, seed):
    t2 = test['teile'][1]
    opts = t2['options']
    if len(opts) != 9:
        return False
    texts = [o['text'] for o in opts]
    l2i = {l: i for i, l in enumerate(LETTERS)}
    item_old_idx = [l2i[it['correct']] for it in t2['items']]
    rng = random.Random(seed)
    perm = list(range(9))
    for _ in range(300):
        rng.shuffle(perm)
        old2new = {perm[p]: p for p in range(9)}
        new_keys = [old2new[oi] for oi in item_old_idx]
        in_fi = sum(1 for k in new_keys if k >= 5)
        # want correct answers spread: at least 2 land in f-i, and not the
        # trivial a-b-c-d-e ordering
        if in_fi >= 2 and new_keys != [0, 1, 2, 3, 4]:
            break
    t2['options'] = [{'letter': LETTERS[p], 'text': texts[perm[p]]} for p in range(9)]
    old2new = {perm[p]: p for p in range(9)}
    for it, oi in zip(t2['items'], item_old_idx):
        it['correct'] = LETTERS[old2new[oi]]
    return True


def balance_teil4_first(test, want_first):
    """Make the first ja/nein item equal to want_first via a single swap."""
    items = test['teile'][3]['items']
    if not items or items[0]['correct'] == want_first:
        return False
    for j in range(1, len(items)):
        if items[j]['correct'] == want_first:
            items[0], items[j] = items[j], items[0]
            return True
    return False


def main():
    files = sorted(TOOLS.glob('_test*_data.json'),
                   key=lambda p: int(re.search(r'_test(\d+)_', p.name).group(1)))
    data = [(f, json.loads(f.read_text(encoding='utf-8'))) for f in files]

    # ---- Teil 2 shuffle ----
    n2 = 0
    for f, d in data:
        tnum = int(re.search(r'_test(\d+)_', f.name).group(1))
        if shuffle_teil2(d, seed=tnum * 7 + 3):
            n2 += 1

    # ---- Teil 4 first-item balance to ~50/50 ----
    # decide target first answer per test to hit a 50/50 global split
    first_now = [d['teile'][3]['items'][0]['correct'] for _, d in data]
    n = len(data)
    target_nein = n // 2
    # assign 'nein' as target to a spread-out half of the tests
    order = sorted(range(n), key=lambda i: (i * 53) % n)  # deterministic spread
    want = ['ja'] * n
    for rank, i in enumerate(order):
        if rank < target_nein:
            want[i] = 'nein'
    n4 = 0
    for (f, d), w in zip(data, want):
        if balance_teil4_first(d, w):
            n4 += 1

    for f, d in data:
        f.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    print(f"Teil 2 options reshuffled in {n2} tests.")
    print(f"Teil 4 first-item reordered in {n4} tests.")


if __name__ == '__main__':
    main()
