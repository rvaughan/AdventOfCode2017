#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 24 of the Advent of Code for 2023.

For this solution you will need to install Z3, so to run use:

python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python3 solution_p2.py

"""
import sys

import z3


def calculate_solution(items):
    result = 0

    hailstones = []
    for line in items:
        points, velocities = line.split(' @ ')
        position = [int(i) for i in points.split(',')]
        velocity = [int(i) for i in velocities.split(',')]

        hailstones.append((position, velocity))

    solver = z3.Solver()
    x, y, z, vx, vy, vz = [z3.Int(var) for var in ["x", "y", "z", "vx", "vy", "vz"]]

    # There are 4 unknowns, so...
    for itx in range(4):
        (cpx, cpy, cpz), (cvx, cvy, cvz) = hailstones[itx]

        t = z3.Int(f"t{itx}")
        solver.add(t >= 0)
        solver.add(x + vx * t == cpx + cvx * t)
        solver.add(y + vy * t == cpy + cvy * t)
        solver.add(z + vz * t == cpz + cvz * t)

    if solver.check() == z3.sat:
        model = solver.model()
        (x, y, z) = (model.eval(x), model.eval(y), model.eval(z))
        result = x.as_long() + y.as_long() + z.as_long()

    return result


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'))

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
result = run_test(test_list, 47)

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
