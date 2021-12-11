#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 11 of the Advent of Code for 2021.
"""

import sys
from collections import defaultdict, deque


# Create a map (of sorts) which tells us which points to look at around a cell.
dir_x = [0, 1, 1, 1, 0, -1, -1, -1]
dir_y = [-1, -1, 0, 1, 1, 1, 0, -1]


def trigger_others(x, y, input_data, flashed):
    for d in range(len(dir_x)):
        xx = x + dir_y[d]
        yy = y + dir_x[d]
        if 0 <= xx < len(input_data[0]) and 0 <= yy < len(input_data):
            input_data[yy][xx] += 1
            if input_data[yy][xx] > 9 and (xx,yy) not in flashed:
                flashed.add((xx,yy))
                trigger_others(xx, yy, input_data, flashed)


def calculate_solution(input_data):
    step = 0
    num_octopodes = len(input_data) * len(input_data[0])
    finished = False

    while not finished:
        flashed = set()

        # Step 1
        for y in range(len(input_data)):
            for x in range(len(input_data[y])):
                input_data[y][x] += 1

        # Step 2
        for y in range(len(input_data)):
            for x in range(len(input_data[y])):
                if input_data[y][x] > 9:
                    if (x,y) not in flashed:
                        flashed.add((x,y))
                        trigger_others(x, y, input_data, flashed)

        if len(flashed) == num_octopodes:
            finished = True
        else:
            # Step 3
            for (x,y) in flashed:
                input_data[y][x] = 0

            # for y in range(len(input_data)):
            #     output = ''
            #     for x in range(len(input_data[y])):
            #         output += str(input_data[y][x])
            #     print(output)
            # print('')

            step += 1
    
    return step + 1


def run_test(test_input, expected_value):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    input_vals = []
    tmp = [item for item in test_input.split('\n')]
    for t in tmp:
        row = []
        for a in t:
            row.append(int(a))
        input_vals.append(row)
    
    result = calculate_solution(input_vals)

    if result != expected_value:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_value}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
result = run_test(test_input, 195)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_vals = []
    tmp = [item.strip() for item in f]
    for t in tmp:
        row = []
        for a in t:
            row.append(int(a))
        input_vals.append(row)
    
    answer = calculate_solution(input_vals)

    print(f'Solution is {answer}')
