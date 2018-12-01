#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 7 of the Advent of Code for 2017.
"""

import sys


def process_nodes(node_list, node_data):
    n = {}
    n["sub"] = []
    n["weight"] = 0
    n["level"] = 0
    n["branch_weight"] = 0

    details = node_data.split("\n")[0].split(" ")
    program_name = details[0]

    n["weight"] = int(details[1].split("(")[1].split(")")[0])
    # print n["weight"]

    if len(details) > 2:
        for sub in xrange(3, len(details)):
            n["sub"].append(details[sub].split(",")[0])

    node_list[program_name] = n

    return node_list


def adjust_node_levels(node_list):
    for n in node_list:
        if len(node_list[n]["sub"]) > 0:
            for sub in node_list[n]["sub"]:
                node_list[sub]["level"] += 1
                # node_list[n]["branch_weight"] += node_list[sub]["weight"]

        # print "Node: {0}, weight={1}, branch={2}".format(n,
        #                                                  node_list[n]["weight"],
        #                                                  node_list[n]["branch_weight"])


    return node_list


def correct_node_levels(node_list, root_node, depth=0):

    node_list[root_node]["level"] = depth
    for sub in node_list[root_node]["sub"]:
        correct_node_levels(node_list, sub, depth + 1)

    return node_list


def calculate_node_weight(node_list, root_node):
    weight = 0

    if len(node_list[root_node]["sub"]) > 0:
        for sub in node_list[root_node]["sub"]:
            weight += calculate_node_weight(node_list, sub)

        node_list[root_node]["branch_weight"] = weight
        
    return node_list[root_node]["weight"] + node_list[root_node]["branch_weight"]


def find_bottom_program(nodes):
    root_node = ""
    first = True

    for n in nodes:
        if first:
            root_node = n
            first = False
        else:
            if nodes[n]["level"] < nodes[root_node]["level"]:
                root_node = n

    return root_node


def find_imbalance(root_node, nodes, show_all=False):
    p_id = None
    current_weight = 0
    actual_weight = 0
    tmp = {}
    for sub in nodes[root_node]["sub"]:
        weight = nodes[sub]["weight"] + nodes[sub]["branch_weight"]

        if weight in tmp:
            tmp[weight].append(sub)
        else:
            tmp[weight] = [sub]

    if len(tmp) > 1:
        for w in tmp:
            if len(tmp[w]) == 1:
                p_id = tmp[w][0]
                actual_weight = w
            else:
                current_weight = w

        if p_id is not None:
            weight = nodes[p_id]["weight"] + nodes[p_id]["branch_weight"]

            # print "****"
            # print "* {0}".format(root_node)
            # print "* {0}".format(nodes[root_node])
            # print "****"

            # for w in tmp:
            #     print "{0} -> {1}".format(w, tmp[w])
            #     print "       {0}".format(nodes[tmp[w][0]])

            diff = (current_weight - actual_weight)
            print "Node: {0}, depth={1}, weight={2}, expected={3}".format(p_id,
                                                                        nodes[p_id]["level"],
                                                                        nodes[p_id]["weight"],
                                                                        nodes[p_id]["weight"] + diff)

            if not show_all:
                return p_id, actual_weight, current_weight
            else:
                tmp_nl = []
                for w in tmp:
                    tmp_nl += tmp[w]

                for node in tmp_nl:
                    find_imbalance(node, nodes, show_all=True)

    return None, 0, 0


with open("test_input.txt", "r") as f:
    expected_program = "ugml"
    expected_weight = 243
    actual_weight = 251

    NODES = {}
    for program_info in f.readlines():
        NODES = process_nodes(NODES, program_info)

    NODES = adjust_node_levels(NODES)
    ROOT_PROGRAM = find_bottom_program(NODES)

    NODES = correct_node_levels(NODES, ROOT_PROGRAM)
    # NODES[ROOT_PROGRAM]["branch_weight"] = calculate_node_weight(NODES, ROOT_PROGRAM)
    calculate_node_weight(NODES, ROOT_PROGRAM)

    # Quick sanity check
    if ROOT_PROGRAM != "tknk":
        print "Test aborted, found wrong bottom program '{0}', was expecting '{1}'.".format(bottom_program, "vvsvez")
        sys.exit(-1)

    e_p, a_w, e_w = find_imbalance(ROOT_PROGRAM, NODES)

    if expected_program != e_p:
        print "Test failed found node '{0}', but was expecting '{1}'.".format(e_p, expected_program)
        sys.exit(-1)
    if actual_weight != a_w:
        print "Test failed, got actual weight of '{0}', but was expecting '{1}'.".format(a_w, actual_weight)
        sys.exit(-1)
    if expected_weight != e_w:
        print "Test failed, got weight of '{0}', but was expecting '{1}'.".format(e_w, expected_weight)
        sys.exit(-1)
    print "Test passed."


with open("input.txt", "r") as f:
    NODES = {}
    for program_info in f.readlines():
        nodes = process_nodes(NODES, program_info)

    NODES = adjust_node_levels(NODES)
    ROOT_PROGRAM = find_bottom_program(NODES)

    NODES = correct_node_levels(NODES, ROOT_PROGRAM)
    # NODES[ROOT_PROGRAM]["branch_weight"] = calculate_node_weight(NODES, ROOT_PROGRAM)
    calculate_node_weight(NODES, ROOT_PROGRAM)

    # Final spot check test. Hand cranked.
    if NODES["ghwgd"]["branch_weight"] != 822:
        print "Check of branch weight for '{0}' failed. {1}".format("ghwgd", NODES["ghwgd"]["branch_weight"])
        sys.exit(-1)

    # Final spot check test. Hand cranked.
    if NODES["fitvk"]["branch_weight"] != 0:
        print "Check of branch weight for '{0}' failed. {1}".format("fitvk", NODES["fitvk"]["branch_weight"])
        sys.exit(-1)

    # Final spot check test. Hand cranked.
    if NODES["uvdikh"]["branch_weight"] != 21:
        print "Check of branch weight for '{0}' failed. {1}".format("uvdikh", NODES["uvdikh"]["branch_weight"])
        sys.exit(-1)

    # Final spot check test. Hand cranked.
    if NODES["jywenab"]["branch_weight"] != 447:
        print "Check of branch weight for '{0}' failed. {1}".format("jywenab", NODES["jywenab"]["branch_weight"])
        print "{0}".format(NODES["jywenab"])
        for sub in NODES["jywenab"]["sub"]:
            print "{0} - {1}".format(sub, NODES[sub])
        sys.exit(-1)

    if NODES["vvsvez"]["branch_weight"] != 402110:
        print "Check of branch weight for '{0}' failed. {1}".format("vvsvez", NODES["vvsvez"]["branch_weight"])
        for sub in NODES["vvsvez"]["sub"]:
            print "{0} - {1}".format(sub, NODES[sub])
        sys.exit(-1)

    if NODES["dwpvwz"]["branch_weight"] != 24:
        print "Check of branch weight for '{0}' failed. {1}".format("dwpvwz", NODES["dwpvwz"]["branch_weight"])
        for sub in NODES["dwpvwz"]["sub"]:
            print "{0} - {1}".format(sub, NODES[sub])
        sys.exit(-1)

    if NODES["ircgvnq"]["branch_weight"] != 495:
        print "Check of branch weight for '{0}' failed. {1}".format("ircgvnq", NODES["ircgvnq"]["branch_weight"])
        for sub in NODES["ircgvnq"]["sub"]:
            print "{0} - {1}".format(sub, NODES[sub])
        sys.exit(-1)

    e_p, a_w, e_w = find_imbalance(ROOT_PROGRAM, NODES, show_all=True)
    # e_p, a_w, e_w = find_imbalance("ghwgd", NODES, show_all=True)
    # print e_p, a_w, e_w
