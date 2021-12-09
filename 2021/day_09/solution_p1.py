#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 9 of the Advent of Code for 2021.
"""

import sys
from collections import defaultdict


def calculate_solution(input_data):
    result = 0
    
    low_points = []
    for y in range(len(input_data)):
        for x in range(len(input_data[y])):
            low_point = True
            if y > 0 and input_data[y][x] >= input_data[y-1][x]:
                low_point = False
            if x > 0 and input_data[y][x] >= input_data[y][x-1]:
                low_point = False
            if y < (len(input_data) - 1) and input_data[y][x] >= input_data[y+1][x]:
                low_point = False
            if x < (len(input_data[y]) - 1) and input_data[y][x] >= input_data[y][x+1]:
                low_point = False            

            if low_point:
                low_points.append(input_data[y][x])

    for x in low_points:
        result += (x + 1)

    return result


def run_test(test_input, expected_value):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    input_vals = []
    tmp = [item for item in test_input.split('\n')]
    for t in tmp:
        row = []
        for a in t:
            row.append(int(a))
        input_vals.append(row)
    result = calculate_solution(input_vals)

    if result != expected_value:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_value}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.


test_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""
result = run_test(test_input, 15)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    #input_data = [item for item in f]
    input_vals = []
    tmp = [item.strip() for item in f]
    for t in tmp:
        row = []
        for a in t:
            row.append(int(a))
        input_vals.append(row)

    answer = calculate_solution(input_vals)

    print(f'Solution is {answer}')
