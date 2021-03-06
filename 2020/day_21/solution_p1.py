#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 21 of the Advent of Code for 2020.
"""
import re
import sys
from collections import defaultdict



def calculate_solution(puzzle_input):
    ingredients = defaultdict(int)
    allergens = {}

    for line in puzzle_input:
        parts = line.split('(contains')

        tmp_ingredients = [x.strip() for x in parts[0].strip().split(' ')]
        tmp_allergens = [x.replace(')', '').strip() for x in parts[1].strip().split(',')]

        for i in tmp_ingredients:
            ingredients[i] += 1
    
        for a in tmp_allergens:
            for i in tmp_ingredients:
                if a not in allergens:
                    allergens[a] = defaultdict(int)
                
                allergens[a][i] += 1
    
    for a in allergens:
        max = 0
        for i in allergens[a]:
            if allergens[a][i] > max:
                max = allergens[a][i]

        reap_list = []
        for i in allergens[a]:
            if allergens[a][i] < max:
                reap_list.append(i)

        for r in reap_list:
            del allergens[a][r]
    
    # for a in allergens:
    #     for i in allergens[a]:
    #         print(a, i)
    # print(ingredients)

    safe_list = {}
    for i in ingredients:
        found = False
        for a in allergens:
            if i in allergens[a]:
                found = True

        if not found:
            safe_list[i] = ingredients[i]

    # print(safe_list)

    result = 0
    for i in safe_list:
        result += safe_list[i]

    return result


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


puzzle_input = [
    "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)",
    "trh fvjkl sbzzf mxmxvkd (contains dairy)",
    "sqjhc fvjkl (contains soy)",
    "sqjhc mxmxvkd sbzzf (contains fish)"
]
run_test(puzzle_input, 5)


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
