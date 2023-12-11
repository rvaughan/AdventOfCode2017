#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 8 of the Advent of Code for 2019.
"""
from collections import defaultdict
import sys


def calculate_solution(items, cols, rows):
    line = items[0]

    layers = [] 
    width = cols * rows
    for i in range(len(line) // width):
        layers.append([list(map(int, line[i*width + j*cols : i*width + (j+1)*cols])) for j in range(rows)])

    image = [['#'] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            pixel = next(layer[r][c] for layer in layers if layer[r][c] != 2)
            image[r][c] = '*' if pixel == 1 else ' '
    
    print('\n'.join(''.join(row) for row in image))

    return 0


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

test_list = """0222112222120000"""

result = run_test(test_list, 2, 2, 0)

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

    print(f'Solution is {answer}')
