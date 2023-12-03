#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 3 of the Advent of Code for 2023.
"""
from collections import defaultdict
import sys


def print_row(row):
    print(''.join(row))


def calculate_solution(items):
    result = 0

    grid = []

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    row = 0
    for row_data in items:
        build_row = []
        for col in row_data:
            thing = 'Y' if col == '*' else '.'
            build_row.append(thing)

        grid.append(build_row)
        # print_row(grid[row])
        row += 1

    ratios = defaultdict(list)
    row = 0
    for row_data in items:
        col_idx = 0
        part_number = ''
        col = row_data
        # print(col)

        min_pos = 0
        max_pos = 0

        while col_idx < len(col):
            if col[col_idx] in numbers:
                min_pos = min(min_pos, col_idx)
                max_pos = max(max_pos, col_idx)
                part_number += row_data[col_idx]
            else:
                if part_number != '':
                    # print(col_idx, part_number, min_pos, max_pos)
                    part_number = int(part_number)

                    for y in range(row - 1, row + 2):
                        for x in range(min_pos - 1, max_pos + 2):
                            if y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y]):
                                # print(y, x, grid[y][x])
                                if grid[y][x] == 'Y':
                                    ratios[(y, x)].append(part_number)

                    part_number = ''

                min_pos = col_idx + 1
                max_pos = col_idx + 1
            
            col_idx += 1

        if part_number != '':
            # print(col_idx, part_number, min_pos, max_pos)
            part_number = int(part_number)

            for y in range(row - 1, row + 2):
                for x in range(min_pos - 1, max_pos + 2):
                    if y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y]):
                        # print(y, x, grid[y][x])
                        if grid[y][x] == 'Y':
                            ratios[(y, x)].append(part_number)

        row += 1

    # print(ratios)
    for k, v in ratios.items():
        # print (k, v)
        if len(v) > 1:
            result += v[0] * v[1]

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

test_list = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

result = run_test(test_list, 467835)

test_list = """467..114.
...*.....
..35..633
......#..
617*.....
.....+.58
..592....
......755
...$.*...
.664.598."""

result = run_test(test_list, 467835)

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
