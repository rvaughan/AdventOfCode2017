#!/usr/bin/env python

import sys


def add_links(programs, link_data):
    links = link_data.strip().split(" ")
    if links[0] not in programs:
        programs[links[0]] = []

    for x in links[2:]:
        b = x.split(",")[0]
        programs[links[0]].append(b)
        if b not in programs:
            programs[b] = []


def find_group(programs, root, p_list):
    if root in programs and root not in p_list:
        p_list[root] = True

        for linked in programs[root]:
            find_group(programs, linked, p_list)


def group_programs(programs, groups):
    for p in programs:
        groups[p] = 0

    g_num = 1

    for p in groups.keys():
        if groups[p] == 0:
            p_list = {}
            find_group(programs, p, p_list)
            for pp in p_list:
                groups[pp] = g_num

            g_num += 1

    return g_num - 1


PROGRAMS = {}
GROUPS = {}
with open("test_input.txt", "r") as f:
    for line in f.readlines():
        add_links(PROGRAMS, line)

    num_groups = group_programs(PROGRAMS, GROUPS)

    if num_groups != 2:
        print "Test failed. {0}".format(num_groups)
        sys.exit(-1)


# If we get to here then all of the tests have passed.


PROGRAMS = {}
with open("input.txt", "r") as f:
    for line in f.readlines():
        add_links(PROGRAMS, line)

    print group_programs(PROGRAMS, GROUPS)
