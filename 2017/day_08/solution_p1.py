#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 8 of the Advent of Code for 2017.
"""

import sys


def check_register(register):
    if register not in registers:
        registers[register] = 0


def perform_check(register, test, test_value):
    register_value = registers[register]

    if test == "<":
        return register_value < test_value

    if test == ">":
        return register_value > test_value

    if test == "==":
        return register_value == test_value

    if test == "!=":
        return register_value != test_value

    if test == "<=":
        return register_value <= test_value

    if test == ">=":
        return register_value >= test_value

    return False


def perform_instruction(register, instruction, value):
    if instruction == "inc":
        registers[register] += value

    if instruction == "dec":
        registers[register] -= value


def process_line(line):
    parts = line.split(" ")

    check_register(parts[0])

    instruction = parts[1]
    amount = int(parts[2])

    check_register(parts[4])

    test = parts[5]
    test_value = int(parts[6])

    if perform_check(parts[4], test, test_value):
        perform_instruction(parts[0], instruction, amount)


registers = {}
with open("test_input.txt", "r") as f:
    for line in f.readlines():
        process_line(line)

max = 0
first = True
for r in registers:
    if first:
        max = registers[r]
        first = False
    else:
        if registers[r] > max:
            max = registers[r]

if max != 1:
    print "Incorrect test value seen."
    sys.exit(-1)
print "Test passed."

# If we get here then all of our tests passed.

registers = {}
with open("input.txt", "r") as f:
    for line in f.readlines():
        process_line(line)

max = 0
first = True
for r in registers:
    if first:
        max = registers[r]
        first = False
    else:
        if registers[r] > max:
            max = registers[r]

print "Max value: {0}".format(max)
