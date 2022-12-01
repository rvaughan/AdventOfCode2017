#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 22 of the Advent of Code for 2021.
"""

import sys
from collections import defaultdict


def move_east(input_data):
    result = []
    for x in range(len(input_data)):
        tmp = input_data[x]
        for y in range(len(input_data[0])):
            if y < len(input_data) - 1:
                if input_data[x+1][y] == '.':
                    tmp[x][y] = '.'
                    tmp[x+1][y] = '>'
                else:
                    tmp[x][y] = input_data[x+1][y]
            else:
                if input_data[0][y] == '.':
                    tmp[x][y] = '.'
                    tmp[0][y] = '>'
                else:
                    tmp[0][y] = input_data[x+1][y]

        result.append(tmp)

    return result


def calculate_solution(input_data):
    return 0


def run_test(test_input, expected_value):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    input_vals = [line.strip() for line in test_input.split('\n')]
    result = calculate_solution(input_vals)

    if result != expected_value:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_value}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_input=['...>>>>>...']
result = move_east(test_input)
assert result == '...>>>>.>..'

test_input="""v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""
result = run_test(test_input, 58)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    answer = calculate_solution([item.strip() for item in f])

    print(f'Solution is {answer}')
