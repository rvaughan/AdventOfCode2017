#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 20 of the Advent of Code for 2022.
"""
import sys


def calculate_solution(items):
    arrangement = [int(x) for x in items]

    zero_index = 0
    mixer = [(idx, a * 811589153) for (idx, a) in enumerate(arrangement)]

    for _ in range(10):
        for i in range(len(arrangement)):
            for j in range(len(arrangement)):
                if mixer[j][0] == i:
                    curr = mixer.pop(j)
                    new_index = (j + curr[1]) % len(mixer)
                    mixer.insert(new_index, (i, curr[1]))
                    break

    for (idx, (_, val)) in enumerate(mixer):
        if val == 0:
            zero_index = idx
            break

    return (
        mixer[(zero_index + 1000) % len(mixer)][1]
            + mixer[(zero_index + 2000) % len(mixer)][1]
            + mixer[(zero_index + 3000) % len(mixer)][1]
    )


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

test_list = """1
2
-3
3
-2
0
4"""

result = run_test(test_list, 1623178306)

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
