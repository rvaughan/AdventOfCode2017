#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 17 of the Advent of Code for 2023.
"""
import copy
import sys


UP = 1
LEFT = 2
DOWN = 3
RIGHT = 4


def calculate_solution(items):
    grid = []

    for row in items:
        grid.append([int(x) for x in row])

    successful_paths = []
    paths = []

    # Set the first two possible paths
    # x, y, direction, num of moves in that direction, list of cells seen so far in the route
    paths.append([(0, 0, RIGHT, 1, set())])
    paths.append([(0, 0, DOWN, 1, set())])

    while any(paths):
        path = paths.pop()

        # Get the last point in the path
        x, y, direction, distance, seen = path[-1]

        # Check if we've reached our goal
        if x == len(grid[0]) - 1 and y == len(grid) - 1:
            successful_paths.append(path)
            continue

        # Check the move is valid...
        if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
            seen.add((x, y))

            if direction == UP:
                if distance < 3 and (x, y-1) not in seen:
                    new_path = copy.deepcopy(path)
                    new_path.append((x, y - 1, UP, distance + 1, seen))
                    paths.append(new_path)

                if (x+1, y) not in seen:
                    new_path = copy.deepcopy(path)
                    new_path.append((x + 1, y, LEFT, 1, seen))
                    paths.append(new_path)

                if (x-1, y) not in seen:
                    new_path = copy.deepcopy(path)
                    new_path.append((x - 1, y, RIGHT, 1, seen))
                    paths.append(new_path)
            elif direction == DOWN:
                if distance < 3 and (x, y+1) not in seen:
                    new_path = copy.deepcopy(path)
                    new_path.append((x, y + 1, DOWN, distance + 1, seen))
                    paths.append(new_path)

                if (x-1, y) not in seen:
                    new_path = copy.deepcopy(path)
                    new_path.append((x - 1, y, LEFT, 1, seen))
                    paths.append(new_path)

                if (x+1, y) not in seen:
                    new_path = copy.deepcopy(path)
                    new_path.append((x + 1, y, RIGHT, 1, seen))
                    paths.append(new_path)
            elif direction == LEFT:
                if distance < 3 and (x-1, y) not in seen:
                    new_path = copy.deepcopy(path)
                    new_path.append((x - 1, y, LEFT, distance + 1, seen))
                    paths.append(new_path)

                if (x, y-1) not in seen:
                    new_path = copy.deepcopy(path)
                    new_path.append((x, y - 1, UP, 1, seen))
                    paths.append(new_path)

                if (x, y+1) not in seen:
                    new_path = copy.deepcopy(path)
                    new_path.append((x, y + 1, DOWN, 1, seen))
                    paths.append(new_path)
            elif direction == RIGHT:
                if distance <= 3 and (x+1, y) not in seen:
                    new_path = copy.deepcopy(path)
                    new_path.append((x + 1, y, RIGHT, distance + 1, seen))
                    paths.append(new_path)

                if (x, y-1) not in seen:
                    new_path = copy.deepcopy(path)
                    new_path.append((x, y - 1, UP, 1, seen))
                    paths.append(new_path)

                if (x, y+1) not in seen:
                    new_path = copy.deepcopy(path)
                    new_path.append((x, y + 1, DOWN, 1, seen))
                    paths.append(new_path)

        # print(len(paths), len(successful_paths))

    min_heat_loss = 99999999
    winning_path = None
    print(len(successful_paths))
    for path in successful_paths:
        loss = sum([grid[step[1]][step[0]] for step in path])
        loss -= grid[0][0]
        # print(loss)
        min_heat_loss = min(min_heat_loss, loss)
        if loss == min_heat_loss:
            winning_path = path

    for step in winning_path:
        grid[step[1]][step[0]] = '*'

    print()
    for row in grid:
        print(''.join([str(x) for x in row]))
    print()

    return min_heat_loss    


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

test_list = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""
result = run_test(test_list, 102)

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
