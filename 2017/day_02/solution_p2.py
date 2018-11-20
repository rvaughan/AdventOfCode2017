#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 2 of the Advent of Code for 2017.
"""

from __future__ import division

import sys


def check_numbers(num_a, num_b):
    """
    Checks to see if the two numbers are evenly divisible by each other.
    """
    div_result = num_a % num_b
    if div_result == 0:
        return True, int(num_a / num_b)

    div_result = num_b % num_a
    if div_result == 0:
        return True, int(num_b / num_a)

    return False, 0


def calc_row_checksum(row_data):
    """
    Method for calculating the checksum for a row.
    """
    values = []
    for cell in row_data.split("\t"):
        values.append(int(cell))

    for idx in xrange(len(values)):
        for idx_2 in xrange(idx + 1, len(values)):
            ok, result = check_numbers(values[idx], values[idx_2])
            if ok:
                return result

    return 0

# Tests

with open("test_spreadsheet_2.txt", "r") as f:
    CHECKSUM = 0

    for row in f.readlines():
        CHECKSUM += calc_row_checksum(row)

    if CHECKSUM != 9:
        print "Invalid test checksum, got {0} not, 9".format(CHECKSUM)
        sys.exit(-1)
    print "Checksum test passed."

print "Test spreadsheet checksum calculated correctly."

# If we reach here, then our test has passed and we will proceed.

with open("input.txt", "r") as f:
    CHECKSUM = 0

    for row in f.readlines():
        CHECKSUM += calc_row_checksum(row)

    print "The checksum for the input spreasheet is {0}".format(CHECKSUM)
