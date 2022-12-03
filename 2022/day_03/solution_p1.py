#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 3 of the Advent of Code for 2022.
"""

import sys


def process_rucksack(item):
    priority = 0
    middle = int(len(item)/2)

    left = item[:middle]
    left_items = set([x for x in left])

    right = item[middle:]
    right_items = set([x for x in right])

    for x in left_items:
        if x in right_items:
            if x > 'a':
                priority = ord(x) - ord('a') + 1
            else:
                priority = ord(x.lower()) - ord('a') + 27
            break

    return priority


def calculate_solution(items):
    result = 0

    for item in items:
        result += process_rucksack(item)

    return result


def run_test(test_input, priorities, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """

    for items, priority in zip(test_input, priorities):
        result = process_rucksack(items)
        if result != priority:
            print(f'Test for {items} FAILED. Got a result of {result}, not {priority}')
            sys.exit(-1) 

    result = calculate_solution(test_input)

    if result != expected_solution:
        print(
            f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg",
             "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]

result = run_test(test_list, [16, 38, 42, 22, 20, 19], 157)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data = [line for line in f]
    answer = calculate_solution(input_data)

    print(f'Solution is {answer}')
