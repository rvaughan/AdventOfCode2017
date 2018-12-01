#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 25 of the Advent of Code for 2017.
"""

from collections import defaultdict
import re
import sys


def grab_initial_state(line):
    r = re.compile(r"Begin in state ([A-Z])\.")
    x = r.search(line)
    return x.group(1)

def get_num_steps(line):
    r = re.compile(r"Perform a diagnostic checksum after (\d+) steps\.")
    x = r.search(line)
    return int(x.group(1))


def process_sub_block(sub_block):
    r = re.compile(r"  If the current value is (\d+):")
    x = r.search(sub_block[0])
    cur_val = int(x.group(1))

    r = re.compile(r"    - Write the value (\d+)\.")
    x = r.search(sub_block[1])
    write_val = int(x.group(1))

    r = re.compile(r"    - Move one slot to the (\w+)\.")
    x = r.search(sub_block[2])
    if x.group(1) == "left":
        direction = -1
    else:
        direction = 1

    r = re.compile(r"    - Continue with state (\w+).")
    x = r.search(sub_block[3])
    next_state = x.group(1)

    return (cur_val, write_val, direction, next_state)


def process_block(block):
    r = re.compile(r"In state ([A-Z]):")
    x = r.search(block[0])
    state = x.group(1)

    data = defaultdict(int)

    cur_val, write_val, direction, next_state = process_sub_block(block[1:5])
    data[cur_val] = (write_val, direction, next_state)

    cur_val, write_val, direction, next_state = process_sub_block(block[5:9])
    data[cur_val] = (write_val, direction, next_state)

    return state, data


def process_input(input_data):
    lines = input_data.split("\n")

    first = lines[0]
    cur_state = grab_initial_state(first)

    second = lines[1]
    max_steps = get_num_steps(second)

    states = defaultdict(str)
    block = []
    for idx in xrange(3, len(lines), 1):
        line = lines[idx]
        if line.strip() != "":
            block.append(line)
        else:
            state, data = process_block(block)
            states[state] = data
            block = []

    if block != "":
        state, data = process_block(block)
        states[state] = data

    program = defaultdict(int)
    cur_pos = 0

    max_pos = 0
    min_pos = 0
    num_move = 0
    while num_move < max_steps:
        cur_val = program[cur_pos]

        instr = states[cur_state][cur_val]

        # Write the next value
        program[cur_pos] = instr[0]

        # Move the program tape
        cur_pos += instr[1]

        cur_state = instr[2]

        num_move += 1

        if cur_pos > max_pos:
            max_pos = cur_pos

        if cur_pos < min_pos:
            min_pos = cur_pos

    checksum = 0
    for pos in xrange(min_pos - 1, max_pos + 1, 1):
        checksum += program[pos]

    return checksum


with open("test_input.txt", "r") as f:
    checksum = process_input(f.read())

    if checksum != 3:
        print "Test failed."
        sys.exit(-1)

with open("input.txt", "r") as f:
    checksum = process_input(f.read())

    print "Solution is: {0}".format(checksum)
