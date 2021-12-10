#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 10 of the Advent of Code for 2021.
"""

import sys
from collections import defaultdict, deque

open_brackets = ['(', '{', '[', '<']
close_brackets = [')', '}', ']', '>']
lookup = {
    '[': ']',
    '(': ')',
    '{': '}',
    '<': '>'
}
costs = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}


def calc_score(line):
    brackets = deque()

    for x in line:
        if x in open_brackets:
            brackets.append(x)
        elif x in close_brackets:
            brackets.pop()

    score = 0
    while len(brackets) > 0:
        closer = brackets.pop()

        score = (5 * score) + costs[closer]

    return score


def calc_error_score(data):
    brackets = deque()

    for x in data:
        if x in open_brackets:
            brackets.append(x)
        elif x in close_brackets:
            cur = brackets.pop()
            if lookup[cur] != x:
                if x == ')':
                    return 3
                elif x == ']':
                    return 57
                elif x == '}':
                    return 1197
                elif x == '>':
                    return 25137

    return 0


def calculate_solution(input_data):
    result = 0
    valid = []

    for line in input_data:
        error = calc_error_score(line)
        if error == 0:
            valid.append(line)
    
    scores = []
    for line in valid:
        scores.append(calc_score(line))

    scores.sort()

    result = scores[int(len(scores) / 2)]

    return result


def run_test(test_input, expected_value):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution([item.strip() for item in test_input.split('\n')])

    if result != expected_value:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_value}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.


test_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
result = run_test(test_input, 288957)

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
