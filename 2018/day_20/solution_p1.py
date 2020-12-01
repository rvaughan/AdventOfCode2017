#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 18 of the Advent of Code for 2018.
"""

class Cell(object):

    def __init__(self, positions, x, y):
        self.positions = positions
        self.x = x
        self.y = y

        self.positions[(self.x, self.y)] = self

        self.north = None
        self.east = None
        self.south = None
        self.west = None

    def add_north(self):
        self.north = Cell(self.positions, self.x, self.y - 1)

    def add_east(self):
        self.east = Cell(self.positions, self.x + 1, self.y)

    def add_south(self):
        self.south = Cell(self.positions, self.x, self.y - 1)

    def add_west(self):
        self.west = Cell(self.positions, self.x - 1, self.y)


def build_map(start, input_data):
    current_cell = start
    pos = 1
    while pos < len(input_data):
        cell = input_data[pos]

        if cell == "N":
            current_cell.add_north()
        elif cell == "E":
            current_cell.add_east()
        elif cell == "S":
            current_cell.add_south()
        elif cell == "W":
            current_cell.add_west()

        pos += 1


def dump_map(positions):
    min_x = 9999999
    max_x = 0
    min_y = 9999999
    max_y = 0
    for key in positions:
        if key[0] < min_x:
            min_x = key[0]
        if key[0] > max_x:
            max_x = key[0]

        if key[1] < min_y:
            min_y = key[1]
        if key[1] > max_y:
            max_y = key[1]

    print min_x, min_y, max_x, max_y

    cur_x = min_x
    cur_y = min_y

    top_line = ""
    mid_line = ""
    while True:
        if (cur_x, cur_y) in positions:
            if positions[(cur_x, cur_y)].north is not None:
                top_line += "-"
            else:
                top_line += "#"

            if positions[(cur_x, cur_y)].west is not None:
                mid_line += "|"
            else:
                mid_line += "#"

            if cur_x == 0 and cur_y == 0:
                mid_line += "X"
            else:
                mid_line += "."
        else:
            # print cur_x, cur_y
            # print positions
            top_line += "++"
            mid_line += "++"
            # x

        cur_x += 1
        if cur_x > max_x:
            cur_x = min_x
            cur_y += 1

            print top_line
            print mid_line

        if cur_y > max_y:
            break


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

print ""
print "-----------------"
print "Testing.........."
print "-----------------"
print ""

test_data="^WNE$"
positions = {}
start = Cell(positions, 0, 0)
build_map(start, test_data)

# print positions
dump_map(positions)

assert False

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [line.strip() for line in f]

    instructions = input_data[1:]

    ip = 0
    registers = [0] * 6
    init_ip = load_instruction_pointer(input_data[0], ip, registers)

    while ip < len(instructions):
        ip = load_instruction(instructions, ip, registers, initial_ip=init_ip)
        # sleep(1)

    print "Solution: {}".format(registers[0])
