import functools
import itertools
import logging


def parse_file(file_name: str) -> tuple[tuple[tuple[str], tuple[str]]]:
    with open(f"advent-of-code-2021/day_8/{file_name}") as f:
        return tuple(
            (
                tuple(l.split("|")[0].strip().split(" ")),
                tuple(l.split("|")[1].strip().split(" ")),
            )
            for l in f
        )


def part_1(displays: tuple[tuple[tuple[str], tuple[str]]]):
    total = 0
    for options, signals in displays:
        for signal in signals:
            if len(signal) in {2, 3, 4, 7}:
                total += 1
    return total


SIGNAL_MAP = {
    "0": "abcefg",
    "1": "cf",
    "2": "acdeg",
    "3": "acdfg",
    "4": "bcdf",
    "5": "abdfg",
    "6": "abdefg",
    "7": "acf",
    "8": "abcdefg",
    "9": "abcdfg",
}


@functools.cache
def sort_str(s: str) -> str:
    return "".join(sorted(c for c in s))


def part_2(displays: tuple[tuple[tuple[str], tuple[str]]]):
    total = 0
    possible_signals = set(SIGNAL_MAP.values())
    # print(f"Possible signals: {possible_signals}")
    signal_to_num = {v: k for k, v in SIGNAL_MAP.items()}
    # print(f"Signal to number: {signal_to_num}")

    for options, signals in displays:
        for perm in itertools.permutations("abcdefg"):
            tmap = str.maketrans("".join(perm), "abcdefg")
            if all(
                sort_str(option.translate(tmap)) in possible_signals
                for option in options
            ):
                translated_signals = [
                    sort_str(signal.translate(tmap)) for signal in signals
                ]
                num = "".join(signal_to_num[ts] for ts in translated_signals)
                # print(f"Displayed Number: {num}")
                total += int(num)
                break  # no need to try any more permutations for this display

    return total
