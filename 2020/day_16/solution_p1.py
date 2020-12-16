#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 16 of the Advent of Code for 2020.
"""
import re
import sys
from collections import defaultdict


def load_fields(data):
    fields = {}

    for field in data:
        fname, settings = field.split(':')

        field_values = {}
        for value in settings.strip().split(' '):
            if value == "or":
                continue
            else:
                start, end = value.split('-')
                for v in range(int(start), int(end) + 1):
                    field_values[v] = True

        fields[fname] = field_values

    return fields


def load_ticket(data):
    return data


def calculate_solution(ticket_data):
    stage = 0
    data = []

    fields = defaultdict(str)
    my_ticket = None
    tickets = []

    for line in ticket_data:
        if line == "":
            if stage == 0:
                fields = load_fields(data)
            elif stage == 1:
                my_ticket = load_ticket(data[1])
            else:
                tickets = [load_ticket(t) for t in data]
            
            data = []
            stage += 1
        else:
            data.append(line)

    tickets = [load_ticket(t) for t in data[1:]]

    error_rate = 0

    for ticket in tickets:
        for fval in ticket.split(','):
            found = False
            for field in fields:
                if int(fval) in fields[field]:
                    found = True
        
            if not found:
                error_rate += int(fval)

    return error_rate


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
    "class: 1-3 or 5-7",
    "row: 6-11 or 33-44",
    "seat: 13-40 or 45-50",
    "",
    "your ticket:",
    "7,1,14",
    "",
    "nearby tickets:",
    "7,3,47",
    "40,4,50",
    "55,2,20",
    "38,6,12"
]
run_test(puzzle_input, 71)


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
