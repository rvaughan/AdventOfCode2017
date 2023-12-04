#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 4 of the Advent of Code for 2023.
"""
from collections import defaultdict
import sys


def calculate_win(cards):
    card = cards.split('|')
    my_card = [int(x) for x in card[0].strip().split()[2:]]
    play_card = [int(x) for x in card[1].strip().split()]

    cards_won = 0
    for number in my_card:
        if number in play_card:
            cards_won += 1

    return cards_won 


def calculate_solution(cards):
    result = 0

    cards_won = defaultdict(int)
    copies = defaultdict(int)

    current_card = 1
    for card in cards:
        won = calculate_win(card)
        cards_won[current_card] += 1
        
        for x in range(current_card + 1, current_card + won + 1):
            copies[x] += (1 + copies[current_card])

        current_card += 1

    for k, v in cards_won.items():
        result += v

    for k, v in copies.items():
        result += v

    return result


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'))

    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.


test_list = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

result = run_test(test_list, 30)

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
