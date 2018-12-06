#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 6 of the Advent of Code for 2018.
"""

from collections import Counter
import sys


def build_grid(test_input):
    co_ords = {}

    max_x = 0
    max_y = 0

    for id, c in zip(xrange(len(test_input)), test_input):
        x, y = c.split(', ')

        co_ords[id] = [int(x), int(y)]

        max_x = max(max_x, int(x))
        max_y = max(max_x, int(y))

    max_x += 2
    max_y += 2

    grid = []
    for col in xrange(max_y):
        grid.append(['.'] * max_x)

    for pos in co_ords.keys():
        grid[co_ords[pos][1]][co_ords[pos][0]] = int(pos)

    return grid, co_ords


def check_grid_cell(co_ords, y, x):
    closest = []
    closest_pos = 999999999999

    for c_val in coords:
        c = coords[c_val]

        # print "  |", c_val, c[0], c[1], x, y, abs(x - c[0]), abs(y - c[1])

        c_pos = abs(x - c[0]) + abs(y - c[1])

        if  c_pos == closest_pos:
            # print "==="
            closest.append(c_val)

            # print " > ", c_val, c_pos, closest_pos
        elif  c_pos < closest_pos:
            # print "<<<"
            closest_pos = c_pos

            closest = []
            closest.append(c_val)

            # print " > ", c_val, c_pos, closest_pos
    #     else:
    #         print ">>>"

    #     print "-> ", c_val, c_pos, closest_pos

    # print "-->", closest

    if len(closest) == 1:
        return closest[0]

    return '.'


def find_closest_points(grid, coords):
    for x in xrange(len(grid)):
        for y in xrange(len(grid[x])):
            if grid[x][y] == '.':

                closest = check_grid_cell(coords, x, y)

                # print x, y, closest

                grid[x][y] = closest


def find_edge_coords(grid):
    ignore_set = set()

    # Top edge
    for y in xrange(len(grid[0])):
        if grid[0][y] != '.':
            ignore_set.add(grid[0][y])

    # Bottom edge
    for y in xrange(len(grid[0])):
        if grid[len(grid[0])-1][y] != '.':
            ignore_set.add(grid[len(grid[0])-1][y])

    # Left edge
    for x in xrange(len(grid)):
        if grid[x][0] != '.':
            ignore_set.add(grid[x][0])

    # Right edge
    for x in xrange(len(grid)):
        if grid[x][len(grid[0])-1] != '.':
            ignore_set.add(grid[x][len(grid[0])-1])

    return ignore_set


def find_none_infinite(grid):
    result_list = set()
    ignore_list = find_edge_coords(grid)

    for x in xrange(len(grid)):
        for y in xrange(len(grid[x])):
            if grid[x][y] != '.' and grid[x][y] not in ignore_list:
                result_list.add(grid[x][y])

    return list(result_list)


def calc_size(grid, coord):
    count = 0

    for x in xrange(len(grid)):
        for y in xrange(len(grid[x])):
            if grid[x][y] == coord:
                count += 1

    return count


def calc_max(grid, coord_list):
    max_size = 0
    max_coord = -1

    for coord in coord_list:
        coord_size = calc_size(grid, coord)

        if coord_size > max_size:
            max_size = coord_size
            max_coord = coord

    return max_coord, max_size


def dump_grid(grid):
    for x in xrange(len(grid)):
        line = ""
        for y in xrange(len(grid[x])):
            line += str(grid[x][y])

        print line


def run_extract_test(test_input, exp_id, exp_offset_x, exp_offset_y, exp_width, exp_height):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    x_id, offset_x, offset_y, width, height = extract_instructions(test_input)

    if x_id != exp_id or offset_x != exp_offset_x or offset_y != exp_offset_y or width != exp_width or height != exp_height:
        print "Test for {0} FAILED. Got a result of {1}, {2}, {3}, {4}, {5}".format(test_input, id, offset_x, offset_y, width, height)
        sys.exit(-1)

    print "Test for {0} passed.".format(test_input)


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

print ""
print "-----------------"
print "Testing.........."
print "-----------------"
print ""

test_input="""1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""

input_data = [line for line in test_input.split('\n')]
grid, coords = build_grid(input_data)

# dump_grid(grid)

result = check_grid_cell(coords, 0, 0)
assert 0 == result, "Wrong result at 0, 1, got %d not %d" % (result, 0)

result = check_grid_cell(coords, 0, 1)
assert 0 == result, "Wrong result at 0, 1, got %d not %d" % (result, 0)

result = check_grid_cell(coords, 0, 2)
assert 0 == result, "Wrong result at 0, 2, got %d not %d" % (result, 0)

result = check_grid_cell(coords, 0, 3)
assert 0 == result, "Wrong result at 0, 3, got %d not %d" % (result, 0)

result = check_grid_cell(coords, 0, 4)
assert 0 == result, "Wrong result at 0, 4, got %d not %d" % (result, 0)

result = check_grid_cell(coords, 0, 5)
assert '.' == result, "Wrong result at 0, 5, got %d not %d" % (result, '.')

result = check_grid_cell(coords, 0, 6)
assert 2 == result, "Wrong result at 0, 6, got %d not %d" % (result, 2)

result = check_grid_cell(coords, 0, 7)
assert 2 == result, "Wrong result at 0, 7, got %d not %d" % (result, 2)

result = check_grid_cell(coords, 0, 8)
assert 2 == result, "Wrong result at 0, 8, got %d not %d" % (result, 2)

find_closest_points(grid, coords)

# dump_grid(grid)

finite_coords = find_none_infinite(grid)

assert len(finite_coords) == 2, "Wrong number of finite results, expected %d but got %d" % (2, len(finite_coords))

assert finite_coords[0] == 3, "Incorrect coordinate found %d was looking for %d" % (3, finite_coords[0])
assert finite_coords[1] == 4, "Incorrect coordinate found %d was looking for %d" % (4, finite_coords[1])

coord_size = calc_size(grid, 3)
assert coord_size == 9, "Incorrect size for coord 3, expected %d but got %d" % (9, coord_size)

coord_size = calc_size(grid, 4)
assert coord_size == 17, "Incorrect size for coord 4, expected %d but got %d" % (17, coord_size)

max_coord, max_size = calc_max(grid, finite_coords)
assert max_coord == 4, "Incorrect size for coord 4, expected %d but got %d" % (17, coord_size)
assert max_size == 17, "Incorrect size for coord 4, expected %d but got %d" % (17, coord_size)

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [line for line in f]
    
    grid, coords = build_grid(input_data)
    
    find_closest_points(grid, coords)
    
    finite_coords = find_none_infinite(grid)

    max_coord, max_size = calc_max(grid, finite_coords)

    print "Solution is coord: {}, size: {}".format(max_coord, max_size)
