#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 2 of the Advent of Code for 2020.
"""

from collections import defaultdict
import sys


def calculate_solution(passwords):
    count = 0
    for password in passwords:
        parts = password.split()

        min, max = parts[0].split('-')
        character = parts[1].split(':')[0]

        letters = defaultdict(int)
        for x in parts[2]:
            letters[x] += 1

        if letters[character] >= int(min) and letters[character] <= int(max):
            count += 1

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

result = run_test(test_list, 2)

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
