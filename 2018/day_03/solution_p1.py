#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 3 of the Advent of Code for 2018.
"""

from collections import Counter
import sys


def extract_instructions(test_input):
    parts = test_input.split(' ')

    x_id = parts[0].split('#')[1]

    offset_x, offset_y = parts[2].split(':')[0].split(',')

    width, height = parts[3].split('x')

    return int(x_id), int(offset_x), int(offset_y), int(width), int(height)


def generate_fabric_grid(grid_size):
    return [[0 for x in range(grid_size)] for y in range(grid_size)]


def mark_fabric(grid, input):
    x_id, offset_x, offset_y, width, height = extract_instructions(input)

    for y in range(offset_y, offset_y + height):
        for x in range(offset_x, offset_x + width):
            grid[x][y] += 1


def find_multiple_claims(grid, width, height):
    inches = 0
    for y in xrange(height):
        for x in xrange(width):
            if grid[x][y] > 1:
                inches += 1

    return inches


def dump_grid(grid, width, height):
    for y in xrange(height):
        line = ""
        for x in xrange(width):
            if grid[x][y] > 0:
                line += "x"
            else:
                line += "."

        print line


def run_extract_test(test_input, exp_id, exp_offset_x, exp_offset_y, exp_width, exp_height):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    x_id, offset_x, offset_y, width, height = extract_instructions(test_input)

    if x_id != exp_id or offset_x != exp_offset_x or offset_y != exp_offset_y or width != exp_width or height != exp_height:
        print "Test for {0} FAILED. Got a result of {1}, {2}, {3}, {4}, {5}".format(test_input, id, offset_x, offset_y, width, height)
        sys.exit(-1)

    print "Test for {0} passed.".format(test_input)


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

run_extract_test("#1 @ 1,3: 4x4", 1, 1, 3, 4, 4)
run_extract_test("#2 @ 3,1: 4x4", 2, 3, 1, 4, 4)
run_extract_test("#3 @ 5,5: 2x2", 3, 5, 5, 2, 2)

test_input="""#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""

grid = generate_fabric_grid(10)

for line in test_input.split('\n'):
    mark_fabric(grid, line.strip())

x = find_multiple_claims(grid, 10, 10)

assert x == 4

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    grid = generate_fabric_grid(1000)
    for line in f:
        mark_fabric(grid, line.strip())

    x = find_multiple_claims(grid, 1000, 1000)

    print "Solution is {0}".format(x)
