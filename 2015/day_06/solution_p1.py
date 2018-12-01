#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 6 of the Advent of Code for 2015.
"""
import hashlib
import sys


def create_light_grid(default_value):
    grid = [[default_value] * 1000 for i in range(1000)]

    return grid


def count_lights(grid):
    result = 0
    for row in xrange(1000):
        result += sum(grid[row])
    
    return result


def toggle_lights(grid, start_pos, end_pos):
    x =  start_pos[0]
    y = start_pos[1]

    while x <= end_pos[0]:
        y = start_pos[1]
        while y <= end_pos[1]:
            grid[x][y] = not grid[x][y]

            y += 1

        x += 1


def set_lights(grid, start_pos, end_pos, state):
    x =  start_pos[0]
    y = start_pos[1]

    while x <= end_pos[0]:
        y = start_pos[1]
        while y <= end_pos[1]:
            grid[x][y] = state

            y += 1

        x += 1


def process_commands(grid, command):
    parts = command.split(' ')

    if parts[0] == 'toggle':
        start_pos = [int(x) for x in parts[1].split(',')]
        end_pos = [int(x) for x in parts[3].split(',')]

        toggle_lights(grid, start_pos, end_pos)
    else:
        start_pos = [int(x) for x in parts[2].split(',')]
        end_pos = [int(x) for x in parts[4].split(',')]

        if parts[1] == 'on':
            set_lights(grid, start_pos, end_pos, True)
    
        if parts[1] == 'off':
            set_lights(grid, start_pos, end_pos, False)

    return count_lights(grid)


def run_test(data, expected_solution, grid):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = process_commands(grid, data)

    if result != expected_solution:
        print "Test for data '{0}' FAILED. Got a result of {1}, not {2}".format(data, result, expected_solution)
        sys.exit(-1)

    print "Test for '{0}' passed.".format(data)


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

light_grid = create_light_grid(False)

run_test("turn on 0,0 through 999,999", 1000000, light_grid)
run_test("toggle 0,0 through 999,0", 999000, light_grid)
run_test("turn off 499,499 through 500,500", 998996, light_grid)

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual data now.

light_grid = create_light_grid(False)
with open("input.txt", "r") as f:
    result = 0
    for line in f:
        result = process_commands(light_grid, line)

    print "Number of lights lit: {}".format(result)
