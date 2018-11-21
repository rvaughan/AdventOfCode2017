#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 3 of the Advent of Code for 2015.
"""

import sys

def deliver_presents(data):
    x = 0
    y = 0
    houses = {}

    houses["{}:{}".format(x,y)] = 1

    for move in data:
        if move == '^':
            y += 1
        elif move == 'v':
            y -= 1
        elif move == "<":
            x -= 1
        elif move == ">":
            x += 1
        else:
            print "Bork! {}".format(move)
            continue

        houses["{}:{}".format(x,y)] = 1

    return len(houses.keys())


def run_test(data, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = deliver_presents(data)

    if result != expected_solution:
        print "Test for data '{0}' FAILED. Got a result of {1}, not {2}".format(data, result, expected_solution)
        sys.exit(-1)

    print "Test for '{0}' passed.".format(data)


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

run_test(">", 2)
run_test("^>v<", 4)
run_test("^v^v^v^v^v", 2)

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual data now.

with open("input.txt", "r") as f:
    result = 0
    for line in f:
        result += deliver_presents(line)

    print "{} houses received at least one present.".format(result)
