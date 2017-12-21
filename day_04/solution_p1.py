#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 4 of the Advent of Code for 2017.
"""

import sys


def has_duplicates(passphrase):
    existing_words = {}
    for words in passphrase.split(" "):
        if words in existing_words:
            return True

        existing_words[words] = True

    return False

# Test code

if has_duplicates("aa bb cc dd ee"):
    print "Test 1 failed."
    sys.exit(-1)
print "Test 1 passed."

if not has_duplicates("aa bb cc dd aa"):
    print "Test 2 failed."
    sys.exit(-1)
print "Test 2 passed."

if has_duplicates("aa bb cc dd aaa"):
    print "Test 3 failed."
    sys.exit(-1)
print "Test 3 passed."

print "All tests passed."

# Solution code goes here.

with open("input.txt", "r") as inputfile:
    PASSPHRASE_COUNT = 0
    VALID_PASSPHRASES = 0
    for passphrase in inputfile.readlines():
        PASSPHRASE_COUNT += 1
        if not has_duplicates(passphrase.split("\n")[0]):
            VALID_PASSPHRASES += 1

    print "Found {0} valid passphrases out of {1}".format(VALID_PASSPHRASES, PASSPHRASE_COUNT)
