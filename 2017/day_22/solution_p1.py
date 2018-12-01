#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 22 of the Advent of Code for 2017.
"""

from collections import defaultdict
import sys


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


def default_factory():
    return "."


def turn_left(direction):
    if direction == UP:
        return LEFT

    if direction == LEFT:
        return DOWN

    if direction == DOWN:
        return RIGHT

    if direction == RIGHT:
        return UP


def turn_right(direction):
    if direction == UP:
        return RIGHT

    if direction == RIGHT:
        return DOWN

    if direction == DOWN:
        return LEFT

    if direction == LEFT:
        return UP


def do_moves(map, cur_pos, num_moves):
    cur_direction = UP
    infected = 0
    for _ in xrange(num_moves):
        # Work out where we are going to move to
        if map[cur_pos] == ".":
            cur_direction = turn_left(cur_direction)
        else:
            cur_direction = turn_right(cur_direction)

        # Infect / cleanse
        if map[cur_pos] == ".":
            map[cur_pos] = "#"
            infected += 1
        else:
            map[cur_pos] = "."

        # Do move
        cur_pos = (cur_pos[0] + cur_direction[0], cur_pos[1] + cur_direction[1])

    return infected


def load_map(filename):
    cur_pos = (0, 0)
    map = defaultdict(default_factory)
    with open(filename, "r") as f:
        for row_idx, line in enumerate(f.readlines()):
            line = line.strip()
            cur_pos = (row_idx, 0)
            for cell_idx, cell in zip(xrange(len(line)), line):
                map[(row_idx, cell_idx)] = cell

                cur_pos = (row_idx, cell_idx)

        cur_pos = (cur_pos[0] / 2), (cur_pos[1] / 2)

    return map, cur_pos


def dump_map(map):
    for row_idx in xrange(-5, 10, 1):
        row = "{0} ".format(row_idx)
        for cell_idx in xrange(-5, 10, 1):
            row += map[(row_idx, cell_idx)]

        print row

# Run some tests on the code.

MAP, CUR_POS = load_map("test_map.txt")
if do_moves(MAP, CUR_POS, 7) != 5:
    print "First map moves failed"
    dump_map(MAP)
    sys.exit(-1)
print "First moves ok"

MAP, CUR_POS = load_map("test_map.txt")
if do_moves(MAP, CUR_POS, 70) != 41:
    print "Second map moves failed"
    dump_map(MAP)
    sys.exit(-1)
print "Second moves ok"

# All tests passing...

MAP, CUR_POS = load_map("input.txt")
print "Solution is: {0}".format(do_moves(MAP, CUR_POS, 10000))
