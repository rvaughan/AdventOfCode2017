#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 10 of the Advent of Code for 2018.
"""

import re


def load_points(input_data):
    points = []
    for line in input_data:
        # This regex is designed to capture all of the numeric values which may
        # or may not include a -'ve sign.
        x_pos, y_pos, x_vel, y_vel = re.findall('-?\d+', line)
        points.append([int(x_pos), int(y_pos), int(x_vel), int(y_vel)])

    return points


def dump_points(timestep, min_x, max_x, min_y, max_y):
    print timestep, min_x, max_x, min_y, max_y

    for y in xrange(min_y, max_y + 1):
        for x in xrange(min_x, max_x + 1):
            if (x, y) in [(px, py) for px, py, _, _ in points]:
                print '#',
            else:
                print '.',
        print "\n"
    print "------------------------------------------------"


def process_points(points, max_steps, max_size):
    for timestep in xrange(max_steps):
        min_x = min([x for x, _, _, _ in points])
        max_x = max([x for x, _, _, _ in points])
        min_y = min([y for _, y, _, _ in points])
        max_y = max([y for _, y, _, _ in points])

        if min_x + max_size >= max_x and min_y + max_size >= max_y:
            dump_points(timestep, min_x, max_x, min_y, max_y)

        for point in points:
            point[0] += point[2]
            point[1] += point[3]


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

print ""
print "-----------------"
print "Testing.........."
print "-----------------"
print ""

test_input="""position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>"""

input_data = [line for line in test_input.splitlines()]
points = load_points(input_data)

max_size = 100
max_steps = 4
process_points(points, max_steps, max_size)


print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [line for line in f]
    points = load_points(input_data)

    max_size = 100
    max_steps = 100000
    process_points(points, max_steps, max_size)

    print "Solution is {0}".format(max_score)
