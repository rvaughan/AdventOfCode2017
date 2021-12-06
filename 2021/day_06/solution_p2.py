#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 6 of the Advent of Code for 2021.
"""

import sys
from collections import defaultdict


def calculate_solution(input_data, num_days):
    fish = defaultdict(int)

    for x in input_data:
        fish[x] += 1

    for _ in range(num_days):
        tmp_fish = defaultdict(int)
        for k,v in fish.items():
            if k == 0:
                tmp_fish[6] += v
                tmp_fish[8] += v
            else:
                tmp_fish[k-1] += v

        fish = tmp_fish
        # print(fish)

    result = 0
    for k,v in fish.items():
        result += v

    return result


def run_test(test_input, num_days, expected_result):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution([int(item) for item in test_input.split(',')], num_days)

    if result != expected_result:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_result}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_input = """3,4,3,1,2"""

result = run_test(test_input, 18, 26)
result = run_test(test_input, 80, 5934)
result = run_test(test_input, 256, 26984457539)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    line = f.readline()
    input_data = [int(item) for item in line.split(',')]
    answer = calculate_solution(input_data, 256)

    print(f'Solution is {answer}')
