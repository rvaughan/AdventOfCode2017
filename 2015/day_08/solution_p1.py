#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 8 of the Advent of Code for 2015.
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


def run_test(data, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = process_line(data)

    if result != expected_solution:
        print "Test for data '{0}' FAILED. Got a result of {1}, not {2}".format(data, result, expected_solution)
        sys.exit(-1)

    print "Test for '{0}' passed.".format(data)


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

run_test('""', (2, 0))
run_test('"abc"', (5, 3))
run_test('"aaa\\"aaa"', (10, 7))
run_test('"\\x27"', (6, 1))

result = 0
test_inputs = ['""', '"abc"', '"aaa\\"aaa"', '"\\x27"']
for test in test_inputs:
    string_len, count = process_line(test.strip())

    result += (string_len - count)
assert result == 12

run_test('"\\\\"', (4, 1))
run_test('"\\""', (4, 1))
run_test('"\\"\\""', (6, 2))
run_test('"\\"\\\\"', (6, 2))

run_test('"abc\\x27aaa"', (12, 7))
run_test('"aabb\\\\aaa\\x27a"', (16, 10))
run_test('"njro"', (6, 4))
run_test('"njro\\x68"', (10, 5))
run_test('"njro\\x68qgbx"', (14, 9))
run_test('"njro\\x68qgbx\\xe4"', (18, 10))
run_test('"njro\\x68qgbx\\xe4af"', (20, 12))
run_test('"njro\\x68qgbx\\xe4af\\""', (22, 13))
run_test('"njro\\x68qgbx\\xe4af\\"\\\\"', (24, 14))
run_test('"njro\\x68qgbx\\xe4af\\"\\\\suan"', (28, 18))

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual data now.

with open("input.txt", "r") as f:
    result = 0
    for line in f:
        string_len, count = process_line(line.strip())

        result += (string_len - count)
        print string_len, count

    print "Result: {}".format(result)
