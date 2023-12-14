#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 14 of the Advent of Code for 2023.
"""
import sys


def roll_north(grid):
    movement = True
    while movement:
        movement = False
        for row_idx in range(1, len(grid)):
            for idx, cell in enumerate(grid[row_idx]):
                if grid[row_idx-1][idx] == '.' and cell == 'O':
                    grid[row_idx-1][idx] = 'O'
                    grid[row_idx][idx] = '.'
                    movement = True
    return grid


def roll_south(grid):
    movement = True
    while movement:
        movement = False
        for row_idx in range(len(grid) - 2, -1, -1):
            for idx, cell in enumerate(grid[row_idx]):
                if grid[row_idx+1][idx] == '.' and cell == 'O':
                    grid[row_idx+1][idx] = 'O'
                    grid[row_idx][idx] = '.'
                    movement = True
    return grid


def roll_east(grid):
    movement = True
    while movement:
        movement = False
        for row_idx in range(len(grid)):
            for idx in range(len(grid[row_idx]) -2, -1, -1):
                if idx == len(grid[row_idx]) - 1:
                    continue
                
                if grid[row_idx][idx+1] == '.' and grid[row_idx][idx] == 'O':
                    grid[row_idx][idx+1] = 'O'
                    grid[row_idx][idx] = '.'
                    movement = True
    return grid


def roll_west(grid):
    movement = True
    while movement:
        movement = False
        for row_idx in range(len(grid)):
            for idx, cell in enumerate(grid[row_idx]):
                if idx == 0:
                    continue

                if grid[row_idx][idx-1] == '.' and cell == 'O':
                    grid[row_idx][idx-1] = 'O'
                    grid[row_idx][idx] = '.'
                    movement = True
    return grid


def grid_signature(grid):
    return hash(tuple(tuple(row) for row in grid))


def calculate_solution(items):
    grid = []
    for item in items:
        grid.append([x for x in item])
        
    cycle = 0
    seen_previously = {}
    for cycle in range(1_000_000_000):
        # Run a cycle
        grid = roll_north(grid)
        # print()
        # for row in grid:
        #     print(''.join(row))

        grid = roll_west(grid)
        # print()
        # for row in grid:
        #     print(''.join(row))

        grid = roll_south(grid)
        # print()
        # for row in grid:
        #     print(''.join(row))

        grid = roll_east(grid)
        
        # print()
        # for row in grid:
        #     print(''.join(row))

        # if cycle == 2:
        #     x

        signature = grid_signature(grid)

        if signature in seen_previously:
            loop_start = seen_previously[signature]['idx']
            loop_size = cycle - loop_start
            break

        seen_previously[signature] = {'idx': cycle, 'grid': grid[:]}

    print(cycle, loop_start, loop_size)
    target = loop_start + (999999999 - loop_start) % loop_size
    print(target)

    # Calculate the load

    grid = None
    for k,v in seen_previously.items():
        if v['idx'] == target:
            grid = v['grid']

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
result = run_test(test_list, 64)

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

    # 91270 is wrong

    print(f'Solution is {answer}')
