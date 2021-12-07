#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 7 of the Advent of Code for 2021.
"""

import sys
from collections import defaultdict


def calc_fuel_use(pos, input_data):
    fuel = 0
    for p in input_data:
        fuel += abs(p - pos)

    return fuel


def calculate_solution(input_data):
    max_pos = max(input_data)

    best_pos = 0
    best_fuel = 9999999999
    for pos in range(max_pos):
        fuel = calc_fuel_use(pos, input_data)

        if fuel < best_fuel:
            best_fuel = fuel
            best_pos = pos

    return best_pos, best_fuel


def run_test(test_input, expected_pos, expected_fuel):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    pos, fuel = calculate_solution([int(item) for item in test_input.split(',')])

    if fuel != expected_fuel:
        print(f'Test for {test_input} FAILED. Got a result of {fuel}, not {expected_fuel}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return fuel


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_input = """16,1,2,0,4,2,7,1,2,14"""

score = calc_fuel_use(2, [16,1,2,0,4,2,7,1,2,14])
assert score == 37, score

score = calc_fuel_use(1, [16,1,2,0,4,2,7,1,2,14])
assert score == 41, score

score = calc_fuel_use(3, [16,1,2,0,4,2,7,1,2,14])
assert score == 39, score

score = calc_fuel_use(10, [16,1,2,0,4,2,7,1,2,14])
assert score == 71, score

result = run_test(test_input, 2, 37)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    line = f.readline()
    input_data = [int(item) for item in line.split(',')]
    pos, answer = calculate_solution(input_data)

    print(f'Solution is {answer}')
