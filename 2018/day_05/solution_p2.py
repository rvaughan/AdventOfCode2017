#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 5 of the Advent of Code for 2018.
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


def redact_polymer(polymer, redact_letter):
    new_polymer = ''

    test_letter = redact_letter.upper()

    for letter in polymer:
        if letter.upper() != test_letter:
            new_polymer += letter

    return new_polymer


def run_redact_test(test_input, redact_letter, expected_output):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    new_polymer = redact_polymer(test_input, redact_letter)

    if new_polymer != expected_output:
        print "Test redaction for '{}' in '{}' FAILED. Got a result of '{}' but expected '{}'".format(redact_letter, test_input, new_polymer, expected_output)
        sys.exit(-1)

    print "Test redaction for '{}' in '{}' passed.".format(redact_letter, test_input)


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
        print "Test step for '{0}' FAILED. Got a result of '{1}' but expected '{2}'".format(test_input, output, expected_output)
        sys.exit(-1)

    print "Test step for {0} passed.".format(test_input)


def run_full_test(test_input, expected_redaction, expected_output):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """

    best_letter = ''
    best_change = 99999999999999999
    best_output = ""

    for redaction in 'abcdefghijklmnopqrstuvwxyz':
        changes_made = True
        input_data = redact_polymer(test_input, redaction)
        while changes_made:
            input_data, changes_made = process_polymer(input_data)

        if len(input_data) < best_change:
            best_letter = redaction
            best_change = len(input_data)
            best_output = input_data

    if best_output != expected_output:
        print "Full test for '{}' FAILED. Got a result of '{}' using '{}' but expected '{}' using '{}'".format(test_input, best_output, best_letter, expected_output, expected_redaction)
        sys.exit(-1)

    print "Full test for {0} passed.".format(test_input)


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

run_redact_test("dabAcCaCBAcCcaDA", "a", "dbcCCBcCcD")
run_test("dbcCCBcCcD", "dbCBcD")

run_redact_test("dabAcCaCBAcCcaDA", "b", "daAcCaCAcCcaDA")
run_test("daAcCaCAcCcaDA", "daCAcaDA")

run_redact_test("dabAcCaCBAcCcaDA", "c", "dabAaBAaDA")
run_test("dabAaBAaDA", "daDA")

run_redact_test("dabAcCaCBAcCcaDA", "d", "abAcCaCBAcCcaA")
run_test("abAcCaCBAcCcaA", "abCBAc")

run_full_test("dabAcCaCBAcCcaDA", "c", "daDA")

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    file_data = f.read()

    best_letter = ''
    best_change = 99999999999999999
    best_output = ""

    for redaction in 'abcdefghijklmnopqrstuvwxyz':
        changes_made = True
        input_data = redact_polymer(file_data, redaction)
        while changes_made:
            input_data, changes_made = process_polymer(input_data)

        if len(input_data) < best_change:
            best_letter = redaction
            best_change = len(input_data)
            best_output = input_data

    print best_change
    print best_output
    print best_letter

    print "Solution is {0}".format(len(best_output))
