#!/usr/bin/env python

import re
import math

BAG_CONTENTS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def game_possible(line):
    for k, v in BAG_CONTENTS.items():
        counts = (int(c) for c in re.findall(r"(\d+) {}".format(k), line))
        if max(counts) > v:
            return False
    return True


def min_contents(line):
    res = {}
    for k in BAG_CONTENTS.keys():
        counts = (int(c) for c in re.findall(r"(\d+) {}".format(k), line))
        res[k] = max(counts)
    return res


def cube_set_power(line):
    return math.prod(min_contents(line).values())


def part1(input):
    s = 0
    for line in input.splitlines():
        if game_possible(line):
            game_id = re.search(r"Game (\d+):", line).group(1)
            s += int(game_id)
    return s


def part2(input):
    return sum(cube_set_power(line) for line in input.splitlines())


def test():
    SAMPLE = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    assert part1(SAMPLE) == 8
    assert part2(SAMPLE) == 2286


def main():
    test()
    input = open("input", "r").read()
    print("Part 1: {}".format(part1(input)))
    print("Part 2: {}".format(part2(input)))


if __name__ == "__main__":
    main()
