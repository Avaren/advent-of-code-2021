import pytest

from .day_8 import part_1, part_2, parse_file


@pytest.mark.parametrize(
    "test_input_file,expected", [("test_data", 0), ("test_data2", 26), ("data", 409)]
)
def test_part1(test_input_file, expected):
    assert part_1(parse_file(test_input_file)) == expected


@pytest.mark.parametrize(
    "test_input_file,expected",
    [("test_data", 5353), ("test_data2", 61229), ("data", 1024649)],
)
def test_part2(test_input_file, expected):
    assert part_2(parse_file(test_input_file)) == expected
