#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 23 of the Advent of Code for 2017.
"""

from collections import defaultdict
import sys


def process_instruction(registers, instruction):
    inst_parts = instruction.strip().split("\n")[0].split(" ")

    if inst_parts[0] == "add":
        try:
            registers[inst_parts[1]] += int(inst_parts[2])
        except ValueError:
            registers[inst_parts[1]] += registers[inst_parts[2]]
    elif inst_parts[0] == "mod":
        try:
            registers[inst_parts[1]] %= int(inst_parts[2])
        except ValueError:
            registers[inst_parts[1]] %= registers[inst_parts[2]]
    elif inst_parts[0] == "mul":
        try:
            registers[inst_parts[1]] *= int(inst_parts[2])
        except ValueError:
            registers[inst_parts[1]] *= registers[inst_parts[2]]
        return 1
    elif inst_parts[0] == "set":
        try:
            registers[inst_parts[1]] = int(inst_parts[2])
        except ValueError:
            registers[inst_parts[1]] = registers[inst_parts[2]]
    # elif inst_parts[0] == "snd":
    #     last_sound = registers[inst_parts[1]]
    elif inst_parts[0] == "sub":
        try:
            registers[inst_parts[1]] -= int(inst_parts[2])
        except ValueError:
            registers[inst_parts[1]] -= registers[inst_parts[2]]

    return 0


def process_instructions(registers, instructions):
    instructions = instructions.split("\n")
    inst_ptr = 0
    mul_count = 0

    while inst_ptr < len(instructions):
        instruction = instructions[inst_ptr]

        # print "{0} - {1}".format(inst_ptr, instruction)

        inst_parts = instruction.strip().split("\n")[0].split(" ")

        # if inst_parts[0] == "jgz":
        #     if registers[inst_parts[1]] > 0:
        #         inst_ptr += int(inst_parts[2])
        #     else:
        #         inst_ptr += 1
        if inst_parts[0] == "jnz":
            try:
                if int(inst_parts[1]) != 0:
                    try:
                        inst_ptr += int(inst_parts[2])
                    except ValueError:
                        inst_ptr += registers[inst_parts[2]]
                else:
                    inst_ptr += 1
            except ValueError:
                if registers[inst_parts[1]] != 0:
                    try:
                        inst_ptr += int(inst_parts[2])
                    except ValueError:
                        inst_ptr += registers[inst_parts[2]]
                else:
                    inst_ptr += 1
        # elif inst_parts[0] == "rcv":
        #     if registers[inst_parts[1]] > 0:
        #         received_val = registers[inst_parts[1]]
        #     else:
        #         inst_ptr += 1
        else:
            mul_count += process_instruction(registers, instruction)
            inst_ptr += 1

        # print inst_ptr, registers

    return mul_count

# Tests

REGISTERS = defaultdict(int)
MUL = 0

MUL_COUNT = process_instruction(REGISTERS, "set a 1")
if REGISTERS["a"] != 1:
    print "Test 1 failed {0}".format(REGISTERS["a"])
    print REGISTERS
    sys.exit(-1)
print "Test 1 passed"

MUL_COUNT = process_instruction(REGISTERS, "add a 2")
if REGISTERS["a"] != 3:
    print "Test 2 failed {0}".format(REGISTERS["a"])
    sys.exit(-1)
print "Test 2 passed"

MUL_COUNT = process_instruction(REGISTERS, "mul a a")
if REGISTERS["a"] != 9:
    print "Test 3 (mul) failed {0}".format(REGISTERS["a"])
    sys.exit(-1)
if MUL_COUNT != 1:
    print "Test 3 (count) failed {0}".format(MUL_COUNT)
    sys.exit(-1)
print "Test 3 passed"

MUL_COUNT = process_instruction(REGISTERS, "mod a 5")
if REGISTERS["a"] != 4:
    print "Test 4 failed {0}".format(REGISTERS["a"])
    sys.exit(-1)
print "Test 4 passed"

MUL_COUNT = process_instruction(REGISTERS, "set a 0")
if REGISTERS["a"] != 0:
    print "Test 5 failed {0}".format(REGISTERS["a"])
    sys.exit(-1)
print "Test 5 passed"


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
REGISTERS = defaultdict(int)
MUL_COUNT = 0

MUL_COUNT = process_instructions(REGISTERS, INSTRUCTIONS)
if MUL_COUNT != 1:
    print "Test 6 failed {0}".format(MUL_COUNT)
    sys.exit(-1)
print "Test 6 passed"

print "All tests passed."

# All good

# Shortcut solution

# Use the values of registers b and c (which are constant) to bound the
# problem, and the value 17 from instruction #31 to increment.
# The program appears to be trying to understand if there are any prime
# factors for the number other than itself. H is the count of such numbers
# between the start and end ranges.
B = 105700
C = 122700
H = 0
for x in range(B, C + 1, 17):
    for i in range(2, x):
        if x % i == 0:
            H += 1
            break
print "(shortcut) Solution is {0}".format(H)

# Full brute force solution - although as far as I can tell, my program
# can never end due to the final jnz instruction.

REGISTERS = defaultdict(int)
REGISTERS["a"] = 1
with open("input.txt", "r") as f:
    INSTRUCTIONS = f.read()

    MUL_COUNT = process_instructions(REGISTERS, INSTRUCTIONS)

    print "Solution is {0}".format(REGISTERS["h"])
