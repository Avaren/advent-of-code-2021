from .day_4 import part_1, part_2, parse_file

TEST_DATA = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']


def test_part1():
    assert part_1(*parse_file('test_data')) == 4512
    assert part_1(*parse_file('data')) == 2745


def test_part2():
    assert part_2(*parse_file('test_data')) == 1924
    assert part_2(*parse_file('data')) == 6594
