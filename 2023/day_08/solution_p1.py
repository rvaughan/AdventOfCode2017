#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 8 of the Advent of Code for 2023.
"""
import sys


def calculate_solution(items):
    instructions = items[0]

    map = {}
    for item in items[2:]:
        parts = item.split()
        map[parts[0]] = {
            'L': parts[2].replace('(', '').replace(',', '').strip(),
            'R': parts[3].replace(')', '').replace(',', '').strip()
        }

    moves = 1
    cur_i = 0
    cur_pos = 'AAA'
    cur_instruction = instructions[cur_i]
    while True:
        # print(moves, cur_i, cur_pos, cur_instruction)

        if map[cur_pos][cur_instruction] == 'ZZZ':
            break

        cur_pos = map[cur_pos][cur_instruction]
        moves += 1
        cur_i += 1
        if cur_i == len(instructions):
            cur_i = 0
        cur_instruction = instructions[cur_i]

    return moves


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

test_list = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

result = run_test(test_list, 2)

test_list = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

result = run_test(test_list, 6)

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
