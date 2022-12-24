#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 24 of the Advent of Code for 2022.
"""
import sys


def calculate_solution(items):
    result = 0
    walls = set()
    blizzards = set()

    for y, line in enumerate(items):
        for x, c in enumerate(line):
            if c == '#':
                walls.add((x-1, y-1))
            if c == '>':
                blizzards.add((x-1, y-1, +1, 0))
            if c == '<':
                blizzards.add((x-1, y-1, -1, 0))
            if c == '^':
                blizzards.add((x-1, y-1, 0, -1))
            if c == 'v':
                blizzards.add((x-1, y-1, 0, +1))

    X = max(x for x, y in walls)
    Y = max(y for x, y in walls)

    # add some walls on the top and bottom, otherwise the player escapes the maze
    walls |= {(x, -2) for x in range(-1, 3)}
    walls |= {(x, Y+1) for x in range(X-3, X+2)}
    start = (0, -1)
    exit = (X-1, Y)

    t = 0
    q = {start}
    goal = exit

    while True:
        t += 1
        b = {((px+t*dx) % X, (py+t*dy) % Y) for px, py, dx, dy in blizzards}
        n = {(px+dx, py+dy) for dx, dy in ((1, 0), (0, 1),
                                           (-1, 0), (0, -1), (0, 0)) for px, py in q}
        q = n - b - walls
        if goal in q:
            result = t
            break

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

test_list = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""

result = run_test(test_list, 18)

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
