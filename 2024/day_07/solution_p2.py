#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 7 of the Advent of Code for 2024.
"""
from collections import deque
import math
import sys


def calculate_solution(items):
    result = 0

    for row in items:
        row = list(map(int, row.replace(":", "").split()))
        target, args = row[0], row[1:]

        todo = deque()
        todo.append((args[0], 1))
        finish = len(args)
        
        while len(todo) > 0:
            val, pos = todo.pop()
            if pos == finish:
                if val == target:
                    result += target
                    break
            elif val <= target:
                x = args[pos]

                # Try an addition step
                todo.append((val + x, pos + 1))

                # Try a multiplication step
                todo.append((val * x, pos + 1))

                # Try a concatenation step
                new = str(val) + str(x)
                todo.append((int(new), pos + 1))

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

test_list = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
result = run_test(test_list, 11387)

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
