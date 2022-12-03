#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 3 of the Advent of Code for 2022.
"""

from collections import defaultdict
import sys


def process_group(group):
    badge_score = 0
    item_map = defaultdict(int)

    for rucksack in group:
        items = set([x for x in rucksack])

        for i in items:
            item_map[i] += 1

    for key, count in item_map.items():
        if count == len(group):
            if key > 'a':
                badge_score = ord(key) - ord('a') + 1
            else:
                badge_score = ord(key.lower()) - ord('a') + 27
            break

    return badge_score


def calculate_solution(items):
    result = 0

    group=[]
    for item in items:
        group.append(item)
        
        if len(group) == 3:
            result += process_group(group)
            group=[]

    return result


def run_test(test_input, groups, priorities, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """

    for items, priority in zip(groups, priorities):
        result=process_group(items)
        if result != priority:
            print(
                f'Test for {items} FAILED. Got a result of {result}, not {priority}')
            sys.exit(-1)

    result=calculate_solution(test_input)

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
groups = [
    ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"],
    ["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
]

result = run_test(test_list, groups, [18, 52], 70)

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
