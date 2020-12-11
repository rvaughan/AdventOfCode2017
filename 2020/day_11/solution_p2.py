#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 11 of the Advent of Code for 2020.
"""
import sys
from collections import defaultdict

edge_seats = {}

def find_edge(seat_map, row, col, direction, width, height):
    key = (row, col, direction)
    if key not in edge_seats:
        new_row = row
        new_col = col

        done = False
        while not done:
            if direction == 1:
                # Left-up-diagonal
                if new_row > 0 and new_col > 0:
                    new_row -= 1
                    new_col -= 1

                    if seat_map[new_row][new_col] != '.':
                        done = True
                else:
                    done = True
            elif direction == 2:
                # Up
                if new_row > 0:
                    new_row -= 1

                    if seat_map[new_row][new_col] != '.':
                        done = True
                else:
                    done = True
            elif direction == 3:
                # Right-Up-Diagonal
                if new_row > 0 and new_col < width - 1:
                    new_row -= 1
                    new_col += 1

                    if seat_map[new_row][new_col] != '.':
                        done = True
                else:
                    done = True

            elif direction == 4:
                # Left
                if new_col > 0:
                    new_col -= 1

                    if seat_map[new_row][new_col] != '.':
                        done = True
                else:
                    done = True
            elif direction == 5:
                # Left
                if new_col < width - 1:
                    new_col += 1

                    if seat_map[new_row][new_col] != '.':
                        done = True
                else:
                    done = True
            elif direction == 6:
                # Left-down-diagonal
                if new_row < height - 1 and new_col > 0:
                    new_row += 1
                    new_col -= 1

                    if seat_map[new_row][new_col] != '.':
                        done = True
                else:
                    done = True
            elif direction == 7:
                # Down
                if new_row < height - 1:
                    new_row += 1

                    if seat_map[new_row][new_col] != '.':
                        done = True
                else:
                    done = True
            elif direction == 8:
                # Right-Down-Diagonal
                if new_row < height - 1 and new_col < width - 1:
                    new_row += 1
                    new_col += 1
        
                    if seat_map[new_row][new_col] != '.':
                        done = True
                else:
                    done = True

        edge_seats[key] = (new_row, new_col)

    return edge_seats[key]


def check_seat(seat_map, row, col):
    adjacent_occupied = 0

    for direction in range(1, 9):
        seat_pos = find_edge(seat_map, row, col, direction, len(seat_map[0]), len(seat_map))

        if row == 0 and direction in [1, 2, 3]:
            continue

        if col == 0 and direction in [1, 4, 5]:
            continue

        if row == 0 and col == 0 and direction == 4:
            continue

        if col == len(seat_map[0]) - 1 and direction in [3, 5, 8]:
            continue

        if row == len(seat_map) - 1 and direction in [6, 7, 8]:
            continue

        # print(seat_pos, direction)

        # print(seat_pos, seat_map[seat_pos[0]][seat_pos[1]])
        if seat_map[seat_pos[0]][seat_pos[1]] == '#':
            adjacent_occupied += 1

    return adjacent_occupied


def calculate_solution(seat_map):
    edge_seats = {}
    num_seats = 0
    iteration = 0

    new_seat_map = []
    for row in seat_map:
        new_seat_map.append(list(row))

    tmp_seat_map = [x[:] for x in new_seat_map]

    while True:
        # if iteration == 1:
        #     print('------->')
        #     print(new_seat_map[1][0])
        #     print(check_seat(new_seat_map, 1, 0))
        #     print('<-------')
        #     boop

        num_seats = 0
        changes_made = False

        for row in range(0, len(new_seat_map)):
            for col in range(0, len(new_seat_map[0])):
                if new_seat_map[row][col] == '#':
                    num_seats += 1
                    occupied = check_seat(new_seat_map, row, col)
                    if occupied >= 5:
                        changes_made = True
                        tmp_seat_map[row][col] = 'L'
                elif seat_map[row][col] == 'L':
                    occupied = check_seat(new_seat_map, row, col)
                    if occupied == 0:
                        changes_made = True
                        tmp_seat_map[row][col] = '#'

        if not changes_made:
            break

        # iteration += 1
        # print(iteration, num_seats)
        # for row in tmp_seat_map:
        #     print("".join(row))

        new_seat_map = [x[:] for x in tmp_seat_map]

        # if iteration == 2:
        #     break
    
    return num_seats


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input)

    if result != expected_solution:
        print("Test for input {0} FAILED. Got a result of {1}, not {2}".format(test_input, result, expected_solution))
        sys.exit(-1)

    print("Test for input {0} passed.".format(test_input))

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.


# assert find_edge(0, 0, 1, 5, 5) == (0, 0)
# assert find_edge(0, 0, 2, 5, 5) == (0, 0)
# assert find_edge(0, 0, 3, 5, 5) == (0, 0)
# assert find_edge(0, 0, 4, 5, 5) == (0, 0)
# assert find_edge(0, 0, 5, 5, 5) == (0, 4)
# assert find_edge(0, 0, 6, 5, 5) == (0, 0)
# assert find_edge(0, 0, 7, 5, 5) == (4, 0)
# assert find_edge(0, 0, 8, 5, 5) == (4, 4)

# assert find_edge(3, 3, 1, 7, 7) == (0, 0)
# assert find_edge(3, 3, 2, 7, 7) == (0, 3)
# assert find_edge(3, 3, 3, 7, 7) == (0, 6)
# assert find_edge(3, 3, 4, 7, 7) == (3, 0)
# assert find_edge(3, 3, 5, 7, 7) == (3, 6)
# assert find_edge(3, 3, 6, 7, 7) == (6, 0)
# assert find_edge(3, 3, 7, 7, 7) == (6, 3)
# assert find_edge(3, 3, 8, 7, 7) == (6, 6)

# assert find_edge(3, 1, 1, 10, 10) == (2, 0)
# assert find_edge(3, 1, 2, 10, 10) == (0, 1)
# assert find_edge(3, 1, 3, 10, 10) == (0, 4)
# assert find_edge(3, 1, 4, 10, 10) == (3, 0)
# assert find_edge(3, 1, 5, 10, 10) == (3, 9)
# assert find_edge(3, 1, 6, 10, 10) == (4, 0)
# assert find_edge(3, 1, 7, 10, 10) == (9, 1)
# assert find_edge(3, 1, 8, 10, 10) == (9, 7)

puzzle_input = [
    "L.LL.LL.LL",
    "LLLLLLL.LL",
    "L.L.L..L..",
    "LLLL.LL.LL",
    "L.LL.LL.LL",
    "L.LLLLL.LL",
    "..L.L.....",
    "LLLLLLLLLL",
    "L.LLLLLL.L",
    "L.LLLLL.LL"
]
run_test(puzzle_input, 26)


print("")
print("-----------------")
print("All Tests PASSED.")
print("-----------------")
print("")

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data)

    print("Solution is {0}".format(answer))
