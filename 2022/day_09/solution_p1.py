#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 9 of the Advent of Code for 2022.
"""

import sys


def dump_grid(start, tail, head):
    height = 5
    width = 6

    grid = []
    for _ in range(height):
        grid += [['.'] * width]

    grid[start[0]][start[1]] = 's'
    grid[tail[0]][tail[1]] = 'T'
    grid[head[0]][head[1]] = 'H'

    for row_idx in range(height):
        print(f'{"".join([x for x in grid[row_idx]])}')
    print('------------------------------')


def calculate_solution(moves):
    tail_positions = set()

    start = (4, 0)
    head = (4, 0)
    tail = (4, 0)

    tail_positions.add(tail)

    # dump_grid(start, tail, head)

    for move in moves:
        # print(move)

        direction, cells = move.split(' ')

        for _ in range(int(cells)):
            if direction == 'L':
                head = (head[0], head[1] - 1)
                if (head[1] - tail[1] == -2):
                    tail = (tail[0], tail[1] - 1)
                    if head[0] != tail[0]:
                        tail = (head[0], tail[1])
                    tail_positions.add(tail)
            elif direction == 'R':
                head = (head[0], head[1] + 1)
                if (head[1] - tail[1] == 2):
                    tail = (tail[0], tail[1] + 1)
                    if head[0] != tail[0]:
                        tail = (head[0], tail[1])
                    tail_positions.add(tail)
            elif direction == 'U':
                head = (head[0] - 1, head[1])
                if (head[0] - tail[0] == -2):
                    tail = (tail[0] - 1, tail[1])
                    if head[1] != tail[1]:
                        tail = (tail[0], head[1])
                    tail_positions.add(tail)
            elif direction == 'D':
                head = (head[0] + 1, head[1])
                if (head[0] - tail[0] == 2):
                    tail = (tail[0] + 1, tail[1])
                    if head[1] != tail[1]:
                        tail = (tail[0], head[1])
                    tail_positions.add(tail)

        # print(head, tail)
        # dump_grid(start, tail, head)

    return len(tail_positions)


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

result = run_test(test_list, 13)

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
