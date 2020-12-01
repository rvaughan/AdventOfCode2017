#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 22 of the Advent of Code for 2018.
"""

def generate_empty_cave(max_x, max_y):
    cave = []
    for _ in xrange(max_y):
        cave.append([0] * max_x)

    return cave


def calc_geologic_index(cave):
    for y in xrange(len(cave)):
        for x in xrange(len(cave[y])):
            if x == 0 and y == 0:
                cave[y][x] = 0
            elif x == 0:
                cave[y][x] = y * 48271
            elif y == 0:
                cave[y][x] = x * 16807
            else:
                cave[y][x] = cave[y - 1][x] * cave[y][x - 1]

    return cave


def calc_erosion_level(cave, depth):
    for y in xrange(len(cave)):
        for x in xrange(len(cave[y])):
            level = (cave[y][x] + depth) % 20183
            cell_type = level % 3
            if cell_type == 0:
                cave[y][x] = 0
            elif cell_type == 1:
                cave[y][x] = 1
            elif cell_type == 2:
                cave[y][x] = 2

    return cave


def build_cave(max_x, max_y, depth):
    cave = generate_empty_cave(max_x, max_y)

    calc_geologic_index(cave)
    calc_erosion_level(cave, depth)

    return cave


def dump_cave(cave):
    for y in xrange(len(cave)):
        line = ""
        for x in xrange(len(cave[y])):
            if cave[y][x] == 0:
                line += '.'
            elif cave[y][x] == 1:
                line += '='
            elif cave[y][x] == 2:
                line += '|'

        print line


def calc_risk(cave, start_x, start_y, end_x, end_y):
    risk_score = 0

    for y in xrange(start_y, end_y + 1):
        for x in xrange(start_x, end_x + 1):
            risk_score += cave[y][x]

    return risk_score


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

print ""
print "-----------------"
print "Testing.........."
print "-----------------"
print ""

cave = build_cave(11, 11, 510)
dump_cave(cave)
cave[10][10] = 0
risk_score = calc_risk(cave, 0, 0, 10, 10)
assert risk_score == 114, risk_score

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    cave = build_cave(6, 747, 4002)
    cave[746][5] = 0
    risk_score = calc_risk(cave, 0, 0, 5, 746)

    print "Solution: {}".format(risk_score)
