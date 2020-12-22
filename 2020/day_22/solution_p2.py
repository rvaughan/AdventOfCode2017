#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 22 of the Advent of Code for 2020.
"""
import re
import sys
from collections import defaultdict, deque


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
            decks.append(deque(player_cards))
            player_cards = []

    decks.append(deque(player_cards))

    return decks


def recurse(p1, p2, seen):
    while (p1 and p2):
        if (tuple(p1), tuple(p2)) in seen:
            return 1, p1
        
        seen.add((tuple(p1), tuple(p2)))
        c1, c2 = p1.popleft(), p2.popleft()
        
        if c1 <= len(p1) and c2 <= len(p2):
            sp1, sp2 = deque(list(p1)[:c1]), deque(list(p2)[:c2])
            winner, _ = recurse(sp1, sp2, set())
        else:
            winner = 1 if c1 > c2 else 0
        
        if winner == 1:
            p1 += deque([c1, c2])
        else:
            p2 += deque([c2, c1])
    
    return (1, p1) if p1 else (0, p2)


def calculate_solution(puzzle_input):
    decks = get_decks(puzzle_input)

    p1 = decks[0]
    p2 = decks[1]
    
    winner = recurse(p1, p2, set())[1]
    res = 0
    for i in range(1, len(winner)+1):
        cur = winner.pop()
        res += (i * cur)

    return res


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
run_test(puzzle_input, 291)


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
