#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 18 of the Advent of Code for 2023.
"""
import sys
from queue import Queue


def calculate_solution(items):
    instructions = [x.split() for x in items]

    grid = []
    explored = {}
    x, y = 0, 0
    for _ in range(15):
        grid.append(['.'] * 15)

    for instruction in instructions:
        direction, count, colour  = instruction
        count = int(count)

        if direction == 'R':
            for _ in range(count):
                x += 1
                grid[y][x] = '#'
        elif direction == 'L':
            for _ in range(count):
                x -= 1
                grid[y][x] = '#'
        elif direction == 'U':
            for _ in range(count):
                y -= 1
                grid[y][x] = '#'
        elif direction == 'D':
            for _ in range(count):
                y += 1
                grid[y][x] = '#'

        explored[(y, x)] = True

    print()
    for row in grid:
        print(''.join(row))
    print()

    result = 0

    for row in grid:
        for cell in row:
            result += 1 if cell == '#' else 0

    # This code is taken from day 10...

    # Now stretch the map
    new_rows = len(grid) * 3
    new_cols = len(grid[0]) * 3
    huge_map = [['.' for _ in range(new_cols)] for _ in range(new_rows)]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) not in explored:
                continue

            if grid[row][col] == '|':
                huge_map[3*row+0][3*col+1] = '*'
                huge_map[3*row+1][3*col+1] = '*'
                huge_map[3*row+2][3*col+1] = '*'
            elif grid[row][col] == '-':
                huge_map[3*row+1][3*col+0] = '*'
                huge_map[3*row+1][3*col+1] = '*'
                huge_map[3*row+1][3*col+2] = '*'
            elif grid[row][col] == '7':
                huge_map[3*row+1][3*col+0] = '*'
                huge_map[3*row+1][3*col+1] = '*'
                huge_map[3*row+2][3*col+1] = '*'
            elif grid[row][col] == 'F':
                huge_map[3*row+2][3*col+1] = '*'
                huge_map[3*row+1][3*col+1] = '*'
                huge_map[3*row+1][3*col+2] = '*'
            elif grid[row][col] == 'J':
                huge_map[3*row+1][3*col+0] = '*'
                huge_map[3*row+1][3*col+1] = '*'
                huge_map[3*row+0][3*col+1] = '*'
            elif grid[row][col] == 'L':
                huge_map[3*row+0][3*col+1] = '*'
                huge_map[3*row+1][3*col+1] = '*'
                huge_map[3*row+1][3*col+2] = '*'
            else:
                pass

    # Now, flood fill the map
    q = Queue()

    i, j = 0, 0
    q.put((i, j))

    di0 = [0, 0, 1, -1]
    dj0 = [1, -1, 0, 0]

    while not q.empty():
        i, j = q.get()
        for d in range(4):
            i_next = i+di0[d]
            j_next = j+dj0[d]
            if i_next >= 0 and j_next >= 0 and i_next < len(huge_map) and j_next < len(huge_map[0]) and huge_map[i_next][j_next] == '.':
                huge_map[i_next][j_next] = ' '
                q.put((i_next, j_next))

    # Ok, so now we should be able to iterate over the row, 3 cells at a time
    # and look at the middle cell. If it's a dot then we count it.
    for row in range(1, len(huge_map), 3):
        row_data = ''
        count = 0
        for col in range(1, len(huge_map[0]), 3):
            row_data += huge_map[row][col]
            if huge_map[row][col] == '.':
                count += 1

        # print(row_data, count)
        result += count

    return result


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'))

    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""
result = run_test(test_list, 62)

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
