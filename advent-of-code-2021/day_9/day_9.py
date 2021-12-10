import math


def parse_file(file_name: str) -> dict[tuple[int, int], int]:
    with open(f"advent-of-code-2021/day_9/{file_name}") as f:
        return {
            (x, y): int(n) for y, l in enumerate(f) for x, n in enumerate(l.strip())
        }


def low_points(heightmap):
    for (x, y), depth in heightmap.items():
        if all(
            depth < heightmap.get((xn, yn), 100)
            for xn, yn in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        ):
            yield (x, y), depth


def part_1(heightmap):
    total = 0
    for (_, _), depth in low_points(heightmap):
        total += 1 + depth
    return total


def map_basin(heightmap, x, y):
    cur_height = heightmap[(x, y)]
    basin = {(x, y)}
    for xn, yn in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        depth = heightmap.get((xn, yn), 9)
        if cur_height < depth < 9:
            basin.update(map_basin(heightmap, xn, yn))
    return basin


def part_2(heightmap):
    basins = []
    for (x, y), _ in low_points(heightmap):
        basin = map_basin(heightmap, x, y)
        # print(len(basin), basin)
        basins.append(len(basin))
    return math.prod(sorted(basins)[-3:])
