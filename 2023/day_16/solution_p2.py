#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 16 of the Advent of Code for 2023.
"""
import copy
import sys


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


def calculate_routes(grid, starting_point):
    energised = energised = set()
    energised.add((starting_point[0], starting_point[1]))

    beams = []
    beams.append(starting_point)
    seen = set()

    while any(beams):
        x, y, direction = beams.pop()

        if direction == UP:
            y -= 1
        elif direction == RIGHT:
            x += 1
        elif direction == DOWN:
            y += 1
        elif direction == LEFT:
            x -= 1

        if 0 <= x < len(grid[0]) and 0 <= y < len(grid) and (x, y, direction) not in seen:
            energised.add((x, y))
            seen.add((x, y, direction))

            if grid[y][x] == '-':
                if direction == UP or direction == DOWN:
                    beams.append((x, y, LEFT))
                    direction = RIGHT
            elif grid[y][x] == '\\':
                if direction == UP:
                    direction = LEFT
                elif direction == RIGHT:
                    direction = DOWN
                elif direction == DOWN:
                    direction = RIGHT
                elif direction == LEFT:
                    direction = UP
            elif grid[y][x] == '/':
                if direction == UP:
                    direction = RIGHT
                elif direction == RIGHT:
                    direction = UP
                elif direction == DOWN:
                    direction = LEFT
                elif direction == LEFT:
                    direction = DOWN
            elif grid[y][x] == '|':
                if direction == RIGHT or direction == LEFT:
                    beams.append((x, y, UP))
                    direction = DOWN

            beams.append((x, y, direction))

    # for row in energised:
    #     print(''.join(row))

    return len(energised)


def calculate_solution(items):
    grid = []
    for row in items:
        row_data = []
        for cell in row:
            row_data.append(cell)

        grid.append(row_data)

    results = []
    possibilities = []
    for row in range(len(grid)):
        possibilities.append((0, row, RIGHT))
        possibilities.append((len(grid) - 1, row, LEFT))

    for row in range(len(grid[0])):
        possibilities.append((row, 0, DOWN))
        possibilities.append((row, len(grid) - 1, UP))


    for possibility in possibilities:
        results.append(calculate_routes(grid, possibility))

    return max(results)


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

test_list = """.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|...."""
result = run_test(test_list, 51)

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
