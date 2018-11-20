#!/usr/bin/env python

import sys


def add_value(buffer, val, cur_pos=0, steps=3):
    next_pos = cur_pos
    for _ in xrange(steps):
        next_pos += 1
        if next_pos == len(buffer):
            next_pos = 0

    # print buffer

    buffer[next_pos+1:] = buffer[next_pos:]

    # print buffer, next_pos, val

    next_pos += 1
    buffer[next_pos] = val

    # print buffer, next_pos, val

    return buffer, next_pos

CUR_POS = 0
BUFFER = [0] * 1
BUFFER, CUR_POS = add_value(BUFFER, 1, CUR_POS)
if BUFFER[1] != 1:
    print "Test 1 failed."
    sys.exit(-1)
print "Test 1 passed"

BUFFER, CUR_POS = add_value(BUFFER, 2, CUR_POS)
if BUFFER[1] != 2:
    print "Test 2 failed."
    sys.exit(-1)
print "Test 2 passed"

BUFFER, CUR_POS = add_value(BUFFER, 3, CUR_POS)
if BUFFER[2] != 3:
    print "Test 3 failed."
    sys.exit(-1)
print "Test 3 passed"

BUFFER, CUR_POS = add_value(BUFFER, 4, CUR_POS)
if BUFFER[2] != 4:
    print "Test 4 failed."
    sys.exit(-1)
print "Test 4 passed"

CUR_POS = 0
BUFFER = [0] * 1
for x in xrange(2017):
    BUFFER, CUR_POS = add_value(BUFFER, x+1, CUR_POS)
if BUFFER[CUR_POS-1] != 151:
    print "Test 5(1) failed."
    sys.exit(-1)
if BUFFER[CUR_POS] != 2017:
    print "Test 5(2) failed."
    sys.exit(-1)
if BUFFER[CUR_POS+1] != 638:
    print "Test 5(3) failed."
    sys.exit(-1)
print "Test 5 passed."

print "All Tests passed."

# ALL TESTS PASSED

CUR_POS = 0
BUFFER = [0] * 1
for x in xrange(2017):
    BUFFER, CUR_POS = add_value(BUFFER, x+1, cur_pos=CUR_POS, steps=304)

print "The solution is {0}".format(BUFFER[CUR_POS+1])
