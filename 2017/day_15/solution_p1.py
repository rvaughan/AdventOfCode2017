#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 15 of the Advent of Code for 2017.
"""

import sys

GEN_A = 65
GEN_A_FACTOR = 16807
GEN_B = 8921
GEN_B_FACTOR = 48271

COUNT = 0
for _ in xrange(5):
    GEN_A = (GEN_A * GEN_A_FACTOR) % 2147483647
    GEN_B = (GEN_B * GEN_B_FACTOR) % 2147483647
    if GEN_A & 0xFFFF == GEN_B & 0xFFFF:
        COUNT += 1
if COUNT != 1:
    print "Test failed."
    sys.exit(-1)
print "Tests pass"

GEN_A = 618
GEN_B = 814
COUNT = 0
for _ in xrange(40000000):
    GEN_A = (GEN_A * GEN_A_FACTOR) % 2147483647
    GEN_B = (GEN_B * GEN_B_FACTOR) % 2147483647
    if GEN_A & 0xFFFF == GEN_B & 0xFFFF:
        COUNT += 1
print COUNT
