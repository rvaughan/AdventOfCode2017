#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 9 of the Advent of Code for 2018.
"""

from collections import defaultdict, deque
import sys


def play(max_players, max_marbles):
    circle = deque([0])
    player_scores = defaultdict(int)
    player_num = 0

    for marble in xrange(1, max_marbles + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            player_scores[player_num] += (marble + circle.pop())
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

        player_num = (player_num + 1) % max_players

    return max(player_scores.values())


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

print ""
print "-----------------"
print "Testing.........."
print "-----------------"
print ""


max_score = play(9, 25)
assert max_score == 32, max_score

max_score = play(10, 1618)
assert max_score == 8317, max_score

max_score = play(13, 7999)
assert max_score == 146373, max_score

max_score = play(17, 1104)
assert max_score == 2764, max_score

max_score = play(21, 6111)
assert max_score == 54718, max_score

max_score = play(30, 5807)
assert max_score == 37305, max_score


print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = f.read()
    pieces = input_data.split(' ')

    circle = deque([0])
    max_players = int(pieces[0])
    max_marbles = int(pieces[6])

    max_score = play(max_players, max_marbles)

    print "Solution is {0}".format(max_score)
