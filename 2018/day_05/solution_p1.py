#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 5 of the Advent of Code for 2018.
"""

from collections import Counter
import sys


def process_polymer(input_polymer):
    new_polymer = ''
    last_letter = ''
    changes_made = False

    for pos, letter in zip(xrange(len(input_polymer)), input_polymer):
        # print pos, letter, new_polymer
        if last_letter == '':
            # print "First"
            last_letter = letter
        else:
            if letter != last_letter:
                # print "...letters are different...", last_letter, letter
                if letter.upper() == last_letter.upper():
                    # print "...letters are the same one, snipping!"
                    changes_made = True

                    last_letter = ''

                    new_polymer = new_polymer[:-1]
                    new_polymer += input_polymer[pos+1:]

                    break

            # print "...ok"

        last_letter = letter

        new_polymer += last_letter

    return new_polymer, changes_made


def run_test(test_input, expected_output):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    changes_made = True
    input_data = test_input
    while changes_made:
        input_data, changes_made = process_polymer(input_data)

    if input_data != expected_output:
        print "Test for '{0}' FAILED. Got a result of '{1}' but expected '{2}'".format(test_input, input_data, expected_output)
        sys.exit(-1)

    print "Test for {0} passed.".format(test_input)


def run_step_test(test_input, expected_output, expected_changes):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    output, changes_made = process_polymer(test_input)

    if output != expected_output or changes_made != expected_changes:
        print "Test for '{0}' FAILED. Got a result of '{1}' but expected '{2}'".format(test_input, output, expected_output)
        sys.exit(-1)

    print "Test for {0} passed.".format(test_input)


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

print ""
print "-----------------"
print "Testing.........."
print "-----------------"
print ""

# run_test("aA", "")

run_step_test("abBA", "aA", True)
run_step_test("aA", "", True)

run_test("abBA", "")
run_test("abAB", "abAB")
run_test("aabAAB", "aabAAB")

run_step_test("dabAcCaCBAcCcaDA", "dabAaCBAcCcaDA", True)
run_step_test("dabAaCBAcCcaDA", "dabCBAcCcaDA", True)
run_step_test("dabCBAcCcaDA", "dabCBAcaDA", True)
run_step_test("dabCBAcaDA", "dabCBAcaDA", False)

run_test("dabAcCaCBAcCcaDA", "dabCBAcaDA")

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    changes_made = True
    input_data = f.read()
    while changes_made:
        input_data, changes_made = process_polymer(input_data)


    print "Solution is {0}".format(len(input_data))
