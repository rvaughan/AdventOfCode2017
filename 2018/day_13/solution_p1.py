#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 13 of the Advent of Code for 2018.
"""

import sys


class Cart(object):

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

        self.moves = {
            '>': [1, 0],
            '<': [-1, 0],
            '^': [0, -1],
            'v': [0, 1]
            }

        self.cross_move = "L"

    def dump_cells(self, start_x, start_y, width, height, tracks, point_x=-1, point_y=-1):
        important_point=(point_x, point_y)
        for y in xrange(start_y, height):
            line = "{:02} ".format(y)
            for x in xrange(start_x, width):
                if important_point == (x,y):
                    line += "X"
                else:
                    if (x,y) in tracks:
                        line += tracks[(x,y)]
                    else:
                        line += "*"

            print line

    def pos(self):
        return (self.x,self.y)

    def tick(self, track):
        move = self.moves[self.direction]

        # print self.direction, move

        self.x += move[0]
        self.y += move[1]

        if (self.x,self.y) not in track:
            print "Oops! {} {} {}".format((self.x,self.y), self.direction, move)

            self.dump_cells(0, 0, 130, 3, tracks, 76, 0)

            sys.exit(-1)

        cell = track[(self.x,self.y)]

        if cell == "/":
            if self.direction == ">":
                self.direction = "^"
            elif self.direction == "<":
                self.direction = "v"
            elif self.direction == "^":
                self.direction = ">"
            elif self.direction == "v":
                self.direction = "<"
        elif cell == "\\":
            if self.direction == ">":
                self.direction = "v"
            elif self.direction == "<":
                self.direction = "^"
            elif self.direction == "^":
                self.direction = "<"
            elif self.direction == "v":
                self.direction = ">"
        elif cell == "+":
            if self.cross_move == "L":
                if self.direction == "<":
                    self.direction = "v"
                elif self.direction == "^":
                    self.direction = "<"
                elif self.direction == ">":
                    self.direction = "^"
                elif self.direction == "v":
                    self.direction = ">"

                self.cross_move = "S"
            elif self.cross_move == "S":
                self.cross_move = "R"
            elif self.cross_move == "R":
                if self.direction == "<":
                    self.direction = "^"
                elif self.direction == "^":
                    self.direction = ">"
                elif self.direction == ">":
                    self.direction = "v"
                elif self.direction == "v":
                    self.direction = "<"

                self.cross_move = "L"


def load_data(input_data):
    carts = []
    track = {}
    positions = {}

    width = 0
    height = len(input_data)

    for y, line in zip(xrange(len(input_data)), input_data):
        # print line
        width = len(line)
        for x, cell in zip(xrange(len(line)), line):
            if cell in "<^>v":
                cart = Cart(x, y, cell)
                carts.append(cart)
                positions[cart.pos()] = cart

                if cell in "<>":
                    track[(x,y)] = "-"
                elif cell in "^v":
                    track[(x,y)] = "|"
                else:
                    track[(x,y)] = "Z"
            else:
                # print "track"
                track[(x,y)] = cell

    return carts, positions, track, width, height


def move_carts(carts, tracks, positions):
    carts = sorted(carts, key = lambda t: (t.x, t.y), reverse=False)
    for cart in carts:
        del positions[cart.pos()]

        if cart.pos() in positions:
            # print "xxx 1"
            return True, cart.pos()

        cart.tick(tracks)

        if cart.pos() in positions:
            # print "xxx 2"
            return True, cart.pos()

        positions[cart.pos()] = cart

    return False, (0,0)


def dump(carts, track, width, height):
    for y in xrange(height):
        line = ""
        for x in xrange(width):
            if (x,y) in positions:
                line += positions[(x,y)].direction
            else:
                if (x,y) in track:
                    line += track[(x,y)]
                else:
                    line += " "

        print line
    
    print ""
    print "----========----"
    print ""


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

print ""
print "-----------------"
print "Testing.........."
print "-----------------"
print ""

test_input="""|
v
|
|
|
^
|"""

input_data = [line for line in test_input.splitlines()]
carts, positions, tracks, width, height = load_data(input_data)

# dump(positions, tracks, width, height)

crashed = False
while not crashed:
    crashed, pos = move_carts(carts, tracks, positions)
    # dump(positions, tracks, width, height)

    if crashed:
        # print "CRASH! {}".format(pos)
        assert pos == (0,3), pos


test_input="""/->-\\        
|   |  /----\\
| /-+--+-\\  |
| | |  | v  |
\\-+-/  \\-+--/
  \\------/   """

input_data = [line for line in test_input.splitlines()]
carts, positions, tracks, width, height = load_data(input_data)

crashed = False
while not crashed:
    crashed, pos = move_carts(carts, tracks, positions)
    # dump(positions, tracks, width, height)

    if crashed:
        # print "CRASH! {}".format(pos)
        assert pos == (7,3), pos

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [line.rstrip() for line in f]
    carts, positions, tracks, width, height = load_data(input_data)

    crashed = False
    while not crashed:
        crashed, pos = move_carts(carts, tracks, positions)
        # dump(positions, tracks, width, height)

        if crashed:
            print "Solution is {}".format(pos)
