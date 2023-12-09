#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 6 of the Advent of Code for 2019.
"""
from collections import defaultdict
import sys


def calculate_solution(items):
    orbits = {}
    for item in items:
        p1, p2 = item.split(')')

        # Intuit: A planet can only orbit ONE other planet
        orbits[p2] = p1

    # Calculate all of the orbit counts from all of the planets in the system.
    # This will include "duplicates".
    result = 1
    for _, planet in orbits.items():
        if planet == 'COM':
            continue

        result += 1
        cur_planet = planet
        while cur_planet != 'COM':
            result += 1
            cur_planet = orbits[cur_planet]

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


test_list = """COM)B"""
result = run_test(test_list, 1)

test_list = """COM)B
B)C"""
result = run_test(test_list, 3)

test_list = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""
result = run_test(test_list, 42)

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
