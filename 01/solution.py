import re

NUMBERS = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def calibration_value(line, part2=False):
    matches = (
        re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
        if part2
        else re.findall(r"(\d)", line)
    )
    digits = tuple(NUMBERS[m] for m in matches)
    return (digits[0] * 10) + digits[-1]


def solve(input, part2=False):
    return sum(calibration_value(line, part2) for line in input)


def tests():
    p1 = {
        "1abc2": 12,
        "pqr3stu8vwx": 38,
        "a1b2c3d4e5f": 15,
        "treb7uchet": 77,
    }
    p2 = {
        "two1nine": 29,
        "eightwothree": 83,
        "abcone2threexyz": 13,
        "xtwone3four": 24,
        "4nineeightseven2": 42,
        "zoneight234": 14,
        "7pqrstsixteen": 76,
    }

    for k, v in p1.items():
        assert calibration_value(k) == v
    for k, v in p2.items():
        assert calibration_value(k, part2=True) == v

    assert solve(p1.keys()) == 142
    assert solve(p2.keys(), part2=True) == 281

    assert calibration_value("oneight", part2=True) == 18


def main():
    tests()
    input = open("input", "r").read().splitlines()
    print("Part 1: {}".format(solve(input)))
    print("Part 2: {}".format(solve(input, part2=True)))


if __name__ == "__main__":
    main()
