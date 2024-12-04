import sys
import re


def mul(x, y):
    return x * y


def part1(text, mul_regex):
    matches = re.findall(mul_regex, text)
    return sum(eval(eq) for eq in matches)


def part2(text, mul_regex, do_regex):
    new_text_list = []
    do = True
    for match in re.split(do_regex, text):
        if match == "do()":
            do = True
        elif match == "don't()":
            do = False
        elif do:
            new_text_list.append(match)
    return part1("".join(new_text_list), mul_regex)


def main():
    data = sys.stdin.read()
    mul_regex = r"mul\(\d{1,3},\d{1,3}\)"
    do_regex = r"(do\(\)|don't\(\))"
    print("Part 1: ", part1(data, mul_regex))
    print("Part 2: ", part2(data, mul_regex, do_regex))


if __name__ == "__main__":
    main()
