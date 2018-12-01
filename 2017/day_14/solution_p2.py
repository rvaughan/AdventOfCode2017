#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 14 of the Advent of Code for 2017.
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


def update_adjacent_cells(region_map, bin_hash, row=0, pos=0, region=0):
    cur_row = row
    cur_pos = pos

    if cur_row < 0 or cur_pos < 0 or cur_row > 128 or cur_pos > 128:
        return region_map

    region_map[cur_row][cur_pos] = region

    try:
        if bin_hash[cur_row][cur_pos+1] == 1 and region_map[cur_row][cur_pos+1] == 0:
            region_map = update_adjacent_cells(region_map, bin_hash, cur_row, cur_pos+1, region)
    except IndexError:
        pass

    try:
        if bin_hash[cur_row][cur_pos-1] == 1 and region_map[cur_row][cur_pos-1] == 0:
            region_map = update_adjacent_cells(region_map, bin_hash, cur_row, cur_pos-1, region)
    except IndexError:
        pass

    try:
        if bin_hash[cur_row+1][cur_pos] == 1 and region_map[cur_row+1][cur_pos] == 0:
            region_map = update_adjacent_cells(region_map, bin_hash, cur_row+1, cur_pos, region)
    except IndexError:
        pass

    try:
        if bin_hash[cur_row-1][cur_pos] == 1 and region_map[cur_row-1][cur_pos] == 0:
            region_map = update_adjacent_cells(region_map, bin_hash, cur_row-1, cur_pos, region)
    except IndexError:
        pass

    return region_map


def update_region_map(region_map, bin_hash):
    cur_row = 0
    max_region = 0

    while cur_row < 128:
        cur_pos = 0

        while cur_pos < 128:
            if bin_hash[cur_row][cur_pos] == 1 and region_map[cur_row][cur_pos] == 0:
                max_region += 1
                # print max_region, cur_row, cur_pos
                region_map = update_adjacent_cells(region_map, bin_hash, cur_row, cur_pos, max_region)

            cur_pos += 1

        cur_row += 1

    # for x in xrange(8):
    #     print bin_hash[x][:8], REGION_MAP[x][:8]

    return region_map, max_region


MAX_REGION = 0
REGION_MAP = []
BHASH_MAP = []
COUNT = 0
for ROW in xrange(128):
    DATA = [x for x in xrange(256)]
    LENGTHS = generate_lengths("flqrgnkx-{0}".format(ROW))
    CUR_POS = 0
    SKIP = 0
    for rnd in xrange(64):
        DATA, CUR_POS, SKIP = hash_data(DATA, LENGTHS, pos=CUR_POS, skip=SKIP)
    dh = generate_dense_hash(DATA)
    bhash = generate_bit_hash(dh)
    BHASH_MAP.append([int(x) for x in bhash])
    COUNT += bhash.count("1")
    REGION_MAP.append([0] * 128)
REGION_MAP, MAX_REGION = update_region_map(REGION_MAP, BHASH_MAP)
if COUNT != 8108:
    print "Binary hash count check failed. {0}".format(COUNT)
    sys.exit(-1)
if MAX_REGION != 1242:
    print "Max region check failed. {0}".format(MAX_REGION)
    sys.exit(-1)
print "Tests passed."


# If we get here then all tests have passed and we are happy.


MAX_REGION = 0
REGION_MAP = []
BHASH_MAP = []
COUNT = 0
for ROW in xrange(128):
    DATA = [x for x in xrange(256)]
    LENGTHS = generate_lengths("xlqgujun-{0}".format(ROW))
    CUR_POS = 0
    SKIP = 0
    for rnd in xrange(64):
        DATA, CUR_POS, SKIP = hash_data(DATA, LENGTHS, pos=CUR_POS, skip=SKIP)
    dh = generate_dense_hash(DATA)
    bhash = generate_bit_hash(dh)
    BHASH_MAP.append([int(x) for x in bhash])
    COUNT += bhash.count("1")
    REGION_MAP.append([0] * 128)
REGION_MAP, MAX_REGION = update_region_map(REGION_MAP, BHASH_MAP)

print MAX_REGION
