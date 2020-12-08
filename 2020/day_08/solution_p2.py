#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 8 of the Advent of Code for 2020.
"""
import sys
from collections import defaultdict


def calculate_solution(opn_list):
    last_changed = 0
    success = False

    last_op = len(opn_list) - 1
    # print('Last op', last_op)

    # We have to brute force this solution, changing one instruction at a time
    # until we get a program that runs to completion.
    while not success:
        accumulator = 0
        operation = 0
        next_operation = 0
        finished = False

        executed_ops = defaultdict(int)
        executed_ops[0] = True

        while not finished:
            op, val = opn_list[operation].split(' ')

            if op == "nop":
                if operation == last_changed:
                    next_operation = operation + int(val)
                else:
                    next_operation = operation + 1
            elif op == "acc":
                next_operation = operation + 1
                accumulator += int(val)
            elif op == "jmp":
                if operation == last_changed:
                    next_operation = operation + 1
                else:
                    next_operation = operation + int(val)

            # print(operation, op, val, accumulator, next_operation)

            if executed_ops[next_operation] == True:
                # print('Infinite loop detected :(')
                finished = True

            executed_ops[next_operation] = True
            operation = next_operation

            # Are we done?
            if operation > last_op:
                finished = True
                success = True

        if not success:
            last_changed += 1

    return accumulator


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

instructions = [
    "nop +0",
    "acc +1",
    "jmp +4",
    "acc +3",
    "jmp -3",
    "acc -99",
    "acc +1",
    "jmp -4",
    "acc +6"
]
run_test(instructions, 8)

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
