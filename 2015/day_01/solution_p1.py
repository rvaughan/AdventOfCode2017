#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 1 of the Advent of Code for 2015.
"""

import sys

def do_moves(data):
    current_floor = 0

    for movement in data:
        if movement == "(":
            current_floor += 1
        elif movement == ")":
            current_floor -= 1

    return current_floor


def run_test(data, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = do_moves(data)

    if result != expected_solution:
        print "Test for data '{0}' FAILED. Got a result of {1}, not {2}".format(data, result, expected_solution)
        sys.exit(-1)

    print "Test for captcha '{0}' passed.".format(data)

# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

run_test("(())", 0)
run_test("()()", 0)
run_test("(((", 3)
run_test("(()(()(", 3)
run_test("))(((((", 3)
run_test("())", -1)
run_test("))(", -1)
run_test(")))", -3)
run_test(")())())", -3)

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    elevator_data = f.readline()

    print "Final floor: {}".format(do_moves(elevator_data))
