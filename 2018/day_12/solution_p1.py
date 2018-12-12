#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 11 of the Advent of Code for 2018.
"""

def read_input(input_data):
    initial_state = input_data[0].split(' ')[2]
    states = {}

    for idx in xrange(2, len(input_data)):
        pieces = input_data[idx].split(' ')
        states[pieces[0]] = pieces[2]

    return initial_state, states


def calc_score(current_state, first):
    score = 0

    for val, pot in zip(xrange(first, len(current_state)), current_state):
        if pot == "#":
            score += val

    return score


def next_state(states, current_state, first=0):
    # print "  ", current_state

    new_state = ".."
    plant_count = 0

    for idx in xrange(len(current_state)):
        check_state = ""

        if idx == 0:
            check_state = ".." + current_state[:3]
            # print ">", check_state
        elif idx == 1:
            check_state = "." + current_state[:4]
            # print ">>", check_state
        else:
            check_state = current_state[idx-2:idx+3]
            # print idx, idx+5, current_state, check_state
            while len(check_state) < 5:
                check_state += "."

        if check_state in states:
            new_state += states[check_state]
            if states[check_state] == "#":
                # print idx, first, (first + idx)
                plant_count += (first + idx)
            
            # print check_state, states[check_state], plant_count, idx, idx+5
        else:
            new_state += "."

            # print check_state, ".", plant_count, idx, idx+5

    new_state += ".."

    return new_state, plant_count


def dump_state(generation, current_state, indent=0, score=0):
    # print indent
    ps = current_state

    while indent > 0:
        ps = "." + ps
        indent -= 1

    if indent < -3:
        # print indent, (abs(indent) -3)
        # print "   ", ps
        ps = ps[(abs(indent) -4):]
        # print "   ", ps

    print "[{:02}] {:03} {}".format(generation, score, ps)


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

print ""
print "-----------------"
print "Testing.........."
print "-----------------"
print ""

test_input="""initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #"""

input_data = [line for line in test_input.splitlines()]

generation = 0
first = 0
current_state, states = read_input(input_data)

ns = states["..#.."]
assert ns == "#", ns

ns = states[".#.#."]
assert ns == "#", ns

ns = states[".##.."]
assert ns == "#", ns

score = calc_score("...#..#.#..##......###...###...........", -3)
assert score == 145, score
score = calc_score("...#...#....#.....#..#..#..#...........", -3)
assert score == 91, score
score = calc_score("...##..##...##....#..#..#..##..........", -3)
assert score == 132, score
score = calc_score("..#.#...#..#.#....#..#..#...#..........", -3)
assert score == 102, score
score = calc_score("...#.#..#...#.#...#..#..##..##.........", -3)
assert score == 154, score
score = calc_score("....#...##...#.#..#..#...#...#.........", -3)
assert score == 115, score
score = calc_score("....##.#.#....#...#..##..##..##........", -3)
assert score == 174, score
score = calc_score("...#..###.#...##..#...#...#...#........", -3)
assert score == 126, score
score = calc_score("....##.#.#....#...#..##..##..##........", -3)
assert score == 174, score
score = calc_score("...#..###.#...##..#...#...#...#........", -3)
assert score == 126, score
score = calc_score("...#....##.#.#.#..##..##..##..##.......", -3)
assert score == 213, score
score = calc_score(".#....##....#####...#######....#.#..##.", -3)
assert score == 325, score

answers = """...#...#....#.....#..#..#..#...........
...##..##...##....#..#..#..##..........
..#.#...#..#.#....#..#..#...#..........
...#.#..#...#.#...#..#..##..##.........
....#...##...#.#..#..#...#...#.........
....##.#.#....#...#..##..##..##........
...#..###.#...##..#...#...#...#........
...#....##.#.#.#..##..##..##..##.......
...##..#..#####....#...#...#...#.......
..#.#..#...#.##....##..##..##..##......
...#...##...#.#...#.#...#...#...#......
...##.#.#....#.#...#.#..##..##..##.....
..#..###.#....#.#...#....#...#...#.....
..#....##.#....#.#..##...##..##..##....
..##..#..#.#....#....#..#.#...#...#....
.#.#..#...#.#...##...#...#.#..##..##...
..#...##...#.#.#.#...##...#....#...#...
..##.#.#....#####.#.#.#...##...##..##..
.#..###.#..#.#.#######.#.#.#..#.#...#..
.#....##....#####...#######....#.#..##."""
real_scores = []
for a in answers.splitlines():
    real_scores.append(calc_score(a, -3))



