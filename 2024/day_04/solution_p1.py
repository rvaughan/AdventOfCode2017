#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 4 of the Advent of Code for 2024.
"""
import sys


def calculate_solution(items):
    result = 0

    grid = { ( x, y ): col
        for y, row in enumerate( items )
        for x, col in enumerate( row.strip( '\n' ) ) }
    xh, yh = max( grid.keys() )

    result = sum( "XMAS" == "".join( grid.get( ( x + dx * n, y + dy * n ), "" )
                               for n in range( 4 ) )
            for y in range( yh + 1 )
            for x in range( xh + 1 )
            for dx in ( -1, 0, 1 )
            for dy in ( -1, 0, 1 ) )

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

test_list = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
result = run_test(test_list, 18)

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
