coordinates = []

with open("input") as f:
    coordinates = [tuple(map(int, l.strip().split(","))) for l in f.readlines()]


def part1():
    ans = 0

    for x1, y1 in coordinates:
        for x2, y2 in coordinates[1:]:
            ans = max(ans, (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1))

    return ans


def part2():
    # Loop through all rectangles sorted by area, if any segments intersect (sorted by length, to handle the rectangle middle) or are inside, then
    # this is not a valid pair of coordinates
    rects = []
    segments = []
    for i, (x1, y1) in enumerate(coordinates):
        for x2, y2 in coordinates[i + 1 :]:
            rects.append(((abs(x2 - x1) + 1) * (abs(y2 - y1) + 1), (x1, y1), (x2, y2)))

        x2, y2 = coordinates[(i + 1) % len(coordinates)]
        length_sq = (x2 - x1) ** 2 + (y2 - y1) ** 2
        segments.append((length_sq, (x1, y1), (x2, y2)))

    rects.sort(reverse=True)
    segments.sort(reverse=True)

    for area, (r1_x, r1_y), (r2_x, r2_y) in rects:
        intersects = False
        for _, (x1, y1), (x2, y2) in segments:
            rect_xmin = min(r1_x, r2_x)
            rect_xmax = max(r1_x, r2_x)
            rect_ymin = min(r1_y, r2_y)
            rect_ymax = max(r1_y, r2_y)

            if not (
                max(x1, x2) <= rect_xmin
                or rect_xmax <= min(x1, x2)
                or max(y1, y2) <= rect_ymin
                or rect_ymax <= min(y1, y2)
            ):
                intersects = True
                break

        if not intersects:
            print(f"Match: {(r1_x, r1_y)}, {(r2_x, r2_y)}")
            return area


print(part1())
print(part2())
