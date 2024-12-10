#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 10 of the Advent of Code for 2024.
"""
import sys


def calculate_solution(items):
    result = 0

    return result


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'))

    print()
    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """0123
1234
8765
9876"""
result = run_test(test_list, 1)

test_list = """...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9"""
result = run_test(test_list, 2)

test_list = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""
result = run_test(test_list, 4)

test_list = """10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01"""
result = run_test(test_list, 3)

test_list = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
result = run_test(test_list, 36)

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
