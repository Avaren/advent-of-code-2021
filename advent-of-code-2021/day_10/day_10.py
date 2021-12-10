from typing import Tuple


def parse_file(file_name: str) -> tuple[str]:
    with open(f"advent-of-code-2021/day_10/{file_name}") as f:
        return tuple(line.strip() for line in f)


ERROR_POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

MISSING_POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

PAIRS = [
    ("{", "}"),
    ("(", ")"),
    ("[", "]"),
    ("<", ">"),
]


def part_1(lines):
    total = 0
    openers = {b: a for a, b in PAIRS}
    for line in lines:
        opened = []
        for c in line:
            if c in ERROR_POINTS:
                if opened[-1] != openers[c]:
                    total += ERROR_POINTS[c]
                    break
                else:
                    del opened[-1]
            else:
                opened.append(c)
    return total


def part_2(lines):
    totals = []
    openers = {b: a for a, b in PAIRS}
    closers = {a: b for a, b in PAIRS}
    for line in lines:
        error = False
        opened = []
        for c in line:
            if c in ERROR_POINTS:
                if opened[-1] != openers[c]:
                    error = True
                    break
                else:
                    del opened[-1]
            else:
                opened.append(c)
        if not error and opened:
            line_score = 0
            to_close = [closers[o] for o in reversed(opened)]
            for tc in to_close:
                line_score *= 5
                line_score += MISSING_POINTS[tc]
            totals.append(line_score)

    return sorted(totals)[len(totals) // 2]
