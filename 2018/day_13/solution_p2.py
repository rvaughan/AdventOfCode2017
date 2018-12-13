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
        self.deleted = False

        self.moves = {
            '>': [1, 0],
            '<': [-1, 0],
            '^': [0, -1],
            'v': [0, 1]
            }

        self.cross_move = "L"

    def dump(self):
        print "{} {} '{}' {}".format(self.x, self.y, self.direction, self.moves[self.direction])

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
    crashed_cart = None

    carts = sorted(carts, key = lambda t: (t.x, t.y), reverse=False)
    for cart in carts:
        if cart.deleted:
            # print "Ignoring: {} {} {}".format(cart.x, cart.y, cart.direction)
            continue

        del positions[cart.pos()]

        cart.tick(tracks)

        if cart.pos() in positions:
            crashed_cart = cart
            cart.deleted = True
            positions[cart.pos()].deleted = True
            # cart.dump()
            # positions[cart.pos()].dump()
            del positions[cart.pos()]

        if not cart.deleted:
            positions[cart.pos()] = cart

    return (crashed_cart is not None), crashed_cart


def move_carts_with_removal(carts, tracks, positions):
    crashed, cart = move_carts(carts, tracks, positions)

    if crashed:
        tmp_carts = list(carts)
        # print "Deleting:"
        for cart in tmp_carts:
            if cart.deleted:
                # cart.dump()
                carts.remove(cart)
                if cart.pos() in positions:
                    del positions[cart.pos()]
        # print ""


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

print "Running Test #1"
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
    crashed, cart = move_carts(carts, tracks, positions)
    # dump(positions, tracks, width, height)

    if crashed:
        # print "CRASH! {}".format(cart.pos())
        assert cart.pos() == (0,3), cart.pos()

print "Running Test #2"

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
    crashed, cart = move_carts(carts, tracks, positions)
    # dump(positions, tracks, width, height)

    if crashed:
        # print "CRASH! {}".format(cart.pos())
        assert cart.pos() == (7,3), cart.pos()

print "Running Test #3"

test_input="""/>-<\\  
|   |  
| /<+-\\
| | | v
\\>+</ |
  |   ^
  \\<->/"""

input_data = [line for line in test_input.splitlines()]
carts, positions, tracks, width, height = load_data(input_data)

last_cart = carts[8]

while len(carts) > 1:
    # last_cart.dump()
    move_carts_with_removal(carts, tracks, positions)
    # dump(positions, tracks, width, height)

    # last_cart.dump_cells(0, 0, width, height, tracks, last_cart.x, last_cart.y)

assert carts[0].pos() == (6,4), carts[0].pos()


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

    while len(carts) > 1:
        move_carts_with_removal(carts, tracks, positions)
        # dump(positions, tracks, width, height)

        # last_cart.dump_cells(0, 0, width, height, tracks, last_cart.x, last_cart.y)

    print "Solution is: {}".format(carts[0].pos())
