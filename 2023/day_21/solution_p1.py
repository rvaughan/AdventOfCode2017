#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 21 of the Advent of Code for 2023.
"""
import sys


def calculate_solution(items, max_steps):
    grid = []
    start_pos = None
    for y, row in enumerate(items):
        row_data = []
        for x, cell in enumerate(row):
            row_data.append(cell)
            if cell == 'S':
                start_pos = (x, y)

        grid.append(row_data)

    # print()
    # for row in grid:
    #     print(''.join(row))
    # print()
    
    positions = [start_pos]
    steps = set()
    step = 1
    while step <= max_steps:
        step += 1
        new_positions = []
        while any(positions):
            pos = positions.pop(0)
            x, y = pos
            if 0 <= x < len(grid[0]) and 0 <= y < len(grid):            
                if x > 0 and grid[y][x - 1] == '.':
                    new_positions.append((x - 1, y))
                if x < len(grid[y]) - 1 and grid[y][x + 1] == '.':
                    new_positions.append((x + 1, y))
                if y > 0 and grid[y - 1][x] == '.':
                    new_positions.append((x, y - 1))
                if y < len(grid) - 1 and grid[y + 1][x] == '.':
                    new_positions.append((x, y + 1))
            
        positions = new_positions
            
        steps |= set(new_positions)

    print()
    for step in positions:
        grid[step[1]][step[0]] = 'O'
    for row in grid:
        print(''.join(row))
    print()

    return len(positions)


def run_test(test_input, max_steps, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'), max_steps)

    print()
    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""
result = run_test(test_list, 6, 16)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data, 64)

    print(f'Solution is {answer}')
