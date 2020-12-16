#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 16 of the Advent of Code for 2020.
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
                my_ticket = [int(x) for x in data[1].split(',')]
            else:
                tickets = [load_ticket(t) for t in data]
            
            data = []
            stage += 1
        else:
            data.append(line)

    tickets = [load_ticket(t) for t in data[1:]]

    # print(len(fields))
    # print(len(tickets))

    error_rate = 0

    valid_tickets = []

    for ticket in tickets:
        for fval in [int(x) for x in ticket.split(',')]:
            for field in fields:
                found = False
                if fval in fields[field]:
                    found = True
                    break

            if not found:
                break
        
        if found:
            valid_tickets.append(ticket)

    matching_fields = {}
    for ticket in valid_tickets:
        field_data = ticket.split(',')
        for idx, fval in zip(range(0, len(field_data)), field_data):
            for field in fields:
                if int(fval) in fields[field]:
                    if idx not in matching_fields:
                        matching_fields[idx] = defaultdict(int)

                    matching_fields[idx][field] += 1

    # print(matching_fields[0])
    # print(len(tickets))
    # print(len(valid_tickets))

    act_fields = {}
    for mf in matching_fields:
        act_fields[mf] = defaultdict(int)

        for x in matching_fields[mf]:
            if matching_fields[mf][x] >= len(valid_tickets):
                act_fields[mf][x] = len(valid_tickets)

    # print(act_fields)

    final_fields = {}
    field = -1
    name = ""
    while True:
        for mf in act_fields:
            if len(act_fields[mf]) == 1:
                field = mf
                name = act_fields[mf].keys()[0]
                break
        
        final_fields[field] = name

        del act_fields[mf]

        if len(act_fields) == 0:
            break

        for mf in act_fields:
            if name in act_fields[mf]:
                del act_fields[mf][name]

    # print(final_fields)

    result = 1
    for field in final_fields:
        if final_fields[field].startswith('departure'):
            result *= my_ticket[field]

    return result


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
    "class: 0-1 or 4-19",
    "row: 0-5 or 8-19",
    "seat: 0-13 or 16-19",
    "",
    "your ticket:",
    "11,12,13",
    "",
    "nearby tickets:",
    "3,9,18",
    "15,1,5",
    "5,14,9"
]
run_test(puzzle_input, 1)


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
