#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 13 of the Advent of Code for 2020.
"""
import sys
from collections import defaultdict


def calc_bus_earliest_time(ref_time, bus_id):
    result = ((ref_time / bus_id)) * bus_id
    if result < ref_time:
        result += bus_id

    return result


def calculate_solution(timetable):
    ref_time = int(timetable[0])

    min = 99999999999
    bus_id = 0
    buses = timetable[1].split(',')
    for bus in buses:
        if bus != 'x':
            ealiest = calc_bus_earliest_time(ref_time, int(bus))
            if ealiest < min:
                min = ealiest
                bus_id = int(bus)

    return bus_id * (min - ref_time)


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


assert calc_bus_earliest_time(939, 59) == 944
assert calc_bus_earliest_time(939, 7) == 945
assert calc_bus_earliest_time(939, 13) == 949


puzzle_input = [
    "939",
    "7,13,x,x,59,x,31,19"
]
run_test(puzzle_input, 295)


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
