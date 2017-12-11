#!/usr/bin/env python

import sys


def find_end_pos(data, start_x, start_y):
    cur_x = start_x
    cur_y = start_y

    for move in data:
        if move == "n":
            cur_y += 1
        elif move == "ne":
            cur_x += 1
            cur_y += 1
        elif move == "e":
            cur_x += 1
        elif move == "se":
            cur_x += 1
            cur_y -=1
        elif move == "s":
            cur_y -= 1
        elif move == "sw":
            cur_x -= 1
            cur_y -= 1
        elif move == "w":
            cur_x -= 1
        elif move == "nw":
            cur_x -= 1
            cur_y += 1

    return cur_x, cur_y


def calc_distance(pos_x, pos_y):
    if POS_X == POS_Y:
        return abs(POS_X)

    distance = 0
    if abs(POS_X) < abs(POS_Y):
        distance = abs(POS_X)
    else:
        distance = abs(POS_Y)

    distance += abs(POS_X) - abs(POS_Y)

    return abs(distance)


INPUT_DATA = "ne,ne,ne"
STEPS = [x for x in INPUT_DATA.split(",")]
CUR_X = 0
CUR_Y = 0
POS_X, POS_Y = find_end_pos(STEPS, CUR_X, CUR_Y)
DISTANCE = calc_distance(POS_X, POS_Y)
if DISTANCE != 3:
    print "Test 1 failed. Distance was {0}".format(DISTANCE)
    sys.exit(-1)
print "Test 1 passed."



INPUT_DATA = "ne,ne,sw,sw"
STEPS = [x for x in INPUT_DATA.split(",")]
CUR_X = 0
CUR_Y = 0
POS_X, POS_Y = find_end_pos(STEPS, CUR_X, CUR_Y)
DISTANCE = calc_distance(POS_X, POS_Y)
if DISTANCE != 0:
    print "Test 2 failed. Distance was {0}".format(DISTANCE)
    sys.exit(-1)
print "Test 2 passed."


INPUT_DATA = "ne,ne,s,s"
STEPS = [x for x in INPUT_DATA.split(",")]
CUR_X = 0
CUR_Y = 0
POS_X, POS_Y = find_end_pos(STEPS, CUR_X, CUR_Y)
DISTANCE = calc_distance(POS_X, POS_Y)
if DISTANCE != 2:
    print "Test 3 failed. Distance was {0}".format(DISTANCE)
    sys.exit(-1)
print "Test 3 passed."


INPUT_DATA = "se,sw,se,sw,sw"
STEPS = [x for x in INPUT_DATA.split(",")]
CUR_X = 0
CUR_Y = 0
POS_X, POS_Y = find_end_pos(STEPS, CUR_X, CUR_Y)
DISTANCE = calc_distance(POS_X, POS_Y)
if DISTANCE != 3:
    print "Test 4 failed. Distance was {0}".format(DISTANCE)
    sys.exit(-1)
print "Test 4 passed."


with open("input.txt", "r") as f:
    INPUT_DATA = f.readline().strip()
    STEPS = [x for x in INPUT_DATA.split(",")]
    CUR_X = 0
    CUR_Y = 0
    POS_X, POS_Y = find_end_pos(STEPS, CUR_X, CUR_Y)
    print calc_distance(POS_X, POS_Y)
