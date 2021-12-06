import pytest

from .day_6 import part_1, part_2, parse_file


def test_parse():
    print(parse_file("test_data"))


@pytest.mark.parametrize(
    "test_input_file,expected", [("test_data", 5934), ("data", 377263)]
)
def test_part1(test_input_file, expected):
    assert part_1(parse_file(test_input_file)) == expected


@pytest.mark.parametrize(
    "test_input_file,expected", [("test_data", 26984457539), ("data", 1695929023803)]
)
def test_part2(test_input_file, expected):
    assert part_2(parse_file(test_input_file)) == expected
