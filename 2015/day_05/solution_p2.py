#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 5 of the Advent of Code for 2015.
"""
import hashlib
import sys

def is_nice(input_data):
    # repeats with exactly one letter between them
    if not any([input_data[i] == input_data[i+2] for i in range(len(input_data) - 2)]):
        return False

    # pair appears at least twice
    if any([(input_data.count(input_data[i:i+2]) >= 2) for i in range(len(input_data) - 2)]):
        return True

    return False


def run_test(data, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = is_nice(data)

    if result != expected_solution:
        print "Test for data '{0}' FAILED. Got a result of {1}, not {2}".format(data, result, expected_solution)
        sys.exit(-1)

    print "Test for '{0}' passed.".format(data)


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

run_test("qjhvhtzxzqqjkmpb", True)
run_test("xxyxx", True)
run_test("uurcxstgmygtbstg", False)
run_test("ieodomkazucvgmuy", False)

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual data now.

with open("input.txt", "r") as f:
    result = 0
    for line in f:
        if is_nice(line):
            result += 1

    print "Nice strings: {}".format(result)
