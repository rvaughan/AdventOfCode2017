#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 23 of the Advent of Code for 2018.
"""

import re


def load_bots(input_data):
    bots = []
    line_regex = re.compile("pos=<([0-9-]+),([0-9-]+),([0-9-]+)>, r=([0-9]+)")
    
    for bot_info in input_data:
        mateches = line_regex.search(bot_info)
        bots.append([int(pos) for pos in mateches.groups()])

    return bots


def find_biggest_bot(bots):
    biggest_bot = None
    max_range = None

    for bot in bots:
        if biggest_bot is None or bot[3] > max_range:
            biggest_bot = bot
            max_range = bot[3]

    return biggest_bot


def find_bots_in_range(bots, biggest_bot):
    in_range = []

    best_x, best_y, best_z, best_dist = biggest_bot

    for bot in bots:
        x, y, z, _dist = bot

        if abs(x - best_x) + abs(y - best_y) + abs(z - best_z) <= best_dist:
            in_range.append(bot)

    return in_range


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

print ""
print "-----------------"
print "Testing.........."
print "-----------------"
print ""

test_data="""pos=<0,0,0>, r=4
pos=<1,0,0>, r=1
pos=<4,0,0>, r=3
pos=<0,2,0>, r=1
pos=<0,5,0>, r=3
pos=<0,0,3>, r=1
pos=<1,1,1>, r=1
pos=<1,1,2>, r=1
pos=<1,3,1>, r=1"""

input_data = [line.strip() for line in test_data.splitlines()]
bots = load_bots(input_data)
biggest_bot = find_biggest_bot(bots)
assert biggest_bot == [0, 0, 0, 4]
in_range = find_bots_in_range(bots, biggest_bot)
assert len(in_range) == 7

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [line.strip() for line in f]

    bots = load_bots(input_data)
    biggest_bot = find_biggest_bot(bots)

    in_range = find_bots_in_range(bots, biggest_bot)

    print "Solution: {}".format(len(in_range))
