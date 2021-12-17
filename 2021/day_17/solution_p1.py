#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 17 of the Advent of Code for 2021.
"""

import sys
from collections import defaultdict, deque


def calc_trajectory(min_x, max_x, min_y, max_y):
    answer = 0
    for x_step in range(-100, 100):
        for y_step in range(-1000, 1000):
            max_height = 0
            hit_target = False
            x = 0
            y = 0
            x_velocity = x_step
            y_velocity = y_step
            for timestep in range(500):
                x += x_velocity
                y += y_velocity
                max_height = max(max_height, y)

                if x_velocity > 0:
                    x_velocity -= 1
                elif x_velocity < 0:
                    x_velocity += 1

                y_velocity -= 1

                if min_x <= x <= max_x and min_y <= y <= max_y:
                    hit_target = True
        
            if hit_target:
                answer = max(max_height, answer)

    return answer


def calculate_solution(input_data):
    tmp = input_data[0].split(',')
    x_min, x_max = tmp[0].split('x=')[1].split('..')
    y_min, y_max = tmp[1].split('y=')[1].split('..')

    return calc_trajectory(int(x_min), int(x_max), int(y_min), int(y_max))


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

test_input="""target area: x=20..30, y=-10..-5"""
result = run_test(test_input, 45)

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
