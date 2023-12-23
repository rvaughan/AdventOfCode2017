#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 23 of the Advent of Code for 2023.
"""
from collections import defaultdict
import sys


def calculate_solution(data):

    edges = defaultdict(set)
    for r, row in enumerate(data):
        for c, v in enumerate(row):
            if v == ".":
                for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    ar, ac = r + dr, c + dc
                    if not (0 <= ar < len(data) and 0 <= ac < len(row)):
                        continue
                    if data[ar][ac] == ".":
                        edges.setdefault((r, c), set()).add((ar, ac))
                        edges.setdefault((ar, ac), set()).add((r, c))
            if v == ">":
                edges.setdefault((r, c), set()).add((r, c + 1))
                edges.setdefault((r, c - 1), set()).add((r, c))
            if v == "v":
                edges.setdefault((r, c), set()).add((r + 1, c))
                edges.setdefault((r - 1, c), set()).add((r, c))

    n, m = len(data), len(data[0])

    q = [(0, 1, 0)]
    visited = set()
    longest = 0
    while q:
        r, c, d = q.pop()
        if d == -1:
            visited.remove((r, c))
            continue
        if (r, c) == (n - 1, m - 2):
            longest = max(longest, d)
            continue
        if (r, c) in visited:
            continue
        visited.add((r, c))
        q.append((r, c, -1))
        for ar, ac in edges[(r, c)]:
            q.append((ar, ac, d + 1))

    return longest


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'))

    print()
    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""
result = run_test(test_list, 94)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data)

    print(f'Solution is {answer}')
