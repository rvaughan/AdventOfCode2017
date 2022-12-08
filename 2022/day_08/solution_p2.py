#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 8 of the Advent of Code for 2022.
"""

import sys


def calculate_solution(items):
    result = 0

    height = len(items)
    width = len(items[0])

    grid = []
    for _ in range(height):
        grid += [[0] * width]

    for row_idx in range(0, height):
        for col_idx, tree in zip(range(0, width), items[row_idx]):
            grid[row_idx][col_idx] = int(tree)

    for row_idx in range(1, height - 1):
        for col_idx in range(1, width - 1):

            scenic_scores = []
            tree = grid[row_idx][col_idx]

            # Check up
            trees = 0
            for check_idx in range(row_idx - 1, -1, -1):
                trees += 1
                if grid[check_idx][col_idx] >= tree:
                    break
            scenic_scores.append(trees)

            # Check left
            trees = 0
            for check_idx in range(col_idx - 1, -1, -1):
                trees += 1
                if grid[row_idx][check_idx] >= tree:
                    break
            scenic_scores.append(trees)

            # Check right
            trees = 0
            for check_idx in range(col_idx + 1, width):
                trees += 1
                if grid[row_idx][check_idx] >= tree:
                    break
            scenic_scores.append(trees)

            # Check down
            trees = 0
            for check_idx in range(row_idx + 1, len(items[row_idx])):
                trees += 1
                if grid[check_idx][col_idx] >= tree:
                    break
            scenic_scores.append(trees)

            scenic_score = scenic_scores[0]
            scenic_score *= scenic_scores[1]
            scenic_score *= scenic_scores[2]
            scenic_score *= scenic_scores[3]

            result = max(scenic_score, result)

    return result


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

test_list = """30373
25512
65332
33549
35390"""

result = run_test(test_list, 8)

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
