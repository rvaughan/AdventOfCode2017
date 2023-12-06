#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 6 of the Advent of Code for 2023.
"""
import sys


def calculate_solution(items):
    result = 0

    max_time = int(''.join(items[0].split()[1:]).replace(' ', ''))
    max_distance = int(''.join(items[1].split()[1:]).replace(' ', ''))

    beaten = []
    
    # Find the first time where we beat the max distance.
    first_time = 0
    speed = 0
    for t in range(0, max_time):
        if (max_time - t) * speed > max_distance:
            # print(t, speed, max_distance, (max_time - t) * speed)
            first_time = t
            break

        speed += 1

    # Find the last time where we beat the max distance.
    last_time = 0
    speed = max_time
    for t in range(max_time, 0, -1):
        if (max_time - t) * speed > max_distance:
            # print(t, speed, max_distance, (max_time - t) * speed)
            last_time = t
            break

        speed -= 1

    return last_time - first_time + 1


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

test_list = """Time:      7  15   30
Distance:  9  40  200"""

result = run_test(test_list, 71503)

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
