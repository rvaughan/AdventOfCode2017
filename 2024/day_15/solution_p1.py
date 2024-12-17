#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 15 of the Advent of Code for 2024.
"""
import sys


def move(grid, p, d):
    print(p,d)
    p += d
    if all([
        grid[p] != '[' or move(grid, p+1, d) and move(grid, p, d),
        grid[p] != ']' or move(grid, p-1, d) and move(grid, p, d),
        grid[p] != 'O' or move(grid, p, d), grid[p] != '#']):
            grid[p], grid[p-d] = grid[p-d], grid[p]
            return True


def calculate_solution(items):
    grid = ''
    moves = ''

    grid_mode = True
    for item in items:
        if item.strip() == '':
            grid_mode = False
            continue

        if grid_mode:
            grid += item
        else:
            moves += item

    grid = {i+j*1j:c for j,r in enumerate(grid.split())
                    for i,c in enumerate(r)}

    pos, = (p for p in grid if grid[p] == '@')

    for m in moves.replace('\n', ''):
        dir = {'<':-1, '>':+1, '^':-1j, 'v':+1j}[m]
        copy = grid.copy()

        if move(grid, pos, dir): pos += dir
        else: grid = copy

    ans = sum(pos for pos in grid if grid[pos] in 'O[')
    
    return int(ans.real + ans.imag*100)


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

test_list = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""
result = run_test(test_list, 2028)

test_list = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
result = run_test(test_list, 10092)

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
