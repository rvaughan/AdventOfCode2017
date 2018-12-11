#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 11 of the Advent of Code for 2018.
"""


def calc_total_power(grid, start_x, start_y, verbose=False):
    total_power = 0

    for y in xrange(start_y, start_y + 3):
        for x in xrange(start_x, start_x + 3):
            if verbose:
                print x, y, grid[y][x]

            total_power += grid[y][x]

    return total_power


def find_max_power(grid):
    max_power = 0
    max_x = 0
    max_y = 0

    for y in xrange(len(grid) - 2):
        for x in xrange(len(grid) - 2):
            power = calc_total_power(grid, x, y)
            if power > max_power:
                max_power = power
                max_x = x
                max_y = y

    return max_x, max_y, max_power


def calc_cell_power(x, y, serial_num, verbose=False):
    rack_id = x + 10

    if verbose:
        print rack_id

    power_level = (rack_id * y)
    if verbose:
        print power_level
    
    power_level += serial_num
    if verbose:
        print power_level
    
    power_level *= rack_id
    if verbose:
        print power_level

    power_level /= 100
    if verbose:
        print power_level
    power_level %= 10
    if verbose:
        print power_level

    power_level -= 5
    if verbose:
        print power_level

    return power_level


def new_fuel_grid(width, height, serial_num):
    fg = []

    for y in xrange(height):
        row = []
        for x in xrange(width):
            row.append(calc_cell_power(x, y, serial_num))

        fg.append(row)

    return fg


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

print ""
print "-----------------"
print "Testing.........."
print "-----------------"
print ""

power = calc_cell_power(3, 5, 8)
assert power == 4, power

power = calc_cell_power(122, 79, 57)
assert power == -5, power

power = calc_cell_power(217, 196, 39)
assert power == 0, power

power = calc_cell_power(101, 153, 71)
assert power == 4, power

fuel_grid = new_fuel_grid(300, 300, 18)
total_power = calc_total_power(fuel_grid, 33, 45)
assert total_power == 29, total_power

max_x, max_y, max_power = find_max_power(fuel_grid)
assert max_x == 33, max_x
assert max_y == 45, max_y
assert max_power == 29, max_power

fuel_grid = new_fuel_grid(300, 300, 42)
total_power = calc_total_power(fuel_grid, 21, 61)
assert total_power == 30, total_power

max_x, max_y, max_power = find_max_power(fuel_grid)
assert max_x == 21, max_x
assert max_y == 61, max_y
assert max_power == 30, max_power

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    fuel_grid = new_fuel_grid(300, 300, 3628)

    max_x, max_y, max_power = find_max_power(fuel_grid)

    print "Solution is {},{}".format(max_x, max_y)
