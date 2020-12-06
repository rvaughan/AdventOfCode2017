#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 6 of the Advent of Code for 2020.
"""
import sys
from collections import defaultdict


def calc_questions(questions, num_passengers):
    answers = defaultdict(int)
    for answer in questions:
        answers[answer] += 1

    count = 0
    for answer in answers:
        if answers[answer] == num_passengers:
            count += 1

    return count


def calculate_solution(q_list):
    count = 0
    passengers = 0
    answers = ""

    for questions in q_list:
        if questions != "":
            passengers += 1
            answers += questions
        else:
            count += calc_questions(answers, passengers)
            answers = ""
            passengers = 0

    if answers != "":
        count += calc_questions(answers, passengers)

    return count


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

questions = [
    "abc",
    "",
    "a",
    "b",
    "c",
    "",
    "ab",
    "ac",
    "",
    "a",
    "a",
    "a",
    "a",
    "",
    "b"
]
run_test(questions, 6)

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
