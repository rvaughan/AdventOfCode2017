#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 11 of the Advent of Code for 2023.
"""
import sys


def print_galaxy(galaxy):
    for row in galaxy:
        print(''.join(row))


def apply_expansion(pre_expansion):
    expanded = []
    mid_expanded = []

    empty_cols = [True] * len(pre_expansion[0])

    # Deal with empty rows first
    for row in pre_expansion:
        mid_expanded.append(row)

        if '#' not in row:
            mid_expanded.append(row)
        else:
            pos = row.find('#')
            while pos != -1:
                empty_cols[pos] = False
                pos = row.find('#', pos+1)

    for row in mid_expanded:
        row_data = []
        for col in range(len(row)):
            if empty_cols[col]:
                row_data.append('.')
            row_data.append(row[col])

        expanded.append(row_data)

    return expanded


def build_map(items):
    galaxy_map = []
    galaxies = {}
    galaxy_num = 1

    post_expansion = apply_expansion(items[:])

    for row in range(len(post_expansion)):
        galaxy_row = []
        for col in range(len(post_expansion[row])):
            point = post_expansion[row][col]
            if point == '#':
                galaxies[galaxy_num] = (row, col)
                galaxy_num += 1
            
            galaxy_row.append(point)

        galaxy_map.append(galaxy_row)

    return galaxy_map, galaxies


def calculate_solution(items):
    result = 0

    galaxy_map, galaxies = build_map(items)

    distances = []
    num_galaxies = len(galaxies)
    for galaxy_id, v in galaxies.items():
        start = galaxies[galaxy_id]
        for next_galaxy_id in range(galaxy_id+1, num_galaxies + 1):
            end = galaxies[next_galaxy_id]
            distance = abs(start[0] - end[0]) + abs(start[1] - end[1])
            # print(galaxy_id, next_galaxy_id, distance, start, end)
            distances.append(distance)

    result = sum(distances)

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

new_galaxy, galaxy_list = build_map(test_list.split('\n'))
assert len(new_galaxy) == 12, f"Expected 12 rows, got {len(new_galaxy)}"
assert len(new_galaxy[0]) == 13, f"Expected 13 cols, got {len(new_galaxy[0])}"
assert len(galaxy_list) == 9, f"Expected 9 galaxies, got {len(galaxy_list)}"
print('Galaxy expansion check ok')

result = run_test(test_list, 374)

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
