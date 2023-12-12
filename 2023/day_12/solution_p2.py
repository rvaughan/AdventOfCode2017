#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 12 of the Advent of Code for 2023.
"""
from functools import lru_cache
import sys


# Need to use a cache here otherwise the code doesn't run in any kind of meaningful time.
@lru_cache
def find_combinations(cell, broken):
    # Recursively parse the string
    
    if len(cell) == 0:
        # empty cell and broken = (,) or (1,)
        return 1 if len(broken) == 0 else 0
    
    if cell.startswith("."):
        # cell is something like ".###?" (4,) so just throw away the "."
        return find_combinations(cell.strip("."), broken)
    
    if cell.startswith("?"):
        # cell is something like "?###?" (4,)
        #  so first try parsing it with a "." and then with a "#"
        # i.e. ".###?" (4,)  and then "####?" (4,)
        return find_combinations(cell.replace("?", ".", 1), broken) \
                + find_combinations(cell.replace("?", "#", 1), broken)
    
    if cell.startswith("#"):
        if len(broken) == 0:
            # There aren't any broken cells "##" (,)
            return 0
        
        if len(cell) < broken[0]:
            # There are less broken cells than we are looking for "##" (3,)
            return 0
        
        if any(c == "." for c in cell[0:broken[0]]):
            # There's a "." in the cells before we reach the number we are looking for
            # e.g. "##.???" (3,1)
            return 0
        
        if len(broken) > 1:
            # There's more than one set of broken cells left to sort out
            if len(cell) < broken[0] + 1 or cell[broken[0]] == "#":
                # If there's not enough cells remaining or the cell at the
                # first broken value is not broken...
                return 0
            
            # Otherwise we have an arrangement like "##.???" (2,1) which we can
            # move on to "???" (1,)
            return find_combinations(cell[broken[0] + 1:], broken[1:])
        else:
            # otherwise we have an arrangement like "##.???" (2,)
            # which we can move to ".???" (,)
            return find_combinations(cell[broken[0]:], broken[1:])


def calculate_solution(items):
    result = 0

    for item in items:
        parts = item.split()

        # Have to use a tuple here as list is unhashable, and the lru_cache
        # uses hashing
        broken = tuple([int(x) for x in parts[1].split(',')] * 5)

        result += find_combinations('?'.join([parts[0]] * 5), broken)
 

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

test_list = """???.### 1,1,3"""
result = run_test(test_list, 1)

test_list = """.??..??...?##. 1,1,3"""
result = run_test(test_list, 16384)

test_list = """?#?#?#?#?#?#?#? 1,3,1,6"""
result = run_test(test_list, 1)

test_list = """????.#...#... 4,1,1"""
result = run_test(test_list, 16)

test_list = """????.######..#####. 1,6,5"""
result = run_test(test_list, 2500)

test_list = """?###???????? 3,2,1"""
result = run_test(test_list, 506250)

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
