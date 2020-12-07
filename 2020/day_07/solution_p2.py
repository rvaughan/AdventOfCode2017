#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 7 of the Advent of Code for 2020.
"""
import sys
from collections import defaultdict


rules = {}


def reset_rules():
    rules = {}


def add_rule(rule):
    parts = rule.split(' ')
    # print(parts)
    contained = []

    bag = " ".join(parts[0:3]).replace('bags', 'bag')
    # print(bag)

    pos = 4
    if parts[pos] != 'no':
        while pos < len(parts):
            number = int(parts[pos])
            pos += 1
            next_bag = " ".join(parts[pos:pos+3]).replace(',', '')
            next_bag = next_bag.replace('bags.', 'bag')
            next_bag = next_bag.replace('bags', 'bag')
            next_bag = next_bag.replace('bag.', 'bag')
            contained.append({'num': number, 'bag': next_bag})

            pos += 3

    # print(contained)

    rules[bag] = contained

    pass


def count_bags(rule):
    count = 0
    
    # print(rules[rule])

    if rule in rules:
        for sub_rule in rules[rule]:
            sub_count = count_bags(sub_rule['bag'])
            sub_count = sub_rule['num'] * (1 + sub_count)
            # print(sub_rule, '-->', sub_count)
            count += sub_count
    
    return count


def calculate_solution(rule_list):
    count = 0
    reset_rules()

    for rule in rule_list:
        add_rule(rule)

    count = count_bags("shiny gold bag")

    return count


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

reset_rules()
bag_rules = [
    "shiny gold bags contain 2 dark red bags.",
    "dark red bags contain 2 dark orange bags.",
    "dark orange bags contain 2 dark yellow bags.",
    "dark yellow bags contain 2 dark green bags.",
    "dark green bags contain 2 dark blue bags.",
    "dark blue bags contain 2 dark violet bags.",
    "dark violet bags contain no other bags."
]
run_test(bag_rules, 126)

print("")
print("-----------------")
print("All Tests PASSED.")
print("-----------------")
print("")

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

reset_rules()

with open("input.txt", "r") as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data)

    print("Solution is {0}".format(answer))
