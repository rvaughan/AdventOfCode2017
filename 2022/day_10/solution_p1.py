#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 10 of the Advent of Code for 2022.
"""

import sys


def get_next_instruction(instructions, idx):
    if idx >= len(instructions):
        return "", 1

    instruction = instructions[idx]
    delay = 1 if instruction == 'noop' else 2

    return instruction, delay


def calculate_solution(instructions):
    result = []

    idx = 0
    delay = 0
    instruction = ''
    signal_strength = 1
    report_cycle = 20

    for cycle in range(1, 221):
        # print(f'{cycle:3d} starts, signal strength={signal_strength}')

        if instruction == "":
            instruction, delay = get_next_instruction(instructions, idx)
            # print(f'   + {instruction} begins execution')

        if cycle == report_cycle:
            result.append(signal_strength * cycle)
            report_cycle += 40

        delay -= 1

        if delay == 0:
            # Execute the current instruction

            # print(f'   - {instruction} executes')
            if 'addx' in instruction:
                signal_strength += int(instruction.split(' ')[1])
            else:
                # It's a noop, so nothing to do
                pass

            instruction = ''
            idx += 1

    return result


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split("\n"))

    if result != expected_solution:
        print(
            f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list="""noop
addx 3
addx -5"""

result = run_test(test_list, [-20, -60, -100, -140, -180, -220])

test_list = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

result = run_test(test_list, [420, 1140, 1800, 2940, 2880, 3960])

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data = [line.strip() for line in f]
    answer = sum(calculate_solution(input_data))

    print(f'Solution is {answer}')
