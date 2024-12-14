#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 12 of the Advent of Code for 2024.
"""
import sys


def is_same(grid, height, width, i, j, plant):
    return (
        i in range(height) and 
        j in range(width) and 
        grid[i][j] == plant
    )


def get_corners(grid, height, width, i, j):
    NW, W, SW, N, S, NE, E, SE = [
        is_same(grid, height, width, i+x, j+y, grid[i][j])
        for x in range(-1, 2) 
        for y in range(-1, 2) 
        if x or y
    ]

    return sum([
        N and W and not NW, 
        N and E and not NE, 
        S and W and not SW, 
        S and E and not SE, 
        not (N or W),
        not (N or E),
        not (S or W),
        not (S or E)
    ])


def find_region(grid, height, width, i, j):
    plant = grid[i][j]
    region = set()
    queue = set([(i, j)])

    while queue:
        i, j = queue.pop()
        region.add((i, j))
        for x, y in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
            if (x in range(height) and 
                y in range(width) and 
                grid[x][y] == plant and
                (x, y) not in region and
                (x, y) not in queue
            ):
                queue.add((x, y))

    corners = sum(get_corners(grid, height, width, x, y) for x, y in region)
    
    return region, corners * len(region)


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
result = run_test(test_list, 80)

test_list = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""
result = run_test(test_list, 436)

test_list = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""
result = run_test(test_list, 236)

test_list = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""
result = run_test(test_list, 368)

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
result = run_test(test_list, 1206)

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
