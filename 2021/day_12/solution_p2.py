#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 12 of the Advent of Code for 2021.
"""

from os import X_OK
import sys
from collections import defaultdict, deque


def counted(move, path):
    # Only need to care about little caves
    if move.islower():
        for key, value in path.items():
            # Have we already seen one of the little caves twice?
            if key.islower() and value == 2:
                return True

    return False


def follow_path(cave_map, moves, path):
    paths = []
    for move in moves:
        if move == 'start':
            continue

        p = path.copy()
        if move == 'end':
            p[move] += 1
            paths.append(p)
        else:
            # Little cave?
            if move.islower():
                # Have we already seen it twice, or seen another litte cave twice?
                if p[move] >= 1 and counted(move, p):
                    continue
        
            p[move] += 1

            found = follow_path(cave_map, cave_map[move], p)
            paths += found

    return paths


def find_paths(cave_map):
    sp = cave_map['start']

    path = defaultdict(int)
    path['start'] = 1

    paths = follow_path(cave_map, sp, path)

    # for path in paths:
    #     print(path)
    #     line = ''
    #     for move, _ in path.items():
    #         line += f'{move},'
    #     print(line)

    return paths


def calculate_solution(input_data):
    cave_map = {}

    for steps in input_data:
        s, e = steps.split('-')
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
result = run_test(test_input, 36)

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
result = run_test(test_input, 103)

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
result = run_test(test_input, 3509)

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
