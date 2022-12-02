#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 2 of the Advent of Code for 2022.
"""

import sys

winning_moves = {
    'Paper': 'Rock',
    'Scissors': 'Paper',
    'Rock': 'Scissors',
}

decoded_moves = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors',
}

win = 6
draw = 3
loss = 0

move_scores = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}


def score_move(opp_move, your_move):
    score = 0

    score += move_scores[decoded_moves[your_move]]

    # print(f'{decoded_moves[your_move]} {decoded_moves[opp_move]} {winning_moves[decoded_moves[your_move]]}')

    if winning_moves[decoded_moves[your_move]] == decoded_moves[opp_move]:
        return score + win

    if decoded_moves[opp_move] == decoded_moves[your_move]:
        return score + draw

    return score+ loss


def calculate_solution(items):
    result = 0

    for item in items:
        opp_move, your_move = item.split(" ")

        result += score_move(opp_move, your_move)

    return result


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input)

    if result != expected_solution:
        print(
            f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = ["A Y", "B X", "C Z"]

result = run_test(test_list, 15)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data)

    print(f'Solution is {answer}')
