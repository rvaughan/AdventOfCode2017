#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 9 of the Advent of Code for 2024.
"""
import sys


def calculate_solution(items):
    # Layout the files on disk
    block = 0
    disk = {}
    files = {}
    file_id = 0

    for idx, file in enumerate(items[0]):
        if idx % 2 == 0:
            # Is a file
            size = int(file)
            files[file_id] = (block, size)
            for idx in range(size):
                disk[block + idx] = file_id
            
            file_id += 1
        else:
            # Free space
            pass

        block += int(file)

    # Compact the files by shuffling complete files from the last to the first
    files_to_compact = list(range(file_id - 1, -1, -1))
    for file_id in files_to_compact:
        # Basically try and brute force find a gap big enough in the disk layout for this file.
        insert_pos = 0
        while insert_pos < files[file_id][0]:
            # Does it fit?
            if all(insert_pos + i not in disk for i in range(files[file_id][1])):
                # Yep, so we can move the file blocks here.
                for i in range(files[file_id][1]):
                    del disk[files[file_id][0] + i]
                    disk[insert_pos + i] = file_id
                break
            else:
                # Nope
                insert_pos += 1

    # Calculate checksum
    result = 0
    for block, file_id in disk.items():
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
result = run_test(test_list, 2858)

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
