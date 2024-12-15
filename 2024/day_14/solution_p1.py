#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 14 of the Advent of Code for 2024.
"""
import re
import sys


def calculate_solution(items, width, height, iterations):
    robots = []

    for robot in items:
        (px, py, vx, vy) = re.findall(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', robot)[0]

        final_px = (int(px) + int(vx) * iterations) % width
        final_py = (int(py) + int(vy) * iterations) % height

        robots.append((final_px, final_py))

    middle_row_x = int(width / 2)
    middle_row_y = int(height / 2)

    top_left = 0
    top_right = 0
    bottom_left = 0
    bottom_right = 0

    result = 0
    for robot in robots:
        px, py = robot

        if px < middle_row_x and py < middle_row_y:
            top_left += 1
        
        if px > middle_row_x and py < middle_row_y:
            top_right += 1

        if px < middle_row_x and py > middle_row_y:
            bottom_left += 1
        
        if px > middle_row_x and py > middle_row_y:
            bottom_right += 1

    # print(top_left, top_right, bottom_left, bottom_right)
    result = top_left * top_right * bottom_left * bottom_right

    return result


def run_test(test_input, width, height, iterations, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'), width, height, iterations)

    print()
    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list="""p=2,4 v=2,-3"""
result = run_test(test_list, 11, 7, 2, 0)

test_list = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""
result = run_test(test_list, 11, 7, 100, 12)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data, 101, 103, 100)

    print(f'Solution is {answer}')
