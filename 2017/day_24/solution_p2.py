#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 24 of the Advent of Code for 2017.
"""

def pick_next_port(port_a, port_b):
    if port_b[0] == port_a[0] or port_b[0] == port_a[1]:
        return port_b[1]

    return port_b[0]


def calc_bridge_strength(bridge):
    score = 0
    for port in bridge:
        score += port[0]
        score += port[1]

    return score


def check(comps, bridge, longest_bridge, best_score):
    next_port = 0

    if len(bridge) >= 2:
        next_port = pick_next_port(bridge[-2], bridge[-1])
    elif len(bridge) == 1:
        next_port = pick_next_port((0, 0), bridge[-1])

    found_a_bridge = False
    for comp in comps:
        if next_port in list(comp):
            found_a_bridge = True
            next_bridge = bridge[:]
            next_bridge.append(comp)
            next_comps = comps[:]
            next_comps.remove(comp)
            best_score, longest_bridge = check(next_comps, next_bridge, longest_bridge, best_score)

    if not found_a_bridge:
        if len(bridge) >= len(longest_bridge):
            score = calc_bridge_strength(bridge)
            if score > best_score:
                longest_bridge = bridge
                best_score = score

    return best_score, longest_bridge


with open("input.txt", "r") as f:
    ALL_COMPONENTS = []
    for line in f:
        ALL_COMPONENTS.append(tuple([int(x) for x in line.strip().split("/")]))

    LONGEST_BRIDGE = []
    LONGEST_BRIDGE_SCORE = 0

    LONGEST_BRIDGE_SCORE, LONGEST_BRIDGE = check(ALL_COMPONENTS, [], LONGEST_BRIDGE, LONGEST_BRIDGE_SCORE)

    print "Solution: {0}".format(LONGEST_BRIDGE_SCORE)
