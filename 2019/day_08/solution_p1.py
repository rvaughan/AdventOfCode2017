#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 1 of the Advent of Code for 2023.
"""
from collections import defaultdict
import sys


def calculate_solution(items, rows, cols):
    width = rows * cols
    line = items[0]

    layers = [line[i:i+width] for i in range(0, len(line), width)]

    print(len(layers))

    max_layer = 0
    max = 9999999
    max_digits = None
    for idx, layer in enumerate(layers):
        digits = defaultdict(int)
        for d in layer:
            digits[d] += 1

        if digits['0'] < max:
            max = digits['0']
            max_layer = idx + 1
            max_digits = digits
            print(f'Layer {idx + 1} has {max} zeros')

    print(f'Max layer is {max_layer}')
    print(f'Max digits are {max_digits}')

    result = max_digits['1'] * max_digits['2']

    return result


def run_test(test_input, rows, cols, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'), rows, cols)

    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """123456789012"""

result = run_test(test_list, 3, 2, 1)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data, 25, 6)

    # 1640 is too high

    print(f'Solution is {answer}')
