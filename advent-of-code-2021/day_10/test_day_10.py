import pytest

from .day_10 import part_1, part_2, parse_file


@pytest.mark.parametrize(
    "test_input_file,expected", [("test_data", 26397), ("data", 367059)]
)
def test_part1(test_input_file, expected):
    assert part_1(parse_file(test_input_file)) == expected


@pytest.mark.parametrize(
    "test_input_file,expected", [("test_data", 288957), ("data", 1952146692)]
)
def test_part2(test_input_file, expected):
    assert part_2(parse_file(test_input_file)) == expected
