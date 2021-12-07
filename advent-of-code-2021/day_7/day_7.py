from typing import Tuple


def parse_file(file_name: str) -> Tuple[int]:
    with open(f"advent-of-code-2021/day_7/{file_name}") as f:
        return tuple(int(i) for i in f.read().split(","))


def part_1(crabs: Tuple[int]):
    return min(
        sum(abs(target - crab) for crab in crabs) for target in range(max(crabs))
    )


def part_2(crabs: Tuple[int]):
    return min(
        sum(abs(target - crab) * (abs(target - crab) + 1) // 2 for crab in crabs)
        for target in range(max(crabs))
    )