dump_state(generation, current_state, first)

generation += 1
current_state, num_pots = next_state(states, current_state, first)
dump_state(generation, current_state, first)
score = calc_score(current_state, first-2)
assert score == 91, score
assert real_scores[0] == score, score
assert num_pots == 91, num_pots
assert current_state == "..#...#....#.....#..#..#..#..", current_state
assert current_state[2] == "#"
assert current_state[3] == "."
assert current_state[4] == "."

generation += 1
first -= 2
current_state, num_pots = next_state(states, current_state, first)
dump_state(generation, current_state, first)
score = calc_score(current_state, first-2)
assert score == 132, score
assert real_scores[1] == score, score
assert num_pots == 132, num_pots
assert current_state == "....##..##...##....#..#..#..##...", current_state
assert current_state[4] == "#"
assert current_state[5] == "#"
assert current_state[6] == "."

generation += 1
first -= 2
current_state, num_pots = next_state(states, current_state, first)
dump_state(generation, current_state, first)
score = calc_score(current_state, first-2)
assert score == 102, score
assert real_scores[2] == score, score
assert num_pots == 102, num_pots
assert current_state == ".....#.#...#..#.#....#..#..#...#.....", current_state
assert current_state[5] == "#", current_state
assert current_state[6] == ".", current_state
assert current_state[7] == "#", current_state

generation += 1
first -= 2
current_state, num_pots = next_state(states, current_state, first)
dump_state(generation, current_state, first)
score = calc_score(current_state, first-2)
assert score == 154, score
assert real_scores[3] == score, score
assert num_pots == 154, num_pots
assert current_state == "........#.#..#...#.#...#..#..##..##......", current_state

generation += 1
first -= 2
current_state, num_pots = next_state(states, current_state, first)
dump_state(generation, current_state, first)
score = calc_score(current_state, first-2)
assert score == 115, score
assert real_scores[4] == score, score
assert num_pots == 115, num_pots

generation += 1
first -= 2
current_state, num_pots = next_state(states, current_state, first)
dump_state(generation, current_state, first)
score = calc_score(current_state, first-2)
assert score == 174, score
assert real_scores[5] == score, score
assert num_pots == 174, num_pots

generation += 1
first -= 2
current_state, num_pots = next_state(states, current_state, first)
dump_state(generation, current_state, first)
score = calc_score(current_state, first-2)
assert score == 126, score
assert real_scores[6] == score, score
assert num_pots == 126, num_pots

generation += 1
first -= 2
current_state, num_pots = next_state(states, current_state, first)
dump_state(generation, current_state, first)
score = calc_score(current_state, first-2)
assert score == 213, score
assert real_scores[7] == score, score
assert num_pots == 213, num_pots

generation += 1
first -= 2
current_state, num_pots = next_state(states, current_state, first)
dump_state(generation, current_state, first)
score = calc_score(current_state, first-2)
assert score == 138, score
assert real_scores[8] == score, score
assert num_pots == 138, num_pots

input_data = [line for line in test_input.splitlines()]
generation = 0
first = 0
current_state, states = read_input(input_data)
for _ in xrange(20):
    current_state, num_pots = next_state(states, current_state, first)
    dump_state(generation, current_state, first, num_pots)
    score = calc_score(current_state, first-2)
    assert real_scores[generation] == score, generation
    first -= 2
    generation += 1
score = calc_score(current_state, first)
assert score == 325, score
assert num_pots == 325, num_pots

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = [line.strip() for line in f]

    first = 0
    current_state, states = read_input(input_data)
    num_pots = 0

    for _ in xrange(20):
        current_state, num_pots = next_state(states, current_state, first)
        first -= 2

    score = calc_score(current_state, first)
    assert score == 325, score

    print "Solution is {}".format(score)
