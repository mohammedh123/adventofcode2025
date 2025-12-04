from copy import deepcopy


input_grid = []
PAPER_ROLL = "@"
EMPTY = "."
with open("input") as f:
    input_grid = [line.strip() for line in f.readlines()]


def part1() -> None:
    ans = 0
    w = len(input_grid[0])
    h = len(input_grid)

    for y in range(h):
        for x in range(w):
            if input_grid[y][x] == EMPTY:
                continue

            neighboring_rolls = 0

            for y_offset in (-1, 0, 1):
                for x_offset in (-1, 0, 1):
                    new_y = y + y_offset
                    new_x = x + x_offset
                    if (
                        y_offset == x_offset == 0
                        or new_y < 0
                        or new_y >= h
                        or new_x < 0
                        or new_x >= w
                    ):
                        continue
                    if input_grid[new_y][new_x] == PAPER_ROLL:
                        neighboring_rolls += 1

            if neighboring_rolls < 4:
                ans += 1

    return ans


def part2() -> None:
    ans = 0

    w = len(input_grid[0])
    h = len(input_grid)
    current_grid = set(
        (x, y) for x in range(w) for y in range(h) if input_grid[y][x] == PAPER_ROLL
    )
    next_grid = set(current_grid)
    num_rolls_removed = -1

    while num_rolls_removed != 0:
        num_rolls_removed = 0
        for x, y in current_grid:
            neighboring_rolls = 0

            for y_offset in (-1, 0, 1):
                for x_offset in (-1, 0, 1):
                    new_y = y + y_offset
                    new_x = x + x_offset
                    if (
                        y_offset == x_offset == 0
                        or new_y < 0
                        or new_y >= h
                        or new_x < 0
                        or new_x >= w
                    ):
                        continue

                    if (new_x, new_y) in current_grid:
                        neighboring_rolls += 1

            if neighboring_rolls < 4:
                next_grid.remove((x, y))
                num_rolls_removed += 1

        ans += num_rolls_removed
        current_grid = next_grid
        next_grid = set(current_grid)

    return ans


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
