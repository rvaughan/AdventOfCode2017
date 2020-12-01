#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 25 of the Advent of Code for 2018.
"""


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

print ""
print "-----------------"
print "Testing.........."
print "-----------------"
print ""


assert False

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [line.strip() for line in f]

    bots = load_bots(input_data)
    biggest_bot = find_biggest_bot(bots)

    in_range = find_bots_in_range(bots, biggest_bot)

    print "Solution: {}".format(len(in_range))
