with open("input") as f:
    s = f.readline()
    ranges = list(
        map(lambda pid_range: list(map(int, pid_range.split("-"))), s.split(","))
    )


def part1() -> None:
    def is_invalid_id(s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        l, r = 0, len(s) // 2
        while r < len(s):
            if s[l] != s[r]:
                return False
            l += 1
            r += 1

        return True

    ans = 0

    for range_start, range_end in ranges:
        for i in range(range_start, range_end + 1):
            if is_invalid_id(str(i)):
                ans += i

    return ans


def part2() -> None:
    ans = 0

    for range_start, range_end in ranges:
        for i in range(range_start, range_end + 1):
            # for each number
            # check each substring to see if it's fully repeatable
            _id = str(i)

            for substr_len in range(1, len(_id)):
                if len(_id) % substr_len != 0:
                    continue

                idx = 0
                substr = _id[0:substr_len]
                substr_start = idx + substr_len
                is_invalid_id = True
                while substr_start + substr_len <= len(_id):
                    if _id[substr_start : substr_start + substr_len] != substr:
                        is_invalid_id = False
                        break

                    substr_start += substr_len

                if is_invalid_id:
                    ans += i
                    break

    return ans


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
