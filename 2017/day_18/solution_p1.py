#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 18 of the Advent of Code for 2017.
"""

import sys


def process_instruction(registers, last_sound, instruction):
    inst_parts = instruction.strip().split("\n")[0].split(" ")

    if inst_parts[0] == "add":
        if inst_parts[1] in registers:
            try:
                registers[inst_parts[1]] += registers[inst_parts[2]]
            except KeyError:
                registers[inst_parts[1]] += int(inst_parts[2])
    elif inst_parts[0] == "mod":
        if inst_parts[1] in registers:
            try:
                registers[inst_parts[1]] %= registers[inst_parts[2]]
            except KeyError:
                registers[inst_parts[1]] %= int(inst_parts[2])
    elif inst_parts[0] == "mul":
        if inst_parts[1] in registers:
            try:
                registers[inst_parts[1]] *= registers[inst_parts[2]]
            except KeyError:
                registers[inst_parts[1]] *= int(inst_parts[2])
    elif inst_parts[0] == "set":
        if inst_parts[1] not in registers:
            registers[inst_parts[1]] = 0
        try:
            registers[inst_parts[1]] = registers[inst_parts[2]]
        except KeyError:
            registers[inst_parts[1]] = int(inst_parts[2])
    elif inst_parts[0] == "snd":
        if inst_parts[1] in registers:
            last_sound = registers[inst_parts[1]]

    return last_sound


def process_instructions(registers, instructions):
    instructions = instructions.split("\n")
    IP = 0
    last_sound = 0
    received = False

    while not received:
        instruction = instructions[IP]

        # print "{0} - {1}".format(IP, instruction)

        inst_parts = instruction.strip().split("\n")[0].split(" ")

        if inst_parts[0] == "jgz":
            if inst_parts[1] in registers and registers[inst_parts[1]] > 0:
                IP += int(inst_parts[2])
            else:
                IP += 1
        elif inst_parts[0] == "rcv":
            if inst_parts[1] in registers and registers[inst_parts[1]] > 0:
                received = True
                received_val = registers[inst_parts[1]]
            else:
                IP += 1
        else:
            last_sound = process_instruction(registers, last_sound, instruction)
            IP += 1

    return received_val, last_sound

# Tests

REGISTERS = {}
LAST_SOUND = 0

LAST_SOUND = process_instruction(REGISTERS, LAST_SOUND, "set a 1")
if "a" not in REGISTERS or REGISTERS["a"] != 1:
    print "Test 1 failed {0}".format(REGISTERS["a"])
    sys.exit(-1)
LAST_SOUND = process_instruction(REGISTERS, LAST_SOUND, "add a 2")
if "a" not in REGISTERS or REGISTERS["a"] != 3:
    print "Test 2 failed {0}".format(REGISTERS["a"])
    sys.exit(-1)
LAST_SOUND = process_instruction(REGISTERS, LAST_SOUND, "mul a a")
if "a" not in REGISTERS or REGISTERS["a"] != 9:
    print "Test 3 failed {0}".format(REGISTERS["a"])
    sys.exit(-1)
LAST_SOUND = process_instruction(REGISTERS, LAST_SOUND, "mod a 5")
if "a" not in REGISTERS or REGISTERS["a"] != 4:
    print "Test 4 failed {0}".format(REGISTERS["a"])
    sys.exit(-1)
LAST_SOUND = process_instruction(REGISTERS, LAST_SOUND, "snd a")
if LAST_SOUND != 4:
    print "Test 5 failed {0}".format(LAST_SOUND)
    sys.exit(-1)
LAST_SOUND = process_instruction(REGISTERS, LAST_SOUND, "set a 0")
if "a" not in REGISTERS or REGISTERS["a"] != 0:
    print "Test 6 failed {0}".format(REGISTERS["a"])
    sys.exit(-1)


INSTRUCTIONS ="""set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""
REGISTERS = {}
LAST_SOUND = 0

RECEIVED, LAST_SOUND = process_instructions(REGISTERS, INSTRUCTIONS)
if RECEIVED != 1:
    print "Test 7a failed {0}".format(RECEIVED)
    sys.exit(-1)
if LAST_SOUND != 4:
    print "Test 7b failed {0}".format(LAST_SOUND)
    sys.exit(-1)

print "All tests passed."

# All Tests passed

with open("input.txt", "r") as f:
    INSTRUCTIONS = f.read()
    REGISTERS = {}
    LAST_SOUND = 0

    RECEIVED, LAST_SOUND = process_instructions(REGISTERS, INSTRUCTIONS)

    print "Solution is {0}".format(LAST_SOUND)
