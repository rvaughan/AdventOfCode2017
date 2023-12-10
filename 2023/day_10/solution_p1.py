#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 10 of the Advent of Code for 2023.
"""
import sys

DIDNT_MOVE = 0
MOVED_UP = 1
MOVED_LEFT = 2
MOVED_DOWN = 3
MOVED_RIGHT = 4


def calculate_solution(field):
    result = 0

    start_pos = None
    grid = []
    row_idx = 0
    for row in field:
        grid.append(list(row))
        col_idx = 0
        for col in row:
            if col == 'S':
                # 0 here is used to hold the direction of travel
                start_pos = (row_idx, col_idx, 0)

            col_idx += 1
        
        row_idx += 1

    # Might have to work out the 'shape' of S first, but I'm hard coding it here...
    if grid[start_pos[0] -1][start_pos[1]] == 'F':
        grid[start_pos[0]][start_pos[1]] = '|'
    else:
        grid[start_pos[0]][start_pos[1]] = 'F'

    # Direction of travel is 1 for up, 2 for left, 3 for down, 4 for right. 0 is
    # a special case - we haven't yet moved, so consider all directions.

    explored = {}
    paths = [[start_pos]]
    moved = True
    while moved:
        tmp_paths = []
        moved = False
        while paths:
            next_pos = None
            cur_path = paths.pop()
            cur_pos = cur_path[-1]
            # print(cur_path, cur_pos)
            cell = grid[cur_pos[0]][cur_pos[1]]

            # If we've already been here, ignore it
            loc = (cur_pos[0], cur_pos[1])
            if loc in explored:
                tmp_paths.append(cur_path)
                continue

            explored[loc] = True

            last_move = cur_pos[2]

            if cell == 'F':
                if last_move == DIDNT_MOVE:
                    # Can go one down, and also one to the right
                    next_pos = [(cur_pos[0]+1, cur_pos[1], MOVED_DOWN), (cur_pos[0], cur_pos[1]+1, MOVED_RIGHT)]
                elif last_move == MOVED_UP:
                    # We can only go right
                    next_pos = [(cur_pos[0], cur_pos[1]+1, MOVED_RIGHT)]
                else:
                    # We can only go down
                    next_pos = [(cur_pos[0]+1, cur_pos[1], MOVED_DOWN)]
            if cell == '|':
                if last_move == DIDNT_MOVE:
                    # Can go one up and one down
                    next_pos = [(cur_pos[0]+1, cur_pos[1], MOVED_DOWN), (cur_pos[0]-1, cur_pos[1], MOVED_UP)]
                elif last_move == MOVED_DOWN:
                    # We can only go down
                    next_pos = [(cur_pos[0]+1, cur_pos[1], MOVED_DOWN)]
                else:
                    # We can only go up
                    next_pos = [(cur_pos[0]-1, cur_pos[1], MOVED_UP)]
            elif cell == '-':
                if last_move == DIDNT_MOVE:
                    # Can go one left and one right
                    next_pos = [(cur_pos[0], cur_pos[1]-1, MOVED_LEFT), (cur_pos[0], cur_pos[1]+1, MOVED_RIGHT)]
                elif last_move == MOVED_RIGHT:
                    # We can only go left
                    next_pos = [(cur_pos[0], cur_pos[1]+1, MOVED_RIGHT)]
                else:
                    # We can only go left
                    next_pos = [(cur_pos[0], cur_pos[1]-1, MOVED_LEFT)]
            elif cell == 'L':
                if last_move == DIDNT_MOVE:
                    # Can go one up and one right
                    next_pos = [(cur_pos[0]-1, cur_pos[1]), MOVED_UP, (cur_pos[0], cur_pos[1]+1, MOVED_RIGHT)]
                elif last_move == MOVED_LEFT:
                    # We can only go up
                    next_pos = [(cur_pos[0]-1, cur_pos[1], MOVED_UP)]
                else:
                    # We can only go right
                    next_pos = [(cur_pos[0], cur_pos[1]+1, MOVED_RIGHT)]
            elif cell == 'J':
                if last_move == DIDNT_MOVE:
                    # Can go one up and one left
                    next_pos = [(cur_pos[0]-1, cur_pos[1], MOVED_UP), (cur_pos[0], cur_pos[1]-1, MOVED_LEFT)]
                elif last_move == MOVED_DOWN:
                    # We can only go left
                    next_pos = [(cur_pos[0], cur_pos[1]-1, MOVED_LEFT)]
                else:
                    # We can only go up
                    next_pos = [(cur_pos[0]-1, cur_pos[1], MOVED_UP)]
                pass
            elif cell == '7':
                if last_move == DIDNT_MOVE:
                    # Can go one up and one right
                    next_pos = [(cur_pos[0]+1, cur_pos[1], MOVED_DOWN), (cur_pos[0], cur_pos[1]-1, MOVED_LEFT)]
                elif last_move == MOVED_RIGHT:
                    # We can only go down
                    next_pos = [(cur_pos[0]+1, cur_pos[1], MOVED_DOWN)]
                else:
                    # We can only go left
                    next_pos = [(cur_pos[0], cur_pos[1]-1, MOVED_LEFT)]
            elif cell == '.':
                # Ground. We can't move to another cell from here.
                pass

            # Do we have any identified next moves?
            if next_pos is not None:
                for moves in next_pos:
                    # As long as the next proposed move has not already been explored...
                    loc = (moves[0], moves[1])
                    if loc not in explored:
                        tmp_paths.append(cur_path[:] + [moves])
                
                        moved = True
            
            tmp_paths.append(cur_path)

        paths = tmp_paths

    for path in paths:
        # print(path)
        # -1 here because we want to ignore our starting point.
        result = max(result, len(path) - 1)

    return result


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'))

    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """.....
.S-7.
.|.|.
.L-J.
....."""

result = run_test(test_list, 4)

test_list = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

result = run_test(test_list, 8)

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

    # 13636 is too high

    print(f'Solution is {answer}')
