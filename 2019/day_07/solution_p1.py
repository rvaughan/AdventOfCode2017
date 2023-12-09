#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 7 of the Advent of Code for 2019.
"""
import itertools
import sys

input_code = 0
input_code_2 = 0
output_code = 0

def run_op(program, inst_ptr):
    global input_code
    global input_code_2
    global output_code

    # print("IP: {} [{}]".format(inst_ptr, len(program)))
    digits = [int(x) for x in str(program[inst_ptr])]
    op = (0 if len(digits) == 1 else digits[-2]) * 10+digits[-1]
    # print(inst_ptr, op)
    digits = digits[:-2]

    if op == 1:
        # print('add', program)
        while (len(digits) < 3):
            digits = [0] + digits

        i1, i2, i3 = program[inst_ptr+1], program[inst_ptr+2], program[inst_ptr+3]
        program[i3] = (i1 if digits[2] == 1 else program[i1]) + (i2 if digits[1] == 1 else program[i2])

        # print('   ', program)
        return 0, program, inst_ptr + 4
    elif op == 2:
        # print('mult')

        while (len(digits) < 3):
            digits = [0] + digits

        i1,i2,i3 = program[inst_ptr+1], program[inst_ptr+2], program[inst_ptr+3]
        program[i3] = (i1 if digits[2] == 1 else program[i1]) * (i2 if digits[1] == 1 else program[i2])

        # print('    ', program)
        return 0, program, inst_ptr + 4
    elif op == 3:
        # print('set')
        program[program[inst_ptr+1]] = input_code   # special input specified in puzzle
                                                    # representing the system to be
                                                    # diagnosed.

        input_code = input_code_2

        return 0, program, inst_ptr + 2
    elif op == 4:
        # print('output')
        # print(f'output: {program[program[inst_ptr+1]]}')
        output_code = program[program[inst_ptr+1]]

        return 0, program, inst_ptr + 2
    elif op == 5:
        # print('jump-if-true')
        while (len(digits) < 3):
            digits = [0] + digits

        i1, i2 = program[inst_ptr+1], program[inst_ptr+2]
        val = (i1 if digits[2] == 1 else program[i1])
        if val != 0:
            inst_ptr = (i2 if digits[1] == 1 else program[i2])
        else:
            inst_ptr += 3

        return 0, program, inst_ptr
    elif op == 6:
        # print('jump-if-false')
        while (len(digits) < 3):
            digits = [0] + digits

        i1, i2 = program[inst_ptr+1], program[inst_ptr+2]
        val = (i1 if digits[2] == 1 else program[i1])
        if val == 0:
            inst_ptr = (i2 if digits[1] == 1 else program[i2])
        else:
            inst_ptr += 3

        return 0, program, inst_ptr
    elif op == 7:
        # print('less than')
        while (len(digits) < 3):
            digits = [0] + digits

        i1, i2, i3 = program[inst_ptr+1], program[inst_ptr+2], program[inst_ptr+3]
        p1 = (i1 if digits[2] == 1 else program[i1])
        p2 = (i2 if digits[1] == 1 else program[i2])
        p3 = (i3 if digits[0] == 1 else program[i3])

        if p1 < p2:
            program[i3] = 1
        else:
            program[i3] = 0

        return 0, program, inst_ptr + 4
    elif op == 8:
        # print('equals')
        while (len(digits) < 3):
            digits = [0] + digits

        i1, i2, i3 = program[inst_ptr+1], program[inst_ptr+2], program[inst_ptr+3]
        p1 = (i1 if digits[2] == 1 else program[i1])
        p2 = (i2 if digits[1] == 1 else program[i2])
        p3 = (i3 if digits[0] == 1 else program[i3])

        print('==', i1, i2, i3, p1, p2, p3)

        if p1 == p2:
            program[i3] = 1
        else:
            program[i3] = 0

        return 0, program, inst_ptr + 4
    elif op == 99:
        # print('end')
        return 1, program, inst_ptr + 1
    else:
        # print('???')
        return -1, program, inst_ptr + 1


def run_program(test_input, amplifier_values):
    global input_code
    global input_code_2
    global inst_ptr
    global output_code

    inst_ptr = 0
    result = 0
    program = test_input

    input_code_2 = 0

    for amplifier in amplifier_values:
        input_code = amplifier

        while result == 0:
            result, program, inst_ptr = run_op(program, inst_ptr)
            # print(result, program[inst_ptr:])

        input_code_2 = output_code
        inst_ptr = 0
        program = test_input
        result = 0

    return output_code


def run_test(test_input, amplifier_values, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    print(f'Verifying: {test_input}')

    result = run_program(test_input, amplifier_values)

    if result != expected_solution:
        print("Test FAILED. Got a result of {}, not {}".format(result, expected_solution))
        sys.exit(-1)

    print("Test passed.".format(test_input))

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

run_test([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0], [4,3,2,1,0], 43210)

run_test([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0], [0,1,2,3,4], 54321)

run_test([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0], [1,0,4,3,2], 65210)

print("")
print("-----------------")
print("All Tests PASSED.")
print("-----------------")
print("")

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    program = [int(x) for x in f.readline().split(',')]


    max_output = 0

    inputs = [0,1,2,3,4]
    for combination in itertools.permutations(inputs, 5):
        max_output = max(max_output, run_program(program, combination))

    print('Solution:', max_output)
