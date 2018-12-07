#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 19 of the Advent of Code for 2015.
"""


def add_replacement(line):
    pieces = line.split(' ')

    replacement = []

    replacement.append(pieces[0])
    replacement.append(pieces[2])

    return replacement


def load_replacements(input_data):
    replacements = []
    molecule = ""
    all_replacements_processed = False
    for line in input_data:
        if line == "":
            all_replacements_processed = True
        else:
            if not all_replacements_processed:
                replacements.append(add_replacement(line))
            else:
                molecule = line

    return replacements, molecule


def find_molecules(replacements, molecule):
    new_molecules = set()
    prefix = ""

    for replacement in replacements:
        # print replacement, molecule
        pos = 0
        while pos != -1 and pos < len(molecule):
            pos = molecule.find(replacement[0], pos)
            if pos != -1:
                new_molecule = molecule[:pos] + replacement[1] + molecule[pos+len(replacement[0]):]
                # print new_molecule
                new_molecules.add(new_molecule)
                pos += len(replacement[0])

    return new_molecules


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_input = """H => HO
H => OH
O => HH

HOH"""

input_data = test_input.splitlines()

replacements, molecule = load_replacements(input_data)

new_molecules = find_molecules(replacements, molecule)

assert len(new_molecules) == 4, len(new_molecules)

new_molecules = find_molecules(replacements, "HOHOHO")

assert len(new_molecules) == 7, len(new_molecules)

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual data now.

with open("input.txt", "r") as f:
    input_data = [line.rstrip() for line in f]

    replacements, molecule = load_replacements(input_data)

    new_molecules = find_molecules(replacements, molecule)

    print("Solution: {}".format(len(new_molecules)))
