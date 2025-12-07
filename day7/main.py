from collections import defaultdict


grid = []
splitter_xs_by_y = defaultdict(set)
start_loc = None
with open("input") as f:
    grid.extend([l.strip() for l in f.readlines()])

for y in range(len(grid)):
    for x in range(len(grid[y])):
        match grid[y][x]:
            case "^":
                splitter_xs_by_y[y].add(x)
            case "S":
                start_loc = (x, y)


def part1() -> None:
    ans = 0
    laser_xs = set([start_loc[0]])
    laser_y = start_loc[1] + 1
    h = len(grid)

    while laser_y < h - 1:
        laser_y += 1
        new_laser_xs = set()
        if not splitter_xs_by_y[laser_y]:
            continue

        for x in laser_xs:
            hit_splitter = False
            for splitter_x in splitter_xs_by_y[laser_y]:
                if x == splitter_x:
                    new_laser_xs.add(splitter_x - 1)
                    new_laser_xs.add(splitter_x + 1)
                    hit_splitter = True

            if not hit_splitter:
                new_laser_xs.add(x)
            else:
                ans += 1

        laser_xs = new_laser_xs

    return ans


def part2() -> None:
    ans = 1
    laser_xs = defaultdict(int)
    laser_xs[start_loc[0]] = 1
    laser_y = start_loc[1] + 1
    h = len(grid)

    while laser_y < h:
        laser_y += 1
        new_laser_xs = defaultdict(int)
        if not splitter_xs_by_y[laser_y]:
            continue

        for x, count in laser_xs.items():
            hit_splitter = False
            for splitter_x in splitter_xs_by_y[laser_y]:
                if x == splitter_x:
                    new_laser_xs[splitter_x - 1] += count
                    new_laser_xs[splitter_x + 1] += count
                    hit_splitter = True

            if not hit_splitter:
                new_laser_xs[x] += count
            else:
                ans += count

        laser_xs = new_laser_xs

    assert ans == sum(laser_xs.values())
    return ans


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
