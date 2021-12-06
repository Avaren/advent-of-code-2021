from typing import Dict


def parse_file(file_name: str) -> Dict[int, int]:
    with open(f"advent-of-code-2021/day_6/{file_name}") as f:
        fish = sorted(int(i) for i in f.read().split(","))
        return {i: fish.count(i) for i in range(9)}


def more_fish(starting_fish: Dict[int, int], days: int) -> Dict[int, int]:
    fish = starting_fish.copy()
    for _ in range(days):
        fish = {i: fish[(i + 1) % 9] for i in range(9)}
        fish[6] += fish[8]  # BABY FISH
    return fish


def part_1(fish: Dict[int, int]):
    return sum(more_fish(fish, 80).values())


def part_2(fish: Dict[int, int]):
    return sum(more_fish(fish, 256).values())
