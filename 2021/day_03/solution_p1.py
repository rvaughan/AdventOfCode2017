#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 3 of the Advent of Code for 2021.
"""

import sys
from typing import DefaultDict


def calculate_solution(diagnostic_data):
    epsilon = 0
    gamma = 0

    columns = DefaultDict(lambda: DefaultDict(int))

    for diag in diagnostic_data:
        for col in range(len(diag)):
            columns[col][diag[col]] += 1

    e_bits = ''
    g_bits = ''
    for _, x in columns.items():
        if x['0'] > x['1']:
            e_bits += '0'
            g_bits += '1'
        else:
            e_bits += '1'
            g_bits += '0'

    epsilon = int(e_bits, 2)
    gamma = int(g_bits, 2)

    return epsilon * gamma


def run_test(test_input, expected_result):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input)

    if result != expected_result:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_result}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = ["00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"]

result = run_test(test_list, 198)

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
