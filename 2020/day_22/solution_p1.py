#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 22 of the Advent of Code for 2020.
"""
import re
import sys
from collections import defaultdict


def get_decks(data):
    decks = []
    player_cards = []

    first = True
    for line in data:
        if line != "":
            if first:
                first = False
                continue
            else:
                player_cards.append(int(line))
        else:
            first = True
            decks.append(player_cards)
            player_cards = []

    decks.append(player_cards)

    return decks


def play_round(p1, p2):
    if p1 > p2:
        return [p1, p2], []
    
    return [], [p2, p1]


def calc_score(deck):
    result = 0
    multiplier = 1
    for val in reversed(deck):
        result += (val * multiplier)
        multiplier += 1

    return result


def calculate_solution(puzzle_input):
    decks = get_decks(puzzle_input)

    while len(decks[0]) > 0 and len(decks[1]) > 0:
        p1, p2 = play_round(decks[0][0], decks[1][0])

        decks[0] = decks[0][1:]
        decks[0] += p1

        decks[1] = decks[1][1:]
        decks[1] += p2
    
    if len(decks[0]) > 0:
        return calc_score(decks[0])
    
    return calc_score(decks[1])


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
    "Player 1:",
    "9",
    "2",
    "6",
    "3",
    "1",
    "",
    "Player 2:",
    "5",
    "8",
    "4",
    "7",
    "10"
]
run_test(puzzle_input, 306)


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
