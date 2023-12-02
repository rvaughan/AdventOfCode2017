#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 2 of the Advent of Code for 2023.
"""
import sys


def check_game(game_data, red, green, blue):
    game_parts = game_data.split('Game ')[1].split(':')
    
    game_num = int(game_parts[0])

    pulls = game_parts[1].split(';')
    for pull in pulls:
        for balls in pull.split(','):
            count, colour = balls.split()
            if colour == 'red':
                if int(count) > red:
                    return 0

            if colour == 'blue':
                if int(count) > blue:
                    return 0

            if colour == 'green':
                if int(count) > green:
                    return 0

    return game_num

def calculate_solution(items, red, green, blue):
    results = 0

    for item in items:
        if item.strip() == '':
            continue

        results += check_game(item, red, green, blue)

    return results


def run_test(test_input, red, green, blue, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'), red, green, blue)

    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
"""
result = run_test(test_list, 12, 13, 14, 1)

test_list = """
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
"""
result = run_test(test_list, 12, 13, 14, 2)

test_list = """
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
"""
result = run_test(test_list, 12, 13, 14, 0)

test_list = """
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
"""
result = run_test(test_list, 12, 13, 14, 0)

test_list = """
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
result = run_test(test_list, 12, 13, 14, 5)

test_list = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

result = run_test(test_list, 12, 13, 14, 8)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data, 12, 13, 14)

    print(f'Solution is {answer}')
