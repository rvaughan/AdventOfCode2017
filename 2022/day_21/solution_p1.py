#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 21 of the Advent of Code for 2022.
"""
import sys


def calculate_solution(items):
    numbers = {}
    remaining = []

    for item in items:
        parts = item.split(': ')
        if len(parts[1].split(' ')) == 1:
            numbers[parts[0]] = int(parts[1])
        else:
            remaining.append(item)

    result = 0
    done = False
    while not done:
        items = remaining.copy()
        remaining = []
        for item in items:
            parts = item.split(' ')

            if parts[1] in numbers and parts[3] in numbers:
                monkey = parts[0].replace(':', '')
                calc = ' '.join(parts[1:])

                calc = calc.replace(parts[1], str(numbers[parts[1]]))
                calc = calc.replace(parts[3], str(numbers[parts[3]]))

                value = eval(calc)
                numbers[monkey] = value

                if monkey == 'root':
                    result = value
                    done = True
            else:
                remaining.append(item)

        if len(remaining) == 0:
            result = numbers['root']
            done = True

    return int(result)


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'))

    if result != expected_solution:
        print(
            f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""

result = run_test(test_list, 152)

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
