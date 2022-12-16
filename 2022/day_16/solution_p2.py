#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 16 of the Advent of Code for 2022.
"""
import itertools
import sys


def get_valves(config):
    valves = {}

    for line in config:
        parts = line.split()
        valve = parts[1]
        flow_rate = int(parts[4][5:-1])
        lead_to = ''.join(parts[9:]).split(',')
        valves[valve] = {
            'flow': flow_rate,
            'tunnels': lead_to,
            'paths': {}
        }

    keys = sorted([x for x in list(valves.keys()) if valves[x]['flow'] != 0])

    def bfs(frontier, end):
        depth = 1
        while True:
            next_frontier = set()
            for x in frontier:
                if x == end:
                    return depth
                for y in valves[x]['tunnels']:
                    next_frontier.add(y)
            frontier = next_frontier
            depth += 1

    for k in keys + ['AA']:
        for k2 in keys:
            if k2 != k:
                valves[k]['paths'][k2] = bfs(valves[k]['tunnels'], k2)

    return valves


def calculate_solution(config):
    valves = get_valves(config)

    best = 0

    def search(opened, flowed, current_room, depth_to_go, elephants_turn):
        nonlocal best
        if flowed > best:
            best = flowed

        if depth_to_go <= 0:
            return

        if current_room not in opened:
            search(opened.union([current_room]), flowed + valves[current_room]['flow'] * depth_to_go, current_room, depth_to_go - 1, elephants_turn)
            if not elephants_turn:
                search(set([current_room]).union(opened), flowed +
                       valves[current_room]['flow'] * depth_to_go, 'AA', 25, True)
        else:
            for k in [x for x in valves[current_room]['paths'].keys() if x not in opened]:
                search(opened, flowed, k, depth_to_go -
                       valves[current_room]['paths'][k], elephants_turn)

    search(set(['AA']), 0, 'AA', 25, False)

    return best


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

test_list = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

result = run_test(test_list, 1707)

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
