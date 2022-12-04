#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 4 of the Advent of Code for 2021.
"""
from collections import defaultdict
import sys


def get_sections(assignments, elf):
    start, end = elf.split('-')

    for section in range(int(start), int(end) + 1):
        assignments[section] += 1


def check_sections(assignments, elf):
    start, end = elf.split('-')

    count = 0
    for section in range(int(start), int(end) + 1):
        if assignments[section] == 2:
            count += 1

    return count > 0


def check_for_overlap(assignment):
    sections = defaultdict(int)
    elf_1, elf_2 = assignment.split(',')

    get_sections(sections, elf_1)
    get_sections(sections, elf_2)

    if check_sections(sections, elf_1):
        return 1
        
    if check_sections(sections, elf_2):
        return 1

    return 0


def calculate_solution(assignments):
    overlaps = 0

    for assignment in assignments:
        overlaps += check_for_overlap(assignment)

    return overlaps


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

test_list = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]

result = run_test(test_list, 4)

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
