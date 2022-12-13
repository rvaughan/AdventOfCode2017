#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 13 of the Advent of Code for 2022.
"""
import json
import sys


## ABANDONED CODE - START ##

# DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# def compare(left, right, indent=0):
#     """
#     Returns:
#     -1 : left is lower than right
#     0 : left is equal to right
#     1 : left is greater than right
#     """
#     print(f'-----------> [{indent:2}]')
#     print(left)
#     print(right)
#     if len(left) == 0 or len(right) == 0:
#         return 0

#     left_pos = 0
#     right_pos = 0

#     while left_pos < len(left) and right_pos < len(right):
#         print(f'[{indent:2}]  pos {left_pos} {right_pos}')
#         print(f'    l', left[left_pos:])
#         print(f'    r', right[right_pos:])

#         if left.startswith('[') and right.startswith('['):
#             print(f'[{indent:2}] brackets')
#             # Don't want the outer square brackets in the next comparison
#             l_bracket_pos=left[left_pos:].find(']')
#             if l_bracket_pos == -1:
#                 l_bracket_pos=len(left)
#             else:
#                 l_bracket_pos += left_pos

#             r_bracket_pos=right[right_pos:].find(']')
#             if r_bracket_pos == -1:
#                 r_bracket_pos=len(right)
#             else:
#                 r_bracket_pos += right_pos
#             result=compare(left[left_pos:l_bracket_pos], right[right_pos:r_bracket_pos], indent+1)
#             if result != 0:
#                 return result

#             left_pos += l_bracket_pos
#             right_pos += r_bracket_pos
#         elif left[left_pos] in DIGITS and right[right_pos] in DIGITS:
#             print(f'[{indent:2}] digits', left[left_pos], right[right_pos])
#             end=left[left_pos:].find(',')
#             if end == -1:
#                 end=len(left)
#             left_digits=left[left_pos:left_pos+end]

#             end=right[right_pos:].find(',')
#             if end == -1:
#                 end=len(right)
#             right_digits=right[right_pos:right_pos+end]

#             left_pos += end + 1
#             right_pos += end + 1

#             if int(left_digits) < int(right_digits):
#                 return -1
#             elif int(left_digits) > int(right_digits):
#                 return 1
#         elif left[left_pos] in DIGITS:
#             print(f'[{indent:2}] ldig')
#             end=left[left_pos:].find(',')
#             if end == -1:
#                 end=len(left)
#             left_digits=f'[{left[left_pos:left_pos+end]}]'

#             left_pos += end + 1

#             result=compare(left_digits, right[right_pos:], indent+1)

#             if result != 0:
#                 return result
#         elif right[right_pos] in DIGITS:
#             print(f'[{indent:2}] rdig')
#             end=right[right_pos:].find(',')
#             if end == -1:
#                 end=len(right)
#             right_digits=f'[{right[right_pos:right_pos+end]}]'

#             right_pos += end + 1

#             result=compare(left[left_pos:], right_digits, indent+1)

#             if result != 0:
#                 return result
#         else:
#             print(f'[{indent:2}] drop')
#             if left[left_pos] == ' ' or left[left_pos] == ']' or left[left_pos] == ',':
#                 left_pos += 1

#             if right[right_pos] == ' ' or right[right_pos] == ']' or right[right_pos] == ',':
#                 right_pos += 1

#     return 0

## ABANDONED CODE - END ##


def compare(left, right):
    max_length = max(len(left), len(right))
    for idx in range(max_length):
        if idx == len(left) and idx < len(right):
            return -1
        if idx < len(left) and idx == len(right):
            return 1

        l_val = left[idx]
        r_val = right[idx]
        if type(l_val) == list and type(r_val) == list:
            result = compare(l_val, r_val)
            if result != 0:
                return result
        elif type(l_val) == int and type(r_val) == int:
            if int(l_val) < int(r_val):
                return -1
            elif int(l_val) > int(r_val):
                return 1
        elif type(l_val) == int and type(r_val) == list:
            result = compare([l_val], r_val)
            if result != 0:
                return result
        else:
            result = compare(l_val, [r_val])
            if result != 0:
                return result

    return 0


def calculate_solution(items):
    idx = 0
    pair = 1
    correct = []
    while idx < len(items):
        left = items[idx]
        right = items[idx + 1]

        correct_order = compare(json.loads(left), json.loads(right))
        if correct_order == -1:
            correct.append(pair)

        pair += 1
        idx += 3

    return sum(correct)


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'))

    if result != expected_solution:
        print(
            f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """[1, 1, 3, 1, 1]
[1, 1, 5, 1, 1]

[[1], [2, 3, 4]]
[[1], 4]

[9]
[[8, 7, 6]]

[[4, 4], 4, 4]
[[4, 4], 4, 4, 4]

[7, 7, 7, 7]
[7, 7, 7]

[]
[3]

[[[]]]
[[]]

[1, [2, [3, [4, [5, 6, 7]]]], 8, 9]
[1, [2, [3, [4, [5, 6, 0]]]], 8, 9]"""

result = run_test(test_list, 13)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data)

    print(f'Solution is {answer}')
