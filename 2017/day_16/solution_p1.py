#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 16 of the Advent of Code for 2017.
"""

import sys


def spin(programs, num):
    p = programs[-num:] + programs[:-num]
    return p


def swap(programs, p1, p2):
    tmp_str = list(programs)

    tmp_str[p1], tmp_str[p2] = tmp_str[p2], tmp_str[p1]

    return ''.join(tmp_str)


def prog_swap(programs, p1, p2):
    return swap(programs, programs.find(p1), programs.find(p2))


# BEGIN TEST SECTION

PROGRAMS = "abcde"

PROGRAMS = spin(PROGRAMS, 1)
if PROGRAMS != "eabcd":
    print "Spin test failed. [{0}]".format(PROGRAMS)
    sys.exit(-1)
print "Spin test passed."

PROGRAMS = swap(PROGRAMS, 3, 4)
if PROGRAMS != "eabdc":
    print "Spin test failed [{0}]".format(PROGRAMS)
    sys.exit(-1)
print "Spin test passed."

PROGRAMS = prog_swap(PROGRAMS, "e", "b")
if PROGRAMS != "baedc":
    print "Spin test failed [{0}]".format(PROGRAMS)
    sys.exit(-1)
print "Spin test passed."


PROGRAMS = "abcde"
CMDS = ["s1", "x3/4", "pe/b"]
for cmd in CMDS:
    if cmd[:1] == 's':
        PROGRAMS = spin(PROGRAMS, int(cmd[1:2]))
    elif cmd[:1] == 'x':
        pos = cmd.find("/")
        PROGRAMS = swap(PROGRAMS, int(cmd[1:pos]), int(cmd[pos+1:]))
    elif cmd[:1] == 'p':
        pos = cmd.find("/")
        PROGRAMS = prog_swap(PROGRAMS, cmd[1:2], cmd[pos+1:])
if PROGRAMS != "baedc":
    print "Spin test failed [{0}]".format(PROGRAMS)
    sys.exit(-1)
print "Command test passed."

print "All tests passed."

# END OF TEST SECTION

PROGRAMS = "abcdefghijklmnop"
with open("input.txt", "r") as f:
    DATA = f.read()
    for cmd in DATA.split(","):
        if cmd[:1] == 's':
            PROGRAMS = spin(PROGRAMS, int(cmd[1:]))
        elif cmd[:1] == 'x':
            pos = cmd.find("/")
            PROGRAMS = swap(PROGRAMS, int(cmd[1:pos]), int(cmd[pos+1:]))
        elif cmd[:1] == 'p':
            pos = cmd.find("/")
            PROGRAMS = prog_swap(PROGRAMS, cmd[1:2], cmd[pos+1:])
print PROGRAMS
