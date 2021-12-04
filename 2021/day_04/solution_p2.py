#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 4 of the Advent of Code for 2021.
"""

import sys


def play(ball, board):
    for row in range(len(board)):
        for cell in range(len(board[row])):
            if board[row][cell] == ball:
                board[row][cell] = 'x'

                # Check the row
                count = 0
                for check_cell in range(len(board[row])):
                    if board[row][check_cell] == 'x':
                        count += 1

                if count == len(board[row]):
                    return True

                # Check the column
                count = 0
                for check_row in range(len(board)):
                    if board[check_row][cell] == 'x':
                        count += 1

                if count == len(board[row]):
                    return True

    return False


def play_game(balls, boards):
    last_ball = 0
    live_boards = boards.copy()
    winning_boards = []

    for ball in balls:
        tmp_boards = []
        winning_boards = []
        for board in live_boards:
            bingo = play(ball, board)
            if not bingo:
                tmp_boards.append(board)
            else:
                winning_boards.append(board)

        if len(tmp_boards) == 0 and len(winning_boards) == 1:
            last_ball = int(ball)            
            break

        live_boards = tmp_boards

    total = 0
    for row in range(len(board[0])):
        for cell in range(len(board[row])):
            if board[row][cell] != 'x':
                total += int(board[row][cell])

    return last_ball * total


def calculate_solution(input_data):
    line_no = 0
    balls_called = [x for x in input_data[line_no].split(',')]

    boards = []

    while line_no < len(input_data) - 1:
        board = []
        line_no += 1
        for _ in range(5):
            line_no += 1
            board.append([x for x in input_data[line_no].split()])

        boards.append(board)

    return play_game(balls_called, boards)


def run_test(test_input, expected_result):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution([line.strip() for line in test_input.split('\n')])

    if result != expected_result:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_result}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

result = run_test(test_input, 1924)

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
