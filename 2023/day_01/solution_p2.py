#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 1 of the Advent of Code for 2023.
"""
import sys


def set_digit(is_first, digit, first, last):
    if is_first:
        first = digit
        last = digit
        is_first = False
    else:
        last = digit

    return is_first, first, last


def search(line, word):
    if len(line) < len(word):
        return False
    
    return line.startswith(word)


def calculate_line_solution(items):
    result = 0

    first_digit = True
    first = 0
    last = 0

    pos = 0
    while pos < len(items):
        if items[pos] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            first_digit, first, last = set_digit(first_digit, int(items[pos]), first, last)
        else:
            remaining = items[pos:]
            if search(remaining, 'one'):
                first_digit, first, last = set_digit(first_digit, 1, first, last)
                pos += 2
                continue
            if search(remaining, 'two'):
                first_digit, first, last = set_digit(first_digit, 2, first, last)
                pos += 2
                continue
            if search(remaining, 'three'):
                first_digit, first, last = set_digit(first_digit, 3, first, last)
                pos += 4
                continue
            if search(remaining, 'four'):
                first_digit, first, last = set_digit(first_digit, 4, first, last)
                pos += 3
                continue
            if search(remaining, 'five'):
                first_digit, first, last = set_digit(first_digit, 5, first, last)
                pos += 3
                continue
            if search(remaining, 'six'):
                first_digit, first, last = set_digit(first_digit, 6, first, last)
                pos += 2
                continue
            if search(remaining, 'seven'):
                first_digit, first, last = set_digit(first_digit, 7, first, last)
                pos += 4
                continue
            if search(remaining, 'eight'):
                first_digit, first, last = set_digit(first_digit, 8, first, last)
                pos += 3
                continue
            if search(remaining, 'nine'):
                first_digit, first, last = set_digit(first_digit, 9, first, last)
                pos += 3
                continue

        pos += 1

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
two1nine
"""

result = run_test(test_list, 29)

test_list= """
eightwothree
"""

result = run_test(test_list, 83)

test_list= """
abcone2threexyz
"""

result = run_test(test_list, 13)

test_list= """
xtwone3four
"""

result = run_test(test_list, 24)

test_list= """
4nineeightseven2
"""

result = run_test(test_list, 42)

test_list= """
zoneight234
"""

result = run_test(test_list, 14)

test_list= """
7pqrstsixteen
"""

result = run_test(test_list, 76)

test_list = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

result = run_test(test_list, 281)

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
