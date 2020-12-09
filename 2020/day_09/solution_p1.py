#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 9 of the Advent of Code for 2020.
"""
import sys
from collections import defaultdict


def calc_list(preamble, start, codes):
    value_list = []

    for idx in range(start, start + preamble):
        for idx2 in range(start, start + preamble):
            if idx != idx2:
                value_list.append(codes[idx] + codes[idx2])

    return value_list

def calculate_solution(preamble, codes):
    result = 0
    start = 0
    finished = False
    current = preamble

    while not finished:
        value_list = calc_list(preamble, start, codes)

        if codes[current] not in value_list:
            return codes[current]

        start += 1
        current += 1


def run_test(test_input, preamble, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(preamble, test_input)

    if result != expected_solution:
        print("Test for input {0} FAILED. Got a result of {1}, not {2}".format(test_input, result, expected_solution))
        sys.exit(-1)

    print("Test for input {0} passed.".format(test_input))

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

codes = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576
]
run_test(codes, 5, 127)

print("")
print("-----------------")
print("All Tests PASSED.")
print("-----------------")
print("")

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [int(line.strip()) for line in f]
    answer = calculate_solution(25, input_data)

    print("Solution is {0}".format(answer))
