#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 3 of the Advent of Code for 2021.
"""

import sys
from typing import DefaultDict


def find_oxygen_rating(data, c):
    columns = DefaultDict(int)

    for diag in data:
        columns[int(diag[c])] += 1

    results = []
    if columns[0] > columns[1]:
        for x in data:
            if x[c] == '0':
                results.append(x)
    elif columns[0] == columns[1]:
        for x in data:
            if x[c] == '1':
                results.append(x)
    else:
        for x in data:
            if x[c] == '1':
                results.append(x)

    return results


def find_co2_rating(data, c):
    columns = DefaultDict(int)

    for diag in data:
        columns[int(diag[c])] += 1

    results = []
    if columns[0] < columns[1]:
        for x in data:
            if x[c] == '0':
                results.append(x)
    elif columns[0] == columns[1]:
        for x in data:
            if x[c] == '0':
                results.append(x)
    else:
        for x in data:
            if x[c] == '1':
                results.append(x)

    return results


def calculate_solution(diagnostic_data):
    data = diagnostic_data.copy()
    
    col = 0
    while len(data) > 1:
        data = find_oxygen_rating(data, col)
        col += 1
    
    oxygen = int(data[0], 2)

    data = diagnostic_data.copy()
    col = 0
    while len(data) > 1:
        data = find_co2_rating(data, col)
        col += 1
    
    co2 = int(data[0], 2)

    return oxygen * co2


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

result = run_test(test_list, 230)

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
