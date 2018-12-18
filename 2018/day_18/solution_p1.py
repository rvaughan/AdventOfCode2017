#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 14 of the Advent of Code for 2018.
"""

import copy


def load_forest(input_data):
    forest = []

    for line in input_data:

        row = []
        for square in line:
            row.append(square)
        
        forest.append(row)

    return forest


def dump_forest(forest):
    for line in forest:
        output = ""
        for square in line:
            output += square
        
        print output


def do_tick(forest, verbose=False):
    copy_forest = copy.deepcopy(forest)

    for y_idx, line in zip(xrange(len(forest)), copy_forest):
        for x_idx, square in zip(xrange(len(line)), line):

            checks = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1 ,0)]

            num_trees = 0
            num_lumberyards = 0
            num_open = 0

            # if x_idx == 8 and y_idx == 2:
            #     verbose = True

            for check in checks:
                xpos = x_idx + check[0]
                ypos = y_idx + check[1]

                if verbose:
                    print xpos, ypos

                if xpos < 0 or ypos < 0 or xpos == len(line) or ypos == len(line):
                    continue
                else:
                    if copy_forest[ypos][xpos] == ".":
                        if verbose:
                            print xpos, ypos, copy_forest[ypos][xpos], forest[ypos][xpos]

                        num_open += 1
                    elif copy_forest[ypos][xpos] == "|":
                        if verbose:
                            print xpos, ypos, copy_forest[ypos][xpos], forest[ypos][xpos]

                        num_trees += 1
                    elif copy_forest[ypos][xpos] == "#":
                        if verbose:
                            print xpos, ypos, copy_forest[ypos][xpos], forest[ypos][xpos]

                        num_lumberyards += 1
        
            # if x_idx == 8 and y_idx == 2:
            #     print square, num_trees, num_lumberyards, num_open
            #     x

            if square == ".":
                if num_trees >= 3:
                    forest[y_idx][x_idx] = "|"
            elif square == "|":
                if num_lumberyards >= 3:
                    forest[y_idx][x_idx] = "#"
            elif square == "#":
                if num_lumberyards >= 1 and num_trees >= 1:
                    continue
                else:
                    forest[y_idx][x_idx] = "."


def calc_score(forest, verbose=False):
    num_trees = 0
    num_lumberyards = 0
    num_open = 0

    for line in forest:
        for square in line:
            if square == ".":
                num_open += 1
            elif square == "|":
                num_trees += 1
            elif square == "#":
                num_lumberyards += 1

    if verbose:
        print num_open, num_lumberyards, num_trees

    return num_lumberyards * num_trees


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

print ""
print "-----------------"
print "Testing.........."
print "-----------------"
print ""

test_input=""".#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|."""

input_data = [line.strip() for line in test_input.splitlines()]
forest = load_forest(input_data)
# dump_forest(forest)

for _ in xrange(10):
    do_tick(forest)
# dump_forest(forest)

score = calc_score(forest, verbose=True)
assert score == 1147, score

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [line.strip() for line in f]

    forest = load_forest(input_data)
    # dump_forest(forest)

    for _ in xrange(10):
        do_tick(forest)

    score = calc_score(forest)

    print "Solution: {}".format(score)
