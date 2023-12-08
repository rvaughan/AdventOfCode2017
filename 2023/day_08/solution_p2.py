#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 8 of the Advent of Code for 2023.
"""
from math import lcm
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

    cur_i = 0

    # Identify all of the starting positions for the ghosts
    ghost_positions = []
    for key in map:
        if key[-1] == 'A':
            ghost_positions.append({
                'pos': key,
                'cur_instruction': instructions[cur_i]
            })

    ghost_moves = []

    for things in ghost_positions:
        moves = 0

        cur_pos = things['pos']
        cur_instruction = things['cur_instruction']
        cur_i = 0

        while True:
            print(moves, cur_i, cur_pos, cur_instruction)

            if map[cur_pos][cur_instruction][-1] == 'Z':
                # Found this ghosts first end position
                ghost_moves.append(moves)
                break

            cur_pos = things['pos']
            cur_instruction = things['cur_instruction']
            
            moves += 1

            things['pos'] = map[cur_pos][cur_instruction]
            
            cur_i += 1
            if cur_i == len(instructions):
                cur_i = 0

            things['cur_instruction'] = instructions[cur_i]

    # We've got all of the ghosts final positions, so now use LCM to work out
    # when they would all stop at the same time using LCM. The intuition here
    # is that ghosts movements are in a pattern and they converge on the solution
    # at the same time, so you just have to find that position by finding the
    # first divisible position - the Least Common Multiplier (LCM) of all of the
    # movements.
    return lcm(*ghost_moves)


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

test_list = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

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
