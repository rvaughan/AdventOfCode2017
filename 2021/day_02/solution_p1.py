#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 2 of the Advent of Code for 2021.
"""

import sys


def move(cur_h_pos, cur_depth, command):
    cmd = command.split(' ')

    if cmd[0] == 'forward':
        cur_h_pos += int(cmd[1])
    elif cmd[0] == 'down':
        cur_depth += int(cmd[1])
    elif cmd[0] == 'up':
        cur_depth -= int(cmd[1])

    return cur_h_pos, cur_depth


def calculate_solution(commands):
    h_pos = 0
    depth = 0

    for cmd in commands:
        h_pos, depth = move(h_pos, depth, cmd)

    return h_pos * depth


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input)

    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = ["forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2"]

result = run_test(test_list, 150)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data = [line for line in f]
    answer = calculate_solution(input_data)

    print(f'Solution is {answer}')
