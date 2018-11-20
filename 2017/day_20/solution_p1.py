#!/usr/bin/env python

from operator import add, abs
import re
import sys


def extract_data(data):
    r = re.compile(r"[pva]=<([ -]?\d+),([ -]?\d+),([ -]?\d+)>")
    p_data = r.match(data)
    if p_data != None:
        return (int(p_data.group(1)), int(p_data.group(2)), int(p_data.group(3)))
    else:
        return (0, 0, 0)


def load_particles(PARTICLE_INPUT):
    particle_list = []

    idx = 0
    for line in PARTICLE_INPUT.split("\n"):
        p = {}

        data = line.split(", ")
        p["id"] = idx
        p["pos"] = extract_data(data[0])
        p["vel"] = extract_data(data[1])
        p["acc"] = extract_data(data[2])
        p["dist"] = tuple(map(abs, p["pos"]))

        particle_list.append(p)

        idx += 1

    return particle_list


def do_move(particles):
    min_distance = 999999
    min_particle = -1

    for p in particles:
        pos = p["pos"]
        vel = p["vel"]
        acc = p["acc"]

        vel = tuple(map(add, vel, acc))
        pos = tuple(map(add, pos, vel))

        p["pos"] = pos
        p["vel"] = vel

        # Calculate the haversine distance.
        new_dist = sum(abs(x) for x in pos)

        if new_dist < min_distance:
            min_distance = new_dist
            min_particle = p

        p["dist"] = new_dist

    return min_distance, min_particle["id"]


PARTICLE_INPUT="p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>"
PARTICLES = load_particles(PARTICLE_INPUT)
if len(PARTICLES) != 1:
    print "Wrong number of particles. {0}".format(len(PARTICLES))
    sys.exit(-1)
do_move(PARTICLES)
if PARTICLES[0]["pos"][0] != 4:
    print "Wrong position after 1st move. {0}".format(PARTICLES[0]["pos"])
    sys.exit(-1)

PARTICLE_INPUT="""p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>"""
PARTICLES = load_particles(PARTICLE_INPUT)
if len(PARTICLES) != 2:
    print "Wrong number of particles. {0}".format(len(PARTICLES))
    sys.exit(-1)
do_move(PARTICLES)
if PARTICLES[0]["pos"][0] != 4:
    print "Wrong position after p0 1st move. {0}".format(PARTICLES[0]["pos"])
    sys.exit(-1)
if PARTICLES[1]["pos"][0] != 2:
    print "Wrong position after p1 1st move. {0}".format(PARTICLES[1]["pos"])
    sys.exit(-1)
do_move(PARTICLES)
if PARTICLES[0]["pos"][0] != 4:
    print "Wrong position after p0 2nd move. {0}".format(PARTICLES[0]["pos"])
    sys.exit(-1)
if PARTICLES[1]["pos"][0] != -2:
    print "Wrong position after p1 2nd move. {0}".format(PARTICLES[1]["pos"])
    sys.exit(-1)
do_move(PARTICLES)
if PARTICLES[0]["pos"][0] != 3:
    print "Wrong position after p0 3rd move. {0}".format(PARTICLES[0]["pos"])
    sys.exit(-1)
if PARTICLES[1]["pos"][0] != -8:
    print "Wrong position after p1 3rd move. {0}".format(PARTICLES[1]["pos"])
    sys.exit(-1)

print "All tests passed."

with open("input.txt", "r") as f:
    PARTICLE_INPUT = f.read()
    PARTICLES = load_particles(PARTICLE_INPUT)

    last_d = 99999
    last_p = -1
    count = 0
    while True:
        min_d, min_p = do_move(PARTICLES)

        if last_p == min_p:
            # We've been "stable" for 500 iterations, so let's bail out.
            if count == 500:
                break
            count += 1
        else:
            count = 0
            last_d = min_d
            last_p = min_p

    print min_d, min_p
