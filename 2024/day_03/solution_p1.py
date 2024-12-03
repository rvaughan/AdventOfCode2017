#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 3 of the Advent of Code for 2024.
"""
import sys


def calculate_solution(items):
    result = 0

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

test_list = """mul(44,46)"""
result = run_test(test_list, 2024)

test_list = """mul(123,4)"""
result = run_test(test_list, 492)

test_list = """mul(4*"""
result = run_test(test_list, 0)

test_list = """mul(6,9!"""
result = run_test(test_list, 0)

test_list = """?(12,34)"""
result = run_test(test_list, 0)

test_list = """mul ( 2 , 4 )"""
result = run_test(test_list, 0)

test_list = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
result = run_test(test_list, 161)

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
