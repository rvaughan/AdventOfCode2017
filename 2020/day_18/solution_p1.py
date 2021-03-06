#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 18 of the Advent of Code for 2020.
"""
import re
import sys
from collections import defaultdict


def plus(num1, num2):
    return num1 + num2


def multiply(num1, num2):
    return num1 * num2


def calculate(formula):
    result = 0
    idx = 0
    op = None
    numbers = []

    num = ""

    while idx < len(formula):
        c = formula[idx]
        if c == "(":
            val, count = calculate(formula[idx+1:])
            numbers.append(val)
            idx += count
            num = ''
        elif c == ")":
            if len(num) > 0:
                numbers.append(int(num))
                num = ''

            if len(numbers) == 2:
                numbers[0] = op(numbers[0], numbers[1])
                del numbers[1]

            return numbers[0], idx + 1
        elif c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            num += c
        elif c == '+':
            op = plus
        elif c == '*':
            op = multiply
        else:
            if len(num) > 0:
                numbers.append(int(num))
                num = ''

        if len(numbers) == 2:
            numbers[0] = op(numbers[0], numbers[1])
            del numbers[1]

        idx += 1

    if len(num) > 0:
        numbers.append(int(num))
        num = ''

    if len(numbers) == 2:
        numbers[0] = op(numbers[0], numbers[1])
        del numbers[1] 

    return numbers[0], idx + 1


def calculate_solution(formulae):
    result = 0

    for formula in formulae:
        val, _ = calculate(formula)
        result += val

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
    "1 + 2 * 3 + 4 * 5 + 6"
]
run_test(puzzle_input, 71)


puzzle_input = [
    "1 + (2 * 3) + (4 * (5 + 6))"
]
run_test(puzzle_input, 51)


puzzle_input = [
    "2 * 3 + (4 * 5)"
]
run_test(puzzle_input, 26)


puzzle_input = [
    "5 + (8 * 3 + 9 + 3 * 4 * 3)"
]
run_test(puzzle_input, 437)


puzzle_input = [
    "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
]
run_test(puzzle_input, 12240)


puzzle_input = [
    "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
]
run_test(puzzle_input, 13632)


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
