#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 12 of the Advent of Code for 2020.
"""
import sys
from collections import defaultdict


def move_wp(cur_x, cur_y, direction, distance):
    if direction == 'E':
        # East
        return cur_x + distance, cur_y
    elif direction == 'S':
        # South
        return cur_x, cur_y - distance
    elif direction == 'W':
        # West
        return cur_x - distance, cur_y
    elif direction == 'N':
        # North
        return cur_x, cur_y + distance
    else:
        print('Wat?', direction)
        boom


def move_ship(cur_x, cur_y, wp_x, wp_y, count):
    return (cur_x + (count * wp_x)), (cur_y + (count * wp_y))


# def turn_ship(cur_dir, turn_direction, degrees):
#     points = degrees / 90

#     if turn_direction == 'L':
#         return ((cur_dir - points) % 4)
#     elif turn_direction == 'R':
#         return ((cur_dir + points) % 4)


def turn_wp(cur_x, cur_y, turn_direction, degrees):
    if degrees == 180:
        return -cur_x, -cur_y

    if turn_direction == 'R':
        if degrees == 90:
            return  cur_y, -cur_x
        else:
            return  -cur_y, cur_x
    else:
        if degrees == 90:
            return -cur_y,  cur_x
        else:
            return cur_y, -cur_x


def calculate_solution(ship_movements):
    cur_ship_x = 0
    cur_ship_y = 0
    # cur_ship_dir = 0
    cur_wp_x = 10
    cur_wp_y = 1

    for movement in ship_movements:
        # print(movement)
        cmd = movement[0]
        count = int(movement[1:])

        if cmd == 'F':
            cur_ship_x, cur_ship_y = move_ship(cur_ship_x, cur_ship_y, cur_wp_x, cur_wp_y, count)
        elif cmd == 'L' or cmd == 'R':
            # We don't need to worry about turning the ship - it's always just moving
            # towards the waypoint.
            # cur_ship_dir = turn_ship(cur_ship_dir, cmd, count)
            cur_wp_x, cur_wp_y = turn_wp(cur_wp_x, cur_wp_y, cmd, count)
        else:
            cur_wp_x, cur_wp_y = move_wp(cur_wp_x, cur_wp_y, cmd, count)

        # print(cur_ship_x, cur_ship_y, ' wp ', cur_wp_x, cur_wp_y)

    return abs(cur_ship_x) + abs(cur_ship_y)


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
run_test(puzzle_input, 286)


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
