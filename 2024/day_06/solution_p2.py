#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 6 of the Advent of Code for 2024.
"""
import sys


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

    pos = start
    visited = set()
    visited.add(pos)
    direction = 0

    while True:
        if direction == 0: # up
            next_pos = (pos[0], pos[1] - 1)
        elif direction == 1: # right
            next_pos = (pos[0] + 1, pos[1])
        elif direction == 2: # down
            next_pos = (pos[0], pos[1] + 1)
        elif direction == 3: # left
            next_pos = (pos[0] - 1, pos[1])

        if next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] > width or next_pos[1] > height:
            break

        if grid[next_pos] == '#':
            direction = (direction + 1) % 4
            continue

        pos = next_pos

        visited.add(pos)

    result = len(visited)

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
result = run_test(test_list, 41)

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
