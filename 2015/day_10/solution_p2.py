#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 10 of the Advent of Code for 2015.
"""
import itertools
import sys


def process_input(input_data):
    result = ""

    for k, g in itertools.groupby(input_data):
        result += "{}{}".format(len(list(g)), k)

    return result


def run_test(check, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = process_input(check)

    if result != expected_solution:
        print "Test for signal '{0}' FAILED. Got a result of {1}, not {2}".format(check, result, expected_solution)
        sys.exit(-1)

    print "Test for signal '{0}' passed.".format(check)


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

run_test('1', '11')
run_test('11', '21')
run_test('21', '1211')
run_test('1211', '111221')
run_test('111221', '312211')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual data now.

with open("input.txt", "r") as f:
    result = f.read()
    
    for x in xrange(50):
        result = process_input(result)

    print "Result: {}".format(len(result))
