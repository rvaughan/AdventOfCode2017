#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 3 of the Advent of Code for 2017.
"""

from __future__ import division

import math
import sys


def calc_spiral_size(number):
    """
    Tries to calculate the maximum size of the spiral.
    """
    size = 1
    found = False

    while not found:
        if (size * size) < number:
            size += 1
        else:
            found = True

    return size


def calc_distance(number):
    """
    Attempts to calculate the Manhatten distance from the memory cell
    containing the value back to the centre of the spiral. Works by
    finding the position of the next square value, and working back
    from there. Possibly not the most efficient solution...
    """

    # Might as well exit early
    if number == 1:
        return 0

    # Another quick early exit.
    if number == 2:
        return 1

    # Work out how far out the number can be.
    spiral_size = calc_spiral_size(number)

    # Find which cell contains #1.
    pos_1_x = int(math.ceil(spiral_size / 2))
    pos_1_y = int(math.ceil(spiral_size / 2))

    cur_x = 0
    cur_y = 0
    cur_val = spiral_size * spiral_size
    cur_direction = None

    NORTH = (0, 1)
    S = (0, -1)
    W = (-1, 0)
    E = (1, 0)

    # old -> new direction
    directions = {NORTH: E, E: S, S: W, W: NORTH}

    if spiral_size % 2 == 0:
        # number is even, so the max point is top left.
        cur_x = 1
        cur_y = spiral_size
        cur_direction = E
    else:
        # Spiral size is odd, so the end point is bottom right.
        cur_x = spiral_size
        cur_y = 1
        cur_direction = W

    diff = cur_val - number

    countdown = spiral_size
    while diff > 0:
        cur_x += cur_direction[0]
        cur_y += cur_direction[1]

        diff -= 1

        countdown -= 1
        if countdown == 1:
            cur_direction = directions[cur_direction]
            countdown = spiral_size

    distance = abs(cur_x - pos_1_x) + abs(cur_y - pos_1_y)

    return distance


# Tests for validating code solution

# Test 1
TEST_VALUE = 1
EXPECTED_DISTANCE = 0
DISTANCE = calc_distance(TEST_VALUE)
if DISTANCE != EXPECTED_DISTANCE:
    print "Test 1 failed. Got {0}, but wanted {1}".format(DISTANCE, EXPECTED_DISTANCE)
    sys.exit(-1)
print "Test 1 passed"

# Test 1a (self-added)
TEST_VALUE = 6
EXPECTED_DISTANCE = 1
DISTANCE = calc_distance(TEST_VALUE)
if DISTANCE != EXPECTED_DISTANCE:
    print "Test 1a failed. Got {0}, but wanted {1}".format(DISTANCE, EXPECTED_DISTANCE)
    sys.exit(-1)
print "Test 1a passed"

# Test 1b (self-added)
TEST_VALUE = 9
EXPECTED_DISTANCE = 2
DISTANCE = calc_distance(TEST_VALUE)
if DISTANCE != EXPECTED_DISTANCE:
    print "Test 1b failed. Got {0}, but wanted {1}".format(DISTANCE, EXPECTED_DISTANCE)
    sys.exit(-1)
print "Test 1b passed"

# Test 2
TEST_VALUE = 12
EXPECTED_DISTANCE = 3
DISTANCE = calc_distance(TEST_VALUE)
if DISTANCE != EXPECTED_DISTANCE:
    print "Test 2 failed. Got {0}, but wanted {1}".format(DISTANCE, EXPECTED_DISTANCE)
    sys.exit(-1)
print "Test 2 passed"

# Test 3
TEST_VALUE = 23
EXPECTED_DISTANCE = 2
DISTANCE = calc_distance(TEST_VALUE)
if DISTANCE != EXPECTED_DISTANCE:
    print "Test 1 failed. Got {0}, but wanted {1}".format(DISTANCE, EXPECTED_DISTANCE)
    sys.exit(-1)
print "Test 3 passed"

# Test 4
TEST_VALUE = 1024
EXPECTED_DISTANCE = 31
DISTANCE = calc_distance(TEST_VALUE)
if DISTANCE != EXPECTED_DISTANCE:
    print "Test 1 failed. Got {0}, but wanted {1}".format(DISTANCE, EXPECTED_DISTANCE)
    sys.exit(-1)
print "Test 4 passed"

print "All tests passed."

# Ok, so if we get here we can be reasonably confident that our code is ok,
# and we can try the real puzzle.

DISTANCE = calc_distance(289326)
print "The solution is {0}".format(DISTANCE)
