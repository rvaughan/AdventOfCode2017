#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 6 of the Advent of Code for 2019.
"""
from collections import defaultdict
import sys


def calculate_solution(items):
    orbits = {}
    for item in items:
        p1, p2 = item.split(')')

        # Intuit: A planet can only orbit ONE other planet
        orbits[p2] = p1

    # Find the route from YOU to COM
    you_transfers = []
    cur_planet = 'YOU'
    while cur_planet != 'COM':
        you_transfers.append(cur_planet)
        cur_planet = orbits[cur_planet]

    # Find the route from SAN to COM
    san_transfers = []
    cur_planet = 'SAN'
    while cur_planet != 'COM':
        san_transfers.append(cur_planet)
        cur_planet = orbits[cur_planet]

    # Find the first common transfer
    for i in range(len(you_transfers)):
        if you_transfers[i] in san_transfers:
            result = i - 1 # Number of transfers to the intersection point
            break

    intersect = you_transfers[i]

    # Now we just need to find the number of transfers to the intersection point
    # from SAN.
    for planet in san_transfers[1:]:
        if planet == intersect:
            break
        result += 1

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
K)L
K)YOU
I)SAN"""
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
