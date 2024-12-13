#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 11 of the Advent of Code for 2024.
"""
import sys


def calculate_solution(list_of_stones, blinks):
    result = 0

    stones = [x for x in list_of_stones[0].strip().split(' ')]

    for blink in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == '0':
                new_stones.append('1')
                continue

            if len(stone) % 2 == 0:
                new_stones.append(str(int(stone[:int(len(stone) / 2)])))
                new_stones.append(str(int(stone[int(len(stone) / 2):len(stone)])))
                continue

            new_stones.append(str(int(stone) * 2024))

        stones = new_stones

    result = len(stones)

    return result


def run_test(test_input, blinks, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'), blinks)

    print()
    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """0 1 10 99 999"""
result = run_test(test_list, 1, 7)

test_list = """125 17"""
result = run_test(test_list, 6, 22)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data, 75)

    print(f'Solution is {answer}')
