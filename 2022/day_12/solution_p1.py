#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 12 of the Advent of Code for 2022.
"""

import sys


def dump_grid(grid):
    for row in grid:
        print(''.join(row))


def calculate_solution(items):
    start = None
    destination = None

    grid = []
    searched_grid = []
    for row_idx, row in zip(range(len(items)), items):
        gr = []
        grid.append(gr)

        sgr = []
        searched_grid.append(sgr)
        for col_idx, col in zip(range(len(row)), row):
            if col == 'E':
                destination = (row_idx, col_idx)
                gr.append('z')
                sgr.append('.')
            else:
                gr.append(col)
                sgr.append('.')

            if col == 'S':
                start = (row_idx, col_idx)

    # Up, right, down, left
    check_pos = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    cur_height = 'a'
    paths = {
        0: {
            'height': cur_height,
            'finished': False,
            'path': set([start]),
            'pos': start
        }
    }

    seen_paths = set([start])

    last_path = 0
    finished = False
    while not finished:
        moved = 0

        # print('----------->')
        # print(paths)
        print(last_path, len(paths))

        # We need a copy of the paths so we can modify the underlying data during
        # the search process.
        search_paths = paths.copy()

        for path_id, path in search_paths.items():
            cur_pos = path['pos']
            cur_height = path['height']
            current_path = path['path']

            # if path_id > 7:
            #     print(cur_pos, cur_height, current_path)
            #     print(paths)
            #     x

            if path['finished']:
                print(f'{path_id} found the target')
                continue

            for check in check_pos:
                search_pos = (cur_pos[0] + check[0], cur_pos[1] + check[1])

                if search_pos[0] < 0 or search_pos[0] >= len(grid) or search_pos[1] < 0 or search_pos[1] >= len(grid[search_pos[0]]):
                    # We'd go out of the grid bounds, so ignore that move.
                    continue

                # if cur_pos[0] == 4 and cur_pos[1] == 4:
                #     print(cur_height, search_pos, grid[search_pos[0]][search_pos[1]])

                # Is it a valid move?
                if grid[search_pos[0]][search_pos[1]] <= cur_height or ord(grid[search_pos[0]][search_pos[1]]) == ord(cur_height) + 1:
                    if (search_pos[0], search_pos[1]) not in seen_paths:

                        seen_paths.add(search_pos)
                        
                        # print(search_pos)
                        searched_grid[search_pos[0]][search_pos[1]] = '*'

                        # We've found a path we've not been down previously.
                        last_path += 1
                        new_path = current_path.copy()
                        new_path.add((search_pos[0], search_pos[1]))
                        paths[last_path] = {
                            'height': grid[search_pos[0]][search_pos[1]],
                            'finished': False,
                            'path': new_path,
                            'pos': search_pos
                        }

                        if (search_pos[0], search_pos[1]) == destination:
                            paths[last_path]['finished'] = True

                            # Finish as soon as we find the destination as this
                            # is likely to be the shortest path.
                            finished = True

                        moved += 1

            # We've either found a dead-end, or added some more paths to search.
            # Either way, this path is no longer required.
            del paths[path_id]

        if moved == 0:
            finished = True

    # dump_grid(grid)
    # dump_grid(searched_grid)
    # print(paths)
    # print(last_path)

    result = 99999
    for _, path in paths.items():
        if path['finished']:
            result = min(result, len(path['path']))

    # We don't include the starting position as a move.
    return result - 1


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split())

    if result != expected_solution:
        print(
            f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

result = run_test(test_list, 31)

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
