#!/usr/bin/env python

import sys


def process_garbage(data, start):
    pos = start
    garbage_count = 0

    while pos < len(data):
        c = data[pos]
        if c == ">":
            break
        if c == "!":
            pos += 2
        else:
            garbage_count += 1
            pos += 1

    return pos, garbage_count


def process_group(data, start, cur_score):
    num_groups = 1
    score = cur_score + 1
    tmp_score = 0
    garbage_count = 0

    # print "   G NS = {0}".format(score)

    pos = start
    while pos < len(data):
        c = data[pos]
        if c == "{":
            g, s, pos, gc = process_group(data, pos + 1, score)
            num_groups += g
            tmp_score += s
            garbage_count += gc
            # print "   NS = {0}".format(score)
        elif c == "<":
            pos, gc = process_garbage(data, pos + 1)
            garbage_count += gc
        elif c == "}":
            break
        else:
            pos += 1

    return num_groups, (score + tmp_score), pos + 1, garbage_count


def process_data(data):
    num_groups = 0
    score = 0
    garbage_count = 0

    pos = 0
    while pos < len(data):
        c = data[pos]
        if c == "{":
            g, s, pos, gc = process_group(data, pos + 1, score)
            num_groups += g
            score += s
            garbage_count += gc
        else:
            pos += 1

    return num_groups, score, gc


def execute_test(test_num, data, expected_num_groups, expected_score, expected_garbage_count):
    print "Test {0}...".format(test_num)
    num_groups, score, garbage_count = process_data(data)
    if num_groups != expected_num_groups:
        print "...wrong num_groups, saw {0}, but wanted {1}.".format(num_groups, expected_num_groups)
        sys.exit(-1)
    if score != expected_score:
        print "...wrong score, saw {0}, but wanted {1}.".format(score, expected_score)
        sys.exit(-1)
    if garbage_count != expected_garbage_count:
        print "...wrong garbage count, saw {0}, but wanted {1}.".format(garbage_count, expected_garbage_count)
        sys.exit(-1)
    print "...passed"


def execute_gc_test(test_num, data, expected_garbage_count):
    print "GC Test {0}...".format(test_num)
    pos, garbage_count = process_garbage(data, 1)
    if garbage_count != expected_garbage_count:
        print "...wrong garbage count, saw {0}, but wanted {1}.".format(garbage_count, expected_garbage_count)
        sys.exit(-1)
    print "...passed"


execute_test(1, "{}", 1, 1, 0)
execute_test(2, "{{{}}}", 3, 6, 0)
execute_test(3, "{{},{}}", 3, 5, 0)
execute_test(4, "{{{},{},{{}}}}", 6, 16, 0)
execute_test(5, "{<{},{},{{}}>}", 1, 1, 10)
execute_test(6, "{<a>,<a>,<a>,<a>}", 1, 1, 4)
execute_test(7, "{{<a>},{<a>},{<a>},{<a>}}", 5, 9, 4)
execute_test(8, "{{<!>},{<!>},{<!>},{<a>}}", 2, 3, 13)

execute_test(9, "{{<ab>},{<ab>},{<ab>},{<ab>}}", 5, 9, 8)
execute_test(10, "{{<!!>},{<!!>},{<!!>},{<!!>}}", 5, 9, 0)
execute_test(11, "{{<a!>},{<a!>},{<a!>},{<ab>}}", 2, 3, 17)

execute_gc_test(1, "<>", 0)
execute_gc_test(2, "<random characters>", 17)
execute_gc_test(3, "<<<<>", 3)
execute_gc_test(4, "<{!>}>", 2)
execute_gc_test(5, "<!!>", 0)
execute_gc_test(6, "<!!!>>", 0)
execute_gc_test(7, "<{o\"i!a,<{i<a>", 10)

with open("input.txt", "r") as f:
    data = f.read()

    num_groups, score, garbage_count = process_data(data)

    print num_groups, score, garbage_count
