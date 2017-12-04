#!/usr/bin/env python

import sys


def has_duplicates(passphrase):
    existing_words = {}
    for words in passphrase.split(" "):
        if words in existing_words:
            return True

        existing_words[words] = True

    return False

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

with open("input.txt", "r") as inputfile:
    passphrase_count = 0
    valid_passphrases = 0
    for passphrase in inputfile.readlines():
        passphrase_count += 1
        if not has_duplicates(passphrase.split("\n")[0]):
            valid_passphrases += 1

    print "Found {0} valid passphrases out of {1}".format(valid_passphrases, passphrase_count)
