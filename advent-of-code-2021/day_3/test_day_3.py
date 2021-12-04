from .day_3 import part_1, part_2

TEST_DATA = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def load_data():
    with open("advent-of-code-2021/day_3/data") as data:
        return [line.strip() for line in data]


def test_part1():
    assert part_1(TEST_DATA) == 198
    assert part_1(load_data()) == 3009600


def test_part2():
    assert part_2(TEST_DATA) == 230
    assert part_2(load_data()) == 6940518
