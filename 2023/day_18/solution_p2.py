#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 18 of the Advent of Code for 2023.
"""
import sys
from queue import Queue


def area(p):
    return int(0.5 * abs(sum(x0*y1 - x1*y0 for ((x0, y0), (x1, y1)) in segments(p))))


def segments(p):
    return zip(p, p[1:] + [p[0]])


def calculate_solution(items):
    instructions = [x.split() for x in items]

    points = []
    cur_pos = (0, 0)
    length = 0

    for instruction in instructions:
        direction, count, colour = instruction
        count = int(count)

        colour = colour[2:-1]
        count, direction = (colour[:-1], colour[-1])
        count = int(count, 16)

        if direction == '0':
            cur_pos = (cur_pos[0], cur_pos[1] + count)
        elif direction == '2':
            cur_pos = ( cur_pos[0], cur_pos[1] - count)
        elif direction == '3':
            cur_pos = (cur_pos[0] - count, cur_pos[1])
        elif direction == '1':
            cur_pos = (cur_pos[0] + count, cur_pos[1])

        length += count

        points.append(cur_pos)

    return int(area(points) + 1 + (length / 2))


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

test_list = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""
result = run_test(test_list, 952408144115)

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
