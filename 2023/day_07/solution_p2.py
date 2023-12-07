#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 7 of the Advent of Code for 2023.
"""
from collections import defaultdict
import sys


def determine_hand(cards):
    hand = defaultdict(int)
    for card in cards:
        hand[card] += 1

    highest = 0
    for card, count in hand.items():
        if card == 'J':
            # We don't include Jokers
            continue

        highest = max(highest, count)

    if highest == 0:
        # Sneaky - all of the cards were Jokers!
        return 6

    if 'J' in hand:
        # Assign all of the jokers points to the highest score which will give
        # you the best hand possible.
        highest += hand['J']
        # Remember to remove the jokers!
        del hand['J']

    if highest == 5: # 5 of a kind
        return 6
    elif highest == 4: # 4 of a kind
        return 5
    elif highest == 3:
        if len(hand) == 2: # Full house
            return 4
        return 3 # 3 of a kind
    elif highest == 2:
        if len(hand) == 3: # 2 pairs
            return 2
        return 1 # one pair
    
    return 0 # high card


def hand_2_better(hand_1, hand_2):
    face_cards = ['Q', 'K', 'A', 'T']
    
    # Check each card in turn
    for c_1, c_2 in zip(hand_1, hand_2):
        if c_1 == 'J':
            c_1 = '1'
        if c_2 == 'J':
            c_2 = '1'
        
        if c_1 in face_cards and c_2 in face_cards:
            if c_1 == 'A' and c_2 != 'A':
                return False
            if c_1 != 'A' and c_2 == 'A':
                return True
            if c_1 == 'K' and c_2 != 'K':
                return False
            if c_1 != 'K' and c_2 == 'K':
                return True
            if c_1 == 'Q' and c_2 != 'Q':
                return False
            if c_1 != 'Q' and c_2 == 'Q':
                return True
            if c_1 == 'T' and c_2 != 'T':
                return False
            if c_1 != 'T' and c_2 == 'T':
                return True
        elif c_1 in face_cards and c_2 not in face_cards:
            return False
        elif c_1 not in face_cards and c_2 in face_cards:
            return True
        elif c_1 > c_2:
            return False
        elif c_1 < c_2:
            return True
            
    return False


def sort_hands(hands):
    sorted_hands = hands.copy()
    changes = True
    max = len(sorted_hands)
    while changes:
        # Bubble sort...
        for i in range(max-1):
            if hand_2_better(sorted_hands[i], sorted_hands[i+1]):
                swap = sorted_hands[i]
                sorted_hands[i] = sorted_hands[i+1]
                sorted_hands[i+1] = swap
                changes = True
        
        if not changes:
            break

        max -= 1
        if max == 0:
            break
    
    return sorted_hands


def calculate_solution(items):
    result = 0

    first_rank = defaultdict(list)
    final_rank = []
    bids = {}

    for item in items:
        cards, bid = item.split()
        first_rank[determine_hand(cards)].append(cards)
        bids[cards] = bid

    for _, hands in sorted(first_rank.items(), reverse=True):
        final_rank += sort_hands(hands)

    multiplier = len(final_rank)
    for card in final_rank:
        # print(card)
        result += (int(bids[card]) * int(multiplier))
        multiplier -= 1

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

assert(determine_hand('AAAAA') == 6)
assert(determine_hand('AA8AA') == 5)
assert determine_hand('23332') == 4, f"Got {determine_hand('23332')}"
assert(determine_hand('TTT98') == 3)
assert(determine_hand('23432') == 2)
assert(determine_hand('A23A4') == 1)
assert(determine_hand('23456') == 0)
assert(determine_hand('QJJQ2') == 5)
assert(determine_hand('9929J') == 5)
assert(determine_hand('9988J') == 4)
assert(determine_hand('5T52J') == 3)
assert(determine_hand('6TT6J') == 4)
assert(determine_hand('JK863') == 1)
assert(determine_hand('JTKJ6') == 3)
assert(determine_hand('J9333') == 5)
assert(determine_hand('JJQQK') == 5)

assert(determine_hand('J2345') == 1)
assert(determine_hand('J2355') == 3)
assert(determine_hand('J3355') == 4)
assert(determine_hand('J2555') == 5)
assert(determine_hand('J5555') == 6)
assert(determine_hand('JJJJ1') == 6)
assert(determine_hand('JJJ11') == 6)
assert(determine_hand('JJJJJ') == 6)

assert(hand_2_better('33332', '2AAAA') == False)
assert(hand_2_better('77788', '77888') == True)
assert(hand_2_better('KK677', 'KTJJT') == False)
assert(hand_2_better('T55J5', 'QQQJA') == True)
assert(hand_2_better('JKKK2', 'QQQQ2') == True)
assert(hand_2_better('T55J5', 'QQQJA') == True)
assert(hand_2_better('QQQJA', 'T55J5') == False)
assert(hand_2_better('T55J5', 'KTJJT') == True)
assert(hand_2_better('KTJJT', 'T55J5') == False)
assert(hand_2_better('QQQJA', 'KTJJT') == True)
assert(hand_2_better('KTJJT', 'QQQJA') == False)
assert(hand_2_better('JJJJJ', '33333') == True)
assert(hand_2_better('JJJJJ', '22222') == True)

test_list = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

result = run_test(test_list, 5905)

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

    # 249696452 is too high
    # 249680336 is wrong
    # 249631254 <-- actual!
    # 248078693 is too low