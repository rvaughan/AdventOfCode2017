#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 4 of the Advent of Code for 2018.
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

    guard_patterns[guard_num].append(current_day)

    return guard_patterns


def calc_most_asleep_time(patterns):
    sleep_pattern = [0] * 60

    for day in patterns:
        for min in xrange(len(day)):
            if day[min] == "#":
                sleep_pattern[min] += 1

    max_asleep = 0
    sleepy_min = 0
    for x, min in zip(xrange(len(sleep_pattern)), sleep_pattern):
        if min > max_asleep:
            max_asleep = min
            sleepy_min = x

    return sleepy_min, max_asleep


def calc_sleepy_guard(guard_patterns):
    sleepy_guard = 0
    max_asleep_time = 0
    max_asleep_mins = 0

    for guard_num in guard_patterns:
        asleep_time, asleep_mins = calc_most_asleep_time(guard_patterns[guard_num])

        if asleep_mins > max_asleep_mins:
            max_asleep_time = asleep_time
            sleepy_guard = guard_num
            max_asleep_mins = asleep_mins

    return sleepy_guard, max_asleep_time, max_asleep_mins


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

print ""
print "-----------------"
print "Testing.........."
print "-----------------"
print ""

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

sleepy_guard, sleepy_minute, asleep_time = calc_sleepy_guard(guard_patterns)

print "Guard {} is asleep mostly at minute {} [{} times].".format(sleepy_guard, sleepy_minute, asleep_time)

assert sleepy_guard == 99, "Incorrectly identified %d as the sleepy guard" % sleepy_guard

assert sleepy_minute == 45, "Incorrectly identified %d as the sleepy time" % sleepy_minute

assert asleep_time == 3, "Incorrectly identified %d as the asleep time" % asleep_time

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

    sleepy_guard, sleepy_minute, asleep_time = calc_sleepy_guard(guard_patterns)

    print "Guard {} is asleep mostly at minute {} [{} times].".format(sleepy_guard, sleepy_minute, asleep_time)

    print "Solution is {0}".format(sleepy_guard * sleepy_minute)
