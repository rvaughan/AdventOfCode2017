#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 9 of the Advent of Code for 2024.
"""
import sys


def calculate_solution(items):
    # Layout the files on disk
    block = 0
    disk = {}
    file_id = 0

    for idx, file in enumerate(items[0]):
        if idx % 2 == 0:
            # Is a file
            for idx in range(int(file)):
                disk[block + idx] = file_id
            
            file_id += 1
        else:
            # Free space
            pass

        block += int(file)

    # Compact the files by shuffling everything from the right to the left
    new_disk = disk.copy()
    left = 0
    # Find the rightmost block used on the disk...
    right = max(new_disk.keys())
    while left < right:
        if right in new_disk:
            file_id = new_disk[right]
            del new_disk[right]
            
            while left in new_disk:
                left += 1
            
            new_disk[left] = file_id
        
        right -= 1

    # Calculate checksum
    result = 0
    for block, file_id in new_disk.items():
        result += block * file_id

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

test_list = """2333133121414131402"""
result = run_test(test_list, 1928)

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
