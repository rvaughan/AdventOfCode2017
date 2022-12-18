#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 18 of the Advent of Code for 2022.
"""
from collections import deque
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


def bounds(items):
    return min(items) - 1, max(items) + 1


def calculate_solution(data):
    lava = { tuple(create_listmap(int, line.split(','))) for line in data }

    # Find the outer edges of the lava
    min_x, max_x = bounds([x for x, _, _ in lava])
    min_y, max_y = bounds([y for _, y, _ in lava])
    min_z, max_z = bounds([z for _, _, z in lava])

    # Try and work out where the water could flow
    water = set()
    queue = deque()
    queue.append((min_x, min_y, min_z))
    while queue:
        x, y, z = queue.popleft()

        # Have we already processed that position?
        if (x, y, z) in water:
            continue

        water.add((x, y, z))
        
        for dx, dy, dz in FACE_OFFSETS:
            nx, ny, nz = x + dx, y + dy, z + dz
            
            # Check that the face is not off the grid that we built.
            if not min_x <= nx <= max_x:
                continue

            if not min_y <= ny <= max_y:
                continue
            
            if not min_z <= nz <= max_z:
                continue
            
            if (nx, ny, nz) not in lava:
                queue.append((nx, ny, nz))
    
    # Rebuild the lava map, essentially removing any of the pockets of water
    # trapped within the lava.
    lava = {
        (x, y, z)
            for x in range(min_x, max_x + 1)
            for y in range(min_y, max_y + 1)
            for z in range(min_z, max_z + 1)
            if (x, y, z) not in water
    }

    # Recalculate the number of faces.
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

result = run_test(test_list, 58)

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
