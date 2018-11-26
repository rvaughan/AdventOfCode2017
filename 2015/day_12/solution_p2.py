#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 4 of the Advent of Code for 2015.
"""
try:
    import simplejson as json
except:
    import json
import sys


def sum_of_items(item):

    if isinstance(item, list):
        # print "list"
        return sum([sum_of_items(i) for i in item])

    if isinstance(item, dict):
        # print "dict"
        if "red" in item.values():
            return 0
        return sum([sum_of_items(i) for i in item.values()])

    if isinstance(item, unicode):
        # print "unicode"
        return 0

    if isinstance(item, int):
        # print "values", item
        return item

    return 0


def run_test(data, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = sum_of_items(data)

    if result != expected_solution:
        print "Test for data '{0}' FAILED. Got a result of {1}, not {2}".format(data, result, expected_solution)
        sys.exit(-1)

    print "Test for '{0}' passed.".format(data)


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

run_test(json.loads("[1,2,3]"), 6)
run_test(json.loads("[1,{\"c\":\"red\",\"b\":2},3]"), 4)
run_test(json.loads("{\"d\":\"red\",\"e\":[1,2,3,4],\"f\":5}"), 0)
run_test(json.loads("[1,\"red\",5]"), 6)

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual data now.

with open("input.txt", "r") as f:
    data = f.read()

    print "Total: {}".format(sum_of_items(json.loads(data)))
