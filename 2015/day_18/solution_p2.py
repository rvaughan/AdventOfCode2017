#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 18 of the Advent of Code for 2015.
"""


def load_grid(raw_grid):
    grid = []

    for line in raw_grid:
        row = [1 if cell == '#' else 0 for cell in line]
        grid.append(row)

    return grid


def peek_cell(grid, position, verbose=True):
    state = 0

    y_pos = position[0]
    x_pos = position[1]

    try:
        if (((y_pos >= 0) and (y_pos < len(grid))) and ((x_pos >= 0) and (y_pos < len(grid[y_pos])))):
            state = grid[y_pos][x_pos]
    except IndexError:
        pass

    return state


def process_grid(grid):
    tmp = []
    for row in grid:
        tmp.append(list(row))

    for y in xrange(len(grid)):
        for x in xrange(len(grid[y])):
            state = grid[y][x]

            cells = [(y-1, x-1), (y-1, x), (y-1, x+1), (y, x-1), (y, x+1), (y+1, x-1), (y+1, x), (y+1, x+1)]
            states = [peek_cell(grid, cell) for cell in cells]

            if state == 1:
                if sum(states) == 2:
                    state = 1
                elif sum(states) == 3:
                    state = 1
                else:
                    state = 0
            else:
                if sum(states) == 3:
                    state = 1

            tmp[y][x] = state

    tmp[0][0] = 1
    tmp[len(tmp)-1][0] = 1
    tmp[0][len(tmp[0])-1] = 1
    tmp[len(tmp)-1][len(tmp[0])-1] = 1

    return tmp


def count_lit_lights(grid):
    count = 0
    for row in grid:
        count += sum(row)

    return count


def dump_grid(grid):
    for y in xrange(len(grid)):
        row = ""
        for x in xrange(len(grid[y])):
            if grid[y][x] == 1:
                row += "#"
            else:
                row += "."

        print row

    print ""


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

raw_grid = """.#.#.#
...##.
#....#
..#...
#.#..#
####.."""

grid_data = [line for line in raw_grid.splitlines()]

grid = load_grid(grid_data)
grid[0][0] = 1
grid[len(grid)-1][0] = 1
grid[0][len(grid[0])-1] = 1
grid[len(grid)-1][len(grid[0])-1] = 1

state = peek_cell(grid, (0, 0))
assert state == 1

state = peek_cell(grid, (0, 1))
assert state == 1

state = peek_cell(grid, (0, 2))
assert state == 0

x = 2
y = 0
cells = [(y-1, x-1), (y-1, x), (y-1, x+1), (y, x-1), (y, x+1), (y+1, x-1), (y+1, x), (y+1, x+1)]
states = [peek_cell(grid, cell) for cell in cells]
assert sum(states) == 3, sum(states)

x = 3
y = 0
cells = [(y-1, x-1), (y-1, x), (y-1, x+1), (y, x-1), (y, x+1), (y+1, x-1), (y+1, x), (y+1, x+1)]
states = [peek_cell(grid, cell) for cell in cells]
assert sum(states) == 2, sum(states)

# grid = load_grid(grid_data)
# new_grid = process_grid(grid)
# dump_grid(grid)
# dump_grid(new_grid)
# assert False

grid = load_grid(grid_data)
grid[0][0] = 1
grid[len(grid)-1][0] = 1
grid[0][len(grid[0])-1] = 1
grid[len(grid)-1][len(grid[0])-1] = 1

# dump_grid(grid)
# assert False

lights_on = count_lit_lights(grid)
assert lights_on == 17, lights_on

grid = process_grid(grid)

# dump_grid(grid)
# assert False

lights_on = count_lit_lights(grid)
assert lights_on == 18, lights_on

grid = process_grid(grid)

# dump_grid(grid)

lights_on = count_lit_lights(grid)
assert lights_on == 18, lights_on

grid = process_grid(grid)

# dump_grid(grid)

lights_on = count_lit_lights(grid)
assert lights_on == 18, lights_on

grid = process_grid(grid)

# dump_grid(grid)

lights_on = count_lit_lights(grid)
assert lights_on == 14, lights_on

grid = load_grid(grid_data)
grid[0][0] = 1
grid[len(grid)-1][0] = 1
grid[0][len(grid[0])-1] = 1
grid[len(grid)-1][len(grid[0])-1] = 1
for _ in xrange(5):
    grid = process_grid(grid)
lights_on = count_lit_lights(grid)
assert lights_on == 17, lights_on

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual data now.

with open("input.txt", "r") as f:
    grid_data = [line.rstrip() for line in f]

    grid = load_grid(grid_data)
    grid[0][0] = 1
    grid[len(grid)-1][0] = 1
    grid[0][len(grid[0])-1] = 1
    grid[len(grid)-1][len(grid[0])-1] = 1

    for _ in xrange(100):
        grid = process_grid(grid)

    count = count_lit_lights(grid)

    print("Solution: {}".format(count))
