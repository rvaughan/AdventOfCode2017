#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 17 of the Advent of Code for 2023.
"""
import copy
import sys
import heapq


UP = 1
LEFT = 2
DOWN = 3
RIGHT = 4


def calculate_solution(items):
    grid = []

    for row in items:
        grid.append([int(x) for x in row])

    num_cols = len(grid)
    num_rows = len(grid[0])

    queue = [(0, 0, 0, -1, 0)]
    D = {}
    while queue:
        heat_loss, row, col, dir_, indir = heapq.heappop(queue)

        # Have we already been through this path, from the direction being travelled?
        if (row, col, dir_, indir) in D:
            continue

        # Store the heat_loss to the current point
        D[(row, col, dir_, indir)] = heat_loss
        
        for i, (dr, dc) in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
            new_row = row + dr
            new_col = col + dc
            new_dir = i
            new_indir = (1 if new_dir != dir_ else indir + 1)
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and new_indir <= 3 and ((new_dir+2)%4 != dir_):
                # Get the heat loss at this cell
                loss = int(grid[new_row][new_col])
                heapq.heappush(queue, (heat_loss + loss, new_row, new_col, new_dir, new_indir))

    ans = 1e9
    for (row, col, dir_, indir), v in D.items():
        if row == num_rows-1 and col == num_cols-1:
            ans = min(ans, v)

    return ans    


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

test_list = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""
result = run_test(test_list, 102)

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
