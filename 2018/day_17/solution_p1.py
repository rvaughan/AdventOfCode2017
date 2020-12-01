#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 14 of the Advent of Code for 2018.
"""


def generate_map(input_data):
    min_y = 999999999
    max_y = 0
    min_x = 500
    max_x = 500
    
    my_map = []
    for _ in xrange(1000):
        my_map.append(['.'] * 1000)

    for line in input_data:
        pieces = line.split(', ')

        x_locs = []
        y_locs = []

        first = pieces[0].split('=')
        if first[0] == 'x':
            x_pos = int(first[1])
            if x_pos < min_x:
                min_x = x_pos
            elif x_pos > max_x:
                max_x = max_x

            x_locs.append(x_pos)
        else:
            y_pos = int(first[1])
            if y_pos < min_y:
                min_y = y_pos
            elif y_pos > max_y:
                max_y = max_y

            y_locs.append(y_pos)

        first = pieces[1].split('=')
        if first[0] == 'x':
            x_pieces = [int(x) for x in pieces[1].split('=')[1].split('..')]
            if x_pieces[0] < min_x:
                min_x = x_pieces[0]
            elif x_pieces[-1] > max_x:
                max_x = x_pieces[-1]

            for pos in xrange(x_pieces[0], x_pieces[1]+1):
                x_locs.append(pos)
        else:
            y_pieces = [int(y) for y in pieces[1].split('=')[1].split('..')]
            if y_pieces[0] < min_y:
                min_y = y_pieces[0]
            elif y_pieces[-1] > max_y:
                max_y = y_pieces[-1]

            for pos in xrange(y_pieces[0], y_pieces[1]+1):
                y_locs.append(pos)

        for y in y_locs:
            for x in x_locs:
                my_map[y][x] = "#"

    # print min_x, max_x, min_y, max_y

    new_map = []
    for row_idx in xrange(min_y-1, max_y+2):
        row = my_map[row_idx]
        new_row = []
        for col_idx in xrange(min_x-1, max_x+4):
            new_row.append(row[col_idx])

        new_map.append(new_row)

    water_point = (500 - min_x) + 1
    new_map[0][water_point] = '+'

    return new_map, water_point


def dump_map(my_map):
    for row in my_map:
        line = ""
        for cell in row:
            line += cell

        print line


def add_water(ground_map, water_point, verbose=False):
    x = water_point
    y = 1
    fill_char = "|"

    while True:
        if verbose:
            print x, y, ground_map[y][x], ground_map[y+1][x]

        if ground_map[y][x] == ".":
            if verbose:
                print "... drop"

            if ground_map[y+1][x] == "#":
                if verbose:
                    print "... settling"

                ground_map[y][x] = "~"
            else:
                ground_map[y][x] = fill_char

            return
        else:
            if ground_map[y][x] == "~":
                if verbose:
                    print "... splash"

                if ground_map[y][x-1] == "#":
                    if verbose:
                        print "... wall (to left)"

                    fill_char = "~"

                    last_pos = x
                    while True:
                        if ground_map[y][x] not in ["|", ".", "#"]:
                            x += 1
                        else:
                            break

                    if ground_map[y][x] == '#':
                        x = last_pos
                        y -= 1
                        while ground_map[y][x] != "|":
                            x += 1
                        ground_map[y][x] = fill_char
                    else:
                        ground_map[y][x] = fill_char
                    
                    return
                else:
                    x -= 1

            elif ground_map[y+1][x] == "~":
                fill_char = "~"

                if verbose:
                    print "... resting water"

                if ground_map[y+1][x-1] != "#":
                    if verbose:
                        print "... not a wall (beneath)"

                    x -= 1
                    y += 1
                else:
                    x += 1
                    y += 1
            elif ground_map[y+1][x] == "#":
                if verbose:
                    print "... settling"

                ground_map[y][x] = "~"
                return
            else:
                y += 1


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

print ""
print "-----------------"
print "Testing.........."
print "-----------------"
print ""

test_input="""x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504"""

input_data = [line.strip() for line in test_input.splitlines()]
ground_map, water_point = generate_map(input_data)

# dump_map(ground_map)

print "Test 1 - Drip to clay"
add_water(ground_map, water_point)
add_water(ground_map, water_point)
add_water(ground_map, water_point)
add_water(ground_map, water_point)
add_water(ground_map, water_point)
# dump_map(ground_map)


print "Test 2 - Pool in bottom of clay"
add_water(ground_map, water_point)
add_water(ground_map, water_point)
add_water(ground_map, water_point)
add_water(ground_map, water_point)
add_water(ground_map, water_point)
# dump_map(ground_map)

print "Test 3 - Start filling clay"
add_water(ground_map, water_point)
add_water(ground_map, water_point)
add_water(ground_map, water_point)
add_water(ground_map, water_point)
add_water(ground_map, water_point)
# dump_map(ground_map)

print "Test 4 - Start filling section"
add_water(ground_map, water_point)
add_water(ground_map, water_point)
# dump_map(ground_map)

print "Test 5 - Keep filling section"
add_water(ground_map, water_point)
add_water(ground_map, water_point)
# dump_map(ground_map)

print "Test 6 - Overflow"
add_water(ground_map, water_point)
add_water(ground_map, water_point)
add_water(ground_map, water_point)
add_water(ground_map, water_point)
add_water(ground_map, water_point)
dump_map(ground_map)

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

    num_samples = 0
    num_triples = 0
    cur_line = 0
    while cur_line < len(input_data):
        if len(input_data[cur_line]) == 0:
            cur_line += 1
        else:
            opcodes = [''] * 16
            if input_data[cur_line][0] == 'B':
                num_samples += 1
                process_sample(opcodes, input_data[cur_line:cur_line+3])
                cur_line += 4

                num_triples += sum([1 if code == "triple" else 0 for code in opcodes])
            else:
                cur_line += 1

    print "Solution: {} [saw {} samples]".format(num_triples, num_samples)
