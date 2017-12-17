#!/usr/bin/env python

import sys


def calc_row_checksum(row_data):
    """
    Method for calculating the checksum for a row.
    """
    min_val = 0
    max_val = 0

    first = True

    for cell in row_data.split("\t"):
        if first:
            min_val = int(cell)
            max_val = int(cell)

            first = False
        else:
            if min_val > int(cell):
                min_val = int(cell)

            if max_val < int(cell):
                max_val = int(cell)

    return max_val - min_val

# Tests for validating code solution

with open("test_spreadsheet.txt", "r") as f:
    CHECKSUM = 0

    for row in f.readlines():
        CHECKSUM += calc_row_checksum(row)

    if CHECKSUM != 18:
        print "Invalid test checksum, got {0} not, 18".format(CHECKSUM)
        sys.exit(-1)
    print "Checksum test passed."

print "All tests passed."

# If we reach here, then our test has passed and we will proceed.

with open("input.txt", "r") as f:
    CHECKSUM = 0

    for row in f.readlines():
        CHECKSUM += calc_row_checksum(row)

    print CHECKSUM
