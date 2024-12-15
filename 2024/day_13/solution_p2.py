#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 13 of the Advent of Code for 2024.
"""
import re
import sys


def solve_puzzle(puzzle):
    x1, y1 = re.findall(r'Button A: X\+(\d+), Y\+(\d+)', puzzle[0])[0]
    x1 = int(x1)
    y1 = int(y1)

    x2, y2 = re.findall(r'Button B: X\+(\d+), Y\+(\d+)', puzzle[1])[0]
    x2 = int(x2)
    y2 = int(y2)

    tx, ty = re.findall(r'Prize: X=(\d+), Y=(\d+)', puzzle[2])[0]
    tx = int(tx) + 10000000000000
    ty = int(ty) + 10000000000000

    a = (tx*y2 - ty*x2) / (x1*y2 - y1*x2)
    b = (ty*x1 - tx*y1) / (x1*y2 - y1*x2)
    
    if a == int(a) and b == int(b):
        return int(3 * a + b)

    return 0


def calculate_solution(items):
    result = 0

    puzzle = []
    for line in items:
        if line != '':
            puzzle.append(line)
        else:
            result += solve_puzzle(puzzle)
            puzzle = []

    if puzzle != []:
        result += solve_puzzle(puzzle)

    return result


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'))

    print()
    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data)

    print(f'Solution is {answer}')
