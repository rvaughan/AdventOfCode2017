#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 4 of the Advent of Code for 2015.
"""
import hashlib
import sys

def calc_hash(input_data):
    for x in xrange(99999999999):
        hash_md5 = hashlib.md5()

        hash_input = "{}{}".format(input_data, x)

        hash_md5.update(hash_input)
        
        if hash_md5.hexdigest().startswith("000000"):
            return x

    return 0

with open("input.txt", "r") as f:
    line = f.readline()
    
    result = calc_hash(line)

    print "Solution: {}".format(result)
