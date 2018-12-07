#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 7 of the Advent of Code for 2018.
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


def next_step(steps, ongoing_work, current_timestep, work_time=0, dump=False):
    result = []

    for step in sorted(steps):
        if len(steps[step]) == 0:
            if step not in ongoing_work:
                for worker_id, busy_until in enumerate(workers):
                    if busy_until == 0 or busy_until < current_timestep:
                        start_time = current_timestep
                        complete_time = current_timestep + (ord(step) - 64) - 1 + work_time
                        workers[worker_id] = complete_time

                        if dump:
                            print '{:03} : Step {} starts at {} and finishes at {}'.format(current_timestep, step, start_time, complete_time)

                        ongoing_work[step] = complete_time

                        break

    tmp = ongoing_work.copy()
    for key in tmp:
        if ongoing_work[key] == current_timestep:
            update_dependants(steps, key)
            del steps[key]
            result.append(key)
            del ongoing_work[key]

    return result


def dump(steps):
    for step in sorted(steps):
        print "{} - {}".format(step, steps[step])


def dump_ongoing_work(ongoing_work):
    for work in sorted(ongoing_work):
        print "{} - {}".format(work, ongoing_work[work])


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

current_timestep = 0
workers = [0, 0]
steps = {}
ongoing_work = {}
for line in test_input.split('\n'):
    add_step(steps, line)

# dump(steps)
# assert False


# print "Current timestamp: {}".format(current_timestep)
# dump_ongoing_work(ongoing_work)

step = next_step(steps, ongoing_work, current_timestep)
assert step == [], "Saw %s not %s" % (step, [])

current_timestep += 1

# print "Current timestamp: {}".format(current_timestep)
# dump_ongoing_work(ongoing_work)

step = next_step(steps, ongoing_work, current_timestep)
assert step == [], "Saw %s not %s" % (step, [])

current_timestep += 1

# print "Current timestamp: {}".format(current_timestep)
# dump_ongoing_work(ongoing_work)

step = next_step(steps, ongoing_work, current_timestep)
assert step == ['C'], "Saw %s not %s" % (step, ['C'])

assert current_timestep == 2, "Saw %s not %s" % (current_timestep, 2)

current_timestep += 1

# dump_ongoing_work(ongoing_work)

step = next_step(steps, ongoing_work, current_timestep)
assert step == ['A'], "Saw %s not %s" % (step, ['A'])

assert current_timestep == 3, "Saw %s not %s" % (current_timestep, 3)

current_timestep += 1

step = next_step(steps, ongoing_work, current_timestep)
assert step == [], "Saw %s not %s" % (step, [])

current_timestep += 1

# dump_ongoing_work(ongoing_work)

step = next_step(steps, ongoing_work, current_timestep, True)
assert step == ['B'], "Saw %s not %s" % (step, ['B'])

assert current_timestep == 5, "Saw %s not %s" % (current_timestep, 5)

current_timestep += 1

step = next_step(steps, ongoing_work, current_timestep)
assert step == [], "Saw %s not %s" % (step, [])

current_timestep += 1

step = next_step(steps, ongoing_work, current_timestep)
assert step == [], "Saw %s not %s" % (step, [])

current_timestep += 1

step = next_step(steps, ongoing_work, current_timestep)
assert step == ['F'], "Saw %s not %s" % (step, ['F'])

assert current_timestep == 8, "Saw %s not %s" % (current_timestep, 8)

current_timestep += 1

step = next_step(steps, ongoing_work, current_timestep)
assert step == ['D'], "Saw %s not %s" % (step, ['D'])

assert current_timestep == 9, "Saw %s not %s" % (current_timestep, 9)

current_timestep += 1

step = next_step(steps, ongoing_work, current_timestep)
assert step == [], "Saw %s not %s" % (step, [])

current_timestep += 1

step = next_step(steps, ongoing_work, current_timestep)
assert step == [], "Saw %s not %s" % (step, [])

current_timestep += 1

step = next_step(steps, ongoing_work, current_timestep)
assert step == [], "Saw %s not %s" % (step, [])

current_timestep += 1

step = next_step(steps, ongoing_work, current_timestep)
assert step == [], "Saw %s not %s" % (step, [])

current_timestep += 1

step = next_step(steps, ongoing_work, current_timestep)
assert step == ['E'], "Saw %s not %s" % (step, ['E'])

assert current_timestep == 14, "Saw %s not %s" % (current_timestep, 14)

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    steps = {}
    ongoing_work = {}
    workers = [0, 0, 0, 0, 0]
    current_timestep = 0
    for line in f:
        add_step(steps, line)

    sequence = ""
    while len(steps) != 0:
        step = next_step(steps, ongoing_work, current_timestep, work_time=60)
        if step != []:
            for x in step:
                sequence += x

        current_timestep += 1

    print "Solution is {} - timesteps: {}".format(sequence, current_timestep)
