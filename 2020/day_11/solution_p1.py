#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 11 of the Advent of Code for 2020.
"""
import sys
from collections import defaultdict


def check_seat(seat_map, row, col):
    adjacent_occupied = 0

    # Check the row above

    chk_row = row - 1
    chk_col = col - 1

    if chk_row >= 0 and chk_row < len(seat_map):
        if chk_col >= 0 and chk_col <= len(seat_map[0]):
            if seat_map[chk_row][chk_col] == '#':
                adjacent_occupied += 1

        chk_col = col
        if seat_map[chk_row][chk_col] == '#':
            adjacent_occupied += 1


        chk_col = col + 1
        if chk_col < len(seat_map[0]):
            if seat_map[chk_row][chk_col] == '#':
                adjacent_occupied += 1

    # Check the current row

    chk_row = row 
    chk_col = col - 1

    if chk_col >= 0:
        if seat_map[chk_row][chk_col] == '#':
            adjacent_occupied += 1

    chk_col = col + 1
    if chk_col < len(seat_map[0]):
        if seat_map[chk_row][chk_col] == '#':
            adjacent_occupied += 1

    # Check the row below

    chk_row = row + 1
    chk_col = col - 1

    if chk_row >= 0 and chk_row < len(seat_map):
        if chk_col >= 0 and chk_col <= len(seat_map[0]):
            if seat_map[chk_row][chk_col] == '#':
                adjacent_occupied += 1

        chk_col = col
        if seat_map[chk_row][chk_col] == '#':
            adjacent_occupied += 1

        chk_col = col + 1
        if chk_col < len(seat_map[0]):
            if seat_map[chk_row][chk_col] == '#':
                adjacent_occupied += 1

    return adjacent_occupied


def calculate_solution(seat_map):
    num_seats = 0
    iteration = 0

    new_seat_map = []
    for row in seat_map:
        new_seat_map.append(list(row))

    tmp_seat_map = [x[:] for x in new_seat_map]

    while True:
        num_seats = 0
        changes_made = False

        for row in range(0, len(new_seat_map)):
            for col in range(0, len(new_seat_map[0])):
                if new_seat_map[row][col] == '#':
                    num_seats += 1
                    occupied = check_seat(new_seat_map, row, col)
                    if occupied >= 4:
                        changes_made = True
                        tmp_seat_map[row][col] = 'L'
                elif seat_map[row][col] == 'L':
                    occupied = check_seat(new_seat_map, row, col)
                    if occupied == 0:
                        changes_made = True
                        tmp_seat_map[row][col] = '#'

        if not changes_made:
            break

        # iteration += 1
        # print(iteration, num_seats)
        # for row in tmp_seat_map:
        #     print("".join(row))

        new_seat_map = [x[:] for x in tmp_seat_map]

        # if iteration == 3:
        #     break
    
    return num_seats


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


puzzle_input = [
    "L.LL.LL.LL",
    "LLLLLLL.LL",
    "L.L.L..L..",
    "LLLL.LL.LL",
    "L.LL.LL.LL",
    "L.LLLLL.LL",
    "..L.L.....",
    "LLLLLLLLLL",
    "L.LLLLLL.L",
    "L.LLLLL.LL"
]
run_test(puzzle_input, 37)


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
