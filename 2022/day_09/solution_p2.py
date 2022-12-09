#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 9 of the Advent of Code for 2022.
"""

import sys


def dump_grid(start, knots):
    height = 20
    width = 20

    grid = []
    for _ in range(height):
        grid += [['.'] * width]

    grid[start[0]][start[1]] = 's'
    for idx in range(len(knots) - 1, -1, -1):
        grid[knots[idx][0]][knots[idx][1]] = str(idx) if idx > 0 else 'H'

    for row_idx in range(height):
        print(f'{"".join([x for x in grid[row_idx]])}')
    print('------------------------------')


def follow(first, second):
    delta_x = first[1] - second[1]
    delta_y = first[0] - second[0]

    if (abs(delta_x) > 1 and delta_y == 0) or (abs(delta_y) > 1 and delta_x == 0):
        # Moving in a straight line left/right, or up/down
        return (second[0] + delta_y//2, second[1] + delta_x//2)
    elif abs(delta_x) > 1 or abs(delta_y) > 1:
        # The first knot is in a diagonal position from the second knot.

        # Get all of the cells around the first knot
        around_first = set([(first[0] + ny, first[1] + nx)
                          for nx in (0, 1, -1) for ny in (0, 1, -1) if not nx == ny == 0])

        # Get all of the cells around the second knot
        around_second = set([(second[0] + ny, second[1] + nx)
                          for nx in (1, -1) for ny in (1, -1)])

        # Return the cell that intersects
        return around_first.intersection(around_second).pop()
    
    # No move required
    return second


def calculate_solution(moves):
    num_knots = 10

    # The delta positions to be applied for the various moves that can be made.
    move_deltas = {
        'R': (0, 1),
        'L': (0, -1),
        'U': (-1, 0),
        'D': (1, 0)
    }

    # We will start in the middle of the grid
    start = (10, 10)
    positions = []
    knots = []

    for knot in range(num_knots):
        knots.append(start)
        positions.append(set())
        positions[knot].add(start)

    # dump_grid(start, knots)

    for move in moves:
        direction, cells = move.split(' ')

        for _ in range(int(cells)):
            change = move_deltas[direction]

            # Move the head of the rope
            knots[0] = (knots[0][0] + change[0], knots[0][1] + change[1])

            # Let the rest of the knots on the rope follow along.
            for idx in range(1, num_knots):
                knots[idx] = follow(knots[idx-1], knots[idx])
                positions[idx].add(knots[idx])

            # print(knots)
            # dump_grid(start, knots)

    return len(positions[num_knots-1])


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

test_list = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

result = run_test(test_list, 1)

test_list = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

result = run_test(test_list, 36)

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
