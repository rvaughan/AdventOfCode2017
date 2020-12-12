#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 12 of the Advent of Code for 2020.
"""
import sys
from collections import defaultdict


def move(cur_x, cur_y, direction, distance):
    if direction == 'E':
        # East
        return cur_x + distance, cur_y
    elif direction == 'S':
        # South
        return cur_x, cur_y + distance
    elif direction == 'W':
        # West
        return cur_x - distance, cur_y
    elif direction == 'N':
        # North
        return cur_x, cur_y - distance
    else:
        print('Wat?', direction)
        boom


def move_forward(cur_x, cur_y, cur_dir, distance):
    if cur_dir == 0:
        # East
        return cur_x + distance, cur_y
    elif cur_dir == 1:
        # South
        return cur_x, cur_y + distance
    elif cur_dir == 2:
        # West
        return cur_x - distance, cur_y
    elif cur_dir == 3:
        # North
        return cur_x, cur_y - distance
    else:
        print('Wat?', cur_dir)
        boom


def turn(cur_dir, turn_direction, degrees):
    points = degrees / 90

    if turn_direction == 'L':
        return ((cur_dir - points) % 4)
    elif turn_direction == 'R':
        return ((cur_dir + points) % 4)


def calculate_solution(ship_movements):
    cur_x = 0
    cur_y = 0
    cur_dir = 0

    for movement in ship_movements:
        cmd = movement[0]
        count = int(movement[1:])

        if cmd == 'F':
            cur_x, cur_y = move_forward(cur_x, cur_y, cur_dir, count)
        elif cmd == 'L' or cmd == 'R':
            cur_dir = turn(cur_dir, cmd, count)
        else:
            cur_x, cur_y = move(cur_x, cur_y, cmd, count)

    return abs(cur_x) + abs(cur_y)


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input)

    if result != expected_solution:
        print("Test for input {0} FAILED. Got a result of {1}, not {2}".format(test_input, result, expected_solution))
        sys.exit(-1)

    print("Test for input {0} passed.".format(test_input))

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.


puzzle_input = [
    "F10",
    "N3",
    "F7",
    "R90",
    "F11"
]
run_test(puzzle_input, 25)


print("")
print("-----------------")
print("All Tests PASSED.")
print("-----------------")
print("")

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data)

    print("Solution is {0}".format(answer))
