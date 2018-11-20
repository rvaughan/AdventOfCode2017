#!/usr/bin/env python


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


def check(comps, bridge, best_score):
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
            best_score = check(next_comps, next_bridge, best_score)

    if not found_a_bridge:
        score = calc_bridge_strength(bridge)
        if score > best_score:
            best_score = score

    return best_score


with open("input.txt", "r") as f:
    ALL_COMPONENTS = []
    for line in f:
        ALL_COMPONENTS.append(tuple([int(x) for x in line.strip().split("/")]))

    STRONGEST_BRIDGE_SCORE = 0
    STRONGEST_BRIDGE_SCORE = check(ALL_COMPONENTS, [], STRONGEST_BRIDGE_SCORE)

    print "Solution: {0}".format(STRONGEST_BRIDGE_SCORE)
