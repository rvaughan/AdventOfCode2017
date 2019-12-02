#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 2 of the Advent of Code for 2019.
"""

import math
import sys


def run_op(program, pos):
    op = program[pos]
    # print(pos, op)

    if op == 1:
        # print('add', program)
        program[program[pos+3]] = program[program[pos+1]] + program[program[pos+2]]
        # print('   ', program)
        return 0, program
    elif op == 2:
        # print('mult')
        program[program[pos+3]] = program[program[pos+1]] * program[program[pos+2]]
        # print('    ', program)
        return 0, program
    elif op == 99:
        # print('end')
        return 1, program
    else:
        # print('???')
        return -1, program


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    pos = 0
    result = 0
    program = test_input
    while result == 0:
        result, program = run_op(program, pos)
        pos += 4

    if test_input != expected_solution:
        print "Test FAILED. Got a result of {}, not {}".format(test_input, expected_solution)
        sys.exit(-1)

    print "Test passed.".format(test_input)

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

run_test([1,9,10,3,2,3,11,0,99,30,40,50], [3500,9,10,70,2,3,11,0,99,30,40,50])
run_test([1,0,0,0,99], [2,0,0,0,99])
run_test([2,3,0,3,99], [2,3,0,6,99])
run_test([2,4,4,5,99,0], [2,4,4,5,99,9801])
run_test([1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99])

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    program = [int(x) for x in f.readline().split(',')]
    program[1] = 65
    program[2] = 77
    # print(program)
    pos = 0
    result = 0
    while result == 0:
        result, program = run_op(program, pos)
        pos += 4

    print "Solution is {0}".format(program[0])
    print("Difference = {}".format(19690720 - program[0]))
    print('{}'.format(65*100 + 77))
