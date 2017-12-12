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


def get_program_list(programs, root, p_list):
    if root in programs and root not in p_list:
        p_list[root] = True

        for linked in programs[root]:
            get_program_list(programs, linked, p_list)


PROGRAMS = {}
with open("test_input.txt", "r") as f:
    for line in f.readlines():
        add_links(PROGRAMS, line)

    P_LIST = {}
    get_program_list(PROGRAMS, "0", P_LIST)

    # for p in P_LIST:
    #     print p

    if len(P_LIST) != 6:
        print "Test failed."
        sys.exit(-1)


# If we get to this point then the test failed.


PROGRAMS = {}
with open("input.txt", "r") as f:
    for line in f.readlines():
        add_links(PROGRAMS, line)

    P_LIST = {}
    get_program_list(PROGRAMS, "0", P_LIST)

    print len(P_LIST)
