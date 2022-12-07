#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 7 of the Advent of Code for 2022.
"""
import sys


class Folder(object):
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.folders = {}
        self.files = []

    def add_folder(self, child):
        self.folders[child.name] = child

    def add_file(self, child):
        self.files.append(child)

    def calc_sizes(self):
        sizes = []
        size = 0

        # print(f'{self.name} - start')

        sub_sizes = []
        for _, sub in self.folders.items():
            sub_sizes += sub.calc_sizes()

        for x in sub_sizes:
            size += x

        for child in self.files:
            # print(f'  - {child.name} {child.size}')
            size += child.get_size()

        sizes.append(size)
        sizes += sub_sizes

        # print(f'{self.name} - {size}')

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
                # Listing directory - can ignore
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

    total_space = 70000000
    update_size = 30000000
    used_space = max(size for size in sizes)
    free_space = total_space - used_space
    space_needed = update_size - free_space

    print(total_space)
    print(used_space)
    print(update_size)
    print(free_space)
    print(space_needed)

    result = min(value for value in sizes if value >= space_needed)

    return result


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result=calculate_solution(test_input.split('\n'))

    if result != expected_solution:
        print(
            f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list="""$ cd /
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

result=run_test(test_list, 24933642)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data=[line.strip() for line in f]
    answer=calculate_solution(input_data)

    print(f'Solution is {answer}')
