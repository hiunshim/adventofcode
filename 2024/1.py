import sys
from collections import Counter


def part1(data):
    print(
        "Part 1: ",
        sum(
            abs(left - right)
            for left, right in zip(
                *map(
                    sorted,
                    zip(*(map(int, location) for location in data)),
                )
            )
        ),
    )


def part2(data):
    print(
        "Part 2: ",
        sum(
            Counter(right for _, right in data)[left] * left
            for left, _ in data
        ),
    )


def main():
    data = [
        (int(left), int(right))
        for left, right in (location.strip().split() for location in sys.stdin)
    ]
    part1(data)
    part2(data)


if __name__ == "__main__":
    main()
