#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 17 of the Advent of Code for 2022.
"""
import sys


def calculate_solution(items):
    cur_jet = 0
    jet_pattern = items[0]
    cur_rock = 0
    rock_patterns = [
        [
            '..####.'
        ],
        [
            '...#...',
            '..###..',
            '...#...'
        ],
        [
            '....#..',
            '....#..',
            '..###..'
        ],
        [
            '...#...',
            '...#...',
            '...#...',
            '...#...'
        ],
        [
            '...##..',
            '...##..'
        ]
    ]

    column = []

    for turn in range(2022):
        # Add the gap to the rocks
        column.append('.......')
        column.append('.......')
        column.append('.......')

        # Add the next rock
        num_rows = len(rock_patterns[cur_rock])
        for idx in range(num_rows):
            column.append(rock_patterns[cur_rock][idx])

        cur_row = len(column) - 1

        stopped = False

        while not stopped:
            # Apply jet stream
            if jet_pattern[cur_jet] == '>':
                # Find the rightmost part of the rock - the bit that will touch the
                # sides of the cave first.
                look_row = 0 if num_rows == 1 else 1

                if column[cur_row-look_row][-1] == '.':
                    for c in range(num_rows):
                        new_row = '.' + ''.join(column[cur_row-c][:-1])
                        column[cur_row - c] = new_row
            elif jet_pattern[cur_jet] == '<':
                # Find the leftmost part of the rock - the bit that will touch the
                # sides of the cave first.
                look_row = 1 if cur_rock == 1 else len(
                    rock_patterns[cur_rock]) - 1
                if column[cur_row-look_row][0] == '.':
                    for c in range(num_rows):
                        new_row = ''.join(column[cur_row-c][1:]) + '.'
                        column[cur_row - c] = new_row

            cur_jet += 1
            if cur_jet == len(jet_pattern):
                cur_jet = 0

            # Now, move the grid down one
            if cur_row >= 0:
                if column[cur_row - 1] == '.......':
                    cur_row -= 1

                    for x in range(len(rock_patterns[cur_rock])):
                        column[cur_row+x] = column[cur_row+x+1]
                    column[cur_row+len(rock_patterns[cur_rock])] = '.......'

                    if cur_row == 0:
                        stopped = True
                else:
                    stopped = True
            else:
                stopped = True
        
        if cur_rock == 1:
            print(f'--- {stopped}')
            for idx in range(len(column)-1, -1, -1):
                print(''.join(x for x in column[idx]))

            xxxx

        cur_rock += 1
        if cur_rock == len(rock_patterns):
            cur_rock = 0

    result = len(column)

    return result


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

test_list = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""

result = run_test(test_list, 3068)

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
