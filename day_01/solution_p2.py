#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 1 of the Advent of Code for 2017.
"""

import sys


def check_digits(digit_a, digit_b):
    """
    Check to see if the two digits are the same.
    """
    return digit_a == digit_b


def solve_captcha(captcha):
    """
    Method for solving the captcha.
    """
    solution = 0

    list_size = len(captcha)
    mid_point = list_size / 2

    for idx in xrange(list_size):

        pos = (idx + mid_point) % list_size

        solution += int(captcha[idx]) if check_digits(captcha[idx], captcha[pos]) else 0

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

run_test("1212", 6)
run_test("1221", 0)
run_test("123425", 4)
run_test("123123", 12)
run_test("12131415", 4)

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    CAPTCHA = f.readline()

    print "Captcha solution is {0}".format(solve_captcha(CAPTCHA))
