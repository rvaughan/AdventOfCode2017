#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 5 of the Advent of Code for 2017.
"""

import sys


def process_stack(stack_data):
    ip = 0

    instruction_count = 0
    while ip >= 0 and ip < len(stack_data):
        cur_inst = stack_data[ip]

        stack_data[ip] += 1

        ip += cur_inst

        instruction_count += 1

    return instruction_count


test_data = [0, 3, 0, 1, -3]
expected_steps = 5
num_steps = process_stack(test_data)
if expected_steps != num_steps:
    print "Test failed."
    sys.exit(-1)
print "Test passed."

instruction_data = []
with open("input.txt", "r") as f:
    for instruction in f.readlines():
        instruction_data.append(int(instruction))

    print process_stack(instruction_data)
