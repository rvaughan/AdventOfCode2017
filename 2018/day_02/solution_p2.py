#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 2 of the Advent of Code for 2018.
"""

import itertools
import sys


def compare(id_a, id_b):
    if len(id_a) != len(id_b):
        return False, ""

    diff = 0
    result = ""
    for letter_a, letter_b in zip(id_a, id_b):
        if letter_a != letter_b:
            diff += 1
        else:
            result += letter_a

    return diff == 1, result


def do_work(my_list):
    for a, b in itertools.combinations(my_list, 2):
        result, answer = compare(a, b)
        if result:
            return a, b, answer

    return "", "", ""


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

input_text="""abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz"""

id_list = [line for line in input_text.split()]

id_a, id_b, answer = do_work(id_list)

assert id_a == 'fghij', 'id_a was incorrect, saw {} instead of {}'.format(id_a, 'fghij')
assert id_b == 'fguij', 'id_a was incorrect, saw {} instead of {}'.format(id_b, 'fguij')
assert answer == 'fgij'

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    id_list = [line for line in f]

    id_a, id_b, answer = do_work(id_list)

    print "Solution is {}, original IDs are {} and {}".format(answer, id_a, id_b)
