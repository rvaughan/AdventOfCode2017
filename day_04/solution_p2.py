#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 4 of the Advent of Code for 2017.
"""

import itertools
import sys


def has_duplicates(passphrase):
    """
    Checks to see if the passphrase is duplicated.
    """
    existing_words = {}

    for word in passphrase.split(" "):
        # Create an anagram list for the word...
        anagrams = ["".join(perm) for perm in itertools.permutations(word)]

        # Need to de-duplicate the anagram words before we check anything.
        a_words = {}
        for w in anagrams:
            if w not in a_words:
                a_words[w] = w

        # Now check each of the words
        for words in a_words:
            if words in existing_words:
                return True

            existing_words[words] = True

    return False

# Test and validation code

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

print "All tests passed."

# If we get here all tests have passed and we can solve the problem.

with open("input.txt", "r") as inputfile:
    PASSPHRASE_COUNT = 0
    VALID_PASSPHRASES = 0
    for user_passphrases in inputfile.readlines():
        PASSPHRASE_COUNT += 1
        if not has_duplicates(user_passphrases.split("\n")[0]):
            VALID_PASSPHRASES += 1

    print "Found {0} valid passphrases out of {1}".format(VALID_PASSPHRASES, PASSPHRASE_COUNT)
