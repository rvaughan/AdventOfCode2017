#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 1 of the Advent of Code for 2023.
"""
import sys


def calculate_line_solution(items):
    result = 0

    first_digit = True
    first = 0
    last = 0

    for item in items:
        for x in item:
            if x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if first_digit:
                    first = x
                    last = x
                    first_digit = False
                else:
                    last = x

    result = int(f'{first}{last}')

    return result


def calculate_solution(items):
    result = 0
    for item in items:
        result += calculate_line_solution(item)

    return result


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'))

    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list= """
1abc2
"""

result = run_test(test_list, 12)

test_list= """
pqr3stu8vwx
"""

result = run_test(test_list, 38)

test_list= """
a1b2c3d4e5f
"""

result = run_test(test_list, 15)

test_list= """
treb7uchet
"""

result = run_test(test_list, 77)

test_list = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

result = run_test(test_list, 142)

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
