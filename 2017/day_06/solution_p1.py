#!/usr/bin/env python

import sys


def find_cycle(input_data):
    count = 0
    finished = False

    previous = {}

    while not finished:

        # Find largest
        first = True
        max_cell = 0
        max = 0
        for idx, cell_value in enumerate(input_data):
            if first:
                max = cell_value
                max_cell = idx
                first = False
            else:
                if cell_value > max:
                    max = cell_value
                    max_cell = idx

        # print "Cell {0} contains the max item [{1}]".format(max_cell, max)

        # Distribute data

        input_data[max_cell] = 0

        cur_cell = max_cell
        while max > 0:
            cur_cell += 1
            if cur_cell == len(input_data):
                cur_cell = 0

            input_data[cur_cell] += 1
            max -= 1

        # Check for duplicate

        idx = " ".join(str(input_data))

        # print idx

        if idx in previous:
            finished = True
        else:
            previous[idx] = True

        count += 1

    return count


test_data = [0, 2, 7, 0]
expected_steps = 5
num_steps = find_cycle(test_data)
if expected_steps != num_steps:
    print "Test failed, got {0} cycles, but was expecting {1}.".format(num_steps, expected_steps)
    sys.exit(-1)
print "Test passed."

instruction_data = []
with open("input.txt", "r") as f:
    for instruction in f.readline().split("\t"):
        instruction_data.append(int(instruction))

    print find_cycle(instruction_data)
