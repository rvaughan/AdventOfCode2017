#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 13 of the Advent of Code for 2020.
"""
import sys
from collections import defaultdict


def calculate_solution(timetable):
    buses = timetable[1].split(',')
    time_index = -1
    schedule = []
    for bus in buses:
        time_index += 1

        if bus == 'x':
            continue
        bus = int(bus)
        schedule.append((bus, time_index))
    
    print('Bus schedule', schedule)

    bus_idx = 0
    bus, time = schedule[bus_idx]
    # The time is irrelevant, but we might as well use it as a
    # starting point and save some computation cycles.
    time_index = time
    interval = bus
    first_hit = -1
    # Step through each bus looking for an intersection.
    while bus_idx < len(schedule):

        # Find the first point after the time period where the bus
        # timetable intersects. Here we are using Chinese remainder
        # theory to find the intervals between the buses.
        my_l = (time_index + time) % bus
        if my_l == 0:
            if first_hit == -1:
                print('First Hit for bus {} at time {} - Interval {}'.format(bus, time_index, interval))
                first_hit = time_index
            else:
                bus_idx += 1
                interval = time_index - first_hit
                print('Second Hit for bus {} at time {} - new Interval {}'.format(bus, time_index, interval))
                
                time_index = first_hit - interval
                first_hit = -1
                if bus_idx < len(schedule):
                    bus, time = schedule[bus_idx]

        time_index += interval

    return time_index


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
    "939",
    "7,13,x,x,59,x,31,19"
]
run_test(puzzle_input, 1068781)


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
