#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 14 of the Advent of Code for 2018.
"""

import re


def do_addi(reg_start, instruction):
    reg_out = reg_start[:]

    reg_out[instruction[3]] = reg_start[instruction[1]] + instruction[2]

    return reg_out


def do_addr(reg_start, instruction):
    reg_out = reg_start[:]

    reg_out[instruction[3]] = reg_start[instruction[1]] + reg_start[instruction[2]]

    return reg_out


def do_bani(reg_start, instruction):
    reg_out = reg_start[:]

    reg_out[instruction[3]] = reg_start[instruction[1]] & instruction[2]

    return reg_out


def do_banr(reg_start, instruction):
    reg_out = reg_start[:]

    reg_out[instruction[3]] = reg_start[instruction[1]] & reg_start[instruction[2]]

    return reg_out


def do_bori(reg_start, instruction):
    reg_out = reg_start[:]

    reg_out[instruction[3]] = reg_start[instruction[1]] | instruction[2]

    return reg_out


def do_borr(reg_start, instruction):
    reg_out = reg_start[:]

    reg_out[instruction[3]] = reg_start[instruction[1]] | reg_start[instruction[2]]

    return reg_out


def do_mulr(reg_start, instruction):
    reg_out = reg_start[:]

    reg_out[instruction[3]] = reg_start[instruction[1]] * reg_start[instruction[2]]

    return reg_out


def do_muli(reg_start, instruction):
    reg_out = reg_start[:]

    reg_out[instruction[3]] = reg_start[instruction[1]] * instruction[2]

    return reg_out


def do_setr(reg_start, instruction):
    reg_out = reg_start[:]

    reg_out[instruction[3]] = reg_start[instruction[1]]

    return reg_out


def do_seti(reg_start, instruction):
    reg_out = reg_start[:]

    reg_out[instruction[3]] = instruction[1]

    return reg_out


def do_gtir(reg_start, instruction):
    reg_out = reg_start[:]

    if instruction[1] > reg_out[instruction[2]]:
        reg_out[instruction[3]] = 1
    else:
        reg_out[instruction[3]] = 0

    return reg_out


def do_gtri(reg_start, instruction):
    reg_out = reg_start[:]

    if reg_out[instruction[1]] > instruction[2]:
        reg_out[instruction[3]] = 1
    else:
        reg_out[instruction[3]] = 0

    return reg_out


def do_gtrr(reg_start, instruction):
    reg_out = reg_start[:]

    if reg_out[instruction[1]] > reg_out[instruction[2]]:
        reg_out[instruction[3]] = 1
    else:
        reg_out[instruction[3]] = 0

    return reg_out


def do_eqir(reg_start, instruction):
    reg_out = reg_start[:]

    if instruction[1] == reg_out[instruction[2]]:
        reg_out[instruction[3]] = 1
    else:
        reg_out[instruction[3]] = 0

    return reg_out


def do_eqri(reg_start, instruction):
    reg_out = reg_start[:]

    if reg_out[instruction[1]] == instruction[2]:
        reg_out[instruction[3]] = 1
    else:
        reg_out[instruction[3]] = 0

    return reg_out


def do_eqrr(reg_start, instruction):
    reg_out = reg_start[:]

    if reg_out[instruction[1]] == reg_out[instruction[2]]:
        reg_out[instruction[3]] = 1
    else:
        reg_out[instruction[3]] = 0

    return reg_out


def process_register_string(input_data):
    registers = []

    matches = re.search(r'[BA].*\[(\d+), (\d+), (\d+), (\d+)\]', input_data)
    if matches:
        reg_values = matches.groups()
        registers = [int(reg_value) for reg_value in reg_values]
    # else:
    #     print "No matches found!"

    return registers


def process_sample(opcodes, input_data):
    instruction_line = input_data[1]
    instruction_pieces = [int(piece) for piece in instruction_line.split(' ')]
    if instruction_pieces[0] in opcodes:
        return

    reg_start = process_register_string(input_data[0])
    reg_end = process_register_string(input_data[2])

    possible_insuctions = []

    if do_addi(reg_start, instruction_pieces) == reg_end:
        possible_insuctions.append('addi')

    if do_addr(reg_start, instruction_pieces) == reg_end:
        possible_insuctions.append('addr')

    if do_mulr(reg_start, instruction_pieces) == reg_end:
        possible_insuctions.append('mulr')

    if do_muli(reg_start, instruction_pieces) == reg_end:
        possible_insuctions.append('muli')

    if do_borr(reg_start, instruction_pieces) == reg_end:
        possible_insuctions.append('borr')

    if do_bori(reg_start, instruction_pieces) == reg_end:
        possible_insuctions.append('bori')

    if do_banr(reg_start, instruction_pieces) == reg_end:
        possible_insuctions.append('banr')

    if do_bani(reg_start, instruction_pieces) == reg_end:
        possible_insuctions.append('bani')

    if do_setr(reg_start, instruction_pieces) == reg_end:
        possible_insuctions.append('setr')

    if do_seti(reg_start, instruction_pieces) == reg_end:
        possible_insuctions.append('seti')

    if do_gtir(reg_start, instruction_pieces) == reg_end:
        possible_insuctions.append('gtir')

    if do_gtri(reg_start, instruction_pieces) == reg_end:
        possible_insuctions.append('gtri')

    if do_gtrr(reg_start, instruction_pieces) == reg_end:
        possible_insuctions.append('gtrr')

    if do_eqir(reg_start, instruction_pieces) == reg_end:
        possible_insuctions.append('eqir')

    if do_eqri(reg_start, instruction_pieces) == reg_end:
        possible_insuctions.append('eqri')

    if do_eqrr(reg_start, instruction_pieces) == reg_end:
        possible_insuctions.append('eqrr')

    if len(possible_insuctions) == 0:
        print "Couldn't identify instruction type!"
    elif len(possible_insuctions) == 1:
        opcodes[instruction_pieces[0]] = possible_insuctions[0]
    elif len(possible_insuctions) >= 3:
        opcodes[instruction_pieces[0]] = "triple"

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
result = do_addr([1, 2, 3, 4], [0, 1, 2, 3])
assert result == [1, 2, 3, 5], result

print "Test 4... check ADDI command"
result = do_addi([1, 2, 3, 4], [0, 1, 2, 3])
assert result == [1, 2, 3, 4], result

print "Test 3... check MULR command"
result = do_mulr([3, 2, 1, 1], [9, 2, 1, 2])
assert result == [3, 2, 2, 1], result

print "Test 4... check MULI command"
result = do_muli([1, 2, 2, 2], [9, 2, 1, 2])
assert result == [1, 2, 2, 2], result

print "Test 5... check BORR command"
result = do_borr([1, 2, 3, 4], [0, 1, 2, 3])
assert result == [1, 2, 3, 3], result

print "Test 6... check BORI command"
result = do_bori([1, 2, 2, 2], [0, 1, 2, 3])
assert result == [1, 2, 2, 2], result

print "Test 7... check BANR command"
result = do_banr([1, 2, 3, 4], [0, 1, 2, 3])
assert result == [1, 2, 3, 2], result

print "Test 8... check BANI command"
result = do_bani([1, 2, 2, 2], [0, 1, 2, 3])
assert result == [1, 2, 2, 2], result

print "Test 9... check SETR command"
result = do_setr([0, 9, 0, 0], [0, 1, 2, 3])
assert result == [0, 9, 0, 9], result

print "Test 10... check SETI command"
result = do_bani([0, 9, 0, 0], [0, 1, 2, 3])
assert result == [0, 9, 0, 0], result

print "Test 11... check GTIR command"
result = do_gtir([1, 2, 2, 2], [0, 1, 2, 3])
assert result == [1, 2, 2, 0], result

print "Test 12... check GTRI command"
result = do_gtri([1, 2, 2, 2], [0, 1, 2, 3])
assert result == [1, 2, 2, 0], result

print "Test 13... check GTRR command"
result = do_gtrr([1, 2, 2, 2], [0, 1, 2, 3])
assert result == [1, 2, 2, 0], result

print "Test 14... check EQIR command"
result = do_eqir([1, 2, 2, 2], [0, 1, 2, 3])
assert result == [1, 2, 2, 0], result

print "Test 15... check EQRI command"
result = do_eqri([1, 2, 2, 2], [0, 1, 2, 3])
assert result == [1, 2, 2, 1], result

print "Test 16... check EQRR command"
result = do_eqrr([1, 2, 2, 2], [0, 1, 2, 3])
assert result == [1, 2, 2, 1], result

print "Test 17... correct sample processing"
registers = [0, 0, 0, 0]
opcodes = [''] * 16
test_input="""Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]"""
input_data = [line.strip() for line in test_input.splitlines()]
process_sample(opcodes, input_data)
assert opcodes[9] == "triple", opcodes[9]


print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [line.strip() for line in f]

    num_samples = 0
    num_triples = 0
    cur_line = 0
    while cur_line < len(input_data):
        if len(input_data[cur_line]) == 0:
            cur_line += 1
        else:
            opcodes = [''] * 16
            if input_data[cur_line][0] == 'B':
                num_samples += 1
                process_sample(opcodes, input_data[cur_line:cur_line+3])
                cur_line += 4

                num_triples += sum([1 if code == "triple" else 0 for code in opcodes])
            else:
                cur_line += 1

    print "Solution: {} [saw {} samples]".format(num_triples, num_samples)
