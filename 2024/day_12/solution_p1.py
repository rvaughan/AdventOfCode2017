#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 12 of the Advent of Code for 2024.
"""
import sys


def find_region(grid, height, width, i, j):
    plant = grid[i][j]
    visited = set()
    fence = 0
    queue = [(i, j)]

    while queue:
        i, j = queue.pop()
        if (i, j) in visited:
            continue

        if i not in range(height) or j not in range(width) or grid[i][j] != plant:
            fence += 1
            continue
        
        visited.add((i, j))
        
        for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if (i+x, j+y) not in visited:
                queue.append((i+x, j+y))
                
    return visited, len(visited) * fence


def calculate_solution(items):
    grid = items
    height = len(grid)
    width = len(grid[0])
            
    result = 0
    visited = set()
    for i in range(height):
        for j in range(width):
            if (i, j) not in visited:
                region, cost = find_region(grid, height, width, i, j)
                visited |= region
                result += cost

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

test_list = """AAAA
BBCD
BBCC
EEEC"""
result = run_test(test_list, 140)

test_list = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""
result = run_test(test_list, 772)

test_list = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
result = run_test(test_list, 1930)

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
