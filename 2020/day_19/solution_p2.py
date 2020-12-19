#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 19 of the Advent of Code for 2020.
"""
import re
import sys
from collections import defaultdict


def check(rules, rule_num, message, start):
    rule = rules[rule_num]

    if rule[0][0][0] == '"':
        return {start + 1} if start < len(message) and  rule[0][0][1] == message[start] else set()
    else:
        endings = set()
        for subrule in rule:
            buffer = {start}
            for part in subrule:
                temp = set()
                for loc in buffer:
                    temp = temp | check(rules, part, message, loc)

                buffer = temp

            endings = endings | buffer

        return endings


def load_rules(rule_data):
    rules = {}

    for rule in rule_data:
        parts = rule.split(': ')

        rule_num = parts[0]

        content = [seq.split(' ') for seq in parts[1].split(' | ')]
        rules[rule_num] = content

    rules['8'] = [['42'],['42','8']]
    rules['11'] = [['42','31'],['42','11','31']]

    return rules


def calculate_solution(puzzle_input):
    rule_text = []
    messages = []

    cur_list = rule_text
    for line in puzzle_input:
        if line == '':
            cur_list = messages
        else:
            cur_list.append(line)

    rules = load_rules(rule_text)

    results = [len(message) in check(rules, '0', message, 0) for message in messages]

    return results.count(True)


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
    "42: 9 14 | 10 1",
    "9: 14 27 | 1 26",
    "10: 23 14 | 28 1",
    "1: \"a\"",
    "11: 42 31",
    "5: 1 14 | 15 1",
    "19: 14 1 | 14 14",
    "12: 24 14 | 19 1",
    "16: 15 1 | 14 14",
    "31: 14 17 | 1 13",
    "6: 14 14 | 1 14",
    "2: 1 24 | 14 4",
    "0: 8 11",
    "13: 14 3 | 1 12",
    "15: 1 | 14",
    "17: 14 2 | 1 7",
    "23: 25 1 | 22 14",
    "28: 16 1",
    "4: 1 1",
    "20: 14 14 | 1 15",
    "3: 5 14 | 16 1",
    "27: 1 6 | 14 18",
    "14: \"b\"",
    "21: 14 1 | 1 14",
    "25: 1 1 | 1 14",
    "22: 14 14",
    "8: 42",
    "26: 14 22 | 1 20",
    "18: 15 15",
    "7: 14 5 | 1 21",
    "24: 14 1",
    "",
    "abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa",
    "bbabbbbaabaabba",
    "babbbbaabbbbbabbbbbbaabaaabaaa",
    "aaabbbbbbaaaabaababaabababbabaaabbababababaaa",
    "bbbbbbbaaaabbbbaaabbabaaa",
    "bbbababbbbaaaaaaaabbababaaababaabab",
    "ababaaaaaabaaab",
    "ababaaaaabbbaba",
    "baabbaaaabbaaaababbaababb",
    "abbbbabbbbaaaababbbbbbaaaababb",
    "aaaaabbaabaaaaababaa",
    "aaaabbaaaabbaaa",
    "aaaabbaabbaaaaaaabbbabbbaaabbaabaaa",
    "babaaabbbaaabaababbaabababaaab",
    "aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"
]
run_test(puzzle_input, 12)


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
