#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 15 of the Advent of Code for 2017.
"""

import sys

def get_next_val(val=0, factor=0, modulus=0):
    while True:
        val *= factor
        val %= 2147483647
        if val % modulus == 0:
            yield val

GEN_A = 65
GEN_A_FACTOR = 16807
GEN_B = 8921
GEN_B_FACTOR = 48271

A = get_next_val(65, 16807, 4)
B = get_next_val(8921, 48271, 8)

if next(A) != 1352636452:
    print "Test A failed. {0}".format(1)
print "Test A passed."

if next(B) != 1233683848:
    print "Test B failed. {0}".format(2)
print "Test B passed."

if next(A) != 1992081072:
    print "Test A failed. {0}".format(1)
print "Test A passed."

if next(B) != 862516352:
    print "Test B failed. {0}".format(2)
print "Test B passed."

if next(A) != 530830436:
    print "Test A failed. {0}".format(1)
print "Test A passed."

if next(B) != 1159784568:
    print "Test B failed. {0}".format(2)
print "Test B passed."

if next(A) != 1980017072:
    print "Test A failed. {0}".format(1)
print "Test A passed."

if next(B) != 1616057672:
    print "Test B failed. {0}".format(2)
print "Test B passed."

if next(A) != 740335192:
    print "Test A failed. {0}".format(1)
print "Test A passed."

if next(B) != 412269392:
    print "Test B failed. {0}".format(2)
print "Test B passed."

COUNT = 0
A_VAL = 0
B_VAL = 0
A = get_next_val(65, 16807, 4)
B = get_next_val(8921, 48271, 8)
for _ in xrange(1056):
    A_VAL = next(A)
    B_VAL = next(B)
    if A_VAL & 0xFFFF == B_VAL & 0xFFFF:
        COUNT += 1
if A_VAL != 1023762912:
    print "Test A failed. {0}".format(A_VAL)
    sys.exit(-1)
print "Test A passed."
if B_VAL != 896885216:
    print "Test B failed. {0}".format(B_VAL)
    sys.exit(-1)
print "Test B passed."
if COUNT != 1:
    print "Test failed. {0}".format(COUNT)
    sys.exit(-1)
print "Tests pass"


COUNT = 0
A_VAL = 0
B_VAL = 0
A = get_next_val(618, 16807, 4)
B = get_next_val(814, 48271, 8)
for _ in xrange(5000000):
    A_VAL = next(A)
    B_VAL = next(B)
    if A_VAL & 0xFFFF == B_VAL & 0xFFFF:
        COUNT += 1
print COUNT
