#!/usr/bin/env python

import sys

def process_garbage(data, start):
    pos = start
    while pos < len(data):
        c = data[pos]
        if c == ">":
            break
        if c == "!":
            pos += 2
        else:
            pos += 1

    return pos

def process_group(data, start, cur_score):
    num_groups = 1
    score = cur_score + 1
    tmp_score = 0

    # print "   G NS = {0}".format(score)

    pos = start
    while pos < len(data):
        c = data[pos]
        if c == "{":
            g, s, pos = process_group(data, pos + 1, score)
            num_groups += g
            tmp_score += s
            # print "   NS = {0}".format(score)
        elif c == "<":
            pos = process_garbage(data, pos + 1)
        elif c == "}":
            break
        else:
            pos += 1

    return num_groups, (score + tmp_score), pos + 1


def process_data(data):
    num_groups = 0
    score = 0

    pos = 0
    while pos < len(data):
        c = data[pos]
        if c == "{":
            g, s, pos = process_group(data, pos + 1, score)
            num_groups += g
            score += s
        else:
            pos += 1

    return num_groups, score


def execute_test(test_num, data, expected_num_groups, expected_score):
    print "Test {0}...".format(test_num)
    num_groups, score = process_data(data)
    if num_groups != expected_num_groups:
        print "...wrong num_groups, saw {0}, but wanted {1}.".format(num_groups, expected_num_groups)
        sys.exit(-1)
    if score != expected_score:
        print "...wrong score, saw {0}, but wanted {1}.".format(score, expected_score)
        sys.exit(-1)
    print "...passed"

execute_test(1, "{}", 1, 1)
execute_test(2, "{{{}}}", 3, 6)
execute_test(3, "{{},{}}", 3, 5)
execute_test(4, "{{{},{},{{}}}}", 6, 16)
execute_test(5, "{<{},{},{{}}>}", 1, 1)
execute_test(6, "{<a>,<a>,<a>,<a>}", 1, 1)
execute_test(7, "{{<a>},{<a>},{<a>},{<a>}}", 5, 9)
execute_test(8, "{{<!>},{<!>},{<!>},{<a>}}", 2, 3)

execute_test(9, "{{<ab>},{<ab>},{<ab>},{<ab>}}", 5, 9)
execute_test(10, "{{<!!>},{<!!>},{<!!>},{<!!>}}", 5, 9)
execute_test(11, "{{<a!>},{<a!>},{<a!>},{<ab>}}", 2, 3)

with open("input.txt", "r") as f:
    data = f.read()

    num_groups, score = process_data(data)

    print num_groups, score
