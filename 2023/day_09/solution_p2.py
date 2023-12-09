#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 9 of the Advent of Code for 2023.
"""
import sys


def calculate_solution(items):
    result = 0

    for item in items:
        layers = []
        numbers = [int(x) for x in item.split()]
        
        descend = True
        row = numbers.copy()
        while descend:
            descend = False
            layer = []
            for idx in range(len(row) - 1):
                diff = row[idx+1] - row[idx]
                if diff != 0:
                    descend = True
                layer.append(diff)

            if len(layer) > 0:
                layers.append(layer)
                row = layer

        # This bottom layer is always zero...
        layers.pop()

        last_row = 0
        while len(layers) > 0:
            layer = layers.pop()
            last_row = layer[0] - last_row

        result += (numbers[0] - last_row)

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

test_list = """0 3 6 9 12 15"""

result = run_test(test_list, -3)

test_list = """1 3 6 10 15 21"""

result = run_test(test_list, 0)

test_list = """10 13 16 21 30 45"""

result = run_test(test_list, 5)

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
