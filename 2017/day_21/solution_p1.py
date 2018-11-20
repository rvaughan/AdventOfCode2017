#!/usr/bin/env python

import sys


def flip_rule(rule):
    """
    Flip the rule from left to right.
    """
    flipped_rule = []

    rows = rule.split("/")
    for row in rows:
        new_row = ""
        for cell in row:
            new_row = cell + new_row

        flipped_rule.append(new_row)

    return "/".join(flipped_rule)


def rotate_rule(rule):
    """
    Rotate the rule clockwise.
    """
    rows = rule.split("/")
    cells = [""] * len(rows)
    for row in rows:
        for idx, cell in zip(xrange(len(row)), row):
            cells[idx] = cell + cells[idx]

    rotated_rule = "/".join([c for c in cells])

    return rotated_rule


def load_grid(input_grid):
    """
    Convert the text form of the grid into an array form. For now this input is
    always the same. If this changes then this code would need to be replaced.
    """
    grid = [".#.", "..#", "###"]

    return grid


def split_sub_grid(grid):
    split_grid = []

    num_rows = len(grid)

    if num_rows % 2 == 0:
        block_size = 2
    else:
        block_size = 3

    # print grid

    num_blocks = num_rows / block_size
    row_idx = 0
    while row_idx < num_blocks:
        col_idx = 0

        col_grid = []

        while col_idx < num_blocks:
            pattern = ''
            for offset in xrange(block_size):
                idx = (col_idx * block_size)
                # print col_idx, block_size, offset, row_idx + offset, idx, idx + block_size
                pattern = '/'.join([pattern, grid[(row_idx *
                                                   block_size) + offset][idx:idx + block_size]])

            pattern = pattern[1:]

            # print " --> {0}".format(pattern)

            col_grid.append(pattern)

            col_idx += 1

        split_grid.append(col_grid)

        row_idx += 1

    return split_grid


def process_grid(patterns, input_grid):
    new_grid = []

    # print " INP: {0}".format(input_grid)

    for row_grid in input_grid:
        grid = split_sub_grid(row_grid)
        print "   G: {0}".format(grid)
        for row in grid:
            print row
            for sub_grid in row:
                # print sub_grid
                new_grid.append(patterns[sub_grid])

                # TODO: Pretty sure the code is failing at this point because
                #       I'm not putting the rows back together here.

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

        rules[parts[0]] = parts[1].split("/")
        rules[flip_rule(parts[0])] = parts[1].split("/")
        rules[rotate_rule(parts[0])] = parts[1].split("/")
        rules[flip_rule(rotate_rule(parts[0]))] = parts[1].split("/")
        rules[rotate_rule(rotate_rule(parts[0]))] = parts[1].split("/")
        rules[flip_rule(rotate_rule(rotate_rule(parts[0])))
              ] = parts[1].split("/")
        rules[rotate_rule(rotate_rule(rotate_rule(parts[0])))
              ] = parts[1].split("/")
        rules[flip_rule(rotate_rule(rotate_rule(
            rotate_rule(parts[0]))))] = parts[1].split("/")

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


#------------------------------------------------------------------------------
# Test code starts here
#------------------------------------------------------------------------------

# Start with some basic tests using a 2x2 grid

TEST_FLIP = flip_rule("../.#")
if TEST_FLIP != "../#.":
    print "Test 2 cell flip failed. {0}".format(TEST_FLIP)
    sys.exit(-1)
print "Test 2 cell flip passed"

TEST_ROTATE = rotate_rule("../.#")
if TEST_ROTATE != "../#.":
    print "Test 2 cell rotate (1) failed. {0}".format(TEST_ROTATE)
    sys.exit(-1)
print "Test 2 cell rotate (1) passed"
TEST_ROTATE = rotate_rule(TEST_ROTATE)
if TEST_ROTATE != "#./..":
    print "Test 2 cell rotate (2) failed. {0}".format(TEST_ROTATE)
    sys.exit(-1)
print "Test 2 cell rotate (2) passed"
TEST_ROTATE = rotate_rule(TEST_ROTATE)
if TEST_ROTATE != ".#/..":
    print "Test 2 cell rotate (3) failed. {0}".format(TEST_ROTATE)
    sys.exit(-1)
print "Test 2 cell rotate (3) passed"

TEST_SPLIT = split_sub_grid(["#..#", "....", "....", "#..#"])
if TEST_SPLIT != [['#./..', '.#/..'], ['../#.', '../.#']]:
    print "Test 2 cell split failed. {0}".format(TEST_SPLIT)
    sys.exit(-1)
print "Test 2 cell split passed"

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

TEST_SPLIT = split_sub_grid(['#..#', '....', '....', '#..#'])
if TEST_SPLIT != [['#./..', '.#/..'], ['../#.', '../.#']]:
    print "Test split (2) failed. {0}".format(TEST_SPLIT)
    sys.exit(-1)
print "Test split (2) passed"

TEST_SPLIT = split_sub_grid(load_grid(init_grid()))
if TEST_SPLIT != [['.#./..#/###']]:
    print "Test split (3) failed. {0}".format(TEST_SPLIT)
    sys.exit(-1)
print "Test split (3) passed"

# Now try and use the test input provided within the puzzle data

INPUT_RULES = """../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
"""
RULES = load_rules(INPUT_RULES)

GRID = load_grid(init_grid())
if GRID != ['.#.', '..#', '###']:
    print "Loading of test grid failed. {0}".format(GRID)
    sys.exit(-1)
print "Loading of test grid passed."

GRID = process_grid(RULES, [GRID])
if GRID != [['#..#', '....', '....', '#..#']]:
    print "Test grid move 1 failed. {0}".format(GRID)
    sys.exit(-1)
print "Test grid move 1 passed"
NUM_PIXELS = count_pixels(GRID)
if NUM_PIXELS != 4:
    print "Test count (move 1) failed. [{0}]".format(NUM_PIXELS)
    sys.exit(-1)
print "Test count (move 1) passed"

GRID = process_grid(RULES, GRID)
if GRID != [['##.', '#..', '...'], ['##.', '#..', '...'], ['##.', '#..', '...'], ['##.', '#..', '...']]:
    print "Test grid move 2 failed. {0}".format(GRID)
    sys.exit(-1)
print "Test grid move 2 passed"
NUM_PIXELS = count_pixels(GRID)
if NUM_PIXELS != 12:
    print "Test count (move 2) failed. [{0}]".format(NUM_PIXELS)
    sys.exit(-1)
print "Test count (move 2) passed"

# RULES["../.."] = "__/__"
# RULES[".#/##"] = "_*/**"
# GRID = [['.#..', '....', '#..#', '..##']]
# GRID = process_grid(RULES, GRID)
# if GRID != [['##.', '#..', '...'], ['##.', '#..', '...'], ['##.', '#..', '...'], ['##.', '#..', '...']]:
#     print "Test grid move x failed. {0}".format(GRID)
#     sys.exit(-1)
# print "Test grid move x passed"

print "All Tests passed."


#------------------------------------------------------------------------------
# Now, try and solve the puzzle itself.
#------------------------------------------------------------------------------


with open("input.txt", "r") as f:
    RULES = load_rules(f.read())

    GRID = [load_grid(init_grid())]

    for IDX in xrange(5):
        GRID = process_grid(RULES, GRID)
        print GRID
        print IDX, count_pixels(GRID)

    print "Solution is {0} pixels.".format(count_pixels(GRID))

#------------------------------------------------------------------------------
