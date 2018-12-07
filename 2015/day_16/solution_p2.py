#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 16 of the Advent of Code for 2015.
"""

known_facts = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

aunts = {}
known_aunt = {}

def extract_field(aunt_info, pieces, pos):
    aunt_info[pieces[pos].rstrip(':')] = int(pieces[pos+1].rstrip(','))


for line in known_facts.splitlines():
    pieces = line.split(':')

    extract_field(known_aunt, pieces, 0)


with open("input.txt", "r") as f:
    for line in f:
        pieces = line.split(' ')

        number = int(pieces[1].rstrip(':'))

        aunt_info = {}

        field = 2
        while field < len(pieces):
            extract_field(aunt_info, pieces, field)
            field += 2

        aunts[number] = aunt_info

    tmp = aunts.copy()
    for name in tmp:
        for prop in ["cats", "trees"]:
            if prop in tmp[name]:
                if known_aunt[prop] > tmp[name][prop]:
                    if name in aunts:
                        del aunts[name]
                    break

        for prop in ["pomeranians", "goldfish"]:
            if prop in tmp[name]:
                if known_aunt[prop] < tmp[name][prop]:
                    if name in aunts:
                        del aunts[name]
                    break

        for prop in ["samoyeds", "akitas", "vizslas", "cars", "perfumes"]:
            if prop in tmp[name]:
                if known_aunt[prop] != tmp[name][prop]:
                    if name in aunts:
                        del aunts[name]
                    break

    print aunts
