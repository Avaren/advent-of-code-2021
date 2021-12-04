from .day_2 import part_1, part_2

TEST_DATA = [('forward', 5), ('down', 5), ('forward', 8), ('up', 3), ('down', 8), ('forward', 2)]


def load_data():
    def fmt(l: str):
        dir, amt = l.split(' ')
        return dir, int(amt)

    with open('advent-of-code-2021/day_2/data') as data:
        return [fmt(line.strip()) for line in data]


def test_part1():
    assert part_1(TEST_DATA) == 150
    assert part_1(load_data()) == 1882980


def test_part2():
    assert part_2(TEST_DATA) == 900
    assert part_2(load_data()) == 1971232560
