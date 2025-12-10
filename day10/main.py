from collections import defaultdict, deque
from dataclasses import dataclass
import re
import bitarray
import scipy
import scipy.optimize


@dataclass
class Machine:
    light_diagram: bitarray.bitarray
    wiring_schematics: list[tuple[int]]
    joltage_requirements: tuple[int]

    def __post_init__(self):
        self.buttons_by_index = defaultdict(set)
        for idx, buttons in enumerate(self.wiring_schematics):
            for button_idx in buttons:
                self.buttons_by_index[button_idx].add(buttons)

        a = 2340803


machines: list[Machine] = []
input_re = r"^\[(.*)\](.*)\{(.*)\}"
with open("input") as f:
    for line in f.readlines():
        lights, wires_str, joltage_str = re.match(input_re, line).groups()
        wires = [tuple(map(int, l[1:-1].split(","))) for l in wires_str.strip().split()]

        machines.append(
            Machine(
                bitarray.bitarray(lights.replace(".", "0").replace("#", "1")),
                wires,
                tuple(map(int, joltage_str.split(","))),
            )
        )


def part1():
    ans = 0

    def _process_machine(machine: Machine):
        cache = set()
        queue: deque[bitarray.frozenbitarray] = deque(
            [bitarray.frozenbitarray(len(machine.joltage_requirements))]
        )
        button_presses = 0

        while queue:
            queue_len = len(queue)

            for _ in range(queue_len):
                current_state = queue.popleft()
                if current_state in cache:
                    continue

                if current_state == machine.light_diagram:
                    return button_presses

                cache.add(current_state)

                for lights_to_flip in machine.wiring_schematics:
                    new_state = bitarray.bitarray(current_state)
                    for idx in lights_to_flip:
                        new_state.invert(idx)
                    queue.append(bitarray.frozenbitarray(new_state))

            button_presses += 1

    # BFS with cache
    for machine in machines:
        ans += _process_machine(machine)

    return ans


def part2():
    ans = 0

    # Basically just a set of equations that looks like:
    # p1, p2, .., pn = number of button presses for button n
    # joltageN = b1*p1 + b2*p2 ... + bnpn
    # where the bn coefficients are a 0/1 per button for whether or not light N gets toggled by hitting that button
    # e.g. for the first example:
    # [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    # its basically:
    # 0*p1 + 0*p2 + 0*p3 + 0*p4 + 1*p5 + 1*p6 = 3
    #   buttons 5 and 6 are the only ones that toggle light 0, so a coefficient of 1
    #   the others have a coefficient of 0 to nullify them
    # p2 + p6 = 5       buttons 2 and 6 are the only ones that toggle light 1
    # p3 + p4 + p5 = 4  etc
    # p1 + p2 + p4 = 7  etc
    # minimize sum(p1 + p2 + ... pn)

    iteration_count = 0
    for machine in machines:
        num_buttons = len(machine.wiring_schematics)
        button_coefficients = [
            [i in b for b in machine.wiring_schematics]
            for i in range(len(machine.joltage_requirements))
        ]
        res = scipy.optimize.milp(
            [1] * num_buttons,
            constraints=scipy.optimize.LinearConstraint(
                button_coefficients,
                machine.joltage_requirements,
                machine.joltage_requirements,
            ),
            integrality=[1] * num_buttons,
        )
        print(res.fun, res.message)
        ans += round(res.fun)
    return ans


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
