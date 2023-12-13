#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 13 of the Advent of Code for 2023.
"""
import sys


def difference(s1, s2):
    # Calculate the difference between the two strings.
    return sum([0 if c1 == c2 else 1 for (c1, c2) in zip(s1, s2)])


def transpose(pattern):
    return ["".join([row[j] for row in pattern]) for j in range(len(pattern[0]))]


def horizontal_value(pattern):
    result = 0
    
    for i in range(len(pattern) - 1):
        tot_dist = 0
        for row1, row2 in zip(pattern[i + 1:], pattern[i::-1]):
            tot_dist += difference(row1, row2)
    
        # If there was only 1 difference then this is the row the smudge is on...
        if tot_dist == 1:
            result += i + 1
    
    return result


def get_value(pat):
    return horizontal_value(pat) * 100 + horizontal_value(transpose(pat))


def read_patterns(filename):
    with open(filename, 'r') as f:
        patterns = [[row for row in grid.split("\n") if row] for grid in f.read().split("\n\n")]
    
    return patterns


def calculate_solution(filename):
    patterns = read_patterns(filename)

    result = sum([get_value(pattern) for pattern in patterns])

    return result


def run_test(filename, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(filename)

    if result != expected_solution:
        print(f'Test for {filename} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {filename} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

result = run_test('input.ex3', 400)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

answer = calculate_solution('input.txt')

print(f'Solution is {answer}')
