import pytest

from .day_7 import part_1, part_2, parse_file


@pytest.mark.parametrize(
    "test_input_file,expected", [("test_data", 37), ("data", 340052)]
)
def test_part1(test_input_file, expected):
    assert part_1(parse_file(test_input_file)) == expected


@pytest.mark.parametrize(
    "test_input_file,expected", [("test_data", 168), ("data", 92948968)]
)
def test_part2(test_input_file, expected):
    assert part_2(parse_file(test_input_file)) == expected
