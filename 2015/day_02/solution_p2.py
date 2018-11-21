#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 2 of the Advent of Code for 2015.
"""

import sys

def calc_ribbon_needed(data):
    result = 0
    dimensions = [int(x) for x in data.split("x")]
    dimensions.sort()

    result += dimensions[0] + dimensions[0] + dimensions[1] + dimensions[1]

    result += (dimensions[0] * dimensions[1] * dimensions[2])

    return result


def run_test(data, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calc_ribbon_needed(data)

    if result != expected_solution:
        print "Test for data '{0}' FAILED. Got a result of {1}, not {2}".format(data, result, expected_solution)
        sys.exit(-1)

    print "Test for '{0}' passed.".format(data)


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

run_test("2x3x4", 34)
run_test("1x1x10", 14)

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual data now.

with open("input.txt", "r") as f:
    result = 0
    for line in f:
        result += calc_ribbon_needed(line)

    print "Ribbon required: {} feet squared".format(result)
