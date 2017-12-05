#!/usr/bin/env python

from __future__ import division

import sys


def check_numbers(num_a, num_b):
    div_result = num_a % num_b
    if div_result == 0:
        return True, int(num_a / num_b)

    div_result = num_b % num_a
    if div_result == 0:
        return True, int(num_b / num_a)

    return False, 0

def calc_row_checksum(row_data):
    min_val = 0
    max_val = 0

    first = True

    values = []
    for cell in row_data.split("\t"):
        values.append(int(cell))

    for idx in xrange(len(values)):
        for idx_2 in xrange(idx + 1, len(values)):
            ok, result = check_numbers(values[idx], values[idx_2])
            if ok:
                return result

    return 0

with open("test_spreadsheet_2.txt", "r") as f:
    checksum = 0

    for row in f.readlines():
        checksum += calc_row_checksum(row)

    if checksum != 9:
        print "Invalid test checksum, got {0} not, 9".format(checksum)
        sys.exit(-1)

print "Test spreadsheet checksum calculated correctly."

# If we reach here, then our test has passed and we will proceed.

with open("input.txt", "r") as f:
    checksum = 0

    for row in f.readlines():
        checksum += calc_row_checksum(row)

    print "The checksum for the input spreasheet is {0}".format(checksum)
