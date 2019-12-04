#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 4 of the Advent of Code for 2019.
"""

import math
import sys


def valid_password(password):
    double = False
    result = True
    pos = 1
    while pos < len(password):
        if password[pos] == password[pos - 1]:
            double = True

        if int(password[pos]) < int(password[pos - 1]):
            result = False
            break
        
        pos += 1

    return result & double


def run_test(test_num, test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = valid_password(test_input)

    if result != expected_solution:
        print "Test {0} FAILED. Got a result of {1}, not {2}".format(test_num, test_input, result, expected_solution)
        sys.exit(-1)

    print "Test {0} passed.".format(test_num)

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

run_test(1, "111111", True)
run_test(2, "223450", False)
run_test(3, "123789", False)

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    start, end = f.readline().split('-')
    count = 0
    for val in range(int(start), int(end)):
        if valid_password(str(val)):
            count += 1

    print "Solution is {0}".format(count)
