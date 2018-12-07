#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 7 of the Advent of Code for 2018.
"""

from collections import Counter
import sys


def add_step(steps, input_data):
    pieces = input_data.split(' ')

    step = pieces[1]
    dependant_step = pieces[7]

    if step not in steps:
        steps[step] = []

    if dependant_step not in steps:
        steps[dependant_step] = []

    steps[dependant_step].append(step)


def update_dependants(steps, step):
    for dependant_step in steps:
        if step != dependant_step:
            if step in steps[dependant_step]:
                steps[dependant_step].remove(step)


def next_step(steps):
    for step in sorted(steps):
        if len(steps[step]) == 0:
            update_dependants(steps, step)
            del steps[step]
            return step

    return None


def dump(steps):
    for step in sorted(steps):
        print "{} - {}".format(step, steps[step])


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

print ""
print "-----------------"
print "Testing.........."
print "-----------------"
print ""

test_input="""Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""

steps = {}
for line in test_input.split('\n'):
    add_step(steps, line)

# dump(steps)
# assert False

step = next_step(steps)
assert step == 'C', "Saw %s not %s" % (step, 'C')

step = next_step(steps)
assert step == 'A', "Saw %s not %s" % (step, 'A')

step = next_step(steps)
assert step == 'B', "Saw %s not %s" % (step, 'B')

step = next_step(steps)
assert step == 'D', "Saw %s not %s" % (step, 'D')

step = next_step(steps)
assert step == 'F', "Saw %s not %s" % (step, 'F')

step = next_step(steps)
assert step == 'E', "Saw %s not %s" % (step, 'E')

step = next_step(steps)
assert step == None, "Saw %s not %s" % (step, None)

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    steps = {}
    for line in f:
        add_step(steps, line)

    sequence = ""
    step = next_step(steps)
    while step != None:
        sequence += step
        step = next_step(steps)

    print "Solution is {0}".format(sequence)
