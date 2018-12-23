#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 23 of the Advent of Code for 2018.
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


def find_best_distance(bots):
    xs = [x[0] for x in bots]
    ys = [x[1] for y in bots]
    zs = [x[2] for z in bots]

    dist = 1
    while dist < max(xs) - min(xs):
        dist *= 2

    while True:
        target_count = 0
        best = None
        best_val = None
        for x in xrange(min(xs), max(xs) + 1, dist):
            for y in xrange(min(ys), max(ys) + 1, dist):
                for z in xrange(min(zs), max(zs) + 1, dist):
                    count = 0
                    for bx, by, bz, bdist in bots:
                        calc = abs(x - bx) + abs(y - by) + abs(z - bz)
                        if (calc - bdist) / dist <= 0:
                            count += 1
                    if count > target_count:
                        target_count = count
                        best_val = abs(x) + abs(y) + abs(z)
                        best = (x, y, z)
                    elif count == target_count:
                        if abs(x) + abs(y) + abs(z) < best_val:
                            best_val = abs(x) + abs(y) + abs(z)
                            best = (x, y, z)

        if dist == 1:
            return best_val
        else:
            xs = [best[0] - dist, best[0] + dist]
            ys = [best[1] - dist, best[1] + dist]
            zs = [best[2] - dist, best[2] + dist]
            dist /= 2


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

print ""
print "-----------------"
print "Testing.........."
print "-----------------"
print ""

print "Running test 1..."
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

print "Running test 2..."
test_data="""pos=<10,12,12>, r=2
pos=<12,14,12>, r=2
pos=<16,12,12>, r=4
pos=<14,14,14>, r=6
pos=<50,50,50>, r=200
pos=<10,10,10>, r=5"""

input_data = [line.strip() for line in test_data.splitlines()]
bots = load_bots(input_data)
best_distance = find_best_distance(bots)
assert best_distance == 36, best_distance

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
    best_distance = find_best_distance(bots)

    print "Solution: {}".format(best_distance)
