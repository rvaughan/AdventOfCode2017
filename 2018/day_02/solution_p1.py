#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 2 of the Advent of Code for 2018.
"""

from collections import Counter
import sys


def calc_checksum(test_input, expected_count):
    c = Counter(test_input)
    for item in c:
        if c[item] == expected_count:
            return 1

    return 0


def run_test(test_input, expected_two_solution, expected_three_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result_2 = calc_checksum(test_input, 2)
    result_3 = calc_checksum(test_input, 3)

    if result_2 != expected_two_solution or result_3 != expected_three_solution:
        print "Test for captcha {0} FAILED. Got a result of {1}, {2}, not {3}, {4}".format(test_input, result_2, result_3, expected_two_solution, expected_three_solution)
        sys.exit(-1)

    print "Test for captcha {0} passed.".format(test_input)


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

run_test("abcdef", 0, 0)
run_test("bababc", 1, 1)
run_test("abbcde", 1, 0)
run_test("abcccd", 0, 1)
run_test("aabcdd", 1, 0)
run_test("abcdee", 1, 0)
run_test("ababab", 0, 1)

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    count_2 = 0
    count_3 = 0
    for line in f:
        count_2 += calc_checksum(line, 2)
        count_3 += calc_checksum(line, 3)

    print "Solution is {0}".format((count_2 * count_3))
