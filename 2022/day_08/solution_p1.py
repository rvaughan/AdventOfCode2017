#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 8 of the Advent of Code for 2022.
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

    # We don't have to work out whether the outer trees are visible.
    result = ((height + width) * 2) - 4

    for row_idx in range(1, height - 1):
        for col_idx in range(1, width - 1):

            tree = grid[row_idx][col_idx]

            # Check north
            tall_enough = False
            max_height = 0
            for check_idx in range(row_idx - 1, -1, -1):
                # print(row_idx, check_idx, col_idx, tree, grid[check_idx][col_idx])
                if grid[check_idx][col_idx] > max_height:
                    max_height = grid[check_idx][col_idx]
            
            if tree > max_height:
                tall_enough = True
                print(f"Tall enough: {row_idx}, {col_idx}")
                result += 1

            if not tall_enough:
                # Check south
                tall_enough = True
                for check_idx in range(row_idx + 1, len(items[row_idx])):
                    if grid[check_idx][col_idx] >= tree:
                        tall_enough = False
                        break
                # if tall_enough:
                #     print(f"Tall enough: {row_idx}, {col_idx}")
                result += 1 if tall_enough else 0

            if not tall_enough:
                # Check east
                tall_enough = True
                for check_idx in range(col_idx - 1, -1, -1):
                    if grid[row_idx][check_idx] >= tree:
                        tall_enough = False
                        break
                # if tall_enough:
                #     print(f"Tall enough: {row_idx}, {col_idx}")
                result += 1 if tall_enough else 0

            if not tall_enough:
                # Check west
                tall_enough = True
                for check_idx in range(col_idx + 1, width):
                    if grid[row_idx][check_idx] >= tree:
                        tall_enough = False
                        break
                # if tall_enough:
                #     print(f"Tall enough: {row_idx}, {col_idx}")
                result += 1 if tall_enough else 0

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

result = run_test(test_list, 21)

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
