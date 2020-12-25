#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 25 of the Advent of Code for 2020.
"""
import re
import sys
from collections import defaultdict


def calc_loop_size(public_value):
    count = 0
    val = 1
    while val != public_value:
        count += 1
        val *= 7
        val %= 20201227

    return count


def calc_private_key(public_key, loops):
    pk = 1
    for l in range(0, loops):
        pk *= public_key
        pk %= 20201227

    return pk


def calculate_solution(puzzle_input):
    card_pk = int(puzzle_input[0])
    door_pk = int(puzzle_input[1])

    card_loop_size = calc_loop_size(card_pk)
    door_loop_size = calc_loop_size(door_pk)

    card_priv_key = calc_private_key(door_pk, card_loop_size)
    door_priv_key = calc_private_key(card_pk, door_loop_size)

    if card_priv_key != door_priv_key:
        panic

    return door_priv_key


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


assert calc_loop_size(5764801) == 8
assert calc_loop_size(17807724) == 11

assert calc_private_key(17807724, 8) == 14897079
assert calc_private_key(5764801, 11) == 14897079

puzzle_input = [
    "5764801",
    "17807724"
]
run_test(puzzle_input, 14897079)


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
