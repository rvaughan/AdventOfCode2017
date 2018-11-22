#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 4 of the Advent of Code for 2015.
"""
import hashlib
import sys

def calc_hash(input_data):
    for x in xrange(99999999999):
        hash_md5 = hashlib.md5()

        hash_input = "{}{}".format(input_data, x)

        hash_md5.update(hash_input)
        
        if hash_md5.hexdigest().startswith("00000"):
            return x

    return 0


def run_test(data, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calc_hash(data)

    if result != expected_solution:
        print "Test for data '{0}' FAILED. Got a result of {1}, not {2}".format(data, result, expected_solution)
        sys.exit(-1)

    print "Test for '{0}' passed.".format(data)


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

run_test("abcdef", 609043)
run_test("pqrstuv", 1048970)

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual data now.

with open("input.txt", "r") as f:
    line = f.readline()
    
    result = calc_hash(line)

    print "Solution: {}".format(result)
