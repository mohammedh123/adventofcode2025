from operator import indexOf


banks = []
with open("input") as f:
    banks = [list(map(int, line.strip())) for line in f.readlines()]


def part1() -> None:
    ans = 0
    for bank in banks:
        maxima_from_right = [0] * len(bank)

        for i in range(len(bank) - 2, -1, -1):
            maxima_from_right[i] = max(bank[i + 1], maxima_from_right[i + 1])

        best_joltage = -1
        for i, battery in enumerate(bank[:-1]):
            best_joltage = max(best_joltage, battery * 10 + maxima_from_right[i])

        ans += best_joltage

    return ans


def part2() -> None:
    ans = 0

    for bank in banks:
        # get the max in the remaining prefix
        # e.g. we need 12 digits, so skip the last 11 digits of the bank,
        # and get the max of the remainder (aka the remaining prefix)
        # 9 6 7 6 [5 4 3 2 1 1 1 1 1 1 1] <-- get the max of [9,6,7,6]
        # rinse and repeat this with fewer digits each time, with the remaining digits
        final_joltage = ""
        prefix_start = 0

        for remaining_digits in range(12, 0, -1):
            if remaining_digits == len(bank[prefix_start:]):
                # just take the rest if we dont have enough to make choices
                final_joltage += "".join(map(str, bank[prefix_start:]))
                prefix_start = len(bank)
                break

            prefix_length = len(bank) - prefix_start - remaining_digits + 1
            joltage = max(bank[prefix_start : prefix_start + prefix_length])
            joltage_idx = bank.index(joltage, prefix_start)

            final_joltage += str(joltage)
            prefix_start = joltage_idx + 1

        assert len(final_joltage) == 12
        ans += int(final_joltage)

    return ans


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
