#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 13 of the Advent of Code for 2015.
"""
import itertools
import sys


def process_input(input_data):
    happiness = {}
    people = set()

    for line in input_data.split('\n'):
        split_line = line.split(' ')

        person1 = split_line[0]
        direction = split_line[2]
        amount = int(split_line[3])
        person2 = split_line[10][:-1]

        people.add(person1)
        people.add(person2)

        if direction == 'lose':
            happiness[person1+person2] = -amount
        else:
            assert direction == 'gain'
            happiness[person1+person2] = amount

    return people, happiness


def calc_optimal_seating(people, happiness):
    maximum_happiness = 0
    for arragement in itertools.permutations(people):
        happiness_gained = 0
        for person1, person2 in zip(arragement[:-1], arragement[1:]):
            happiness_gained += happiness[person1 + person2]
            happiness_gained += happiness[person2 + person1]
        
        # add happiness for first and last pair
        person1 = arragement[0]
        person2 = arragement[-1]
        happiness_gained += happiness[person1 + person2]
        happiness_gained += happiness[person2 + person1]
        maximum_happiness = max(maximum_happiness, happiness_gained)

    return maximum_happiness


def run_test(people, happiness, person1, person2, expected_value):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = happiness[person1+person2]

    if result != expected_value:
        print "Test for data '{0} next to {1}' FAILED. Got a result of {2}, not {3}".format(person1, person2, result, expected_value)
        sys.exit(-1)

    print "Test for '{0} next to {1}' passed.".format(person1, person2)


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_input="""Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""

people, happiness = process_input(test_input)

run_test(people, happiness, 'Alice', 'David', -2)
run_test(people, happiness, 'David', 'Alice', 46)
run_test(people, happiness, 'Bob', 'Alice', 83)
run_test(people, happiness, 'Alice', 'Bob', 54)
run_test(people, happiness, 'Carol', 'Bob', 60)
run_test(people, happiness, 'Bob', 'Carol', -7)
run_test(people, happiness, 'Carol', 'David', 55)
run_test(people, happiness, 'David', 'Carol', 41)

assert calc_optimal_seating(people, happiness) == 330

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual data now.

with open("input.txt", "r") as f:
    input_data = f.read()

    people, happiness = process_input(input_data)

    for person in people:
        happiness['Self' + person] = 0
        happiness[person + 'Self'] = 0
    people.add('Self')

    print "Optimal: {}".format(calc_optimal_seating(people, happiness))
