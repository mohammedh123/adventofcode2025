from math import prod


math_problems = []
with open("input") as f:
    lines = f.readlines()

    split_idxs = []
    prev_boundary = -1
    for x in range(len(lines[0])):
        if lines[0][x].isspace():
            boundary_found = True
            for y in range(1, len(lines)):
                if not lines[y][x].isspace():
                    boundary_found = False
                    break

            if boundary_found:
                math_problems.append(
                    [lines[y][prev_boundary + 1 : x] for y in range(len(lines))]
                )
                prev_boundary = x


def part1() -> None:
    ans = 0

    for values in math_problems:
        operator = values[-1].strip()
        operands = [int(s.strip()) for s in values[0:-1]]

        match operator:
            case "*":
                ans += prod(map(int, operands))
            case "+":
                ans += sum(map(int, operands))

    return ans


def part2() -> None:
    ans = 0

    for values in math_problems:
        operator = values[-1].strip()
        operands = []

        max_digits = len(values[0])

        for x in range(max_digits - 1, -1, -1):
            operand = "".join(
                values[y][x] for y in range(len(values) - 1)
            )  # -1 to skip the operator

            operands.append(int(operand.strip()))

        match operator:
            case "*":
                ans += prod(map(int, operands))
            case "+":
                ans += sum(map(int, operands))

    return ans


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
