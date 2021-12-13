#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 13 of the Advent of Code for 2021.
"""

import sys
from collections import defaultdict, deque


def fold_horizontally(paper, pos):
    new_paper = defaultdict(dict)

    for x, x_val in paper.items():
        if x < pos:
            for y, y_val in x_val.items():
                new_paper[x][y] = 1
        else:
            for y, y_val in x_val.items():
                new_paper[(pos-(x-pos))][y] = 1

    return new_paper


def fold_vertically(paper, pos):
    new_paper = defaultdict(dict)

    for x, x_val in paper.items():
        for y, y_val in x_val.items():
            if y < pos:
                new_paper[x][y] = 1
            else:
                new_paper[x][(pos-(y-pos))] = 1

    return new_paper


def do_fold(paper, fold):
    direction, pos = fold.split('=')
    if direction == 'x':
        return fold_horizontally(paper, int(pos))
    else:
        return fold_vertically(paper, int(pos))


def calculate_solution(input_data):
    paper = defaultdict(dict)
    folds = []
    building_paper = True

    for line in input_data:
        if line == '':
            building_paper = False
            continue

        if building_paper:
            x, y = line.split(',')
            paper[int(x)][int(y)] = 1
        else:
            folds.append(line.split('fold along')[1].strip())

    new_paper = paper.copy()
    for fold in folds:
        new_paper = do_fold(new_paper, fold)

    count = 0
    for x, x_val in new_paper.items():
        count += len(x_val.items())

    x_keys = list(reversed(sorted(new_paper.keys())))
    for x in reversed(range(x_keys[0]+1)):
        line = ''
        y_keys = list(reversed(sorted(new_paper[x].keys())))
        if len(y_keys) > 0:
            for y in range(y_keys[0]+1):
                if y in y_keys:
                    line += '#'
                else:
                    line += '.'
        print(line)
    
    return count


def run_test(test_input, expected_value):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    input_vals = [line.strip() for line in test_input.split('\n')]
    result = calculate_solution(input_vals)

    if result != expected_value:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_value}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_input="""6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
result = run_test(test_input, 16)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    answer = calculate_solution([item.strip() for item in f])

    print(f'Solution is {answer}')
