ingredient_id_ranges = []
ingredient_ids = set()

with open("input") as f:
    while line := f.readline().strip():
        range_start, range_end = list(map(int, line.split("-")))
        ingredient_id_ranges.append((range_start, range_end))
    while line := f.readline().strip():
        ingredient_ids.add(int(line))


def part1() -> None:
    ans = 0

    for ingredient_id in ingredient_ids:
        for range_start, range_end in ingredient_id_ranges:
            if range_start <= ingredient_id <= range_end:
                ans += 1
                break

    return ans


def part2() -> None:
    ans = 0

    ingredient_id_ranges.sort()
    merged_ranges = [ingredient_id_ranges[0]]
    for range_start, range_end in ingredient_id_ranges:
        prev_start, prev_end = merged_ranges[-1]
        if range_start >= prev_start and range_start <= prev_end:
            merged_ranges[-1] = (prev_start, max(prev_end, range_end))
        else:
            merged_ranges.append((range_start, range_end))

    for range_start, range_end in merged_ranges:
        ans += range_end - range_start + 1

    return ans


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
