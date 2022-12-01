#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 1 of the Advent of Code for 2022.
"""

import sys


def calculate_solution(items):
    stars = []

    count = 0
    for item in items:
        if item == '' or item == '\n':
            stars.append(count)
            count = 0
        else:
            count += int(item)

    if count > 0:
        stars.append(count)

    stars.sort()

    return sum(stars[-3:])


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

test_list = [
"1000",
"2000",
"3000",
"",
"4000",
"",
"5000",
"6000",
"",
"7000",
"8000",
"9000",
"",
"10000"]

result = run_test(test_list, 45000)

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
