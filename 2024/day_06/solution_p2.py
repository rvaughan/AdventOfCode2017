#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 6 of the Advent of Code for 2024.
"""
import sys


def dump_grid(grid, height, width, visited):
    for y in range(height + 1):
        for x in range(0, width + 1):
            for direction in range(4):
                if ((x, y), direction) in visited:
                    grid[(x,y)] = 'x'

    for y in range(height + 1):
        row = ''
        for x in range(0, width + 1):
            row += grid[(x, y)]

        print(row)


def check_obstruction(starting_grid, height, width, start, obstruction):
    pos = start
    visited = set()
    direction = 0
    visited.add((pos, direction))

    # Can't place the obstacle on the guards starting position.
    if start == obstruction:
        return False

    # If there's an obstruction already in that location, just ignore this run as it won't change
    # anything.
    if starting_grid[obstruction] == '#':
        return False

    # Make a copy of the original grid so we don't just end up filling it with obstacles!
    grid = starting_grid.copy()

    grid[obstruction] = '#'

    spinning = 0
    while True:
        if direction == 0: # up
            next_pos = (pos[0], pos[1] - 1)
        elif direction == 1: # right
            next_pos = (pos[0] + 1, pos[1])
        elif direction == 2: # down
            next_pos = (pos[0], pos[1] + 1)
        elif direction == 3: # left
            next_pos = (pos[0] - 1, pos[1])

        # Have we been here, walking in the same direction previously?
        if (next_pos, direction) in visited:
            return True

        # Have we gone off the end of the grid?
        if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] > width or next_pos[1] > height:
            break

        # Are we blocked in that direction?
        if grid[next_pos] == '#':
            direction = (direction + 1) % 4

            # There's a chance we're stuck somewhere, are we just spinning?
            spinning += 1
            if spinning > 4:
                return False
            
            continue

        spinning = 0

        # Move there
        pos = next_pos

        visited.add((pos, direction))

    # dump_grid(grid, width, height, visited)

    return False


def calculate_solution(items):
    result = 0

    start = (0,0)
    grid = {}
    for y, line in enumerate(items):
        for x, char in enumerate(line):
            grid[(x, y)] = char
            if char == '^':
                start = (x, y)

    height = len(items) - 1
    width = len(items[0]) - 1

    # result = check_obstruction(grid, height, width, start, (start[0]-1, start[1]))
    # result = check_obstruction(grid, height, width, start, (1, 9))

    for x in range(width + 1):
        for y in range(height + 1):
            obstruction = (x, y)
            if check_obstruction(grid, height, width, start, obstruction):
                result += 1
                # print(f'Found solution at {obstruction}')

    return result


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'))

    print()
    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
result = run_test(test_list, 6)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data)

    print(f'Solution is {answer}')
