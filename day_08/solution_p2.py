#!/usr/bin/env python

import sys


def check_register(register):
    global registers

    if register not in registers:
        registers[register] = 0


def perform_check(register, test, test_value):
    global registers

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
    global registers
    global max_register_value

    if instruction == "inc":
        registers[register] += value

    if instruction == "dec":
        registers[register] -= value

    if registers[register] > max_register_value:
        max_register_value = registers[register]


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


max_register_value = 0
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
    print "Incorrect max register current value seen."
    sys.exit(-1)
if max_register_value != 10:
    print "Incorrect max register value value seen."
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

print "Max value: {0}, max value ever: {1}".format(max, max_register_value)
