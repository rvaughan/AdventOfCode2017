#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 4 of the Advent of Code for 2015.
"""
import sys


class Wire(object):

    def __init__(self, line):
        self._line = line
        self.parse_line(line)

    def parse_line(self, line):
        pieces = line.split()

        # Extract where we are outputting to.
        self.output = pieces[-1]

        # Calculate the 'ledt hand side'.
        left_hand_side = pieces[:-2]

        # Set a default operation
        self.op = 'ASSIGN'

        # Work out the 'actual' operation
        for op in ['NOT', 'AND', 'OR', 'LSHIFT', 'RSHIFT']:
            if op in left_hand_side:
                self.op = op
                left_hand_side.remove(op)

        # Work out the inputs to this wire
        self.inputs = [int(i) if i.isdigit() else i for i in left_hand_side]

    def evaluate(self):
        if self.op == 'ASSIGN':
            return int(self.inputs[0])
        elif self.op == 'NOT':
            return int(65535 - self.inputs[0])
        elif self.op == 'AND':
            return int(self.inputs[0] & self.inputs[1])
        elif self.op == 'OR':
            return int(self.inputs[0] | self.inputs[1])
        elif self.op == 'LSHIFT':
            return int(self.inputs[0] << self.inputs[1])
        elif self.op == 'RSHIFT':
            return int(self.inputs[0] >> self.inputs[1])
        else:
            raise ValueError('invalid operator')

    def fill_inputs(self, signals):
        self.inputs = [signals[i] if i in signals else i for i in self.inputs]

    def is_complete(self):
        return all([isinstance(i, int) for i in self.inputs])


def process_circuit(wires, signals):
    tmp_wires = list(wires)

    while len(tmp_wires) != 0:
        new_wires = []
        for wire in wires:
            if wire.is_complete():
                signals[wire.output] = wire.evaluate()
            else:
                wire.fill_inputs(signals)
                new_wires.append(wire)

        tmp_wires = new_wires

    return signals


def run_test(signals, check, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = signals[check]

    if result != expected_solution:
        print "Test for signal '{0}' FAILED. Got a result of {1}, not {2}".format(check, result, expected_solution)
        sys.exit(-1)

    print "Test for signal '{0}' passed.".format(check)


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_input = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""

wires = [Wire(line) for line in test_input.split('\n')]
signals = {}

process_circuit(wires, signals)

run_test(signals, 'd', 72)
run_test(signals, 'e', 507)
run_test(signals, 'f', 492)
run_test(signals, 'g', 114)
run_test(signals, 'h', 65412)
run_test(signals, 'i', 65079)
run_test(signals, 'x', 123)
run_test(signals, 'y', 456)

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual data now.

with open("input.txt", "r") as f:
    wires = [Wire(line) for line in f]
    signals = {}

    signals = process_circuit(wires, signals)

    print "Signal for wire a: {}".format(signals['a'])
