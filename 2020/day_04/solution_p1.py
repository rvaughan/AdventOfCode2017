#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 4 of the Advent of Code for 2020.
"""
import sys


def check_passport(passport):
    expected = {
        'byr': False,
        'iyr': False,
        'eyr': False,
        'hgt': False,
        'hcl': False,
        'ecl': False,
        'pid': False,
        # 'cid': False
    }
    codes = " ".join(passport).split(' ')

    for code_str in codes:
        code = code_str.split(':')[0]
        if code in expected:
            expected[code] = True

    for code in expected:
        if not expected[code]:
            return False

    return True

def calculate_solution(passports):
    count = 0
    passport = []
    for line in passports:
        if line != '':
            passport.append(line)
        else:
            if check_passport(passport):
                count += 1
            passport = []

    if passport != []:
        if check_passport(passport):
            count += 1
        passport = []

    return count


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input)

    if result != expected_solution:
        print("Test for input {0} FAILED. Got a result of {1}, not {2}".format(test_input, result, expected_solution))
        sys.exit(-1)

    print("Test for input {0} passed.".format(test_input))

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

passport = [
    "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
    "byr:1937 iyr:2017 cid:147 hgt:183cm",
]
assert check_passport(passport) == True

passport = [
    "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
    "hcl:#cfa07d byr:1929",
]
assert check_passport(passport) == False

passport = [
    "hcl:#ae17e1 iyr:2013",
    "eyr:2024",
    "ecl:brn pid:760753108 byr:1931",
    "hgt:179cm",
]
assert check_passport(passport) == True

passport = [
    "hcl:#cfa07d eyr:2025 pid:166559648",
    "iyr:2011 ecl:brn hgt:59in"
]
assert check_passport(passport) == False

test_list = [
    "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
    "byr:1937 iyr:2017 cid:147 hgt:183cm",
    "",
    "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
    "hcl:#cfa07d byr:1929",
    "",
    "hcl:#ae17e1 iyr:2013",
    "eyr:2024",
    "ecl:brn pid:760753108 byr:1931",
    "hgt:179cm",
    "",
    "hcl:#cfa07d eyr:2025 pid:166559648",
    "iyr:2011 ecl:brn hgt:59in"
]

result = run_test(test_list, 2)

print("")
print("-----------------")
print("All Tests PASSED.")
print("-----------------")
print("")

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data)

    print("Solution is {0}".format(answer))
