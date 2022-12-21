#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 21 of the Advent of Code for 2022.
"""
import sys


def parse(task_input):
    for line in task_input:
        first_monkey = line.split(': ')[0]
        s = line.split(': ')[1].split(' ')
        
        yield first_monkey, int(s[0]) if len(s) == 1 else list(s)

    return


def find_value_monkey(lines, requested_monkey_name):
    for monkey_name, monkey_instruction in lines:
        if monkey_name == requested_monkey_name:
            if isinstance(monkey_instruction, list):
                if monkey_instruction[1] == '+':
                    operation = lambda x, y: x + y
                if monkey_instruction[1] == '*':
                    operation = lambda x, y: x * y
                if monkey_instruction[1] == '-':
                    operation = lambda x, y: x - y
                if monkey_instruction[1] == '/':
                    operation = lambda x, y: x // y

                x = find_value_monkey(lines, monkey_instruction[0])
                y = find_value_monkey(lines, monkey_instruction[2])
                
                if x == None or y == None:
                    return None

                return operation(x, y)
            else:
                return monkey_instruction

    return None


def seek(lines, seek_value, monkey_name):
    if monkey_name == 'humn':
        return seek_value

    root = [l for l in lines if l[0] == monkey_name][0][1]
    if not isinstance(root, list):
        raise Exception('')

    x = find_value_monkey(lines, root[0])
    y = find_value_monkey(lines, root[2])

    if x == None:
        if root[1] == '+':
            seek_value -= y
        elif root[1] == '-': # x - y == seek_value
            seek_value += y
        elif root[1] == '*': 
            seek_value //= y
        elif root[1] == '/': # x // y == seek_value
            seek_value *= y

        return seek(lines, seek_value, root[0])
    else:
        if root[1] == '+':
            seek_value -= x
        elif root[1] == '-': # x - y == seek_value
            seek_value = x - seek_value
        elif root[1] == '*': 
            seek_value //= x
        elif root[1] == '/': # x // y == seek_value
            seek_value = x // seek_value

        return seek(lines, seek_value, root[2])


def calculate_solution(task_input):
    lines = list(parse(task_input))
    lines = [l for l in lines if l[0] != 'humn']

    root = [l for l in lines if l[0] == 'root'][0][1]
    x = find_value_monkey(lines, root[0])
    y = find_value_monkey(lines, root[2])

    # If the result is None then we've found the path where the humn is.
    if x == None:
        return seek(lines, y, root[0])
    else: 
        return seek(lines, x, root[2])


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

result = run_test(test_list, 301)

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
