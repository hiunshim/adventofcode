import sys


def part1(reports):
    return sum(_is_safe(report, 0) for report in reports)


def part2(reports):
    return sum(_is_safe(report, 1) for report in reports)


def _is_safe(report, tolerance):
    return _increasing(report, tolerance) or _decreasing(report, tolerance)


def _increasing(report, tolerance):
    offset = tolerance
    for i in range(len(report) - 1):
        if not (
            report[i] < report[i + 1] and _differ(report[i], report[i + 1])
        ):
            tolerance -= 1
            if tolerance < 0:
                return False
            if 0 < i and report[i - offset] > report[i + 1]:
                return False
    return True


def _decreasing(report, tolerance):
    offset = tolerance
    for i in range(len(report) - 1):
        if not (
            report[i] > report[i + 1] and _differ(report[i], report[i + 1])
        ):
            tolerance -= 1
            if tolerance < 0:
                return False
            if 0 < i and report[i - offset] < report[i + 1]:
                return False
    return True


def _differ(current_level, next_level):
    return 1 <= abs(current_level - next_level) <= 3


def main():
    data = list(list(map(int, line.strip().split())) for line in sys.stdin)
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))


if __name__ == "__main__":
    main()
