#!/usr/bin/env python

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
    print "Command test failed [{0}]".format(PROGRAMS)
    sys.exit(-1)
print "Command test passed."

PROGRAMS = "abcde"
CMDS = ["s1", "x3/4", "pe/b"]
for _ in xrange(2):
    for cmd in CMDS:
        if cmd[:1] == 's':
            PROGRAMS = spin(PROGRAMS, int(cmd[1:2]))
        elif cmd[:1] == 'x':
            pos = cmd.find("/")
            PROGRAMS = swap(PROGRAMS, int(cmd[1:pos]), int(cmd[pos+1:]))
        elif cmd[:1] == 'p':
            pos = cmd.find("/")
            PROGRAMS = prog_swap(PROGRAMS, cmd[1:2], cmd[pos+1:])
if PROGRAMS != "ceadb":
    print "Repeatitive test failed [{0}]".format(PROGRAMS)
    sys.exit(-1)
print "Repeatitive test passed."

print "All tests passed."

# END OF TEST SECTION

PROGRAMS = "abcdefghijklmnop"
with open("input.txt", "r") as f:
    DATA = f.read()
    # Clearly the 1 billion iterations would take a long time to complete. We
    # 'know' that the solution is cyclical. 
    SEEN = []
    for idx in xrange(1000000000):
        if PROGRAMS in SEEN:
            print "Cycle detected at tteration: {0}".format(len(SEEN))
            # Work out which of the solutions would occur after the 1 billionth
            # attempt.
            print "Solution: {0}".format(SEEN[1000000000 % len(SEEN)])
            break

        SEEN.append(PROGRAMS)

        for cmd in DATA.split(","):
            if cmd[:1] == 's':
                PROGRAMS = spin(PROGRAMS, int(cmd[1:]))
            elif cmd[:1] == 'x':
                pos = cmd.find("/")
                PROGRAMS = swap(PROGRAMS, int(cmd[1:pos]), int(cmd[pos+1:]))
            elif cmd[:1] == 'p':
                pos = cmd.find("/")
                PROGRAMS = prog_swap(PROGRAMS, cmd[1:2], cmd[pos+1:])
