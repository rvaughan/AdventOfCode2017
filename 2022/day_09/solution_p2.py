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


def calculate_solution(moves):
    num_knots = 10

    start= (10, 10)
    positions= []
    knots= []

    for knot in range(num_knots):
        knots.append(start)
        positions.append(set())
        positions[knot].add(start)

    # dump_grid(start, knots)

    for move in moves:
        direction, cells= move.split(' ')

        for _ in range(int(cells)):
            if direction == 'L':
                knots[0] = (knots[0][0], knots[0][1] - 1)
                for idx in range(1, num_knots):
                    if (knots[idx-1][1] - knots[idx][1] == -2):
                        knots[idx] = (knots[idx][0], knots[idx][1] - 1)
                        if knots[idx-1][0] != knots[idx][0]:
                            knots[idx] = (knots[idx-1][0], knots[idx][1])
                        positions[idx].add(knots[idx])
            elif direction == 'R':
                knots[0] = (knots[0][0], knots[0][1] + 1)
                for idx in range(1, num_knots):
                    if (knots[idx-1][1] - knots[idx][1] == 2):
                        knots[idx] = (knots[idx][0], knots[idx][1] + 1)
                        if knots[idx-1][0] != knots[idx][0]:
                            knots[idx] = (knots[idx-1][0], knots[idx][1])
                        positions[idx].add(knots[idx])
            elif direction == 'U':
                knots[0] = (knots[0][0] - 1, knots[0][1])
                for idx in range(1, num_knots):
                    if ((knots[idx-1][0] - knots[idx][0] == -2) or (knots[idx-1][1] - knots[idx][1] == -2)):
                        knots[idx] = (knots[idx][0] - 1, knots[idx][1])
                        if knots[idx-1][1] != knots[idx][1]:
                            knots[idx] = (knots[idx][0], knots[idx-1][1])
                        positions[idx].add(knots[idx])
            elif direction == 'D':
                knots[0] = (knots[0][0] + 1, knots[0][1])
                for idx in range(1, num_knots):
                    if (knots[idx-1][0] - knots[idx][0] == 2):
                        knots[idx] = (knots[idx][0] + 1, knots[idx][1])
                        if knots[idx-1][1] != knots[idx][1]:
                            knots[idx] = (knots[idx][0], knots[idx-1][1])
                        positions[idx].add(knots[idx])

            print(knots)
            dump_grid(start, knots)

    return len(positions[num_knots-1])


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result= calculate_solution(test_input.split('\n'))

    if result != expected_solution:
        print(
            f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """R 4
U 4"""
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2"""

result = run_test(test_list, 0)

# test_list = """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20"""

# result = run_test(test_list, 36)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data= [line.strip() for line in f]
    answer= calculate_solution(input_data)

    print(f'Solution is {answer}')
