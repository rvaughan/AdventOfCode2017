#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 13 of the Advent of Code for 2017.
"""

import sys


def build_firewall(area_data):
    firewall = []
    cur_area = 0

    for line in area_data.split("\n"):
        parts = line.strip().split(":")
        while int(parts[0]) > cur_area:
            firewall.append(0)
            cur_area += 1
        firewall.append(int(parts[1]))
        cur_area += 1

    return firewall


def calc_position(start_time, depth):
    cur_pos = start_time % ((depth - 1) * 2)

    return 2 * (depth - 1) - cur_pos if cur_pos > depth - 1 else cur_pos


def get_caught(firewall, delay=0):
    cur_time = delay

    for area in xrange(len(firewall)):
        if calc_position(cur_time, firewall[area]) == 0:
            return True

        cur_time += 1

    return False


def calc_minimum_delay(firewall):
    delay = 0
    while True:
        if not get_caught(FIREWALL, delay=delay):
            min_delay = delay
            break

        delay += 1

    return min_delay

FIREWALL = []
with open("test_input.txt", "r") as f:
    data = f.read()

    FIREWALL = build_firewall(data)

    MIN_DELAY = calc_minimum_delay(FIREWALL)

    if MIN_DELAY != 10:
        print "Test failed, wrong delay. {0}".format(MIN_DELAY)
        sys.exit(-1)
print "Test passed."

# If we reach here then our test has passed:

FIREWALL = []
with open("input.txt", "r") as f:
    data = f.read()

    FIREWALL = build_firewall(data)

    MIN_DELAY = calc_minimum_delay(FIREWALL)

    print "Min delay = {0}.".format(MIN_DELAY)
