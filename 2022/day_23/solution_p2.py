#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 23 of the Advent of Code for 2022.
"""
from collections import Counter
import sys


def calculate_solution(items):
    locations = set()
    for i in range(len(items)):
        line = items[i]
    
        for j, ch in enumerate(line):
            if ch == '#':
                locations.add((i, j))

    stay_still = lambda x, y, locations: all([(x+dx, y+dy) not in locations for (dx, dy) in [(-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0)]])
    
    checks = [
        lambda x, y, locations: all([(x+dx, y+dy) not in locations for (dx, dy) in [(-1, -1), (-1, 0), (-1, 1)]]) and (x - 1, y + 0), # N
        lambda x, y, locations: all([(x+dx, y+dy) not in locations for (dx, dy) in [(1, -1), (1, 0), (1, 1)]]) and (x + 1, y + 0), # S
        lambda x, y, locations: all([(x+dx, y+dy) not in locations for (dx, dy) in [(-1, -1), (0, -1), (1, -1)]]) and (x + 0, y - 1), # W
        lambda x, y, locations: all([(x+dx, y+dy) not in locations for (dx, dy) in [(-1, 1), (0, 1), (1, 1)]]) and (x + 0, y + 1), # E
    ]
    
    old_locations = locations.copy()

    round = 0
    while True:
        round += 1

        proposals = {}
        for location in locations:
            if stay_still(location[0], location[1], locations):
                proposals[location] = location
                continue
            
            for check in checks:
                direction = check(location[0], location[1], locations)
                if direction:
                    proposals[location] = direction
                    break
            
            if location not in proposals:
                proposals[location] = location

        valid_targets = set(x[0] for x in Counter(proposals.values()).items() if x[1] == 1)
        filtered_proposals = dict([(x, y) for (x, y) in proposals.items() if y in valid_targets])
        filtered_proposals = dict([(x, y) for (x, y) in filtered_proposals.items() if x != y])

        locations = locations.difference(filtered_proposals.keys())
        locations.update(filtered_proposals.values())

        if old_locations == locations:
            break

        old_locations = locations.copy()

        checks.append(checks.pop(0))
        
    return round


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

test_list = """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#.."""

result = run_test(test_list, 20)

test_list = """..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
.............."""

result = run_test(test_list, 20)

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
