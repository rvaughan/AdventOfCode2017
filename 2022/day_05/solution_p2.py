#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 5 of the Advent of Code for 2021.
"""

import sys


def calculate_solution(items):
    result = ""

    sorting_stacks = True
    num_stacks = int(len(items[0]) / 3)

    if num_stacks == 2:
        num_stacks = 3

    stacks = []
    for _ in range(0, num_stacks):
        stacks.append([])

    for item in items:
        if sorting_stacks:
            if item != '':
                if item[1] == '1':
                    continue

                for s in range(0, int(len(item) / 3)):
                    pos = (s * 4) + 1
                    try:
                        if pos <= len(item):
                            crate = item[pos]
                            if crate != ' ':
                                stacks[s].append(crate)
                    except IndexError:
                        print(pos, len(item))
                        print(item)
                        print(item[pos-1])
                        x
            else:
                sorting_stacks = False
        else:
            move = item.split()

            count = int(move[1])
            from_stack = int(move[3]) - 1
            to_stack = int(move[5]) - 1

            stacks[to_stack] = stacks[from_stack][:count] + stacks[to_stack]
            stacks[from_stack] = stacks[from_stack][count:]

    for idx in range(num_stacks):
        result += stacks[idx][0] if len(stacks[idx]) > 0 else ' '

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

test_list = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

result = run_test(test_list, "MCD")

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data = [line.strip('\n') for line in f]
    answer = calculate_solution(input_data)

    print(f'Solution is {answer}')
