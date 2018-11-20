#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 1 of the Advent of Code for 2017.
"""

import sys


def solve_captcha(captcha):
    """
    Method for trying to solve the captcha.
    """
    solution = 0

    prev_digit = captcha[-1]

    for digit in captcha:
        if prev_digit == digit:
            solution += int(digit)

        prev_digit = digit

    return solution


def run_test(test_captcha, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = solve_captcha(test_captcha)

    if result != expected_solution:
        print "Test for captcha {0} FAILED. Got a result of {1}, not {2}".format(test_captcha, result, expected_solution)
        sys.exit(-1)

    print "Test for captcha {0} passed.".format(test_captcha)

# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

run_test("1122", 3)
run_test("1111", 4)
run_test("1234", 0)
run_test("91212129", 9)

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    CAPTCHA = f.readline()

    print "Captcha solution is {0}".format(solve_captcha(CAPTCHA))
