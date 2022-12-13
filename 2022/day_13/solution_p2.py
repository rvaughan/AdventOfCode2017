#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 13 of the Advent of Code for 2022.
"""
from functools import cmp_to_key
import json
import sys


def compare(left, right):
    max_length = max(len(left), len(right))
    for idx in range(max_length):
        if idx == len(left) and idx < len(right):
            return -1
        if idx < len(left) and idx == len(right):
            return 1

        l_val = left[idx]
        r_val = right[idx]
        if type(l_val) == list and type(r_val) == list:
            result = compare(l_val, r_val)
            if result != 0:
                return result
        elif type(l_val) == int and type(r_val) == int:
            if int(l_val) < int(r_val):
                return -1
            elif int(l_val) > int(r_val):
                return 1
        elif type(l_val) == int and type(r_val) == list:
            result = compare([l_val], r_val)
            if result != 0:
                return result
        else:
            result = compare(l_val, [r_val])
            if result != 0:
                return result

    return 0


def calculate_solution(lines):
    signals = []
    for line in lines:
        if line.strip() != '':
            signals.append(json.loads(line))

    signals.append(json.loads('[[2]]'))
    signals.append(json.loads('[[6]]'))

    sorted_signals = sorted(signals, key=cmp_to_key(lambda a, b: -1 if compare(a, b) == -1 else 1))
    index_2 = sorted_signals.index([[2]]) + 1
    index_6 = sorted_signals.index([[6]]) + 1

    return (index_2 * index_6)


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'))

    if result != expected_solution:
        print(
            f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """[1, 1, 3, 1, 1]
[1, 1, 5, 1, 1]

[[1], [2, 3, 4]]
[[1], 4]

[9]
[[8, 7, 6]]

[[4, 4], 4, 4]
[[4, 4], 4, 4, 4]

[7, 7, 7, 7]
[7, 7, 7]

[]
[3]

[[[]]]
[[]]

[1, [2, [3, [4, [5, 6, 7]]]], 8, 9]
[1, [2, [3, [4, [5, 6, 0]]]], 8, 9]"""

result = run_test(test_list, 140)

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
