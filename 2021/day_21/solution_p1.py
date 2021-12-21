#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 17 of the Advent of Code for 2021.
"""

import sys
from collections import defaultdict, deque


roll = 0

def roll_die():
    global roll

    roll += 1
    while roll > 100:
        roll -= 100

    return roll


def move(start_pos):
    new_pos = start_pos + roll_die()
    while new_pos > 10:
        new_pos -= 10

    return new_pos


def calculate_solution(input_data):
    p1_score = 0
    p2_score = 0
    die_rolls = 0

    p1_pos = int(input_data[0].split()[-1])
    p2_pos = int(input_data[1].split()[-1])

    while True:
        p1_pos = move(p1_pos)
        p1_pos = move(p1_pos)
        p1_pos = move(p1_pos)
        p1_score += p1_pos
        die_rolls += 3
        # print('p1', p1_pos, p1_score, die_rolls)
        if p1_score >= 1000:
            break

        p2_pos = move(p2_pos)
        p2_pos = move(p2_pos)
        p2_pos = move(p2_pos)
        p2_score += p2_pos
        die_rolls += 3
        # print('p2', p2_pos, p2_score, die_rolls)
        if p2_score >= 1000:
            break

    print(p1_score, die_rolls)
    print(p2_score, die_rolls)

    if p1_score < p2_score:
        return p1_score * die_rolls

    return p2_score * die_rolls


def run_test(test_input, expected_value):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    input_vals = [line.strip() for line in test_input.split('\n')]
    result = calculate_solution(input_vals)

    if result != expected_value:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_value}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_input="""Player 1 starting position: 4
Player 2 starting position: 8"""
result = run_test(test_input, 739785)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    answer = calculate_solution([item.strip() for item in f])

    print(f'Solution is {answer}')
