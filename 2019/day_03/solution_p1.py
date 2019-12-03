#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 3 of the Advent of Code for 2019.
"""

import math
import sys


def get_points(wire):
    """
    Given a set of wire instructions, return a set of all of the points making
    up the wire.

    Parameters
    ----------
    wire (str)
      The list of instructions for building the wire

    Returns
    -------
    A set of all of the points comprising the wire when the instructions are
    followed.
    """
    x = 0
    y = 0
    result = set()

    DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
    DY = {'L': -0, 'R': 0, 'U': -1, 'D': 1}

    for move in wire:
        direction = move[0]
        steps = int(move[1:])

        for _ in range(steps):
            x += DX[direction]
            y += DY[direction]

            result.add((x, y))

    return result


def calculate_distance(wire_1, wire_2):
    w1_points = get_points(wire_1)
    w2_points = get_points(wire_2)

    # Find the intersections of the wires
    intersections = w1_points & w2_points

    # Find the minimum intersection of the point and calculate the distance
    # from the centre position.
    minimum_distance = min([abs(x) + abs(y) for (x,y) in intersections])

    return minimum_distance


def run_test(test_number, test_input_1, test_input_2, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_distance(test_input_1, test_input_2)

    if result != expected_solution:
        print "Test for test {0} FAILED. Got a result of {1}, not {2}".format(test_number, result, expected_solution)
        sys.exit(-1)

    print "Test for mass {0} passed.".format(test_number)

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

run_test(1, ['R8','U5','L5','D3'], ['U7','R6','D4','L4'], 6)
run_test(2, ['R75','D30','R83','U83','L12','D49','R71','U7','L72'], ['U62','R66','U55','R34','D71','R55','D58','R83'], 159)
run_test(3, ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'], ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7'], 135)
print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    wires = []
    for line in f:
        wires.append([x for x in line.split(',')])

    distance = calculate_distance(wires[0], wires[1])

    print "Solution is {0}".format(distance)
