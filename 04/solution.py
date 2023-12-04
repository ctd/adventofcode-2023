#!/usr/bin/env python

import re
import math


class Card:
    def __init__(self, line):
        self.id = int(re.findall(r"Card\s+(\d+):", line)[0])
        _, numbers = line.split(": ")
        winning_numbers, numbers_have = numbers.split(" | ")
        self.winning_numbers = self._parse_numbers(winning_numbers)
        self.numbers_have = self._parse_numbers(numbers_have)

    def _parse_numbers(self, line):
        return set(int(x) for x in re.findall(r"\d+", line))

    def matches(self):
        return len(self.winning_numbers & self.numbers_have)

    def points(self):
        matches = self.matches()
        if matches == 0:
            return 0
        return int(math.pow(2, matches - 1))


def part1(puzzle):
    return sum(Card(line).points() for line in puzzle.splitlines())


def part2(puzzle):
    cards = [Card(line) for line in puzzle.splitlines()]
    cards_in_hand = {}
    for card in cards:
        cards_in_hand[card.id] = cards_in_hand.get(card.id, 1)
        if card.id not in cards_in_hand:
            cards_in_hand[card.id] = 1
        for i in range(card.id + 1, card.id + card.matches() + 1):
            cards_in_hand[i] = cards_in_hand.get(i, 1) + cards_in_hand.get(card.id)
    return sum(cards_in_hand.values())


def test():
    SAMPLE = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    assert part1(SAMPLE) == 13
    assert part2(SAMPLE) == 30


def main():
    test()
    puzzle = open("input").read()
    print("Part 1:", part1(puzzle))
    print("Part 2:", part2(puzzle))


if __name__ == "__main__":
    main()
