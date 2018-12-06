#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 14 of the Advent of Code for 2015.
"""
import itertools
import sys


class Reindeer(object):

    def __init__(self, name, max_speed, longevity, rest_time):
        self.name = name
        self.max_speed = max_speed
        self.longevity = longevity
        self.rest_time = rest_time

        self.current_time = 0
        self.currently_flying = True
        self.current_rest_time = 0
        self.current_flight_time = 0
        self.current_travel = 0
        self.current_distance = 0

    def getCurrentDistance(self):
        return self.current_distance * self.max_speed

    def getCurrentlyFlying(self):
        return self.currently_flying

    def getLongevity(self):
        return self.longevity

    def getMaxSpeed(self):
        return self.max_speed

    def getName(self):
        return self.name

    def getRestTime(self):
        return self.rest_time

    def move_by(self, interval):
        for _ in xrange(interval):
            self.current_time += 1

            if self.currently_flying:
                self.current_distance += 1
                self.current_travel += 1

                if self.current_travel == self.longevity:
                    self.currently_flying = False
                    self.current_travel = 0
            else:
                self.current_rest_time += 1
                if self.current_rest_time == self.rest_time:
                    self.current_rest_time = 0
                    self.currently_flying = True

    def move_to(self, new_time):
        while self.current_time != new_time:
            self.move_by(1)


def create_reindeer(input_data):
    pieces = input_data.split(' ')

    reindeer = Reindeer(pieces[0], int(pieces[3]), int(pieces[6]), int(pieces[13]))

    return reindeer


def run_test_reindeer(reindeer, expected_name, expected_max_speed, expected_longevity, expected_rest_time):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """

    if reindeer.getName() != expected_name:
        print "Test for name '{} FAILED. Got a result of {}.".format(expected_name, reindeer.getName())
        sys.exit(-1)

    if reindeer.getMaxSpeed() != expected_max_speed:
        print "Test for max speed '{} FAILED. Got a result of {}.".format(expected_name, reindeer.getMaxSpeed())
        sys.exit(-1)

    if reindeer.getLongevity() != expected_longevity:
        print "Test for longevity '{} FAILED. Got a result of {}.".format(expected_name, reindeer.getLongevity())
        sys.exit(-1)

    if reindeer.getRestTime() != expected_rest_time:
        print "Test for rest time '{} FAILED. Got a result of {}.".format(expected_name, reindeer.getRestTime())
        sys.exit(-1)

    print "Tests for reindeer {0} passed.".format(expected_name)


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_input="""Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""

reindeer_map = {}
for line in test_input.split('\n'):
    reindeer = create_reindeer(line)

    reindeer_map[reindeer.getName()] = reindeer

assert 'Comet' in reindeer_map
run_test_reindeer(reindeer_map['Comet'], 'Comet', 14, 10, 127)

assert 'Dancer' in reindeer_map
run_test_reindeer(reindeer_map['Dancer'], 'Dancer', 16, 11, 162)

reindeer_map['Comet'].move_by(1)
assert reindeer_map['Comet'].getCurrentlyFlying()
assert reindeer_map['Comet'].getCurrentDistance() == 14

reindeer_map['Dancer'].move_by(1)
assert reindeer_map['Dancer'].getCurrentlyFlying()
assert reindeer_map['Dancer'].getCurrentDistance() == 16

reindeer_map['Comet'].move_to(10)
assert not reindeer_map['Comet'].getCurrentlyFlying()
assert reindeer_map['Comet'].getCurrentDistance() == 140

reindeer_map['Dancer'].move_to(10)
assert reindeer_map['Dancer'].getCurrentlyFlying()
assert reindeer_map['Dancer'].getCurrentDistance() == 160

reindeer_map['Comet'].move_to(11)
assert not reindeer_map['Comet'].getCurrentlyFlying()
assert reindeer_map['Comet'].getCurrentDistance() == 140

reindeer_map['Dancer'].move_to(11)
assert not reindeer_map['Dancer'].getCurrentlyFlying()
assert reindeer_map['Dancer'].getCurrentDistance() == 176

reindeer_map['Comet'].move_to(12)
assert not reindeer_map['Comet'].getCurrentlyFlying()
assert reindeer_map['Comet'].getCurrentDistance() == 140

reindeer_map['Dancer'].move_to(12)
assert not reindeer_map['Dancer'].getCurrentlyFlying()
assert reindeer_map['Dancer'].getCurrentDistance() == 176

reindeer_map['Comet'].move_to(138)
assert reindeer_map['Comet'].getCurrentlyFlying()
assert reindeer_map['Comet'].getCurrentDistance() == 154

reindeer_map['Dancer'].move_to(138)
assert not reindeer_map['Dancer'].getCurrentlyFlying()
assert reindeer_map['Dancer'].getCurrentDistance() == 176

reindeer_map['Dancer'].move_to(174)
assert reindeer_map['Dancer'].getCurrentlyFlying()
assert reindeer_map['Dancer'].getCurrentDistance() == 192

reindeer_map['Comet'].move_to(1000)
assert not reindeer_map['Comet'].getCurrentlyFlying()
assert reindeer_map['Comet'].getCurrentDistance() == 1120

reindeer_map['Dancer'].move_to(1000)
assert not reindeer_map['Dancer'].getCurrentlyFlying()
assert reindeer_map['Dancer'].getCurrentDistance() == 1056

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual data now.

with open("input.txt", "r") as f:
    reindeer_map = {}
    for line in f:
        reindeer = create_reindeer(line)
        reindeer_map[reindeer.getName()] = reindeer

    max_distance = 0
    for name in reindeer_map.keys():
        reindeer_map[name].move_to(2503)

        max_distance = max(max_distance, reindeer_map[name].getCurrentDistance())

    print "Furthest: {}".format(max_distance)
