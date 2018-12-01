#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 18 of the Advent of Code for 2017.
"""

from collections import defaultdict
import sys


def get_value(registers, inst_val):
    if inst_val in "abcdefghijklmnopqrstuvwxyz":
        if inst_val in registers:
            return registers[inst_val]

        return 0

    return int(inst_val)


def process_instruction(registers, instruction, send_q):
    inst_parts = instruction.strip().split("\n")[0].split(" ")

    if inst_parts[0] == "add":
        # print "     add"
        registers[inst_parts[1]] += get_value(registers, inst_parts[2])
    elif inst_parts[0] == "mod":
        # print "     mod"
        registers[inst_parts[1]] %= get_value(registers, inst_parts[2])
    elif inst_parts[0] == "mul":
        # print "     mul"
        registers[inst_parts[1]] *= get_value(registers, inst_parts[2])
    elif inst_parts[0] == "set":
        # print "     set"
        registers[inst_parts[1]] = get_value(registers, inst_parts[2])
    elif inst_parts[0] == "snd":
        # print "     send -->"
        try:
            send_q.append(int(inst_parts[1]))
        except ValueError:
            if inst_parts[1] in registers:
                send_q.append(registers[inst_parts[1]])
            else:
                send_q.append(0)


def process_instructions(registers, instructions, recv_q, send_q, ip=0):
    instructions = instructions.split("\n")
    IP = ip
    waiting = len(send_q)

    while IP < len(instructions):
        instruction = instructions[IP]

        inst_parts = instruction.strip().split("\n")[0].split(" ")

        if inst_parts[0] == "jgz":
            # print "     jgz"
            val = get_value(registers, inst_parts[1])
            jmp_val = get_value(registers, inst_parts[2])
            if val > 0:
                IP += jmp_val
                continue
        elif inst_parts[0] == "rcv":
            if len(recv_q) > 0:
                val = recv_q.pop(0)
                registers[inst_parts[1]] = val
            else:
                # print " --> blocked"
                break
        else:
            process_instruction(registers, instruction, send_q)

        IP += 1

    return (len(send_q) - waiting), IP

# Tests

INSTRUCTIONS = """
snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""

REGISTERS_p0 = defaultdict(int)
REGISTERS_p1 = defaultdict(int)
MSG_Q_p0 = []
MSG_Q_p1 = []
p0_sent = 0
p1_sent = 0
p0_ip = 0
p1_ip = 0

while True:
    p0_sent_last = p0_sent
    p1_sent_last = p1_sent

    sent, p0_ip = process_instructions(REGISTERS_p0, INSTRUCTIONS, MSG_Q_p0, MSG_Q_p1, ip=p0_ip)
    p0_sent += sent

    sent, p1_ip = process_instructions(REGISTERS_p1, INSTRUCTIONS, MSG_Q_p1, MSG_Q_p0, ip=p1_ip)
    p1_sent += sent

    if p0_sent == p0_sent_last and p1_sent == p1_sent_last:
        break

if p0_sent != 3:
    print "Failed to find correct test solution. [{0}]".format(p1_sent)
    sys.exit(-1)
if p1_sent != 3:
    print "Failed to find correct test solution. [{0}]".format(p1_sent)
    sys.exit(-1)
print "Test passed."


# All tests complete.

with open("input.txt", "r") as f:
    INSTRUCTIONS = f.read()
    REGISTERS_p0 = defaultdict(int)
    REGISTERS_p1 = defaultdict(int)
    REGISTERS_p1["p"] = 1
    MSG_Q_p0 = []
    MSG_Q_p1 = []

    p0_sent = 0
    p1_sent = 0

    p0_ip = 0
    p1_ip = 0

    while True:
        p0_sent_last = p0_sent
        p1_sent_last = p1_sent

        sent, p0_ip = process_instructions(REGISTERS_p0, INSTRUCTIONS, MSG_Q_p0, MSG_Q_p1, ip=p0_ip)
        p0_sent += sent

        sent, p1_ip = process_instructions(REGISTERS_p1, INSTRUCTIONS, MSG_Q_p1, MSG_Q_p0, ip=p1_ip)
        p1_sent += sent

        if p0_sent == p0_sent_last and p1_sent == p1_sent_last:
            break

    print "Solution is {0}".format(p1_sent)
