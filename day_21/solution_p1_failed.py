#!/usr/bin/env python
"""
This is a failed attempt at solving the problem.

Works by splitting up the grid into arrays of smaller grids. I think this
approach misses out on some patterns though.

Abandoned.
"""

import sys


def flip_rule(rule):
    """
    Flip the rule from left to right.
    """
    flipped_rule = ""

    rows = rule.split("/")
    for row in rows:
        new_row = ""
        for cell in row:
            new_row = cell + new_row

        flipped_rule += (new_row + "/")

    # Chomp off the last '/'.
    flipped_rule = flipped_rule[:-1]

    return flipped_rule


def rotate_rule(rule):
    """
    Rotate the rule clockwise.
    """
    rotated_rule = ""

    rows = rule.split("/")
    cells = [""] * len(rows)
    for row in rows:
        for idx, cell in zip(xrange(len(row)), row):
            cells[idx] = cell + cells[idx]

    rotated_rule = "/".join(cells)

    return rotated_rule


def load_grid(input_grid):
    """
    Convert the text form of the grid into an array form. For now this input is
    always the same. If this changes then this code would need to be replaced.
    """
    grid = [
        [".#./..#/###"]
    ]

    return grid


def split_sub_grid(grid):
    split_grid = []

    rows = grid.split("/")

    if len(rows) % 2 == 0:
        new_row = []
        new_row.append(rows[0][0] + rows[0][1] + "/" + rows[1][0] + rows[1][1])
        new_row.append(rows[0][2] + rows[0][3] + "/" + rows[1][2] + rows[1][3])
        split_grid.append(new_row)

        new_row = []
        new_row.append(rows[2][0] + rows[2][1] + "/" + rows[3][0] + rows[3][1])
        new_row.append(rows[2][2] + rows[2][3] + "/" + rows[3][2] + rows[3][3])
        split_grid.append(new_row)
    else:
        # MUST be divisible by 3...
        new_row = []
        new_row.append(rows[0][0] + rows[0][1] + rows[0][2] + "/" + rows[1][0] + rows[1][1] + rows[1][2] + "/" + rows[2][0] + rows[2][1] + rows[2][2])
        new_row.append(rows[0][3] + rows[0][4] + rows[0][5] + "/" + rows[1][3] + rows[1][4] + rows[1][5] + "/" + rows[2][3] + rows[2][4] + rows[2][5])
        new_row.append(rows[0][6] + rows[0][7] + rows[0][8] + "/" + rows[1][6] + rows[1][7] + rows[1][8] + "/" + rows[2][6] + rows[2][7] + rows[2][8])
        split_grid.append(new_row)

        new_row = []
        new_row.append(rows[3][0] + rows[3][1] + rows[3][2] + "/" + rows[4][0] + rows[4][1] + rows[4][2] + "/" + rows[5][0] + rows[5][1] + rows[5][2])
        new_row.append(rows[3][3] + rows[3][4] + rows[3][5] + "/" + rows[4][3] + rows[4][4] + rows[4][5] + "/" + rows[5][3] + rows[5][4] + rows[5][5])
        new_row.append(rows[3][6] + rows[3][7] + rows[3][8] + "/" + rows[4][6] + rows[4][7] + rows[4][8] + "/" + rows[5][6] + rows[5][7] + rows[5][8])
        split_grid.append(new_row)

        new_row = []
        new_row.append(rows[6][0] + rows[6][1] + rows[6][2] + "/" + rows[7][0] + rows[7][1] + rows[7][2] + "/" + rows[8][0] + rows[8][1] + rows[8][2])
        new_row.append(rows[6][3] + rows[6][4] + rows[6][5] + "/" + rows[7][3] + rows[7][4] + rows[7][5] + "/" + rows[8][3] + rows[8][4] + rows[8][5])
        new_row.append(rows[6][6] + rows[6][7] + rows[6][8] + "/" + rows[7][6] + rows[7][7] + rows[7][8] + "/" + rows[8][6] + rows[8][7] + rows[8][8])
        split_grid.append(new_row)
        
    return split_grid


def process_grid(patterns, input_grid):
    new_grid = []

    for row in input_grid:
        new_row = []
        for sub_grid in row:
            if len(sub_grid) <= 11:
                if isinstance(sub_grid, str):
                    new_row.append(patterns[sub_grid])
                else:
                    for g in sub_grid:
                        new_row.append(patterns[g])
            else:
                sb = split_sub_grid(sub_grid)

                for sub_row in process_grid(patterns, sb):
                    new_row.append(sub_row)

        new_grid.append(new_row)

    return new_grid


def load_rules(input_rules):
    """
    Load all of the rules in, and map all of the variations out in memory.
    """
    rules = {}

    for rule in input_rules.split("\n"):
        if rule.strip() == "":
            continue

        parts = rule.split(" => ")

        rules[parts[0]] = parts[1]
        rules[flip_rule(parts[0])] = parts[1]
        rules[rotate_rule(parts[0])] = parts[1]
        rules[flip_rule(rotate_rule(parts[0]))] = parts[1]
        rules[rotate_rule(rotate_rule(parts[0]))] = parts[1]
        rules[flip_rule(rotate_rule(rotate_rule(parts[0])))] = parts[1]
        rules[rotate_rule(rotate_rule(rotate_rule(parts[0])))] = parts[1]
        rules[flip_rule(rotate_rule(rotate_rule(rotate_rule(parts[0]))))] = parts[1]

    return rules


