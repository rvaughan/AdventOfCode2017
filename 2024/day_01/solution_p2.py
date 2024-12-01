#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 1 of the Advent of Code for 2024.
"""
import sys


def calculate_solution(numbers):
    result = 0

    left = []
    right = []

    for line in numbers:
        (l, r) = line.split('   ')

        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()

    for l, r in zip(left, right):
        result += abs(int(l) - int(r))

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

test_list = """3   4
4   3
2   5
1   3
3   9
3   3"""
result = run_test(test_list, 31)

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
