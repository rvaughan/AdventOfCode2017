#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 8 of the Advent of Code for 2021.
"""

import sys
from collections import defaultdict


def calc_overlap(a, b):
    result = 0

    for c in b:
        if c in a:
            result += 1

    return ((result == len(a)) and (len(a) == len(b))), result


def find_digits(input):
    result = ''

    digits = {}

    parts = input.split('|')
    output = parts[0].split()
    for o in output:
        if len(o) == 2: # Digit 1
            digits[1] = o
        elif len(o) == 3: # Digit 7
            digits[7] = o
        elif len(o) == 4: # Digit 4
            digits[4] = o
        elif len(o) == 7: # Digit 8
            digits[8] = o

    print(digits)

    output = parts[1].split()
    for o in output:
        if len(o) == 2: # Digit 1
            digits[1] = o
            result += '1'
            continue
        elif len(o) == 3: # Digit 7
            digits[7] = o
            result += '7'
            continue
        elif len(o) == 4: # Digit 4
            digits[4] = o
            result += '4'
            continue
        elif len(o) == 5:
            _, num_overlap = calc_overlap(digits[1], o)
            if num_overlap == 2:
                result += '3'
                continue
            else:
                _, num_overlap = calc_overlap(digits[4], o)
                if num_overlap == 3:
                    result += '5'
                    continue
                else:
                    result += '2'
                    continue
        elif len(o) == 6: # Digit 0
            _, num_overlap = calc_overlap(digits[8], o)
            if num_overlap == 6:
                _, num_overlap = calc_overlap(digits[1], o)
                if num_overlap == 2:
                    _, num_overlap = calc_overlap(digits[4], o)
                    if num_overlap == 4:
                        # It's a zero
                        result += '9'
                        continue
                    else:
                        # It's a zero
                        result += '0'
                        continue
                else:
                    result += '6'
                    continue
        elif len(o) == 7: # Digit 8
            digits[8] = o
            result += '8'
            continue

    return int(result)


def calculate_solution(input_data):
    result = 0
    for row in input_data:
        result += find_digits(row)

    return result


def run_test(test_input, expected_value):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution([item for item in test_input.split('\n')])

    if result != expected_value:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_value}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_input = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"
result = find_digits(test_input)
assert result == 8394, result
result = run_test(test_input, 8394)

test_input = "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc"
result = find_digits(test_input)
assert result == 9781, result
result = run_test(test_input, 9781)

test_input = "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg"
result = find_digits(test_input)
assert result == 1197, result
result = run_test(test_input, 1197)

test_input = "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb"
result = find_digits(test_input)
assert result == 9361, result
result = run_test(test_input, 9361)

test_input = "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea"
result = find_digits(test_input)
assert result == 4873, result
result = run_test(test_input, 4873)

test_input = "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb"
result = find_digits(test_input)
assert result == 8418, result
result = run_test(test_input, 8418)

test_input = "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe"
result = find_digits(test_input)
assert result == 4548, result
result = run_test(test_input, 4548)

test_input = "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef"
result = find_digits(test_input)
assert result == 1625, result
result = run_test(test_input, 1625)

test_input = "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb"
result = find_digits(test_input)
assert result == 8717, result
result = run_test(test_input, 8717)

test_input = "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
result = find_digits(test_input)
assert result == 4315, result
result = run_test(test_input, 4315)

test_input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
result = run_test(test_input, 61229)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data = [item for item in f]
    answer = calculate_solution(input_data)

    print(f'Solution is {answer}')
