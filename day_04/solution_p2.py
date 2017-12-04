#!/usr/bin/env python

import itertools
import sys


def has_duplicates(passphrase):
    existing_words = {}

    for word in passphrase.split(" "):
        anagrams = ["".join(perm) for perm in itertools.permutations(word)]

        # Need to de-duplicate the anagram words before we check anything.
        a_words = {}
        for w in anagrams:
            if w not in a_words:
                a_words[w] = w

        for words in a_words:
            if words in existing_words:
                return True

            existing_words[words] = True

    return False

if has_duplicates("abcde fghij"):
    print "Test 1 failed."
    sys.exit(-1)
print "Test 1 passed."

if not has_duplicates("abcde xyz ecdab"):
    print "Test 2 failed."
    sys.exit(-1)
print "Test 2 passed."

if has_duplicates("a ab abc abd abf abj"):
    print "Test 3 failed."
    sys.exit(-1)
print "Test 3 passed."

if has_duplicates("iiii oiii ooii oooi oooo"):
    print "Test 4 failed."
    sys.exit(-1)
print "Test 4 passed."

if not has_duplicates("oiii ioii iioi iiio"):
    print "Test 5 failed."
    sys.exit(-1)
print "Test 5 passed."

with open("input.txt", "r") as inputfile:
    passphrase_count = 0
    valid_passphrases = 0
    for passphrase in inputfile.readlines():
        passphrase_count += 1
        if not has_duplicates(passphrase.split("\n")[0]):
            valid_passphrases += 1

    print "Found {0} valid passphrases out of {1}".format(valid_passphrases, passphrase_count)
