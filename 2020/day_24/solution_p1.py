#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 24 of the Advent of Code for 2020.
"""
import re
import sys
from collections import defaultdict

direction = {'nw':(0, -1), 'sw':(-1, 0), 'ne':(0, 1), 'se':(0, 1), 'w':(-1, -1), 'e':(1, 1)}


def do_move(line):
    x = 0
    y = 0

    idx = 0
    while idx < len(line):
        move = line[idx]
        if line[idx] == 's' or line[idx] == 'n':
            idx += 1
            move += line[idx]
        
        idx += 1

        x += direction[move][0]
        y += direction[move][1]

    return x, y


def calculate_solution(puzzle_input):
    # white = false, black = true
    floor = defaultdict(bool)

    for line in puzzle_input:
        x, y = do_move(line)

        floor[(x,y)] = not floor[(x,y)]

        # print((x,y))

    return sum(floor.values())


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


puzzle_input = [
    "esew"
]
run_test(puzzle_input, 1)


assert do_move("nwwswee") == (0, 0)
puzzle_input = [
    "nwwswee"
]
run_test(puzzle_input, 1)


puzzle_input = [
    "sesenwnenenewseeswwswswwnenewsewsw",
    "neeenesenwnwwswnenewnwwsewnenwseswesw",
    "seswneswswsenwwnwse",
    "nwnwneseeswswnenewneswwnewseswneseene",
    "swweswneswnenwsewnwneneseenw",
    "eesenwseswswnenwswnwnwsewwnwsene",
    "sewnenenenesenwsewnenwwwse",
    "wenwwweseeeweswwwnwwe",
    "wsweesenenewnwwnwsenewsenwwsesesenwne",
    "neeswseenwwswnwswswnw",
    "nenwswwsewswnenenewsenwsenwnesesenew",
    "enewnwewneswsewnwswenweswnenwsenwsw",
    "sweneswneswneneenwnewenewwneswswnese",
    "swwesenesewenwneswnwwneseswwne",
    "enesenwswwswneneswsenwnewswseenwsese",
    "wnwnesenesenenwwnenwsewesewsesesew",
    "nenewswnwewswnenesenwnesewesw",
    "eneswnwswnwsenenwnwnwwseeswneewsenese",
    "neswnwewnwnwseenwseesewsenwsweewe",
    "wseweeenwnesenwwwswnew"
]
run_test(puzzle_input, 10)


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
