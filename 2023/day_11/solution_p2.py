#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 11 of the Advent of Code for 2023.
"""
import sys


def print_galaxy(galaxy):
    for row in galaxy:
        print(''.join(row))


def find_empty_row(pre_expansion):
    empty_rows = {i for i, row in enumerate(pre_expansion) if all(c == "." for c in row)}
    empty_cols = {j for j, col in enumerate(zip(*pre_expansion)) if all(c == "." for c in col)}

    return empty_rows, empty_cols


def build_map(items, expand_amount):
    galaxies = {}
    galaxy_num = 1

    # Handle special case...
    expand_amount = 2 if expand_amount == 1 else expand_amount

    empty_rows, empty_cols = find_empty_row(items)

    real_row = 0
    for row_idx, row in enumerate(items):
        # Add an expansion amount if necessary
        if row_idx in empty_rows:
            real_row += expand_amount - 1
    
        real_col = 0
        for col_idx, point in enumerate(items[row_idx]):
            # Add an expansion amount if necessary
            if col_idx in empty_cols:
                real_col += expand_amount - 1

            if point == '#':
                galaxies[galaxy_num] = (real_row + row_idx, real_col + col_idx)
                galaxy_num += 1

    return galaxies


def calculate_solution(items, expand_amount):
    result = 0

    galaxies = build_map(items, expand_amount)

    distances = []
    num_galaxies = len(galaxies)
    for galaxy_id, _ in galaxies.items():
        start = galaxies[galaxy_id]
        for next_galaxy_id in range(galaxy_id+1, num_galaxies + 1):
            end = galaxies[next_galaxy_id]
            
            # Manhatten distance calculation.
            distance = abs(start[0] - end[0]) + abs(start[1] - end[1])
            
            # print(galaxy_id, next_galaxy_id, distance, start, end)
            
            distances.append(distance)

    result = sum(distances)

    return result


def run_test(test_input, expand_amount, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'), expand_amount)

    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

result = run_test(test_list, 1, 374)

result = run_test(test_list, 10, 1030)
print('Galaxy expansion check (10) ok')

result = run_test(test_list, 100, 8410)
print('Galaxy expansion check (100) ok')

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data, 1000000)

    print(f'Solution is {answer}')
