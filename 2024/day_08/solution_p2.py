#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 8 of the Advent of Code for 2024.
"""
import sys


def antinode(pr1, pr2, width, height):
    x1, y1 = pr1
    x2, y2 = pr2
    newx = x2 + (x2 - x1)
    newy = y2 + (y2 - y1)
    if newx >= 0 and newx < height and newy >= 0 and newy < width:
        return True, newx, newy

    return False, None, None


def calculate_solution(items):
    result = 0

    antinodes = set()

    grid = []

    for line in items:
        grid.append(line.strip())

    height = len(grid)
    width = len(grid[0])

    nodes = {}

    for i in range(height):
        for j in range(width):
            if grid[i][j] != ".":
                if grid[i][j] in nodes:
                    nodes[grid[i][j]].append((i, j))
                else:
                    nodes[grid[i][j]] = [(i, j)]

    for k in nodes:
        node_list = nodes[k]
        L = len(node_list)
        for i in range(L):
            for j in range(i):
                node1 = node_list[i]
                node2 = node_list[j]

                ok, x, y = antinode(node1, node2, height, width)
                if ok:
                    antinodes.add((x, y))
                
                ok, x, y = antinode(node2, node1, height, width)
                if ok:
                    antinodes.add((x, y))

    result = len(antinodes)

    return result


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'))

    print()
    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
.........."""
result = run_test(test_list, 9)

test_list = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
result = run_test(test_list, 34)

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
