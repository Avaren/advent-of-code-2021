import pytest

from .day_9 import part_1, part_2, parse_file


@pytest.mark.parametrize("test_input_file,expected", [("test_data", 15), ("data", 539)])
def test_part1(test_input_file, expected):
    assert part_1(parse_file(test_input_file)) == expected


@pytest.mark.parametrize(
    "test_input_file,expected", [("test_data", 1134), ("data", 736920)]
)
def test_part2(test_input_file, expected):
    assert part_2(parse_file(test_input_file)) == expected
