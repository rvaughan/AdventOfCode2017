#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 10 of the Advent of Code for 2020.
"""
import sys
from collections import defaultdict


def calculate_solution(adaptors):
    result = 0

    # Add the wall socket itself
    adaptors.append(0)

    adaptors.sort()

    # Add the device jolts - always the max + 3
    adaptors.append(adaptors[len(adaptors) - 1] + 3)

    counts = defaultdict(int)

    for idx in range(1, len(adaptors)):
        counts[adaptors[idx] - adaptors[idx-1]] += 1

    return counts


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input)

    if result != expected_solution:
        print("Test for input {0} FAILED. Got a result of {1}, not {2}".format(test_input, result, expected_solution))
        sys.exit(-1)

    print("Test for input {0} passed.".format(test_input))

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

adaptors = [
    16,
    10,
    15,
    5,
    1,
    11,
    7,
    19,
    6,
    12,
    4
]
run_test(adaptors, {1: 7, 3: 5})

adaptors = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3
]
run_test(adaptors, {1: 22, 3: 10})

print("")
print("-----------------")
print("All Tests PASSED.")
print("-----------------")
print("")

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [int(line.strip()) for line in f]
    result = calculate_solution(input_data)

    answer = result[1] * result[3]

    print("Solution is {0}".format(answer))
