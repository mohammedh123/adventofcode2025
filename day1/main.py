from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    LEFT = 0
    RIGHT = 1


@dataclass
class DialTurn:
    direction: Direction
    magnitude: int


turns = []
with open("input") as f:
    lines = f.readlines()

    for line in lines:
        turns.append(
            DialTurn(
                Direction.LEFT if line[0] == "L" else Direction.RIGHT, int(line[1:])
            )
        )


def part1() -> None:
    ans = 0
    dial_value = 50
    for t in turns:
        mag_constant = -1 if t.direction == Direction.LEFT else 1
        dial_value = (dial_value + (t.magnitude * mag_constant)) % 100

        if dial_value == 0:
            ans += 1

    return ans


def part2() -> None:
    ans = 0
    dial_value = 50
    for t in turns:
        mag_constant = -1 if t.direction == Direction.LEFT else 1
        if t.direction == Direction.LEFT:
            distance_to_zero = dial_value or 100
        else:
            distance_to_zero = 100 - dial_value

        dial_value = (dial_value + (t.magnitude * mag_constant)) % 100

        ans += 1 + (t.magnitude - distance_to_zero) // 100

    return ans


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
