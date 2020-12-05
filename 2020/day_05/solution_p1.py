#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 5 of the Advent of Code for 2020.
"""
import sys


def identify_row(boarding_pass):
    min_row = 0
    max_row = 127
    for letter in boarding_pass[:-4]:
        # print(letter, min_row, max_row)
        if letter == 'F':
            max_row = min_row + ((max_row - min_row) // 2)
        else:
            min_row = min_row + ((max_row - min_row) // 2) + 1
        # print('----->', min_row, max_row)

    if boarding_pass[6] == 'F':
        return min_row

    return max_row


def identify_seat(boarding_pass):
    min_col = 0
    max_col = 7
    for letter in boarding_pass[-3:]:
        # print(letter, min_col, max_col)
        if letter == 'L':
            max_col = min_col + ((max_col - min_col) / 2)
        else:
            min_col = min_col + ((max_col - min_col) / 2)
        # print('----->', min_col, max_col)

    if boarding_pass[6] == 'L':
        return min_col

    return max_col


def calc_seat_id(row, col):
    return (row * 8) + col


def calculate_solution(boarding_passes):
    max = 0

    for boarding_pass in boarding_passes:
        seat_id = calc_seat_id(identify_row(boarding_pass), identify_seat(boarding_pass))
        if seat_id > max:
            max = seat_id

    return max


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

boarding_pass = "FBFBBFFRLR"
row = identify_row(boarding_pass)
assert row == 44
col = identify_seat(boarding_pass)
assert col == 5
assert calc_seat_id(row, col) == 357


boarding_pass = "BFFFBBFRRR"
row = identify_row(boarding_pass)
assert row == 70
col = identify_seat(boarding_pass)
assert col == 7
assert calc_seat_id(row, col) == 567


boarding_pass = "FFFBBBFRRR"
row = identify_row(boarding_pass)
assert row == 14
col = identify_seat(boarding_pass)
assert col == 7
assert calc_seat_id(row, col) == 119


boarding_pass = "BBFFBBFRLL"
row = identify_row(boarding_pass)
assert row == 102
col = identify_seat(boarding_pass)
assert col == 4
assert calc_seat_id(row, col) == 820


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
