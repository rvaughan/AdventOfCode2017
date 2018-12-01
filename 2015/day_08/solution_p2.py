#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 8 of the Advent of Code for 2015.
"""
import hashlib
import sys


def process_line(line):
    count = 0

    escape = False
    escape_count = 0

    for x in line:
        if escape:
            if x == 'x':
                continue

            if x == '"':
                count += 1
                escape = False

                continue

            if x == '\\':
                count += 1
                escape = False

                continue

            if x in "0123456789abcdef":
                escape_count += 1
                if escape_count == 2:
                    count += 1
                    escape_count = 0
                    escape = False
                    continue
        else:
            if x == "\\":
                escape = True
            elif x != '"':
                count += 1

    return len(line), count


def calc_encoded(line):
    encoded = line

    encoded = encoded.replace("\\", "\\\\")
    encoded = encoded.replace('"', '\\"')
    encoded = '"' + encoded + '"'

    return len(encoded)


def run_test(data, expected_solution, exp_encoded):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = process_line(data)
    enc = calc_encoded(data)

    if result != expected_solution or enc != exp_encoded:
        print "Test for data '{0}' FAILED. Got a result of {1} {2}, not {3} {4}".format(data, result, enc, expected_solution, exp_encoded)
        sys.exit(-1)

    print "Test for '{0}' passed.".format(data)


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

run_test('""', (2, 0), 6)
run_test('"abc"', (5, 3), 9)
run_test('"aaa\\"aaa"', (10, 7), 16)
run_test('"\\x27"', (6, 1), 11)

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual data now.

with open("input.txt", "r") as f:
    result = 0
    for line in f:
        string_len, count = process_line(line.strip())
        enc = calc_encoded(line.strip())

        result += (enc - string_len)

    print "Result: {}".format(result)
