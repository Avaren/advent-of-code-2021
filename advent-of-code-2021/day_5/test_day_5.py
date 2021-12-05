from .day_5 import part_1, part_2, parse_file


def test_parse():
    for line in parse_file("test_data"):
        print(
            line, len(line.points), line.isVert() or line.isHoriz(), sorted(line.points)
        )


def test_part1():
    assert part_1(parse_file("test_data")) == 5
    assert part_1(parse_file("data")) == 5632


def test_part2():
    assert part_2(parse_file("test_data")) == 12
    assert part_2(parse_file("data")) == 22213
