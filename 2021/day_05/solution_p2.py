#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 5 of the Advent of Code for 2021.
"""

import sys
from collections import defaultdict


def decode_line(line):
    parts = line.split('->')

    start_part = parts[0].split(',')
    end_part = parts[1].split(',')

    start_x = int(start_part[0])
    start_y = int(start_part[1])
    end_x = int(end_part[0])
    end_y = int(end_part[1])

    return start_x, start_y, end_x, end_y


def calculate_solution(input_data):
    board = defaultdict(int)
    max_x = 0
    max_y = 0

    for line in input_data:
        start_x, start_y, end_x, end_y = decode_line(line)

        x = start_x
        y = start_y
        while x != end_x or y != end_y:
            board[f'{x},{y}'] += 1
            
            if x != end_x:
                if start_x < end_x:
                    x += 1
                else:
                    x -= 1

            if y != end_y:
                if start_y < end_y:
                    y += 1
                else:
                    y -= 1
        
        board[f'{x},{y}'] += 1
        
        max_x = max(start_x, max_x)
        max_y = max(start_y, max_y)
        max_x = max(end_x, max_x)
        max_y = max(end_y, max_y)

    # for y in range(max_y+1):
    #     row = ''
    #     for x in range(max_x+1):
    #         row += str(board[f'{x},{y}']) if board[f'{x},{y}'] > 0 else '.'
    #     print(row)

    overlaps = 0
    for x in range(max_x+1):
        for y in range(max_y+1):
            overlaps += 1 if board[f'{x},{y}'] > 1 else 0

    return overlaps


def run_test(test_input, expected_result):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution([line.strip() for line in test_input.split('\n')])

    if result != expected_result:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_result}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

result = run_test(test_input, 12)

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
