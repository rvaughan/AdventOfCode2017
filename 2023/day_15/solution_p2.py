#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 15 of the Advent of Code for 2023.
"""
from collections import defaultdict
import sys


def calculate_solution(items):
    result = 0

    boxes = defaultdict(list)
    focal_lengths = {}

    for item in items:
        for parts in item.split(','):
            box = 0
            lens = ''
            for idx, char in enumerate(parts):
                if char not in ['-', '=']:
                    lens += char
                    box += ord(char)
                    box *= 17
                    box %= 256
                else:
                    lenses = boxes[box]
                    if char == '-':
                        if lens in lenses:
                            lenses.remove(lens)
                    else:
                        value = int(parts[idx+1:])
                        focal_lengths[lens] = value

                        if lens not in lenses:
                            lenses.append(lens)

                    break

    for box in boxes:
        for lens_idx, lens in enumerate(boxes[box]):
            lens_value = (box + 1) * (lens_idx + 1) * focal_lengths[lens]
            
            result += lens_value

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

test_list = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
result = run_test(test_list, 145)

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
