#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 17 of the Advent of Code for 2015.
"""


def generate_combinations(containers, goal, used=()):
    if goal == 0:
        yield used
    else:
        for i, container in enumerate(containers):
            if container <= goal:
                yield from generate_combinations(
                    containers[i + 1:],
                    goal - container,
                    used + (container,)
                )


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

containers = """20
15
10
5
5"""

containers = tuple([int(line) for line in containers.splitlines()])

combinations = list(generate_combinations(containers, 25))

shortest = min(len(combination) for combination in combinations)

assert len(combinations) == 4

assert shortest == 2

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual data now.

with open("input.txt", "r") as f:
    containers = tuple([int(line) for line in f])

    combinations = list(generate_combinations(containers, 150))

    shortest = min(len(combination) for combination in combinations)

    count = sum([1 if len(combination) == shortest else 0 for combination in combinations])

    print("Solution: min is {}, with {} combinations".format(shortest, count))
