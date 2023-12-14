#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 14 of the Advent of Code for 2023.
"""
import sys


def calculate_solution(items):

    grid = []
    for item in items:
        grid.append([x for x in item])
        
    # Move the rocks north
    movement = True
    while movement:
        movement = False
        for row_idx in range(1, len(grid)):
            for idx, cell in enumerate(grid[row_idx]):
                if grid[row_idx-1][idx] == '.' and cell == 'O':
                    grid[row_idx-1][idx] = 'O'
                    grid[row_idx][idx] = '.'
                    movement = True

    # Calculate the load
    load = 0

    for row_idx in range(len(grid)):
        rock_score = len(grid) - row_idx
        for idx, cell in enumerate(grid[row_idx]):
            load += rock_score if cell == 'O' else 0

    return load


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

test_list = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

result = run_test(test_list, 136)

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
