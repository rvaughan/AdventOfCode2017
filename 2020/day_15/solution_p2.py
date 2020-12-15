#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 15 of the Advent of Code for 2020.
"""
import re
import sys
from collections import defaultdict


def calculate_solution(turns):
    numbers = defaultdict(int)
    numbers2 = defaultdict(int)
    turn = 1
    spoken = 0

    n_list = [int(x) for x in turns[0].split(',')]
    for n in n_list:
        numbers[n] = 1
        numbers2[n] = [turn]
        turn += 1
        spoken = n

    while turn <= 30000000:
        next_number = 0
        if numbers[spoken] > 1:
            last = len(numbers2[spoken]) - 1
            next_number = numbers2[spoken][last] - numbers2[spoken][last - 1]
        
        numbers[next_number] += 1
        if numbers[next_number] == 1:
            numbers2[next_number] = [turn]
        else:
            numbers2[next_number].append(turn)

        spoken = next_number

        turn += 1

    return spoken


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


puzzle_input = [
    "0,3,6"
]
run_test(puzzle_input, 175594)


print("")
print("-----------------")
print("All Tests PASSED.")
print("-----------------")
print("")

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data)

    print("Solution is {0}".format(answer))
