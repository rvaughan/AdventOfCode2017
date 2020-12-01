#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 1 of the Advent of Code for 2020.
"""

import math
import sys


def calculate_solution(mass):
    return 0


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input)

    if result != expected_solution:
        print "Test for mass {0} FAILED. Got a result of {1}, not {2}".format(test_input, result, expected_solution)
        sys.exit(-1)

    print "Test for mass {0} passed.".format(test_input)

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = [1721, 979, 366, 299, 675, 1456]

result = run_test(test_list, 514579)

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [int(line) for line in f]
    answer = calculate_solution(input_data)

    print "Solution is {0}".format(answer)
