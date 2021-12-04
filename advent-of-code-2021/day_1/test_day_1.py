from .day_1 import part_1, part_2

TEST_DATA = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def load_data():
    with open("advent-of-code-2021/day_1/data") as data:
        return [int(depth.strip()) for depth in data]


def test_part1():
    assert part_1(TEST_DATA) == 7
    assert part_1(load_data()) == 1387


def test_part2():
    assert part_2(TEST_DATA) == 5
    assert part_2(load_data()) == 1362
