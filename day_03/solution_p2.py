#!/usr/bin/env python

from __future__ import division

import math
import sys

cell_sums = {1: 1}
cell_positions = {(0, 0): 1}

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


def calc_cell_position(number):
    """
    Attempts to calculate the Manhatten distance from the memory cell
    containing the value back to the centre of the spiral. Works by
    finding the position of the next square value, and working back
    from there. Possibly not the most efficient solution...
    """

    # Might as well exit early
    if number == 1:
        return (0, 0)

    # Another quick early exit.
    if number == 2:
        return (1, 0)

    # Work out how far out the number can be.
    spiral_size = calc_spiral_size(number)

    print "Spiral size: {0}".format(spiral_size)

    cur_x = 0
    cur_y = 0
    cur_val = spiral_size * spiral_size
    cur_direction = None

    NORTH = (0, 1)
    S = (0, -1)
    W = (-1, 0)
    E = (1, 0)

    # old -> new direction, note this is used to unwind the spiral, so
    # it is the opposite direction to the spirals direction of travel.
    directions = {NORTH: E, E: S, S: W, W: NORTH}

    if spiral_size % 2 == 0:
        print "Even"
        # number is even, so the max point is top left.
        cur_x = 0 - int(math.floor((spiral_size - 1) / 2))
        cur_y = int(math.floor(spiral_size / 2))
        cur_direction = E

        if spiral_size == 2:
            cur_x = 0
            cur_y = 1

        print cur_x, cur_y
    else:
        print "Odd"
        # Spiral size is odd, so the end point is bottom right.
        cur_x = int(math.floor(spiral_size / 2))
        cur_y = 0 - int(math.floor(spiral_size / 2))
        cur_direction = W

        print cur_x, cur_y

    diff = cur_val - number

    countdown = spiral_size
    while diff > 0:
        cur_x += cur_direction[0]
        cur_y += cur_direction[1]

        print "** {0}, {1}".format(cur_x, cur_y)

        diff -= 1

        countdown -= 1
        if countdown == 1:
            cur_direction = directions[cur_direction]
            countdown = spiral_size

    return (cur_x, cur_y)


def calc_cell_value(cell):
    if cell in cell_sums:
        return cell_sums[cell]

    rollback = cell
    while rollback not in cell_sums:
        cell_id = calc_cell_position(cell)
        cell_positions[cell_id] = cell
        rollback -= 1

    print "Have solutions back to cell {0}".format(rollback)

    rollback += 1
    while rollback <= cell:
        print "Generating solution for cell {0}".format(rollback)
        cell_id = calc_cell_position(rollback)
        print "Cell ID: {0}".format(cell_id)

        surrounding = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]

        tmp = 0

        for idx_diff in surrounding:
            print idx_diff
            idx = (cell_id[0] + idx_diff[0], cell_id[1] + idx_diff[1])
            if idx in cell_positions:
                print "pos: {0}, cell: {1}, val: {2}".format(idx, cell_positions[idx], cell_sums[cell_positions[idx]])
                tmp += cell_sums[cell_positions[idx]]

        cell_positions[cell_id] = rollback
        cell_sums[cell] = tmp

        rollback += 1

    rollback -= 1

    return cell_sums[rollback]

def run_test(cell_number, expected_sum):
    act_sum = calc_cell_value(cell_number)
    if act_sum != expected_sum:
        print "Test {0} failed. Got {1}, but wanted {2}".format(cell_number, act_sum, expected_sum)
        sys.exit(-1)
    print "Test {0} passed".format(cell_number)


print "----------------------------------------------------------------"
print " RUN STARTING"
print "----------------------------------------------------------------"

run_test(1, 1)
run_test(2, 1)
run_test(3, 2)
run_test(4, 4)
run_test(5, 5)
run_test(6, 10)
run_test(7, 11)
run_test(8, 23)
run_test(9, 25)
run_test(10, 26)
run_test(11, 54)
run_test(12, 57)
run_test(13, 59)
run_test(14, 122)
run_test(15, 133)
run_test(16, 142)
run_test(17, 147)
run_test(18, 304)
run_test(19, 330)
run_test(20, 351)
run_test(21, 362)
run_test(22, 747)
run_test(23, 806)

# Ok, so if we get here we can be reasonably confident that our code is ok,
# and we can try the real puzzle.

act_sum = 0
cell_number = 1
while act_sum < 289326:
    act_sum = calc_cell_value(cell_number)
    cell_number += 1

print "The solution is {0}".format(act_sum)

print "----------------------------------------------------------------"
