#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 3 of the Advent of Code for 2020.
"""
import sys


def calculate_solution(map, right, down):
    cur_row = 0
    cur_col = 0
    count = 0
    width = len(map[0])

    while cur_row < len(map):
        if map[cur_row][cur_col] == "#":
            count += 1
        elif map[cur_row][cur_col] != ".":
            # Used this to detect if we were accidentally going
            # past the end of the data in the row.
            print(cur_row, cur_col, count)
            print('Boom!')
            sys.exit(-1)

        cur_row += down
        cur_col += right

        if cur_col >= width:
            # old_col = cur_col
            cur_col -= width
            # print('  ** {} --> {} : [{}]'.format(old_col, cur_col, len(map[cur_row])))

    return count


def run_test(test_input, right, down, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input, right, down)

    if result != expected_solution:
        print("Test for input {0} FAILED. Got a result of {1}, not {2}".format(test_input, result, expected_solution))
        sys.exit(-1)

    print("Test for input {0} passed.".format(test_input))

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#"
]

result = run_test(test_list, 3, 1, 7)

movements = [
    [1, 1, 2],
    [3, 1, 7],
    [5, 1, 3],
    [7, 1, 4],
    [1, 2, 2]
]

result = 0
for x in movements:
    answer = calculate_solution(test_list, x[0], x[1])
    assert answer == x[2]
    if result == 0:
        result = answer
    else:
        result *= answer
assert result == 336

print("")
print("-----------------")
print("All Tests PASSED.")
print("-----------------")
print("")

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [line.strip() for line in f]

    result = 0
    for x in movements:
        answer = calculate_solution(input_data, x[0], x[1])
        if result == 0:
            result = answer
        else:
            result *= answer

    print("Solution is {0}".format(result))