def count_pixels(grid):
    count = 0

    if isinstance(grid, list):
        for sub_grid in grid:
            count += count_pixels(sub_grid)
    else:
        for cell in grid:
            if cell == "#":
                count += 1

    return count


def init_grid():
    return """.#.\n..#\n###"""


# Test code starts here

# Start with some basic tests using a 2x2 grid

TEST_FLIP = flip_rule("../.#")
if TEST_FLIP != "../#.":
    print "Test 2 cell flip failed. [{0}]".format(TEST_FLIP)
    sys.exit(-1)
print "Test 2 cell flip passed"

TEST_ROTATE = rotate_rule("../.#")
if TEST_ROTATE != "../#.":
    print "Test 2 cell rotate (1) failed. [{0}]".format(TEST_ROTATE)
    sys.exit(-1)
print "Test 2 cell rotate (1) passed"
TEST_ROTATE = rotate_rule(TEST_ROTATE)
if TEST_ROTATE != "#./..":
    print "Test 2 cell rotate (2) failed. [{0}]".format(TEST_ROTATE)
    sys.exit(-1)
print "Test 2 cell rotate (2) passed"
TEST_ROTATE = rotate_rule(TEST_ROTATE)
if TEST_ROTATE != ".#/..":
    print "Test 2 cell rotate (3) failed. [{0}]".format(TEST_ROTATE)
    sys.exit(-1)
print "Test 2 cell rotate (3) passed"

TEST_SPLIT = split_sub_grid('#..#/..../..../#..#')
if TEST_SPLIT != [['#./..', '.#/..'], ['../#.', '../.#']]:
    print "Test split failed. {0}".format(TEST_SPLIT)
    sys.exit(-1)
print "Test split passed"

INPUT_RULES = "../.# => ##./#../..."
TEST_RULES = load_rules(INPUT_RULES)
if len(TEST_RULES) != 4:
    print "Test rule length (1) failed. [{0}]".format(len(TEST_RULES))
    sys.exit(-1)
print "Test rule length (1) passed."

TEST_FLIP = flip_rule(".#./..#/###")
if TEST_FLIP != ".#./#../###":
    print "Test 3 cell flip failed. ['{0}']".format(TEST_FLIP)
    sys.exit(-1)
print "Test 3 cell flip passed"

TEST_ROTATE = rotate_rule(".#./..#/###")
if TEST_ROTATE != '#../#.#/##.':
    print "Test 3 cell rotate (1) failed. ['{0}']".format(TEST_ROTATE)
    sys.exit(-1)
print "Test 3 cell rotate (1) passed"
TEST_ROTATE = rotate_rule(TEST_ROTATE)
if TEST_ROTATE != '###/#../.#.':
    print "Test 3 cell rotate (2) failed. ['{0}']".format(TEST_ROTATE)
    sys.exit(-1)
print "Test 3 cell rotate (2) passed"
TEST_ROTATE = rotate_rule(TEST_ROTATE)
if TEST_ROTATE != '.##/#.#/..#':
    print "Test 3 cell rotate (3) failed. ['{0}']".format(TEST_ROTATE)
    sys.exit(-1)
print "Test 3 cell rotate (3) passed"

INPUT_RULES = ".#./..#/### => #..#/..../..../#..#"
TEST_RULES = load_rules(INPUT_RULES)
if len(TEST_RULES) != 8:
    print "Test rule length (2) failed. [{0}]".format(len(TEST_RULES))
    for r in TEST_RULES:
        print r
    sys.exit(-1)
print "Test rule length (2) passed."

TEST_SPLIT = split_sub_grid('#..#/..../..../#..#')
if TEST_SPLIT != [['#./..', '.#/..'], ['../#.', '../.#']]:
    print "Test split failed. {0}".format(TEST_SPLIT)
    sys.exit(-1)
print "Test split passed"

# Now try and use the test input provided within the puzzle data

INPUT_RULES = """../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
"""
RULES = load_rules(INPUT_RULES)

START_GRID = init_grid()
GRID = load_grid(START_GRID)
if GRID != [[".#./..#/###"]]:
    print "Loading of test grid failed. {0}".format(GRID)
    sys.exit(-1)
print "Loading of test grid passed."

GRID = process_grid(RULES, GRID)
if GRID != [['#..#/..../..../#..#']]:
    print "Test grid move 1 failed. {0}".format(GRID)
    sys.exit(-1)
print "Test grid move 1 passed"

GRID = process_grid(RULES, GRID)
if GRID != [[['##./#../...', '##./#../...'], ['##./#../...', '##./#../...']]]:
    print "Test grid move 2 failed. {0}".format(GRID)
    sys.exit(-1)
print "Test grid move 2 passed"

NUM_PIXELS = count_pixels(GRID)
if NUM_PIXELS != 12:
    print "Test count failed. [{0}]".format(NUM_PIXELS)
    sys.exit(-1)
print "Test count passed"

print "All Tests passed."


# Now, try and solve the puzzle itself.


with open("input.txt", "r") as f:
    INPUT_RULES = f.read()
    RULES = load_rules(INPUT_RULES)

    GRID = load_grid(init_grid())

    for IDX in xrange(5):
        GRID = process_grid(RULES, GRID)
        print GRID
        print IDX, count_pixels(GRID)

    print "Solution is {0} pixels.".format(count_pixels(GRID))
