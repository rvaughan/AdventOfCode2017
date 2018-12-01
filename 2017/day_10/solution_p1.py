#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 10 of the Advent of Code for 2017.
"""

import sys


def get_sublist(data, pos, length):
    sub_list = [0] * length
    count = 0
    cur_pos = pos
    while count < length:
        sub_list[count] = data[cur_pos]

        cur_pos += 1
        if cur_pos == len(data):
            cur_pos = 0

        count += 1

    return [x for x in reversed(sub_list)]


def apply_sublist(data, pos, sub_list):
    count = 0
    cur_pos = pos
    while count < len(sub_list):
        data[cur_pos] = sub_list[count]

        cur_pos += 1
        if cur_pos == len(data):
            cur_pos = 0

        count += 1

    return data


def hash_data(data, lengths, pos=0, l_idx=0, skip=0):

    sub_list = get_sublist(data, pos, lengths[l_idx])

    data = apply_sublist(data, pos, sub_list)

    jump = skip + lengths[l_idx]
    pos += skip + lengths[l_idx]
    if pos >= len(data):
        pos -= len(data)

    l_idx += 1
    skip += 1

    if l_idx < len(lengths):
        data = hash_data(data, lengths, pos, l_idx, skip)

    return data


data = [x for x in xrange(5)]
lengths = [3, 4, 1, 5]
result = hash_data(data, lengths)

if result[0] != 3:
    print "Text failed."
    sys.exit(-1)
if result[1] != 4:
    print "Text failed."
    sys.exit(-1)

# If we get here then we've some confidence that the code is ok...

data = [x for x in xrange(256)]
with open("input.txt", "r") as f:
    length_data = f.readline()
    lengths = [int(x) for x in length_data.split(",")]
    result = hash_data(data, lengths)

    print result

    print result[0] * result[1]
