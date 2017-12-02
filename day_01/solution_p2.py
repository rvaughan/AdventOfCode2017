#!/usr/bin/env python

import sys


def check_digits(digit_a, digit_b):
    return digit_a == digit_b

def solve_captcha(captcha):
    solution = 0

    list_size = len(captcha)

    for idx in xrange(list_size):

        pos = idx + (list_size / 2)
        if pos >= list_size:
            pos -= list_size

        check_digit = captcha[pos]

        if check_digits(captcha[idx], check_digit):
            solution += int(captcha[idx])

    return solution


def run_test(test_captcha, expected_solution):
    result = solve_captcha(test_captcha)

    if result != expected_solution:
        print "Test for captcha {0} FAILED. Got a result of {1}, not {2}".format(test_captcha, result, expected_solution)
        sys.exit(-1)

    print "Test for captcha {0} passed.".format(test_captcha)


run_test("1212", 6)
run_test("1221", 0)
run_test("123425", 4)
run_test("123123", 12)
run_test("12131415", 4)

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    captcha = f.readline()

    print "Captcha solution is {0}".format(solve_captcha(captcha))
