#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 1 of the Advent of Code for 2019.
"""

import math
import sys


def calculate_fuel_needs(mass):
    return math.floor(mass / 3) - 2


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_fuel_needs(test_input)

    if result != expected_solution:
        print "Test for mass {0} FAILED. Got a result of {1}, not {2}".format(test_input, result, expected_solution)
        sys.exit(-1)

    print "Test for mass {0} passed.".format(test_input)

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

fuel_needed = 0

fuel_needed = run_test(12, 2)
fuel_needed = run_test(14, 2)
fuel_needed = run_test(1969, 654)
fuel_needed = run_test(100756, 33583)

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    fuel_needed = 0
    for line in f:
        fuel_needed += calculate_fuel_needs(int(line))

    print "Solution is {0}".format(fuel_needed)
