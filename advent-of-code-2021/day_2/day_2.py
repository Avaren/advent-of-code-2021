import collections
import itertools


def part_1(moves):
    vert, horiz = 0, 0
    for dir, amt in moves:
        match dir:
            case "forward":
                horiz += amt
            case "down":
                vert += amt
            case "up":
                vert -= amt
    return horiz * vert


def part_2(moves):
    vert, horiz, aim = 0, 0, 0
    for dir, amt in moves:
        match dir:
            case "forward":
                horiz += amt
                vert += amt * aim
            case "down":
                aim += amt
            case "up":
                aim -= amt
    return horiz * vert
