#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 3 of the Advent of Code for 2024.
"""
import re
import sys


def calculate_solution(program):
    result = 0

    # For this puzzle we need to treat all of the lines as a single program.
    line = ''.join([line for line in program])

    # Create a multi select regex to cover all of the cases which we can use to
    # step through the program
    exps = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", line)
    enabled = True
    for x, y, doit, dont_doit in exps:
        if x:
            # We hit a valid mul(x,y) command...
            if enabled:
                result += int(x) * int(y)
        elif doit:
            # We hit a do() command...
            enabled = True
        elif dont_doit:
            # We hit a don't command
            enabled = False

    return result


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

test_list = """mul(44,46)"""
result = run_test(test_list, 2024)

test_list = """mul(123,4)"""
result = run_test(test_list, 492)

test_list = """mul(4*"""
result = run_test(test_list, 0)

test_list = """mul(6,9!"""
result = run_test(test_list, 0)

test_list = """?(12,34)"""
result = run_test(test_list, 0)

test_list = """mul ( 2 , 4 )"""
result = run_test(test_list, 0)

test_list = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
result = run_test(test_list, 48)

test_list = """xmul(1,1)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(1,1))don't()_mul(5,5)+mul(32,64](mul(11,8)undo()mul(1,1)"""
result = run_test(test_list, 3)

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
