#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 7 of the Advent of Code for 2017.
"""

import sys


def process_nodes(node_data, program_info):
    n = {}
    n["sub"] = []
    n["weight"] = 0
    n["level"] = 0

    details = program_info.split("\n")[0].split(" ")
    program_name = details[0]

    n["weight"] = int(details[1].split("(")[1].split(")")[0])

    if len(details) > 2:
        for sub in xrange(3, len(details)):
            n["sub"].append(details[sub].split(",")[0])

    node_data[program_name] = n

    return node_data


def adjust_node_levels(nodes):
    for n in nodes:
        if len(nodes[n]["sub"]) > 0:
            for sub in nodes[n]["sub"]:
                nodes[sub]["level"] += 1

    return nodes

def find_bottom_program(nodes):
    adjust_node_levels(nodes)

    max = ""
    first = True

    for n in nodes:
        if first:
            max = n
            first = False
        else:
            if nodes[n]["level"] < nodes[max]["level"]:
                max = n

    return max


with open("test_input.txt", "r") as f:
    expected_program = "tknk"
    nodes = {}
    for program_info in f.readlines():
        nodes = process_nodes(nodes, program_info)

    bottom_program = find_bottom_program(nodes)

    if expected_program != bottom_program:
        print "Test failed, got '{0}', but was expecting '{1}'.".format(bottom_program, expected_program)
        sys.exit(-1)
    print "Test passed."


with open("input.txt", "r") as f:
    nodes = {}
    for program_info in f.readlines():
        nodes = process_nodes(nodes, program_info)

    bottom_program = find_bottom_program(nodes)

    print "Bottom program is '{0}'.".format(bottom_program)
