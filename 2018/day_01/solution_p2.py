#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 1 of the Advent of Code for 2018.
"""

import sys


def update_frequency(current_frequency, test_input):
    adjustment = int(test_input)

    return current_frequency + adjustment


def run_test(current_frequency, test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = update_frequency(current_frequency, test_input)

    if result != expected_solution:
        print "Test for captcha {0} FAILED. Got a result of {1}, not {2}".format(test_input, result, expected_solution)
        sys.exit(-1)

    print "Test for captcha {0} passed.".format(test_input)

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

current_frequency = 0

current_frequency = run_test(current_frequency, "+1", 1)
current_frequency = run_test(current_frequency, "-2", -1)
current_frequency = run_test(current_frequency, "+3", 2)
current_frequency = run_test(current_frequency, "+1", 3)

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.


freqs = {}
freqs[0] = True
current_frequency = 0
finished = False

while not finished:
    with open("input.txt", "r") as f:
        for line in f:
            current_frequency = update_frequency(current_frequency, line)
            if current_frequency in freqs:
                finished = True
                break
            else:
                freqs[current_frequency] = True

print "Solution is {0}".format(current_frequency)
