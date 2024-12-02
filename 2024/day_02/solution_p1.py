#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 2 of the Advent of Code for 2024.
"""
import sys


def check_levels(report):
    is_safe = False

    diffs = [(x - y) for x, y in zip(report, report[1:])]

    all_decreasing = all([x < 0 for x in diffs])
    all_increasing = all([x > 0 for x in diffs])
    
    if all_decreasing or all_increasing:
        is_safe = all([(abs(x) < 4 and abs(x) > 0) for x in diffs])

    return is_safe


def calculate_solution(reports):
    result = 0

    for report in reports:
        report = [int(x) for x in report.split(' ')]

        result += 1 if check_levels(report) else 0

    return result


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'))

    print()
    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
result = run_test(test_list, 2)

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
