#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 11 of the Advent of Code for 2022.
"""

import sys


def load_monkeys(monkey_data):
    monkeys = []
    monkey = {
        'inspections': 0
    }

    for line in monkey_data:
        if line == '':
            monkeys.append(monkey)
            monkey = {
                'inspections': 0
            }
            continue

        if line.startswith('Monkey'):
            monkey['id'] = int(line.split()[1].replace(':', ''))
        elif line.strip().startswith('Starting'):
            monkey['items'] = line.split(':')[1].strip().split(',')
        elif line.strip().startswith('Operation'):
            monkey['op'] = line.split(':')[1].strip()
        elif line.strip().startswith('Test'):
            monkey['test'] = int(line.split(
                ':')[1].replace('divisible by', '').strip())
        elif line.strip().startswith('If true'):
            monkey[True] = int(line.split(':')[1].strip().split()[-1])
        elif line.strip().startswith('If false'):
            monkey[False] = int(line.split(':')[1].strip().split()[-1])

    if monkey != {}:
        monkeys.append(monkey)

    return monkeys


def calc_worry(monkey, item):
    op = monkey['op']

    op = op.replace('new =', '')
    op = op.replace('old', str(item))

    return eval(op)


def calculate_solution(monkey_data):
    result = 0

    monkeys = load_monkeys(monkey_data)

    for round in range(20):
        for idx in range(len(monkeys)):
            monkey = monkeys[idx]
            items = monkey['items']
            monkeys[idx]['items'] = []
            for item in items:
                worry_level = calc_worry(monkey, item)
                worry_level = int(worry_level / 3)

                if (worry_level % monkey['test'] == 0):
                    monkeys[monkey[True]]['items'].append(worry_level)
                else:
                    monkeys[monkey[False]]['items'].append(worry_level)

                monkeys[idx]['inspections'] += 1

    total_inspections = []
    for idx in range(len(monkeys)):
        total_inspections.append(monkeys[idx]['inspections'])

    total_inspections.sort()

    result = total_inspections[-2] * total_inspections[-1]

    return result


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

test_list = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

result = run_test(test_list, 10605)

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
