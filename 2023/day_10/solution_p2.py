#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 10 of the Advent of Code for 2023.
"""
import sys
from queue import Queue

DIDNT_MOVE = 0
MOVED_UP = 1
MOVED_LEFT = 2
MOVED_DOWN = 3
MOVED_RIGHT = 4


def calculate_solution(field):
    start_pos = None
    grid = []
    row_idx = 0
    for row in field:
        grid.append(list(row))
        col_idx = 0
        for col in row:
            if col == 'S':
                # 0 here is used to hold the direction of travel
                start_move = (row_idx, col_idx, 0)

            col_idx += 1
        
        row_idx += 1

    # Might have to work out the 'shape' of S first, but I'm hard coding it here
    # after eye-balling the various inputs.
    if grid[start_move[0] -1][start_move[1]] == 'F':
        grid[start_move[0]][start_move[1]] = '|'
    else:
        if grid[start_move[0]][start_move[1]-1] == 'F':
            grid[start_move[0]][start_move[1]] = '7'
        else:
            grid[start_move[0]][start_move[1]] = 'F'

    # Direction of travel is 1 for up, 2 for left, 3 for down, 4 for right. 0 is
    # a special case - we haven't yet moved, so consider all directions.

    explored = {}
    paths = [[start_move]]
    moved = True
    loop = []
    start_pos = (start_move[0], start_move[1])
    while moved:
        tmp_paths = []
        moved = False
        while paths:
            next_pos = None
            cur_path = paths.pop()
            cur_pos = cur_path[-1]
            # print(cur_path, cur_pos)
            cell = grid[cur_pos[0]][cur_pos[1]]

            # Have we reached the starting point yet?
            loc = (cur_pos[0], cur_pos[1])
            if loc == start_pos and len(cur_path) > 1:
                loop = cur_path
                moved = False
                break

            # print(start_pos, loc)
            # print(cur_path)

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
                for move in next_pos:
                    tmp_paths.append(cur_path[:] + [move])
                
                    moved = True
            
            # tmp_paths.append(cur_path)

        paths = tmp_paths

    # print(loop)

    # Fun - it shows up the picture that's being draw - presumably this was the
    #       original input for the day? Otherwise it breaks things later.
    # # 'Draw' the loop in asterixs'
    # for points in loop:
    #     grid[points[0]][points[1]] = '*'
    
    # for row in grid:
    #     print(''.join(row))

    # Initial attempt - just read across and count the dots. Works for the first
    # basic test, but not the others due to the column arrangements (I think)
    # result = 0
    # for row in grid:
    #     inside = False
    #     count = 0
    #     for cell in row:
    #         if inside and cell == '.':
    #             count += 1
    #         elif cell == '*':
    #             if inside:
    #                 result += count
    #                 count = 0
                
    #             inside = not inside

    #     print(''.join(row), count, result)

    # Going to have to get a bit more adventurous and try a flood fill.
    # Ref: https://gamedev.stackexchange.com/questions/141460/how-can-i-fill-the-interior-of-a-closed-loop-on-a-tile-map

    # This code isn't needed if we expand the grid
    # # Create an empty border around the map - this allows the flood fill to catch
    # # everything around the edge of the 'map',
    # larger_map = []
    # larger_map.append(['.'] * (len(grid[0]) + 2))
    # for row in grid:
    #     larger_map.append(['.'] + row[:] + ['.'])
    # larger_map.append(['.'] * (len(grid[0]) + 2))

    # for row in larger_map:
    #     print(''.join(row))

    # Normally this would be enough. The flood would work and all is right with
    # the world. This puzzle is a little tricker though. They want you to
    # allow the flood to pass between two pipes - even if there is no gap. This
    # means that you need to pad all of the cells out. Additionally, the puzzle
    # is asking for the number of tiles enclosed - not just the empty ones, so
    # don't do anything with those tiles and pretend they are empty ground.

    new_rows = len(grid) * 3
    new_cols = len(grid[0]) * 3
    huge_map = [['.' for _ in range(new_cols)] for _ in range(new_rows)]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) not in explored:
                continue

            if grid[row][col] == '|':
                huge_map[3*row+0][3*col+1] = '*'
                huge_map[3*row+1][3*col+1] = '*'
                huge_map[3*row+2][3*col+1] = '*'
            elif grid[row][col] == '-':
                huge_map[3*row+1][3*col+0] = '*'
                huge_map[3*row+1][3*col+1] = '*'
                huge_map[3*row+1][3*col+2] = '*'
            elif grid[row][col] == '7':
                huge_map[3*row+1][3*col+0] = '*'
                huge_map[3*row+1][3*col+1] = '*'
                huge_map[3*row+2][3*col+1] = '*'
            elif grid[row][col] == 'F':
                huge_map[3*row+2][3*col+1] = '*'
                huge_map[3*row+1][3*col+1] = '*'
                huge_map[3*row+1][3*col+2] = '*'
            elif grid[row][col] == 'J':
                huge_map[3*row+1][3*col+0] = '*'
                huge_map[3*row+1][3*col+1] = '*'
                huge_map[3*row+0][3*col+1] = '*'
            elif grid[row][col] == 'L':
                huge_map[3*row+0][3*col+1] = '*'
                huge_map[3*row+1][3*col+1] = '*'
                huge_map[3*row+1][3*col+2] = '*'
            else:
                pass

    # for row in huge_map:
    #     print(''.join(row))

    # Now, flood fill the map
    q = Queue()

    i, j = 0, 0
    q.put((i, j))

    di0 = [0, 0, 1, -1]
    dj0 = [1, -1, 0, 0]

    while not q.empty():
        i, j = q.get()
        for d in range(4):
            i_next = i+di0[d]
            j_next = j+dj0[d]
            if i_next >= 0 and j_next >= 0 and i_next < len(huge_map) and j_next < len(huge_map[0]) and huge_map[i_next][j_next] == '.':
                huge_map[i_next][j_next] = ' '
                q.put((i_next, j_next))
    
    # for row in huge_map:
    #     print(''.join(row))

    # # Any remaining dots should be the ones we want
    # result = 0
    # for row in huge_map:
    #     print(''.join(row))
    #     for cell in row:
    #         if cell == '.':
    #             result += 1

    # Ok, so now we should be able to iterate over the row, 3 cells at a time
    # and look at the middle cell. If it's a dot then we count it.
    result = 0
    for row in range(1, len(huge_map), 3):
        row_data = ''
        count = 0
        for col in range(1, len(huge_map[0]), 3):
            row_data += huge_map[row][col]
            if huge_map[row][col] == '.':
                count += 1

        # print(row_data, count)
        result += count

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

test_list = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

result = run_test(test_list, 4)

test_list = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""

result = run_test(test_list, 8)

test_list = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

result = run_test(test_list, 10)

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

    # 534 is too high

    print(f'Solution is {answer}')
