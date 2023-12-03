#!/usr/bin/env python

from functools import lru_cache
from collections import namedtuple
import math

Point = namedtuple("Point", "x y")
Digits = namedtuple("Digits", "y start_x end_x value")

def find_digits(line, y):
    digits = []
    start_i, end_i, chars = None, None, ""
    for i, c in enumerate(line):
        if c.isdigit():
            if start_i is None:
                start_i = i
            chars += c
            end_i = i
        else:
            if start_i is not None:
                digits.append(Digits(y, start_i, end_i, int(chars)))
                start_i, end_i, chars = None, None, ""
    if start_i is not None:
        digits.append(Digits(y, start_i, end_i, int(chars)))
    return digits


# Lazy runtime optimisation
@lru_cache(maxsize=None)
def adjacent_points(digits: Digits):
    points = set()
    for y in range(digits.y - 1, digits.y + 2):
        for x in range(digits.start_x - 1, digits.end_x + 2):
            if y == digits.y and x >= digits.start_x and x <= digits.end_x:
                continue
            points.add(Point(x, y))
    return points


def is_symbol(c):
    return c != "." and not c.isdigit()


def part1(puzzle):
    s = 0
    lines = puzzle.splitlines()
    for y, line in enumerate(lines):
        digits = find_digits(line, y)
        for digit in digits:
            for point in adjacent_points(digit):
                if (
                    point.y < 0
                    or point.y >= len(lines)
                    or point.x < 0
                    or point.x >= len(lines[point.y])
                ):
                    continue
                if is_symbol(lines[point.y][point.x]):
                    s += digit.value
                    continue
    return s


def part2(puzzle):
    s = 0
    lines = puzzle.splitlines()
    digits = []
    gears = set()
    for y, line in enumerate(lines):
        digits += find_digits(line, y)
        for x, c in enumerate(line):
            if c == "*":
                gears.add(Point(x, y))
    for gear in gears:
        matches = []
        for digit in digits:
            if gear in adjacent_points(digit):
                matches.append(digit)
        if len(matches) > 1:
            s += math.prod(m.value for m in matches)
            continue
    return s


def test():
    SAMPLE = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    assert part1(SAMPLE) == 4361
    assert part2(SAMPLE) == 467835


def main():
    test()
    puzzle = open("input").read()
    print("Part 1:", part1(puzzle))
    print("Part 2:", part2(puzzle))


if __name__ == "__main__":
    main()
