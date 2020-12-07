#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 7 of the Advent of Code for 2020.
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


def check_rule(rule, bag_colour):
    count = 0
    
    # print(rules[rule])

    if rule in rules:
        for sub_rule in rules[rule]:
            if sub_rule['bag'] == bag_colour:
                # count += sub_rule['num']
                count += 1
            else:
                count += check_rule(sub_rule['bag'], bag_colour)
    
    return count


def calculate_solution(rule_list):
    count = 0
    reset_rules()

    for rule in rule_list:
        add_rule(rule)

    for rule in rules:
        # count += check_rule(rule, "shiny gold bag")
        bags = check_rule(rule, "shiny gold bag")
        if bags > 0:
            count += 1

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

# add_rule("light red bags contain 1 bright white bag, 2 muted yellow bags.")
# add_rule("dark orange bags contain 3 bright white bags, 4 muted yellow bags.")
# add_rule("bright white bags contain 1 shiny gold bag.")
# add_rule("muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.")
# add_rule("shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.")
# add_rule("dark olive bags contain 3 faded blue bags, 4 dotted black bags.")
# add_rule("vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.")
# add_rule("faded blue bags contain no other bags.")
# add_rule("dotted black bags contain no other bags.")

reset_rules()
questions = [
    "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags."
]
run_test(questions, 4)

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
