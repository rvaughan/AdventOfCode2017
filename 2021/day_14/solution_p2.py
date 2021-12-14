#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 14 of the Advent of Code for 2021.
"""

import sys
from collections import defaultdict, deque


def calculate_solution(input_data, num_steps):
    polymer = input_data[0]

    additions = defaultdict(lambda: defaultdict(str))
    for x in input_data[2:]:
        left, right = x.split(' -> ')
        additions[left[0]][left[1]] = right

    for _ in range(num_steps):
        tmp_polymer = ''
        for x in range(len(polymer)-1):
            tmp_polymer += polymer[x]
            if polymer[x] in additions and polymer[x+1] in additions[polymer[x]]:
                tmp_polymer += additions[polymer[x]][polymer[x+1]]

        tmp_polymer += polymer[-1]

        polymer = tmp_polymer
    
    counts = defaultdict(int)
    for x in polymer:
        counts[x] += 1
    # print(polymer)
    # print(counts)
    sorted_counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1])}
    # print(sorted_counts)
    key_list = list(sorted_counts.keys())

    return sorted_counts[key_list[-1]] - sorted_counts[key_list[0]]


def run_test(test_input, num_steps, expected_value):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    input_vals = [line.strip() for line in test_input.split('\n')]
    result = calculate_solution(input_vals, num_steps)

    if result != expected_value:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_value}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_input="""NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
result = run_test(test_input, 10, 1588)

test_input="""NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
result = run_test(test_input, 40, 2188189693529)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    answer = calculate_solution([item.strip() for item in f], 40)

    print(f'Solution is {answer}')
