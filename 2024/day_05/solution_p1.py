#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 5 of the Advent of Code for 2024.
"""
from collections import defaultdict
import sys


def calculate_solution(items):
    result = 0

    orderings, updates = ''.join(items).split('\n\n')

    order = defaultdict(list)
    for o in orderings.split('\n'):
        src, dest = o.strip().split('|')
        order[int(src)].append(int(dest))

    manuals = []
    for lst in updates.split('\n'):
        manuals.append(tuple(int(i) for i in lst.strip().split(',')))

    for manual in manuals:
        for idx, page in enumerate(manual[1:], 1):
            prev = set(manual[:idx])
            bad = set(order[page])
            
            if prev.intersection(bad):  
                break
        else:
            result += manual[len(manual)//2]

    return result


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input)

    print()
    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
result = run_test(test_list, 143)

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
