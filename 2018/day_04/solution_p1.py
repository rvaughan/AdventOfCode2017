#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 4 of the Advent of Code for 2018.
"""

from datetime import datetime
import sys


def add_line_to_store(store, line):
    pieces = line.split(']')

    dt = datetime.strptime(pieces[0][1:], "%Y-%m-%d %H:%M")

    store[dt] = pieces[1].strip()


def calc_patterns(store):
    guard_num = 0
    current_day = []
    asleep_start = 0
    asleep_end = 0

    guard_patterns = {}

    for k in sorted(store):
        pieces = store[k].split(' ')
        if pieces[0] == 'Guard':
            if len(current_day) != 0:
                guard_patterns[guard_num].append(current_day)

            guard_num = int(pieces[1].split('#')[1])
            current_day = ['.'] * 60

            if guard_num not in guard_patterns:
                guard_patterns[guard_num] = []
        elif pieces[0] == 'falls':
            asleep_start = k.minute
        else:
            asleep_end = k.minute
            # print "Guard %d sleeps from %d to %d" % (guard_num, asleep_start, asleep_end)

            for min in xrange(asleep_start, asleep_end):
                current_day[min] = "#"

    return guard_patterns


def calc_most_asleep_time(patterns):
    sleep_pattern = [0] * 60

    for day in patterns:
        for min in xrange(len(day)):
            if day[min] == "#":
                sleep_pattern[min] += 1

    # print sleep_pattern

    max = 0
    sleepy_min = 0
    for x, min in zip(xrange(len(sleep_pattern)), sleep_pattern):
        if min > max:
            max = min
            sleepy_min = x

    return sleepy_min


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_input="""[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""

ordered_store = {}
for line in test_input.split('\n'):
    add_line_to_store(ordered_store, line)

guard_patterns = calc_patterns(ordered_store)

sleepy_guard = 0
max_asleep = 0
for guard_num in guard_patterns:
    asleep_time = 0

    for day in guard_patterns[guard_num]:
        for min in day:
            if min == "#":
                asleep_time += 1

    if asleep_time > max_asleep:
        max_asleep = asleep_time
        sleepy_guard = guard_num

assert sleepy_guard == 10, "Incorrectly identified %d as the sleepy guard" % sleepy_guard

sleepy_minute = calc_most_asleep_time(guard_patterns[10])

assert sleepy_minute == 24, "Incorrectly identified %d as the sleepy time" % sleepy_minute

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:

    ordered_store = {}
    for line in f:
        add_line_to_store(ordered_store, line)

    guard_patterns = calc_patterns(ordered_store)

    sleepy_guard = 0
    max_asleep = 0
    for guard_num in guard_patterns:
        asleep_time = 0

        for day in guard_patterns[guard_num]:
            for min in day:
                if min == "#":
                    asleep_time += 1

        if asleep_time > max_asleep:
            max_asleep = asleep_time
            sleepy_guard = guard_num

    sleepy_minute = calc_most_asleep_time(guard_patterns[sleepy_guard])

    print "Solution is {0}".format(sleepy_guard * sleepy_minute)
