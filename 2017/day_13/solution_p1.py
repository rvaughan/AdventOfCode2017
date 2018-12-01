#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 13 of the Advent of Code for 2017.
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


def calc_position(cur_time, depth):
    cur_pos = 1
    add = 1

    while True:
        if cur_time == 0:
            break

        cur_pos += add
        if cur_pos == depth:
            add = -1
        elif cur_pos == 1:
            add = 1

        cur_time -= 1

    return cur_pos - 1


def calc_severity(firewall):
    severity = 0
    cur_time = 0

    for area in xrange(len(firewall)):
        if cur_time > 0 and firewall[area] > 0:
            if calc_position(cur_time, firewall[area]) == 0:
                severity += (area * firewall[area])
                # print cur_time, area, firewall[area], severity

        cur_time += 1

    return severity


FIREWALL = []
with open("test_input.txt", "r") as f:
    data = f.read()

    FIREWALL = build_firewall(data)

    SEVERITY = calc_severity(FIREWALL)

    if SEVERITY != 24:
        print "Test failed. {0}".format(SEVERITY)
        sys.exit(-1)
print "Test passed."

# If we reach here then our test has passed:

FIREWALL = []
with open("input.txt", "r") as f:
    data = f.read()

    FIREWALL = build_firewall(data)

    SEVERITY = calc_severity(FIREWALL)

    print "Severity: {0}".format(SEVERITY)
