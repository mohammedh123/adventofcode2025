from collections import defaultdict
from functools import cache


adj_list = defaultdict(list)

with open("input") as f:
    for name, output_str in [l.strip().split(":") for l in f.readlines()]:
        adj_list[name] = output_str.strip().split()


@cache
def dfs(start, end):
    if start == end:
        return 1

    total = 0
    for neighbor in adj_list[start]:
        total += dfs(neighbor, end)

    return total


def part1():
    return dfs("you", "out")


def part2():
    return dfs("dac", "out") * dfs("fft", "dac") * dfs("svr", "fft")


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
