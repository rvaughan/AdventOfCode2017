#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 5 of the Advent of Code for 2019.
"""

import math
import sys

POSITION_MODE = 0
IMMEDIATE_MODE = 1


def run_op(program, inst_ptr):
    # print('->', program, inst_ptr)
    digits = [int(x) for x in str(program[inst_ptr])]
    # print('>>', digits)
    # print('*' if len(digits) < 3 else digits[-3])
    # print('*' if len(digits) < 4 else digits[-4])
    # print('*' if len(digits) < 5 else digits[-5])
    op = (0 if len(digits) == 1 else digits[-2]) * 10+digits[-1]
    mode_1 = False if len(digits) < 3 else digits[-3] == 1
    mode_2 = False if len(digits) < 4 else digits[-4] == 1
    mode_3 = False if len(digits) < 5 else digits[-5] == 1
    # print(op, mode_1, mode_2, mode_3)
    digits = digits[:-2]

    if op == 1:
        # print('add', program)
        while (len(digits) < 3):
            digits = [0] + digits

        i1, i2, i3 = program[inst_ptr+1], program[inst_ptr+2], program[inst_ptr+3]
        program[i3] = (i1 if mode_1 else program[i1]) + (i2 if mode_2 else program[i2])

        # print('   ', program)
        return 0, program, inst_ptr + 4
    elif op == 2:
        # print('mult')

        while (len(digits) < 3):
            digits = [0] + digits

        i1, i2, i3 = program[inst_ptr+1], program[inst_ptr+2], program[inst_ptr+3]
        program[i3] = (i1 if mode_1 else program[i1]) * (i2 if mode_2 else program[i2])

        # print('    ', program)
        # print('mult', program[i3], i1, program[i1], i2, program[i2])
        return 0, program, inst_ptr + 4
    elif op == 3:
        # print('set')
        if mode_1:
            program
        program[program[inst_ptr+1]] = 1    # special input specified in puzzle
                                            # representing the system to be
                                            # diagnosed.
        return 0, program, inst_ptr + 2
    elif op == 4:
        # print('output')
        print(program[program[inst_ptr+1]])

        return 0, program, inst_ptr + 2
    elif op == 99:
        # print('end')
        return 1, program, inst_ptr + 1
    else:
        print('UNKNOWN', op)
        return -1, program, inst_ptr + 1


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    # print(test_input)
    inst_ptr = 0
    result = 0
    program = test_input
    while result == 0:
        result, program, inst_ptr = run_op(program, inst_ptr)

    if test_input != expected_solution:
        print("Test FAILED. Got a result of {}, not {}".format(test_input, expected_solution))
        sys.exit(-1)

    print("Test passed.".format(test_input))

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

# The tests from day 2.
run_test([1,9,10,3,2,3,11,0,99,30,40,50], [3500,9,10,70,2,3,11,0,99,30,40,50])
run_test([1,0,0,0,99], [2,0,0,0,99])
run_test([2,3,0,3,99], [2,3,0,6,99])
run_test([2,4,4,5,99,0], [2,4,4,5,99,9801])
run_test([1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99])

# The tests from this day (day 5).
run_test([1002,4,3,4,33], [1002,4,3,4,99])
run_test([3,0,4,0,99], [1,0,4,0,99])

print("")
print("-----------------")
print("All Tests PASSED.")
print("-----------------")
print("")

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    program = [int(x) for x in f.readline().split(',')]
    # print(program)
    inst_ptr = 0
    result = 0
    while result == 0:
        result, program, inst_ptr = run_op(program, inst_ptr)

        # print(result, program, inst_ptr)
