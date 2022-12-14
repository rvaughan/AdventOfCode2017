#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 1 of the Advent of Code for 2021.
"""

import sys


def build_grid(lines, rows=1000, cols=1000):
    grid = []
    for _ in range(rows):
        grid.append(['.'] * cols)

    max_depth = 0
    for item in lines:
        rock_positions = item.split(' -> ')
        for idx in range(len(rock_positions) - 1):
            rock_start = [int(x) for x in rock_positions[idx].split(',')]
            rock_end = [int(x) for x in rock_positions[idx+1].split(',')]

            row_direction = 1
            if rock_start[0] > rock_end[0]:
                rock_end[0] -= 1
                row_direction = -1
            elif rock_start[0] == rock_end[0]:
                rock_end[0] += 1

            col_direction = 1
            if rock_start[1] > rock_end[1]:
                col_direction = -1
            elif rock_start[1] == rock_end[1]:
                rock_end[1] += 1

            for row in range(rock_start[1], rock_end[1], col_direction):
                for col in range(rock_start[0], rock_end[0], row_direction):
                    grid[row][col] = '#'
                    max_depth = max(max_depth, row)

    return grid, max_depth


def dump_grid(grid, start_row=0, end_row=1000, start_col=0, end_col=1000):
    for row in range(start_row, end_row):
        line = []
        for col in range(start_col, end_col):
            line.append(grid[row][col])

        print(''.join(line))


def calculate_solution(items):
    grid, max_depth = build_grid(items)

    start_pos = [0, 500]

    # dump_grid(grid, 0, 11, 490, 510)
    # x

    sand_grains = 0
    while True:
        sg_pos = start_pos.copy()
        moved = True
        stopped = False
        while moved and not stopped:
            # print(sg_pos)

            if sg_pos[0] > max_depth:
                print(f'Sand grain {sand_grains+1} went off the board')
                moved = False
                break

            if grid[sg_pos[0]][sg_pos[1]] != '.':
                if grid[sg_pos[0]][sg_pos[1]-1] != '.':
                    if grid[sg_pos[0]][sg_pos[1]+1] != '.':
                        # Stopped - so back up one cell
                        sg_pos[0] -= 1
                        sand_grains += 1
                        stopped = True
                        print(f'Sand grain {sand_grains} stopped')
                    else:
                        # Move right
                        sg_pos[1] += 1
                else:
                    # Move left
                    sg_pos[1] -= 1

            if not stopped:
                grid[sg_pos[0]][sg_pos[1]] = '+'
                # print('')
                # dump_grid(grid, 0, 11, 490, 510)
                grid[sg_pos[0]][sg_pos[1]] = '.'

                # Move down one cell
                sg_pos[0] += 1
            else:
                grid[sg_pos[0]][sg_pos[1]] = 'o'
                # if sand_grains == 24:
                #     print('')
                #     dump_grid(grid, 0, 11, 490, 510)
                #     x

        if moved == False:
            break

    return sand_grains


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'))

    if result != expected_solution:
        print(
            f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

result = run_test(test_list, 24)

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
