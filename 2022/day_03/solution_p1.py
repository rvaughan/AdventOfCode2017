#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 3 of the Advent of Code for 2022.
"""

import sys


def calculate_solution(items):
    result = 0

    return result


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

test_list = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

result = run_test(test_list, 7)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data = [int(line) for line in f]
    answer = calculate_solution(input_data)

    print(f'Solution is {answer}')
