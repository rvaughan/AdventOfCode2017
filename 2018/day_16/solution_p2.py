#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 16 of the Advent of Code for 2018.
"""

import re


def do_addi(reg_start, instruction):
    reg_start[instruction[3]] = reg_start[instruction[1]] + instruction[2]


def do_addr(reg_start, instruction):
    reg_start[instruction[3]] = reg_start[instruction[1]] + reg_start[instruction[2]]


def do_bani(reg_start, instruction):
    reg_start[instruction[3]] = reg_start[instruction[1]] & instruction[2]


def do_banr(reg_start, instruction):
    reg_start[instruction[3]] = reg_start[instruction[1]] & reg_start[instruction[2]]


def do_bori(reg_start, instruction):
    reg_start[instruction[3]] = reg_start[instruction[1]] | instruction[2]


def do_borr(reg_start, instruction):
    reg_start[instruction[3]] = reg_start[instruction[1]] | reg_start[instruction[2]]


def do_mulr(reg_start, instruction):
    reg_start[instruction[3]] = reg_start[instruction[1]] * reg_start[instruction[2]]


def do_muli(reg_start, instruction):
    reg_start[instruction[3]] = reg_start[instruction[1]] * instruction[2]


def do_setr(reg_start, instruction):
    reg_start[instruction[3]] = reg_start[instruction[1]]


def do_seti(reg_start, instruction):
    reg_start[instruction[3]] = instruction[1]


def do_gtir(reg_start, instruction):
    if instruction[1] > reg_start[instruction[2]]:
        reg_start[instruction[3]] = 1
    else:
        reg_start[instruction[3]] = 0


def do_gtri(reg_start, instruction):
    if reg_start[instruction[1]] > instruction[2]:
        reg_start[instruction[3]] = 1
    else:
        reg_start[instruction[3]] = 0


def do_gtrr(reg_start, instruction):
    if reg_start[instruction[1]] > reg_start[instruction[2]]:
        reg_start[instruction[3]] = 1
    else:
        reg_start[instruction[3]] = 0


def do_eqir(reg_start, instruction):
    if instruction[1] == reg_start[instruction[2]]:
        reg_start[instruction[3]] = 1
    else:
        reg_start[instruction[3]] = 0


def do_eqri(reg_start, instruction):
    if reg_start[instruction[1]] == instruction[2]:
        reg_start[instruction[3]] = 1
    else:
        reg_start[instruction[3]] = 0


def do_eqrr(reg_start, instruction):
    if reg_start[instruction[1]] == reg_start[instruction[2]]:
        reg_start[instruction[3]] = 1
    else:
        reg_start[instruction[3]] = 0


def process_register_string(input_data):
    registers = []

    matches = re.search(r'[BA].*\[(\d+), (\d+), (\d+), (\d+)\]', input_data)
    if matches:
        reg_values = matches.groups()
        registers = [int(reg_value) for reg_value in reg_values]
    # else:
    #     print "No matches found!"

    return registers


def _process_sample_data(possible_insuctions, input_data):
    instruction_line = input_data[1]
    instruction_pieces = [int(piece) for piece in instruction_line.split(' ')]

    reg_start = process_register_string(input_data[0])
    reg_end = process_register_string(input_data[2])

    reg_start = process_register_string(input_data[0])
    do_addi(reg_start, instruction_pieces)
    if reg_start == reg_end:
        possible_insuctions.append('addi')

    reg_start = process_register_string(input_data[0])
    do_addr(reg_start, instruction_pieces)
    if reg_start == reg_end:
        possible_insuctions.append('addr')

    reg_start = process_register_string(input_data[0])
    do_mulr(reg_start, instruction_pieces)
    if reg_start == reg_end:
        possible_insuctions.append('mulr')

    reg_start = process_register_string(input_data[0])
    do_muli(reg_start, instruction_pieces)
    if reg_start == reg_end:
        possible_insuctions.append('muli')

    reg_start = process_register_string(input_data[0])
    do_borr(reg_start, instruction_pieces)
    if reg_start == reg_end:
        possible_insuctions.append('borr')

    reg_start = process_register_string(input_data[0])
    do_bori(reg_start, instruction_pieces)
    if reg_start == reg_end:
        possible_insuctions.append('bori')

    reg_start = process_register_string(input_data[0])
    do_banr(reg_start, instruction_pieces)
    if reg_start == reg_end:
        possible_insuctions.append('banr')

    reg_start = process_register_string(input_data[0])
    do_bani(reg_start, instruction_pieces)
    if reg_start == reg_end:
        possible_insuctions.append('bani')

    reg_start = process_register_string(input_data[0])
    do_setr(reg_start, instruction_pieces)
    if reg_start == reg_end:
        possible_insuctions.append('setr')

    reg_start = process_register_string(input_data[0])
    do_seti(reg_start, instruction_pieces)
    if reg_start == reg_end:
        possible_insuctions.append('seti')

    reg_start = process_register_string(input_data[0])
    do_gtir(reg_start, instruction_pieces)
    if reg_start == reg_end:
        possible_insuctions.append('gtir')

    reg_start = process_register_string(input_data[0])
    do_gtri(reg_start, instruction_pieces)
    if reg_start == reg_end:
        possible_insuctions.append('gtri')

    reg_start = process_register_string(input_data[0])
    do_gtrr(reg_start, instruction_pieces)
    if reg_start == reg_end:
        possible_insuctions.append('gtrr')

    reg_start = process_register_string(input_data[0])
    do_eqir(reg_start, instruction_pieces)
    if reg_start == reg_end:
        possible_insuctions.append('eqir')

    reg_start = process_register_string(input_data[0])
    do_eqri(reg_start, instruction_pieces)
    if reg_start == reg_end:
        possible_insuctions.append('eqri')

    reg_start = process_register_string(input_data[0])
    do_eqrr(reg_start, instruction_pieces)
    if reg_start == reg_end:
        possible_insuctions.append('eqrr')

    return instruction_pieces[0]


def process_sample(sampled_opcodes, input_data):
    possible_opcodes = []
    opcode = _process_sample_data(possible_opcodes, input_data)

    # print opcode, possible_opcodes

    if opcode not in sampled_opcodes:
        sampled_opcodes[opcode] = set(possible_opcodes)
    else:
        [sampled_opcodes[opcode].add(item) for item in possible_opcodes]


def execute(registers, opcodes, input_data):
    instruction_pieces = [int(piece) for piece in input_data.split(' ')]

    if opcodes[instruction_pieces[0]] == "addi":
        registers = do_addi(registers, instruction_pieces)
    elif opcodes[instruction_pieces[0]] == "addr":
        registers = do_addr(registers, instruction_pieces)
    elif opcodes[instruction_pieces[0]] == "bani":
        registers = do_bani(registers, instruction_pieces)
    elif opcodes[instruction_pieces[0]] == "banr":
        registers = do_banr(registers, instruction_pieces)
    elif opcodes[instruction_pieces[0]] == "bori":
        registers = do_bori(registers, instruction_pieces)
    elif opcodes[instruction_pieces[0]] == "borr":
        registers = do_borr(registers, instruction_pieces)
    elif opcodes[instruction_pieces[0]] == "eqir":
        registers = do_eqir(registers, instruction_pieces)
    elif opcodes[instruction_pieces[0]] == "eqri":
        registers = do_eqri(registers, instruction_pieces)
    elif opcodes[instruction_pieces[0]] == "eqrr":
        registers = do_eqrr(registers, instruction_pieces)
    elif opcodes[instruction_pieces[0]] == "gtir":
        registers = do_gtir(registers, instruction_pieces)
    elif opcodes[instruction_pieces[0]] == "gtri":
        registers = do_gtri(registers, instruction_pieces)
    elif opcodes[instruction_pieces[0]] == "gtrr":
        registers = do_gtrr(registers, instruction_pieces)
    elif opcodes[instruction_pieces[0]] == "muli":
        registers = do_muli(registers, instruction_pieces)
    elif opcodes[instruction_pieces[0]] == "mulr":
        registers = do_mulr(registers, instruction_pieces)
    elif opcodes[instruction_pieces[0]] == "seti":
        registers = do_seti(registers, instruction_pieces)
    elif opcodes[instruction_pieces[0]] == "setr":
        registers = do_setr(registers, instruction_pieces)
    else:
        print "Unknown instruction: '{}' [opcode={}]".format(opcodes[instruction_pieces[0]], instruction_pieces[0])


def winnow_opcodes(sampled_opcodes):
    opcodes = {}

    # The insight here is that at each pass through the opcodes list one of them
    # will only have a single possible opcode, which we can then use to slowly
    # winnow out the possibilities.

    while len(sampled_opcodes) > 0:
        tmp_opcodes = sampled_opcodes.copy()
        for key in tmp_opcodes:
            possibilities = set(sampled_opcodes[key])
            if len(possibilities) == 1:
                # print key, possibilities
                opcodes[key] = possibilities.pop()
                del sampled_opcodes[key]
                # print len(sampled_opcodes)

                for x in sampled_opcodes:
                    possibilities = set(sampled_opcodes[x])
                    if opcodes[key] in possibilities:
                        possibilities.remove(opcodes[key])
                        sampled_opcodes[x] = possibilities
                continue

    return opcodes


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

print ""
print "-----------------"
print "Testing.........."
print "-----------------"
print ""

print "Test 1... we can split register info"
register = process_register_string("Before: [3, 2, 1, 1]")
assert register == [3, 2, 1, 1], register

print "Test 2... another register split info check"
register = process_register_string("After:  [3, 2, 2, 1]")
assert register == [3, 2, 2, 1], register

print "Test 3... check ADDR command"
registers = [1, 2, 3, 4]
do_addr(registers, [0, 1, 2, 3])
assert registers == [1, 2, 3, 5], registers

print "Test 4... check ADDI command"
registers = [1, 2, 3, 4]
do_addi(registers, [0, 1, 4, 3])
assert registers == [1, 2, 3, 6], registers

print "Test 3... check MULR command"
registers = [3, 2, 1, 1]
do_mulr(registers, [9, 2, 1, 2])
assert registers == [3, 2, 2, 1], registers

print "Test 4... check MULI command"
registers = [1, 2, 2, 2]
do_muli(registers, [9, 2, 1, 2])
assert registers == [1, 2, 2, 2], registers

print "Test 5... check BORR command"
registers = [1, 2, 3, 4]
do_borr(registers, [0, 1, 2, 3])
assert registers == [1, 2, 3, 3], registers

print "Test 6... check BORI command"
registers = [1, 2, 2, 2]
do_bori(registers, [0, 1, 2, 3])
assert registers == [1, 2, 2, 2], registers

print "Test 7... check BANR command"
registers = [1, 2, 3, 4]
do_banr(registers, [0, 1, 2, 3])
assert registers == [1, 2, 3, 2], registers

print "Test 8... check BANI command"
registers = [1, 2, 2, 2]
do_bani(registers, [0, 1, 2, 3])
assert registers == [1, 2, 2, 2], registers

print "Test 9... check SETR command"
registers = [0, 9, 0, 0]
do_setr(registers, [0, 1, 2, 3])
assert registers == [0, 9, 0, 9], registers

print "Test 10... check SETI command"
registers = [0, 9, 0, 0]
do_bani(registers, [0, 1, 2, 3])
assert registers == [0, 9, 0, 0], registers

print "Test 11... check GTIR command"
registers = [1, 2, 2, 2]
do_gtir(registers, [0, 1, 2, 3])
assert registers == [1, 2, 2, 0], registers

print "Test 12... check GTRI command"
registers = [1, 2, 2, 2]
do_gtri(registers, [0, 1, 2, 3])
assert registers == [1, 2, 2, 0], registers

print "Test 13... check GTRR command"
registers = [1, 2, 2, 2]
do_gtrr(registers, [0, 1, 2, 3])
assert registers == [1, 2, 2, 0], registers

print "Test 14... check EQIR command"
registers = [1, 2, 2, 2]
do_eqir(registers, [0, 1, 2, 3])
assert registers == [1, 2, 2, 0], registers

print "Test 15... check EQRI command"
registers = [1, 2, 2, 2]
do_eqri(registers, [0, 1, 2, 3])
assert registers == [1, 2, 2, 1], registers

print "Test 16... check EQRR command"
registers = [1, 2, 2, 2]
do_eqrr(registers, [0, 1, 2, 3])
assert registers == [1, 2, 2, 1], registers


print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [line.strip() for line in f]

    opcodes = None
    sampled_opcodes = {}
    registers = [0, 0, 0 ,0]
    cur_line = 0
    while cur_line < len(input_data):
        if len(input_data[cur_line]) == 0:
            cur_line += 1
            if opcodes is None:
                # This is the first time we reach here. We need to winnow down
                # the opcodes.
                # print "winnowing..."
                opcodes = winnow_opcodes(sampled_opcodes)
                # print "...complete"
        else:
            if input_data[cur_line][0] == 'B':
                process_sample(sampled_opcodes, input_data[cur_line:cur_line+3])
                cur_line += 4
            else:
                execute(registers, opcodes, input_data[cur_line])
                # print registers
                cur_line += 1

    print "Solution: {}".format(registers[0])
