#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 25 of the Advent of Code for 2022.
"""
import sys


def snafu2digit(snafu_digit: str):
    if snafu_digit.isdigit():
        return int(snafu_digit)
    elif snafu_digit == '-':
        return -1
    elif snafu_digit == '=':
        return -2
    else:
        # Sanity checking
        raise NotImplementedError


def de_snafu(number:str):
    results = 0
    for digit in number:
        results *= 5
        results += snafu2digit(digit)
    
    return results


def snafu(number: int):
    snafu = []
    translation = {-2: '=', -1: '-'}

    while number:
        number, res = divmod(number, 5)
        if res == 3:
            number += 1
            res = -2
        elif res == 4:
            number += 1
            res = -1
        
        snafu.append(res)
    
    return ''.join([str(digit) if digit >= 0 else translation[digit] for digit in reversed(snafu)])


def calculate_solution(numbers):
    result = 0

    for number in numbers:
        result += de_snafu(number)

    result = snafu(result)

    return result


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result=calculate_solution(test_input.split('\n'))

    if result != expected_solution:
        print(
            f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

assert 8 == de_snafu('2=')

assert 976 == de_snafu('2=-01')

assert 1 == de_snafu('1')
assert 2 == de_snafu('2')
assert 3 == de_snafu('1=')
assert 4 == de_snafu('1-')
assert 5 == de_snafu('10')
assert 6 == de_snafu('11')
assert 7 == de_snafu('12')
assert 8 == de_snafu('2=')
assert 9 == de_snafu('2-')
assert 10 == de_snafu('20')
assert 15 == de_snafu('1=0')
assert 20 == de_snafu('1-0')
assert 2022 == de_snafu('1=11-2')
assert 12345 == de_snafu('1-0---0')
assert 314159265 == de_snafu('1121-1110-1=0')

test_list="""1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""

result=run_test(test_list, '2=-1=0')

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data=[line.strip() for line in f]
    answer=calculate_solution(input_data)

    print(f'Solution is {answer}')
