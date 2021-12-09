#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 9 of the Advent of Code for 2021.
"""

import sys
from collections import defaultdict, deque


def calculate_solution(input_data):
    basin_sizes = []
    visited = set()

    # Create a map (of sorts) which tells us which points to look at around a cell.
    dir_x = [-1, 0, 1, 0]
    dir_y = [0, 1, 0, -1]

    # Change in tack here. We will try and flood fill the basin areas, using the
    # fact that they are bordered by 9's.

    for y in range(len(input_data)):
        for x in range(len(input_data[y])):
            if (x,y) not in visited and input_data[y][x] != 9:
                # We've found a cell which is part of a basin we've not seen before.
                basin_size = 0
                queue = deque()
                queue.append((x,y))
                while queue:
                    (x,y) = queue.popleft()

                    if (x,y) in visited:
                        # Skip this cell, we've already seen in
                        continue

                    # This is a cell we've not already seen, so count it.
                    visited.add((x,y))
                    basin_size += 1

                    # Add each of the (valid) cells around the current cell to
                    # the list of cells to check next.
                    for d in range(len(dir_x)):
                        xx = x + dir_y[d]
                        yy = y + dir_x[d]
                        if 0 <= xx < len(input_data[0]) and 0 <= yy < len(input_data) and input_data[yy][xx] != 9:
                            queue.append((xx,yy))

                basin_sizes.append(basin_size)

    basin_sizes.sort()

    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]


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

test_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""
result = run_test(test_input, 1134)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    #input_data = [item for item in f]
    input_vals = []
    tmp = [item.strip() for item in f]
    for t in tmp:
        row = []
        for a in t:
            row.append(int(a))
        input_vals.append(row)

    answer = calculate_solution(input_vals)

    print(f'Solution is {answer}')
