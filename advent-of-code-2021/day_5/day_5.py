import functools
from collections import namedtuple
from typing import Generator

VentLine = namedtuple("VentLine", ["x1", "y1", "x2", "y2"])


class VentLine(VentLine):
    def isHoriz(self):
        return self.x1 == self.x2

    def isVert(self):
        return self.y1 == self.y2

    @functools.cached_property
    def points(self):
        if self.isHoriz():
            # MAke y2 biggest
            y1, y2 = (self.y1, self.y2) if self.y2 > self.y1 else (self.y2, self.y1)
            return {(self.x1, y) for y in range(y1, y2 + 1)}
        elif self.isVert():
            x1, x2 = (self.x1, self.x2) if self.x2 > self.x1 else (self.x2, self.x1)
            return {(x, self.y1) for x in range(x1, x2 + 1)}
        else:
            # make x1 -> x2 ascending, reverse line if necessary
            if self.x1 > self.x2:
                x1, x2, y1, y2 = self.x2, self.x1, self.y2, self.y1
            else:
                x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2

            if y1 > y2:
                # Down left
                return {(x1 + i, y1 - i) for i in range(x2 + 1 - x1)}
            else:
                # Down right
                return {(x1 + i, y1 + i) for i in range(x2 + 1 - x1)}


def parse_file(file_name: str) -> Generator[VentLine, None, None]:
    with open(f"advent-of-code-2021/day_5/{file_name}") as f:
        for line in f:
            coords = [int(c) for l in line.split(" -> ") for c in l.split(",")]
            yield VentLine(*coords)


def overlapping(lines: Generator[VentLine, None, None]):
    seen_points = set()
    overlap = set()
    for line in lines:
        overlap.update(
            seen_points.intersection(line.points)
        )  # any points in this line already seen
        seen_points.update(line.points)  # update list of lines

    return len(overlap)


def part_1(lines: Generator[VentLine, None, None]):
    return overlapping(line for line in lines if line.isHoriz() or line.isVert())


def part_2(lines: Generator[VentLine, None, None]):
    return overlapping(lines)
