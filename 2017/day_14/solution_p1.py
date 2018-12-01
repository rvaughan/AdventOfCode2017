#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 14 of the Advent of Code for 2017.
"""

import sys


###### Code from Day 10 ---->

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

    pos += skip + lengths[l_idx]
    while pos >= len(data):
        pos -= len(data)

    l_idx += 1
    skip += 1

    if l_idx < len(lengths):
        data, pos, skip = hash_data(data, lengths, pos=pos, l_idx=l_idx, skip=skip)

    return data, pos, skip


def generate_lengths(input_data):
    length_list = []
    length_list = [ord(x) for x in input_data] + [17, 31, 73, 47, 23]

    return length_list


def generate_dense_hash(d):
    final = ""

    for i in xrange(16):
        sub = d[i * 16:(i + 1) * 16]

        h = sub[0]
        for c in sub[1:]:
            h = h ^ c

        final += "{:02x}".format(h)

    return final

######### <-----


def generate_bit_hash(dense_has):
    scale = 16
    num_of_bits = 128

    bh = bin(int(dense_has, scale))[2:].zfill(num_of_bits)

    return bh


count = 0
for row in xrange(128):
    DATA = [x for x in xrange(256)]
    LENGTHS = generate_lengths("flqrgnkx-{0}".format(row))
    CUR_POS = 0
    SKIP = 0
    for rnd in xrange(64):
        DATA, CUR_POS, SKIP = hash_data(DATA, LENGTHS, pos=CUR_POS, skip=SKIP)
    dh = generate_dense_hash(DATA)
    bhash = generate_bit_hash(dh)
    count += bhash.count("1")

if count != 8108:
    print "Binary hash count check failed. {0}".format(dh)
    sys.exit(-1)
print "Tests passed."

count = 0
for row in xrange(128):
    DATA = [x for x in xrange(256)]
    LENGTHS = generate_lengths("xlqgujun-{0}".format(row))
    CUR_POS = 0
    SKIP = 0
    for rnd in xrange(64):
        DATA, CUR_POS, SKIP = hash_data(DATA, LENGTHS, pos=CUR_POS, skip=SKIP)
    dh = generate_dense_hash(DATA)
    bhash = generate_bit_hash(dh)
    count += bhash.count("1")

print count
