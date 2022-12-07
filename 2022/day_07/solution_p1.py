#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 7 of the Advent of Code for 2022.
"""
from collections import defaultdict
import sys


def calculate_solution_abandoned(items):
    result = 0
    dir_stack = ['/']
    folder_sizes = defaultdict(int)
    folder_structure = defaultdict(set)
    current_folder = '/'

    for item in items:
        if item[0] == '$':
            # command
            cmd = item.split(' ')

            if cmd[1] == 'ls':
                # Listing directory
                folder_sizes[current_folder] = 0
            elif cmd[1] == 'cd':
                # Changing directory
                if cmd[2] == '..':
                    # We can't go back past the root directory
                    if len(dir_stack) > 1:
                        dir_stack = dir_stack[:-1]
                        current_folder = dir_stack[-1]
                elif cmd[2] == '/':
                    # Jump to the root directory
                    dir_stack = ['/']
                    current_folder = '/'
                else:
                    dir_stack.append(cmd[2])
                    current_folder = cmd[2]
        else:
            # Not a command, we're looking at a directory listing
            folder_entry = item.split(' ')
            if folder_entry[0] == 'dir':
                # Add this directory to all of its parents as well
                for f in dir_stack:
                    folder_structure[f].add(folder_entry[1])
            else:
                folder_sizes[current_folder] += int(folder_entry[0])

    for folder, size in folder_sizes.items():
        folder_size = size

        # Add all of the sub-folder sizes as well
        for sub_folder in folder_structure[folder]:
            folder_size += folder_sizes[sub_folder]

        if folder_size <= 100000:
            result += folder_size

    return result


class Folder(object):
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.folders = []
        self.files = []

    def add_folder(self, child):
        self.folders.append(child)

    def add_file(self, child):
        self.files.append(child)

    def calc_sizes(self):
        sizes = []
        size = 0

        print(f'{self.name} - start')

        sub_sizes = []
        for sub in self.folders:
            sub_sizes += sub.calc_sizes()

        for x in sub_sizes:
            size += x

        for child in self.files:
            print(f'  - {child.name} {child.size}')
            size += child.get_size()

        sizes.append(size)
        sizes += sub_sizes

        print(f'{self.name} - {size}')

        return sizes

    def get_parent(self):
        return self.parent


class File(object):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size


def calculate_solution(items):
    result = 0
    root = Folder(None, '/')
    current_folder = root

    for item in items:
        if item[0] == '$':
            # command
            cmd = item.split(' ')

            if cmd[1] == 'ls':
                # Listing directory
                pass
            elif cmd[1] == 'cd':
                # Changing directory
                if cmd[2] == '..':
                    parent = current_folder.get_parent()
                    if parent is not None:
                        current_folder = parent
                elif cmd[2] == '/':
                    # Jump to the root directory
                    current_folder = root
                else:
                    new_folder = Folder(current_folder, cmd[2])
                    current_folder.add_folder(new_folder)
                    current_folder = new_folder
        else:
            # Not a command, we're looking at a directory listing
            folder_entry = item.split(' ')
            if folder_entry[0] != 'dir':
                current_folder.add_file(
                    File(folder_entry[1], int(folder_entry[0])))

    sizes = root.calc_sizes()
    for x in sizes:
        if x < 100000:
            result += x

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

test_list = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

result = run_test(test_list, 95437)

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
