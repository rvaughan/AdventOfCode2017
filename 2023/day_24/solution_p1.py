#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 24 of the Advent of Code for 2023.
"""
import sys


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


def hail_to_line(h):
    p,v = h
    p1 = (p[0], p[1])
    p2 = (p[0] + v[0], p[1] + v[1])

    pt = [p1, p2]

    return pt


def sign(a):
    if a < 0:
        return -1
    elif a == 0:
        return 0
    else:
        return 1


def check_intersection(a,b):
    intersect = line_intersection(hail_to_line(a), hail_to_line(b))
    if intersect != None:
        def crossed_future(sect, a):
            sx,sy = sect

            return sign(sx - a[0][0]) == sign(a[1][0]) and sign(sy - a[0][1]) == sign(a[1][1])
      
        if crossed_future(intersect, a) and crossed_future(intersect, b):
            return intersect
      
    return None


def calculate_solution(items, start_loc, end_loc):
    result = 0

    hailstones = []
    for line in items:
        points, velocities = line.split(' @ ')
        position = [int(i) for i in points.split(',')]
        velocity = [int(i) for i in velocities.split(',')]

        hailstones.append((position, velocity))

    for i, a in enumerate(hailstones):
        for j, b in enumerate(hailstones):
            if i == j:
                break
    
            intersect = check_intersection(a, b)

            if intersect != None and start_loc <= intersect[0] <= end_loc and  start_loc <= intersect[1] <= end_loc:
                result += 1

    return result


def run_test(test_input, start_loc, end_loc, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'), start_loc, end_loc)

    print()
    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""
result = run_test(test_list, 7, 27, 2)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input.txt', 'r') as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data, 200000000000000, 400000000000000)

    print(f'Solution is {answer}')
