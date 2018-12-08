#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 8 of the Advent of Code for 2018.
"""

from collections import Counter
import sys


class Node(object):

    def __init__(self):
        self.children = []
        self.metadata = []

    def build_children(self, data, start_pos=0):
        cur_pos = start_pos

        num_children = data[cur_pos]
        num_metadata = data[cur_pos+1]

        cur_pos += 2

        for x in xrange(num_children):
            # print "New child -->", cur_pos
            child = Node()

            cur_pos = child.build_children(data, cur_pos)

            self.children.append(child)

        for x in xrange(num_metadata):
            self.metadata.append(data[cur_pos])
            cur_pos += 1

        return cur_pos

    def calc_license(self):
        license = 0

        for val in self.metadata:
            license += val

        for child in self.children:
            license += child.calc_license()

        return license


def process_tree_data(input_data):
    data = [int(x) for x in input_data.split(' ')]

    root_node = Node()

    root_node.build_children(data, 0)

    return root_node


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

print ""
print "-----------------"
print "Testing.........."
print "-----------------"
print ""

test_input="""2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"""

tree = process_tree_data(test_input)

licence_key = tree.calc_license()
assert licence_key == 138, licence_key

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = f.read()

    tree = process_tree_data(input_data)

    licence_key = tree.calc_license()

    print "Solution is {0}".format(licence_key)
