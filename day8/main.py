from collections import defaultdict
from heapq import heapify, heappop, heappush, heappushpop
from math import prod


positions = None
with open("input") as f:
    positions = [tuple(map(int, l.strip().split(","))) for l in f.readlines()]


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = set(range(n))

    def find(self, n):
        root = n
        while root != self.parent[root]:
            root = self.parent[root]

        while n != root:
            nxt = self.parent[n]
            self.parent[n] = root
            n = nxt

        return root

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)

        if i == j:
            return False

        if self.size[i] < self.size[j]:
            i, j = j, i
        self.parent[j] = i
        self.size[i] += self.size[j]
        self.components.remove(j)

        return True

    def n_largest_sizes(self, n):
        heap = []

        for i in self.components:
            p = self.find(i)
            if len(heap) < n:
                heappush(heap, (self.size[p], i))
            else:
                heappushpop(heap, (self.size[p], i))

        return [size for size, _ in heap]


distances = {}
adj_list = defaultdict(set)

for i in range(len(positions)):
    adj_list[i].add(i)
    for j in range(i + 1, len(positions)):
        dist_sq = (
            (positions[j][0] - positions[i][0]) ** 2
            + (positions[j][1] - positions[i][1]) ** 2
            + (positions[j][2] - positions[i][2]) ** 2
        )

        distances[i, j] = dist_sq


def part1(num_connections_to_make: int) -> None:
    dj = DisjointSet(len(positions))

    # Form a min heap of the distances to begin connecting
    distances_heap = [(v, k) for k, v in distances.items()]

    heapify(distances_heap)
    connected = 0
    while connected < num_connections_to_make and (val := heappop(distances_heap)):
        _, (i, j) = val

        dj.union(i, j)

        connected += 1

    return prod(dj.n_largest_sizes(3))


def part2() -> None:
    dj = DisjointSet(len(positions))

    # Form a min heap of the distances to begin connecting
    distances_heap = [(v, k) for k, v in distances.items()]

    heapify(distances_heap)
    last_connection_made = []
    while distances_heap and (val := heappop(distances_heap)):
        _, (i, j) = val

        if dj.union(i, j):
            last_connection_made = (positions[i], positions[j])

    return last_connection_made[0][0] * last_connection_made[1][0]


print(f"Part 1: {part1(1000)}")
print(f"Part 2: {part2()}")
