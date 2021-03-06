#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 14 of the Advent of Code for 2020.
"""
import re
import sys
from collections import defaultdict


def to_value(bits):
    value = 0
    digit = 2 ** 35

    for bit in bits:
        if bit == '1':
            value += digit
        
        digit /= 2

    return value


def to_bits(value):
    cmp_val = value
    digit = 2 ** 35
    bits = ''

    while digit > 0:
        if cmp_val / digit == 1:
            bits += '1'
            cmp_val -= digit
        else:
            bits += '0'

        digit /= 2

    return bits


def apply(mask, value):
    v_bits = to_bits(value)

    bit_val = ''
    for a, b in zip(mask, v_bits):
        if a == '1':
            bit_val += '1'
        elif a == '0':
            bit_val += '0'
        else:
            bit_val += b

    return to_value(bit_val)


def calculate_solution(program):
    mask = ""
    memory = defaultdict(int)
    max_mem = 0

    p = re.compile(r'\[(.*?)\]')

    for instruction in program:
        if instruction[:4] == 'mask':
            mask = instruction[7:]
        elif instruction[:3] == 'mem':
            m = p.findall(instruction)
            addr = int(m[0])
            value = int(instruction.split(' = ')[1])

            memory[addr] = apply(mask, value)

            if addr > max_mem:
                max_mem = addr

    result = 0
    for x in memory:
        result += memory[x]

    return result


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input)

    if result != expected_solution:
        print("Test for input {0} FAILED. Got a result of {1}, not {2}".format(test_input, result, expected_solution))
        sys.exit(-1)

    print("Test for input {0} passed.".format(test_input))

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.


print('000000000000000000000000000000001011', '<-- exp')
assert to_bits(11) == '000000000000000000000000000000001011'
assert to_bits(73) == '000000000000000000000000000001001001'
assert to_bits(101) == '000000000000000000000000000001100101'


puzzle_input = [
    "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
    "mem[8] = 11",
    "mem[7] = 101",
    "mem[8] = 0"
]
run_test(puzzle_input, 165)


print("")
print("-----------------")
print("All Tests PASSED.")
print("-----------------")
print("")

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data)

    print("Solution is {0}".format(answer))
