#!/usr/bin/env python

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


test_lengths = generate_lengths("1,2,3")
test_result = [49,44,50,44,51,17,31,73,47,23]
for tv, val in zip(test_result, test_lengths):
    if tv != val:
        print "Check failed"
        print tv
        print val
        sys.exit(-1)
print "Length check passed."


DATA = [x for x in xrange(256)]
LENGTHS = generate_lengths("")
CUR_POS = 0
SKIP = 0
for rnd in xrange(64):
    DATA, CUR_POS, SKIP = hash_data(DATA, LENGTHS, pos=CUR_POS, skip=SKIP)
dh = generate_dense_hash(DATA)
if dh != "a2582a3a0e66e6e86e3812dcb672a272":
    print "Empty string dense hash check failed. {0}".format(dh)
    sys.exit(-1)


DATA = [x for x in xrange(256)]
LENGTHS = generate_lengths("AoC 2017")
CUR_POS = 0
SKIP = 0
for rnd in xrange(64):
    DATA, CUR_POS, SKIP = hash_data(DATA, LENGTHS, pos=CUR_POS, skip=SKIP)
dh = generate_dense_hash(DATA)
if dh != "33efeb34ea91902bb2f59c9920caa6cd":
    print "'AoC 2017' string dense hash check failed. {0}".format(dh)
    sys.exit(-1)


DATA = [x for x in xrange(256)]
LENGTHS = generate_lengths("1,2,3")
CUR_POS = 0
SKIP = 0
for rnd in xrange(64):
    DATA, CUR_POS, SKIP = hash_data(DATA, LENGTHS, pos=CUR_POS, skip=SKIP)
dh = generate_dense_hash(DATA)
if dh != "3efbe78a8d82f29979031a4aa0b16a9d":
    print "'1,2,3' string dense hash check failed. {0}".format(dh)
    sys.exit(-1)


DATA = [x for x in xrange(256)]
LENGTHS = generate_lengths("1,2,4")
CUR_POS = 0
SKIP = 0
for rnd in xrange(64):
    DATA, CUR_POS, SKIP = hash_data(DATA, LENGTHS, pos=CUR_POS, skip=SKIP)
dh = generate_dense_hash(DATA)
if dh != "63960835bcdc130f0b66d7ff4f6a5a8e":
    print "'1,2,4' string dense hash check failed. {0}".format(dh)
    sys.exit(-1)


print "*** ALL TESTS PASSED ***"

# If we get here then we've some confidence that the code is ok...

DATA = [x for x in xrange(256)]
with open("input.txt", "r") as f:
    length_data = f.readline()
    LENGTHS = generate_lengths(length_data.strip())
    CUR_POS = 0
    SKIP = 0
    for rnd in xrange(64):
        DATA, CUR_POS, SKIP = hash_data(DATA, LENGTHS, pos=CUR_POS, skip=SKIP)

    print generate_dense_hash(DATA)
