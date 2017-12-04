#!/usr/bin/env python

from __future__ import division

import math
import sys


# NORTH, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0) # directions
# turn_right = {NORTH: E, E: S, S: W, W: NORTH} # old -> new direction
# turn_left = {NORTH: W, E: NORTH, S: E, W: S} # old -> new direction


# def create_right_spiral(width, height):
#     if width < 1 or height < 1:
#         raise ValueError

#     x, y = width // 2, height // 2 # start near the center
#     dx, dy = E # initial direction
#     matrix = [[None] * width for _ in range(height)]
#     count = 0
#     while True:
#         count += 1
#         matrix[y][x] = count # visit
#         # try to turn right
#         new_dx, new_dy = turn_right[dx,dy]
#         new_x, new_y = x + new_dx, y + new_dy
#         if (0 <= new_x < width and 0 <= new_y < height and
#             matrix[new_y][new_x] is None): # can turn right
#             x, y = new_x, new_y
#             dx, dy = new_dx, new_dy
#         else: # try to move straight
#             x, y = x + dx, y + dy
#             if not (0 <= x < width and 0 <= y < height):
#                 return matrix # nowhere to go


# def create_left_spiral(width, height):
#     if width < 1 or height < 1:
#         raise ValueError

#     x, y = width // 2, height // 2 # start near the center
#     dx, dy = W # initial direction
#     matrix = [[None] * width for _ in range(height)]
#     count = 0
#     while True:
#         count += 1
#         matrix[y][x] = count # visit
#         # try to turn left
#         new_dx, new_dy = turn_left[dx,dy]
#         new_x, new_y = x + new_dx, y + new_dy
#         if (0 <= new_x < width and 0 <= new_y < height and
#             matrix[new_y][new_x] is None): # can turn left
#             x, y = new_x, new_y
#             dx, dy = new_dx, new_dy
#         else: # try to move straight
#             x, y = x + dx, y + dy
#             if not (0 <= x < width and 0 <= y < height):
#                 return matrix # nowhere to go


# def print_matrix(matrix):
#     width = len(str(max(el for row in matrix for el in row if el is not None)))
#     fmt = "{:0%dd}" % width
#     for row in matrix:
#         print(" ".join("_"*width if el is None else fmt.format(el) for el in row))


# # def create_spiral(spiral_size, number):
# #     if spiral_size == 1:
# #         return 0

# #     current_x = 1
# #     current_y = 1
# #     current_val = 1
# #     next_track = [(0,1)]
# #     while current_val < number:

# #         distance += 1

# #         current_val += 1

# #     square = 1
# #     found = False

# #     while not found:
# #         if (square * square) < number:
# #             square += 1
# #         else:
# #             found = True

# #     print "square: {0}".format(square)

# #     return square


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

    print "spiral size: {0}".format(size)

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

    print "1 is at ({0}, {1})".format(pos_1_x, pos_1_y)

    cur_x = 0
    cur_y = 0
    cur_val = spiral_size * spiral_size
    cur_direction = None

    print cur_val

    NORTH = (0, 1)
    S = (0, -1)
    W = (-1, 0)
    E = (1, 0)

    # old -> new direction
    directions = {NORTH: E, E: S, S: W, W: NORTH}

    if spiral_size % 2 == 0:
        print "Even"
        # number is even, so the max point is top left.
        cur_x = 1
        cur_y = spiral_size
        cur_direction = E
    else:
        print "Odd"
        # Spiral size is odd, so the end point is bottom right.
        cur_x = spiral_size
        cur_y = 1
        cur_direction = W

    print "Starting @ {0}, {1}".format(cur_x, cur_y)

    diff = cur_val - number

    print "Diff: {0} cells".format(diff)

    countdown = spiral_size
    while diff > 0:
        cur_x += cur_direction[0]
        cur_y += cur_direction[1]
        
        diff -= 1

        print "--- @ {0}, {1}".format(cur_x, cur_y)

        countdown -= 1
        if countdown == 1:
            cur_direction = directions[cur_direction]
            countdown = spiral_size

    print "Ended @ {0}, {1}".format(cur_x, cur_y)

    distance = abs(cur_x - pos_1_x) + abs(cur_y - pos_1_y)

    return distance


# Basic Algorithm:
#   1. Find where 1 is.
#   2. Find where x is.
#   3. Diff pos


# Test 1
test_value = 1
expected_distance = 0
distance = calc_distance(test_value)
if distance != expected_distance:
    print "Test 1 failed. Got {0}, but wanted {1}".format(distance, expected_distance)
    sys.exit(-1)
print "Test 1 passed"

# Test 1a (self-added)
test_value = 6
expected_distance = 1
distance = calc_distance(test_value)
if distance != expected_distance:
    print "Test 1a failed. Got {0}, but wanted {1}".format(distance, expected_distance)
    sys.exit(-1)
print "Test 1a passed"

# Test 1b (self-added)
test_value = 9
expected_distance = 2
distance = calc_distance(test_value)
if distance != expected_distance:
    print "Test 1b failed. Got {0}, but wanted {1}".format(distance, expected_distance)
    sys.exit(-1)
print "Test 1b passed"

# Test 2
test_value = 12
expected_distance = 3
distance = calc_distance(test_value)
if distance != expected_distance:
    print "Test 2 failed. Got {0}, but wanted {1}".format(distance, expected_distance)
    sys.exit(-1)
print "Test 2 passed"

# Test 3
test_value = 23
expected_distance = 2
distance = calc_distance(test_value)
if distance != expected_distance:
    print "Test 1 failed. Got {0}, but wanted {1}".format(distance, expected_distance)
    sys.exit(-1)
print "Test 3 passed"

# Test 4
test_value = 1024
expected_distance = 31
distance = calc_distance(test_value)
if distance != expected_distance:
    print "Test 1 failed. Got {0}, but wanted {1}".format(distance, expected_distance)
    sys.exit(-1)
print "Test 4 passed"

# Ok, so if we get here we can be reasonably confident that our code is ok,
# and we can try the real puzzle.

distance = calc_distance(289326)
print "The solution is {0}".format(distance)
