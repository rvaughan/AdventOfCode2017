#!/bin/bash

import sys


def calc_row_checksum(row_data):
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

with open("test_spreadsheet.txt", "r") as f:
    checksum = 0

    for row in f.readlines():
        checksum += calc_row_checksum(row)

    if checksum != 18:
        print "Invalid test checksum, got {0} not, 18".format(checksum)
        sys.exit(-1)

# If we reach here, then our test has passed and we will proceed.

with open("input.txt", "r") as f:
    checksum = 0

    for row in f.readlines():
        checksum += calc_row_checksum(row)

    print checksum
