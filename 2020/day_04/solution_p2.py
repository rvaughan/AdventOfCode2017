#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 4 of the Advent of Code for 2020.
"""
import re
import sys


def valid_birthday(value):
    byr = int(value)
    if byr >= 1920 and byr <= 2002:
        return True

    return False


def valid_issue_year(value):
    iyr = int(value)
    if iyr >= 2010 and iyr <= 2020:
        return True

    return False


def valid_expiry_year(value):
    eyr = int(value)
    if eyr >= 2020 and eyr <= 2030:
        return True

    return False


def valid_height(value):
    try:
        height = int(value[:-2])
        units = value[-2:]
        if units == 'cm':
            if height >= 150 and height <= 193:
                return True
        elif units == 'in':
            if height >= 59 and height <= 76:
                return True
    except:
        pass

    return False


def valid_hair_colour(value):
    return re.match(r'#([0-9a-f]){6}', value) is not None


def valid_eye_colour(value):
    valid = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if value in valid:
        return True

    return False


def valid_passport_id(value):
    try:
        pid = int(value)
        if len(value) == 9:
            return True
    except:
        pass

    return False


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
        code, value = code_str.split(':')
        if code in expected:
            if code == 'byr':
                if not valid_birthday(value):
                    continue
            elif code == 'iyr':
                if not valid_issue_year(value):
                    continue
            elif code == 'eyr':
                if not valid_expiry_year(value):
                    continue
            elif code == 'hgt':
                if not valid_height(value):
                    continue
            elif code == 'hcl':
                if not valid_hair_colour(value):
                    continue
            if code == 'ecl':
                if not valid_eye_colour(value):
                    continue
            if code == 'pid':
                if not valid_passport_id(value):
                    continue
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

assert valid_birthday("1919") == False
assert valid_birthday("1920") == True
assert valid_birthday("2002") == True
assert valid_birthday("2003") == False

assert valid_issue_year("2009") == False
assert valid_issue_year("2010") == True
assert valid_issue_year("2020") == True
assert valid_issue_year("2021") == False

assert valid_expiry_year("2019") == False
assert valid_expiry_year("2020") == True
assert valid_expiry_year("2030") == True
assert valid_expiry_year("2031") == False

assert valid_height("1in") == False
assert valid_height("58in") == False
assert valid_height("59in") == True
assert valid_height("69in") == True
assert valid_height("76in") == True
assert valid_height("77in") == False
assert valid_height("1cm") == False
assert valid_height("10cm") == False
assert valid_height("149cm") == False
assert valid_height("150cm") == True
assert valid_height("190cm") == True
assert valid_height("193cm") == True
assert valid_height("194cm") == False
assert valid_height("190in") == False
assert valid_height("190") == False
assert valid_height("") == False
assert valid_height("monkeys") == False
assert valid_height("34monkeys") == False
assert valid_height("193mn") == False

assert valid_hair_colour("#123abc") == True
assert valid_hair_colour("#123abz") == False
assert valid_hair_colour("#123abz") == False
assert valid_hair_colour("#000000") == True
assert valid_hair_colour("#999999") == True
assert valid_hair_colour("#aaaaaa") == True
assert valid_hair_colour("#cccccc") == True
assert valid_hair_colour("#dddddd") == True
assert valid_hair_colour("#gggggg") == False
assert valid_hair_colour("123abc") == False
assert valid_hair_colour("#") == False
assert valid_hair_colour("#0") == False
assert valid_hair_colour("#00") == False
assert valid_hair_colour("#000") == False
assert valid_hair_colour("#0000") == False
assert valid_hair_colour("#00000") == False

assert valid_eye_colour("amb") == True
assert valid_eye_colour("blu") == True
assert valid_eye_colour("brn") == True
assert valid_eye_colour("gry") == True
assert valid_eye_colour("grn") == True
assert valid_eye_colour("hzl") == True
assert valid_eye_colour("oth") == True
assert valid_eye_colour("wat") == False
assert valid_eye_colour("aaa") == False
assert valid_eye_colour("zzz") == False
assert valid_eye_colour("") == False

assert valid_passport_id("") == False
assert valid_passport_id("0") == False
assert valid_passport_id("00") == False
assert valid_passport_id("000") == False
assert valid_passport_id("0000") == False
assert valid_passport_id("00000") == False
assert valid_passport_id("000000") == False
assert valid_passport_id("0000000") == False
assert valid_passport_id("00000000") == False
assert valid_passport_id("000000001") == True
assert valid_passport_id("999999999") == True
assert valid_passport_id("0123456789") == False
assert valid_passport_id("abcdefghi") == False

passport = [
    "eyr:1972 cid:100",
    "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
]
assert check_passport(passport) == False

passport = [
    "iyr:2019",
    "hcl:#602927 eyr:1967 hgt:170cm",
    "ecl:grn pid:012533040 byr:1946",
]
assert check_passport(passport) == False

passport = [
    "hcl:dab227 iyr:2012",
    "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
]
assert check_passport(passport) == False

passport = [
    "hgt:59cm ecl:zzz",
    "eyr:2038 hcl:74454a iyr:2023",
    "pid:3556412378 byr:2007"
]
assert check_passport(passport) == False

passport = [
    "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
    "hcl:#623a2f"
]
assert check_passport(passport) == True

passport = [
    "eyr:2029 ecl:blu cid:129 byr:1989",
    "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm"
]
assert check_passport(passport) == True

passport = [
    "hcl:#888785",
    "hgt:164cm byr:2001 iyr:2015 cid:88",
    "pid:545766238 ecl:hzl",
    "eyr:2022"
]
assert check_passport(passport) == True

passport = [
    "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"
]
assert check_passport(passport) == True

test_data = [
    "eyr:1972 cid:100",
    "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
    "",
    "iyr:2019",
    "hcl:#602927 eyr:1967 hgt:170cm",
    "ecl:grn pid:012533040 byr:1946",
    "",
    "hcl:dab227 iyr:2012",
    "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
    "",
    "hgt:59cm ecl:zzz",
    "eyr:2038 hcl:74454a iyr:2023",
    "pid:3556412378 byr:2007",
    "",
    "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
    "hcl:#623a2f",
    "",
    "eyr:2029 ecl:blu cid:129 byr:1989",
    "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
    "",
    "hcl:#888785",
    "hgt:164cm byr:2001 iyr:2015 cid:88",
    "pid:545766238 ecl:hzl",
    "eyr:2022",
    "",
    "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"
]
result = run_test(test_data, 4)

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
