#!/usr/bin/env python

import sys


# We know from part 1 that pos 0 is always 0 and never changes.
# Given the number of iterations brute forcing is not the best idea.
# Since we only can about pos 1 in the 'array' we can also ignore the
# array completely and not worry about manipulating it, saving additional
# runtime.
CUR_POS = 0
VAL = 0
NEXT_POS = 0
for x in xrange(1, 50000001):
    NEXT_POS = ((NEXT_POS + 304) % x) + 1

    if NEXT_POS == 1:
        VAL = x

print "The solution is {0}".format(VAL)
