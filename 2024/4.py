import sys


def part1(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]
    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def find_xmas(x, y, dx, dy):
        for i in range(4):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != "XMAS"[i]:
                return False
        return True

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if find_xmas(i, j, dx, dy):
                    count += 1

    return count


def part2(grid):
    rows = len(grid)
    cols = len(grid[0])
    RIGHT_TOP = (-1, 1)
    RIGHT_BOTTOM = (1, 1)
    LEFT_BOTTOM = (1, -1)
    LEFT_TOP = (-1, -1)
    MAS = "MAS"
    SAM = "SAM"
    directions = [RIGHT_TOP, RIGHT_BOTTOM, LEFT_BOTTOM, LEFT_TOP]
    DIAG = (LEFT_TOP, (0, 0), RIGHT_BOTTOM)
    ANTI_DIAG = (LEFT_BOTTOM, (0, 0), RIGHT_TOP)
    REV_DIAG = DIAG[::-1]
    REV_ANTI_DIAG = ANTI_DIAG[::-1]
    patterns = [DIAG, ANTI_DIAG, REV_DIAG, REV_ANTI_DIAG]
    count = 0

    def neighbors(x, y):
        for direction in directions:
            yield x + direction[0], y + direction[1]

    def is_valid(x, y):
        return all(
            0 <= nx < rows and 0 <= ny < cols for nx, ny in neighbors(x, y)
        )

    def match_xmas(x, y):
        for p in patterns:
            c1, c2 = p[0]
            c3, c4 = p[1]
            c5, c6 = p[2]
            mas = (
                grid[x + c1][y + c2]
                + grid[x + c3][y + c4]
                + grid[x + c5][y + c6]
            )
            if not (mas == MAS or mas == SAM):
                return False
        return True

    def find_xmas(x, y):
        if not is_valid(x, y) or not match_xmas(x, y):
            return False
        return True

    for i in range(rows):
        for j in range(cols):
            if find_xmas(i, j):
                count += 1

    return count


def main():
    data = list(line for line in sys.stdin)
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))


if __name__ == "__main__":
    main()
