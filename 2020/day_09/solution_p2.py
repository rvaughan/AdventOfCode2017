#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 9 of the Advent of Code for 2020.
"""
import sys
from collections import defaultdict


def calculate_solution(search_value, codes):
    start = 0
    value = 0
    finished = False

    while not finished:
        if start == len(codes):
            break

        for idx in range(start, len(codes)):
            value += codes[idx]

            if value == search_value:
                max = 0
                min = 99999999999999

                for idx2 in range(start, idx + 1):
                    if codes[idx2] > max:
                        max = codes[idx2]
                    
                    if codes[idx2] < min:
                        min = codes[idx2]

                return min + max
            elif value > search_value:
                value = 0
                start += 1
                break

    return -1


def run_test(test_input, search_value, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(search_value, test_input)

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
run_test(codes, 127, 62)

print("")
print("-----------------")
print("All Tests PASSED.")
print("-----------------")
print("")

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [int(line.strip()) for line in f]
    answer = calculate_solution(167829540, input_data)

    print("Solution is {0}".format(answer))
