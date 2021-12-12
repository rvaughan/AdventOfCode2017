#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 12 of the Advent of Code for 2021.
"""

import sys
from collections import defaultdict, deque


def follow_path(cave_map, moves, path):
    paths = []
    for move in moves:
        if move == 'start':
            continue

        if move.isupper() or move not in path:
            p = path.copy()
            p.append(move)

            if move != 'end':            
                found = follow_path(cave_map, cave_map[move], p)
                if len(found) > 0:
                    paths += found
            else:
                paths.append(p)

    return paths


def find_paths(cave_map):
    sp = cave_map['start']

    path = ['start']

    paths = follow_path(cave_map, sp, path)

    return paths


def calculate_solution(input_data):
    cave_map = {}

    for steps in input_data:
        s,e = steps.split('-')
        if s not in cave_map:
            cave_map[s] = []
        cave_map[s].append(e)

        # Paths are bidirectional
        if e not in cave_map:
            cave_map[e] = []
        cave_map[e].append(s)

    paths = find_paths(cave_map)

    return len(paths)


def run_test(test_input, expected_value):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    input_vals = [line.strip() for line in test_input.split('\n')]
    result = calculate_solution(input_vals)

    if result != expected_value:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_value}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_input="""start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
result = run_test(test_input, 10)

test_input="""dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""
result = run_test(test_input, 19)

test_input="""fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""
result = run_test(test_input, 226)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    answer = calculate_solution([item.strip() for item in f])

    print(f'Solution is {answer}')
