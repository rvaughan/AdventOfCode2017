#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 5 of the Advent of Code for 2015.
"""
import hashlib
import sys

def is_nice(input_data):
    last = ''
    first = True

    vowels = 0
    double_check = False

    for x in input_data:
        if not first:
            if "{}{}".format(last, x) == "ab":
                return False

            if "{}{}".format(last, x) == "cd":
                return False

            if "{}{}".format(last, x) == "pq":
                return False

            if "{}{}".format(last, x) == "xy":
                return False

            if x == last:
                double_check = True

            if x in 'aeiou':
                vowels += 1

        else:
            if x in 'aeiou':
                vowels += 1

            first = False

        last = x

    if vowels >= 3 and double_check:
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

run_test("ugknbfddgicrmopn", True)
run_test("aaa", True)
run_test("jchzalrnumimnmhp", False)
run_test("haegwjzuvuyypxyu", False)
run_test("dvszwmarrgswjxmb", False)

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual data now.

with open("input.txt", "r") as f:
    result = 0
    for line in f:
        if is_nice(line):
            result += 1

    print "Nice strings: {}".format(result)
