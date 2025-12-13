from dataclasses import dataclass


@dataclass
class Shape:
    visual_area: list[str]

    def __post_init__(self):
        self.area = 0
        for row in self.visual_area:
            self.area += row.count("#")


shapes: list[Shape] = []
tree_areas = []
with open("input") as f:
    while line := f.readline():
        if "x" in line:
            dimensions, counts_needed_str = line.split(":")
            tree_areas.append(
                (
                    tuple(map(int, dimensions.split("x"))),
                    list(map(int, counts_needed_str.strip().split())),
                )
            )
        elif ":" in line:
            rows = []
            while line := f.readline().strip():
                rows.append(line)
            shapes.append(Shape(rows))


def part1():
    ans = 0

    # Apparently this is the only check you need
    # since I tried it and it passed
    for (w, h), counts_needed in tree_areas:
        available_area = w * h

        can_fit = True
        required_area = 0
        for i, count in enumerate(counts_needed):
            required_area += count * shapes[i].area

        if required_area > available_area:
            can_fit = False

        if can_fit:
            ans += 1

    return ans


def part2():
    pass


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
