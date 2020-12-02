#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 2 of the Advent of Code for 2020.
"""

from collections import defaultdict
import sys


def calculate_solution(passwords):
    count = 0
    for password in passwords:
        parts = password.split()

        pos_1, pos_2 = parts[0].split('-')
        pos_1 = int(pos_1) - 1
        pos_2 = int(pos_2) - 1
        character = parts[1].split(':')[0]

        if parts[2][pos_1] == character and parts[2][pos_2] != character:
            count += 1
            continue

        if parts[2][pos_1] != character and parts[2][pos_2] == character:
            count += 1
            continue

    return count


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input)

    if result != expected_solution:
        print "Test for input {0} FAILED. Got a result of {1}, not {2}".format(test_input, result, expected_solution)
        sys.exit(-1)

    print "Test for input {0} passed.".format(test_input)

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc"
]

result = run_test(test_list, 1)

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [line for line in f]
    answer = calculate_solution(input_data)

    print "Solution is {0}".format(answer)
