#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 17 of the Advent of Code for 2020.
"""
import re
import sys
from collections import defaultdict


def find_active(grid, i, j, k, m):
    num = 0

    # Find the active cells around the one we
    # are interested in
    for di in range(-1, 2):
        for dj in range(-1, 2):
            for dk in range(-1, 2):
                for dm in range(-1, 2):
                    if grid[i+di][j+dj][k+dk][m+dm] == '#':
                        num += 1

    # Make sure we ignore the grid
    # we are checking!
    act = 1 if grid[i][j][k][m] == '#' else 0
    num -= act 

    return [act, num]


def step(grid, num):
    # Create any empty grid whch will be filled in
    new_grid = [[[['.' for k in range(num)] for j in range(num)] for i in range(num)] for m in range(num)]

    for i in range(1, num-1):
        for j in range(1, num-1):
            for k in range(1, num-1):
                for m in range(1, num-1):
                    act = find_active(grid, i, j, k, m)

                    # If this is an active cell and 2 or 3 cells around
                    # it are active then it should stay active in the
                    # new grid.
                    if (act[0] == 1) and (act[1] == 2 or act[1] == 3):
                        new_grid[i][j][k][m] = '#'
                    
                    # If this is not an active cell but 3 cells around
                    # it are active then this cell should become
                    # active in the new grid.
                    if (act[0] == 0) and (act[1] == 3): 
                        new_grid[i][j][k][m] = '#'
    
    return new_grid


def count_active(grid, num):
    count = 0

    for i in range(0, num):
        for j in range(0, num):
            for k in range(0, num):
                for m in range(0, num):
                    if grid[i][j][k][m] == '#':
                        count += 1
    
    return count


def calculate_solution(grid_data):
    cycles = 6

    # Work out how large the eventual grid will be.
    grid_size = (len(grid_data) + (cycles + 3) * 2)

    # Find the middle of the grid so that we can
    # put the puzzle input there.
    offset = grid_size // 2 - (len(grid_data) // 2)

    # Build the initial grid
    grid = [[[['.' for k in range(grid_size)] for j in range(grid_size)] for i in range(grid_size)] for m in range(grid_size)]
    for i in range(len(grid_data)):
        for j in range(len(grid_data[i])):
            grid[offset][offset][i+offset][j+offset] = grid_data[i][j]

    for _ in range(0, cycles):
        grid = step(grid, grid_size)

    return count_active(grid, grid_size)


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input)

    if result != expected_solution:
        print("Test for input {0} FAILED. Got a result of {1}, not {2}".format(test_input, result, expected_solution))
        sys.exit(-1)

    print("Test for input {0} passed.".format(test_input))

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.


puzzle_input = [
    ".#.",
    "..#",
    "###"
]
run_test(puzzle_input, 848)


print("")
print("-----------------")
print("All Tests PASSED.")
print("-----------------")
print("")

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data)

    print("Solution is {0}".format(answer))
