#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 18 of the Advent of Code for 2022.
"""
import sys

FACE_OFFSETS = [
    (0, 0, 1),
    (0, 0, -1),
    (0, 1, 0),
    (0, -1, 0),
    (1, 0, 0),
    (-1, 0, 0),
]


def create_listmap(func, sequence) -> list:
    """
    >>> lmap(int, "12345")
    [1, 2, 3, 4, 5]
    """
    return list(map(func, sequence))


def calculate_solution(data):
    lava = { tuple(create_listmap(int, line.split(','))) for line in data }

    result = 0
    for x, y, z in lava:
        for dx, dy, dz in FACE_OFFSETS:
            if (x + dx, y + dy, z + dz) not in lava:
                result += 1
    
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

test_list = """1,1,1
2,1,1"""

result = run_test(test_list, 10)

test_list = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""

result = run_test(test_list, 64)

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
