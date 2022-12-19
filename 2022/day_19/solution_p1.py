#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 19 of the Advent of Code for 2022.
"""
from collections import deque
import sys


def build_blueprints(entries):
    blueprints = []

    for entry in entries:
        robots = entry.split('.')

        robot_requirements = (
            int(robots[0].split(' ')[1].replace(':', '')),  # Blueprint id
            # ore cost, c_cost, ob_cost_ore, ob_cost_clay, g_cost_ore, g_cost_obs
            int(robots[0].split(' ')[-2]),
            int(robots[1].split(' ')[-2]),
            int(robots[2].split(' ')[-5]),
            int(robots[2].split(' ')[-2]),
            int(robots[3].split(' ')[-5]),
            int(robots[3].split(' ')[-2])
        )

        blueprints.append(robot_requirements)

    return blueprints


def solve(o_cost, c_cost, ob_cost_ore, ob_cost_clay, g_cost_ore, g_cost_obs, max_time):
    """
    Solve for a given blueprint.

    Params:
    -------
    ore_cost, clay_cost, obsidian_cost_ore, obsidian_cost_clay, geode_cost_ore, geode_cost_clay
    o_cost - The amount of ore required to build an ore robot.
    c_cost - The amount of ore required to build a clay robot.
    ob_cost_ore - The amount of ore required to make an obsidian robot.
    ob_cost_clay - The amount of clay required to make an obsidian robot.
    g_cost_ore - The amount of ore required to make an geode robot.
    g_cost_obs - The amount of obsidian required to make an geode robot.
    max_time - The maximum time to run.

    Returns:
    --------
    The most number of geodes that can be produced by this blueprint.
    """
    best = 0

    # state is (ore, clay, obsidian, geodes, ore_robots, clay_robots, obsidian_robots, geode_robots, time)
    state = (0, 0, 0, 0, 1, 0, 0, 0, max_time)

    search_space = deque([state])
    seen_states = set()
    while search_space:
        state = search_space.popleft()
        # print(state)
        o, c, ob, g, r1, r2, r3, r4, time_s = state

        best = max(best, g)
        if time_s == 0:
            continue

        # What's the most number of ore robots we can build?
        max_ore = max([o_cost, c_cost, ob_cost_ore, g_cost_ore])

        if r1 >= max_ore:
            r1 = max_ore

        if r2 >= ob_cost_clay:
            r2 = ob_cost_clay

        if r3 >= g_cost_obs:
            r3 = g_cost_obs

        if o >= time_s * max_ore - r1 * (time_s - 1):
            o = time_s * max_ore - r1 * (time_s - 1)

        if c >= time_s * ob_cost_clay - r2 * (time_s - 1):
            c = time_s * ob_cost_clay - r2 * (time_s - 1)

        if ob >= time_s * g_cost_obs - r3 * (time_s - 1):
            ob = time_s * g_cost_obs - r3 * (time_s - 1)

        state = (o, c, ob, g, r1, r2, r3, r4, time_s)

        if state in seen_states:
            continue

        seen_states.add(state)

        if len(seen_states) % 1000000 == 0:
            print(time_s, best, len(seen_states))

        assert o >= 0 and c >= 0 and ob >= 0 and g >= 0, state

        search_space.append((o + r1, c + r2, ob + r3, g + r4, r1, r2, r3, r4, time_s - 1))

        if o >= o_cost:  # build an ore robot
            search_space.append((o - o_cost + r1, c + r2, ob + r3, g +
                     r4, r1 + 1, r2, r3, r4, time_s - 1))

        if o >= c_cost:  # build a clay robot
            search_space.append((o - c_cost + r1, c + r2, ob + r3, g +
                     r4, r1, r2 + 1, r3, r4, time_s - 1))

        if o >= ob_cost_ore and c >= ob_cost_clay:  # build an obsidian robot
            search_space.append((o - ob_cost_ore + r1, c - ob_cost_clay + r2,
                     ob + r3, g + r4, r1, r2, r3 + 1, r4, time_s - 1))

        if o >= g_cost_ore and ob >= g_cost_obs: # build a geode robot
            search_space.append((o - g_cost_ore + r1, c + r2, ob - g_cost_obs +
                     r3, g + r4, r1, r2, r3, r4 + 1, time_s - 1))

    return best


def calculate_solution(items):
    blueprints = build_blueprints(items)

    scores = 0
    for blueprint in blueprints:
        b_id, o_cost, c_cost, ob_cost_ore, ob_cost_clay, g_cost_ore, g_cost_obs = blueprint
        scores += (b_id * solve(o_cost, c_cost, ob_cost_ore,
                   ob_cost_clay, g_cost_ore, g_cost_obs, 24))

    return scores


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

test_list = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian."""
result = run_test(test_list, 9)

test_list = """Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""
result = run_test(test_list, 24)

test_list = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""
result = run_test(test_list, 33)

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
