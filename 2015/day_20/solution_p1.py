#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 20 of the Advent of Code for 2015.
"""


def find_elves(target_number):
    # Actually this code helps us find all of the 'factors' that can be used
    # for this target_number.
    elves = set()
    for factor in xrange(1, int(target_number ** 0.5) + 1):
        if target_number % factor == 0:
            elves.add(int(factor))
            elves.add(int(target_number / factor))

    return elves


def calc_presents(num_houses=10, num_presents=10, expected_value=0):
    elves = find_elves(num_houses)

    total = sum(elves) * num_presents

    return total

# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

houses = {}
for house_num in xrange(10):
    houses[house_num] = calc_presents(house_num, 10, 0)

assert houses[1] == 10, houses[1]
assert houses[2] == 30, houses[2]
assert houses[3] == 40, houses[3]
assert houses[4] == 70, houses[4]
assert houses[5] == 60, houses[5]
assert houses[6] == 120, houses[6]
assert houses[7] == 80, houses[7]
assert houses[8] == 150, houses[8]
assert houses[9] == 130, houses[9]


# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual data now.

with open("input.txt", "r") as f:
    input_data = int(f.read())

    solution = 0

    houses = {}
    for house_num in xrange(1000000):
        houses[house_num] = calc_presents(house_num, 10, 0)

        if houses[house_num] >= input_data:
            solution = house_num
            break

    print("Solution: {}".format(solution))
