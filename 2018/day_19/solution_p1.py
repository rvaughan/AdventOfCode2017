#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 18 of the Advent of Code for 2018.
"""

from time import sleep



def execute_command(instruction, registers):
    if instruction[0] == "addi":
        registers[instruction[3]] = registers[instruction[1]] + instruction[2]
    elif instruction[0] == "addr":
        registers[instruction[3]] = registers[instruction[1]] + registers[instruction[2]]
    elif instruction[0] == "bani":
        registers[instruction[3]] = registers[instruction[1]] & instruction[2]
    elif instruction[0] == "banr":
        registers[instruction[3]] = registers[instruction[1]] & registers[instruction[2]]
    elif instruction[0] == "bori":
        registers[instruction[3]] = registers[instruction[1]] | instruction[2]
    elif instruction[0] == "borr":
        registers[instruction[3]] = registers[instruction[1]] | registers[instruction[2]]
    elif instruction[0] == "eqir":
        registers[instruction[3]] = 1 if instruction[1] == registers[instruction[2]] else 0
    elif instruction[0] == "eqri":
        registers[instruction[3]] = 1 if registers[instruction[1]] == instruction[2] else 0
    elif instruction[0] == "eqrr":
        registers[instruction[3]] = 1 if registers[instruction[1]] == registers[instruction[2]] else 0
    elif instruction[0] == "gtir":
        registers[instruction[3]] = 1 if instruction[1] > registers[instruction[2]] else 0
    elif instruction[0] == "gtri":
        registers[instruction[3]] = 1 if registers[instruction[1]] > instruction[2] else 0
    elif instruction[0] == "gtrr":
        registers[instruction[3]] = 1 if registers[instruction[1]] > registers[instruction[2]] else 0
    elif instruction[0] == "muli":
        registers[instruction[3]] = registers[instruction[1]] * instruction[2]
    elif instruction[0] == "mulr":
        registers[instruction[3]] = registers[instruction[1]] * registers[instruction[2]]
    elif instruction[0] == "seti":
        registers[instruction[3]] = instruction[1]
    elif instruction[0] == "setr":
        registers[instruction[3]] = registers[instruction[1]]
    else:
        print instruction[0]
        x


def load_instruction(instructions, ip, registers, initial_ip=0, verbose=False):
    instruction = instructions[ip]

    registers[initial_ip] = ip

    text_output = ""
    if verbose:
        text_output = "ip={} [".format(ip)
        text_output += ",".join([str(reg) for reg in registers])
        text_output += "] "
        text_output += instruction

    pieces = instruction.split(' ')
    pieces[1:] = [int(x) for x in pieces[1:]]

    execute_command(pieces, registers)

    if verbose:
        text_output += " ["
        text_output += ",".join([str(reg) for reg in registers])
        text_output += "]"

    if verbose:
        print text_output

    ip = registers[initial_ip]

    ip += 1

    return ip


def load_instruction_pointer(instruction, ip, registers, verbose=False):
    pieces = instruction.split(' ')
    ip = int(pieces[1])

    return ip


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

print ""
print "-----------------"
print "Testing.........."
print "-----------------"
print ""

test_input="""#ip 0
seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5"""

input_data = [line.strip() for line in test_input.splitlines()]

instructions = input_data[1:]

ip = 0
registers = [0] * 6
ip = load_instruction_pointer(input_data[0], ip, registers)

ip = load_instruction(instructions, ip, registers, verbose=True)
assert ip == 1, ip
assert registers[0] == 0
assert registers[1] == 5

ip = load_instruction(instructions, ip, registers, verbose=True)
assert ip == 2, ip
assert registers[0] == 1
assert registers[1] == 5
assert registers[2] == 6

ip = load_instruction(instructions, ip, registers, verbose=True)
assert ip == 4, ip
assert registers[0] == 3
assert registers[1] == 5
assert registers[2] == 6

ip = load_instruction(instructions, ip, registers, verbose=True)
assert ip == 6, ip
assert registers[0] == 5
assert registers[1] == 5
assert registers[2] == 6

ip = load_instruction(instructions, ip, registers, verbose=True)
assert ip == 7, ip
assert registers[0] == 6
assert registers[1] == 5
assert registers[2] == 6
assert registers[5] == 9

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [line.strip() for line in f]

    instructions = input_data[1:]

    ip = 0
    registers = [0] * 6
    init_ip = load_instruction_pointer(input_data[0], ip, registers)

    while ip < len(instructions):
        ip = load_instruction(instructions, ip, registers, initial_ip=init_ip)
        # sleep(1)

    print "Solution: {}".format(registers[0])
