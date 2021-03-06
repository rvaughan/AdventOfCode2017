#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 3 of the Advent of Code for 2018.
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
    grid = [[0 for x in range(grid_size)] for y in range(grid_size)]
    id_grid = [[set() for x in range(grid_size)] for y in range(grid_size)]

    return grid, id_grid


def mark_fabric(grid, id_grid, clean_set, input):
    x_id, offset_x, offset_y, width, height = extract_instructions(input)

    ok_to_add = True

    for y in range(offset_y, offset_y + height):
        for x in range(offset_x, offset_x + width):
            grid[x][y] += 1
            id_grid[x][y].add(x_id)
            if grid[x][y] > 1:
                ok_to_add = False

                for val in id_grid[x][y]:
                    if val in clean_set:
                        clean_set.remove(val)

    if ok_to_add:
        clean_set.add(x_id)


def find_multiple_claims(grid, id_grid, width, height):
    inches = 0
    for y in xrange(height):
        for x in xrange(width):
            if grid[x][y] > 1:
                inches += 1

    return inches


def find_single_claim(grid, id_grid, width, height):
    for y in xrange(height):
        for x in xrange(width):
            if grid[x][y] == 1:
                return id_grid[x][y]

    return None


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

grid, id_grid = generate_fabric_grid(10)
clean_set = set()
for line in test_input.split('\n'):
    mark_fabric(grid, id_grid, clean_set, line.strip())

num_inches = find_multiple_claims(grid, id_grid, 10, 10)

assert num_inches == 4

assert len(clean_set) == 1

val = clean_set.pop()

assert val == 3

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    grid, id_grid = generate_fabric_grid(1000)
    clean_set = set()
    for line in f:
        mark_fabric(grid, id_grid, clean_set, line.strip())

    num_inches = find_multiple_claims(grid, id_grid, 1000, 1000)

    val = clean_set.pop()

    print "Solution is {0}".format(val)
