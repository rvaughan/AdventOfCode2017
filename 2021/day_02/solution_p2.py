#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 2 of the Advent of Code for 2021.
"""

import sys


def move(cur_h_pos, cur_depth, cur_aim, command):
    cmd = command.split(' ')

    if cmd[0] == 'forward':
        cur_h_pos += int(cmd[1])
        cur_depth += (cur_aim * int(cmd[1]))
    elif cmd[0] == 'down':
        cur_aim += int(cmd[1])
    elif cmd[0] == 'up':
        cur_aim -= int(cmd[1])

    return cur_h_pos, cur_depth, cur_aim


def calculate_solution(commands):
    h_pos = 0
    depth = 0
    aim = 0

    for cmd in commands:
        h_pos, depth, aim = move(h_pos, depth, aim, cmd)

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

a = 0
p = 0
d = 0

p,d,a = move(p,d,a,"forward 5")
assert p == 5
assert a == 0
assert d == 0

p,d,a = move(p,d,a,"down 5")
assert p == 5
assert a == 5

p,d,a = move(p,d,a,"forward 8")
assert p == 13, p
assert a == 5, a
assert d == 40, d

p,d,a = move(p,d,a,"up 3")
assert a == 2

p,d,a = move(p,d,a,"down 8")
assert a == 10

p,d,a = move(p,d,a,"forward 2")
assert p == 15
assert a == 10
assert d == 60

test_list = ["forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2"]

result = run_test(test_list, 900)

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
