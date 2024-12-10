#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 10 of the Advent of Code for 2024.
"""
import sys


def search(grid, pos):
    summits = []

    # left, right, up, down
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        npos = (pos[0] + dx, pos[1] + dy)
        if npos[0] < 0 or npos[1] < 0 or npos[0] > len(grid[0]) - 1 or npos[1] > len(grid) -1:
            continue

        nval = grid[npos[1]][npos[0]]
        if grid[pos[1]][pos[0]] + 1 == nval:
            summits += [npos] if nval == 9 else search(grid, npos)

    return summits


def calculate_solution(items):
    grid = []
    for line in items:
        grid.append([int(x) for x in line.strip()])

    trail_heads = []
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if grid[y][x] == 0:
                trail_heads.append((x, y))

    trails = [search(grid, trail_head) for trail_head in trail_heads]

    result = sum(len(set(trail)) for trail in trails)

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

test_list = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
result = run_test(test_list, 81)

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
