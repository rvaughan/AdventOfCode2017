#!/usr/bin/env python

import sys


def solve_captcha(captcha):
    solution = 0

    first = True
    last_digit = None

    for digit in captcha:
        if first:
            first_digit = digit
            first = False
        else:
            if last_digit == digit:
                solution += int(digit)

        last_digit = digit

    if last_digit == first_digit:
        solution += int(last_digit)

    return solution


def run_test(test_captcha, expected_solution):
    result = solve_captcha(test_captcha)

    if result != expected_solution:
        print "Test for captcha {0} FAILED. Got a result of {1}, not {2}".format(test_captcha, result, expected_solution)
        sys.exit(-1)

    print "Test for captcha {0} passed.".format(test_captcha)


run_test("1122", 3)
run_test("1111", 4)
run_test("1234", 0)
run_test("91212129", 9)

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input_p1.txt", "r") as f:
    captcha = f.readline()

    print "Captcha solution is {0}".format(solve_captcha(captcha))
