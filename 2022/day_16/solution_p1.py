#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 16 of the Advent of Code for 2022.
"""

import sys


def get_valves(config):
    valves = {}

    for line in config:
        parts = line.split()
        valve = parts[1]
        flow_rate = int(parts[4][5:-1])
        lead_to = ''.join(parts[9:]).split(',')
        valves[valve] = (flow_rate, lead_to)

    # We will create a bitmap index to allow us to interrogate the system more easily
    bitmap_idx = {}
    for key in sorted(valves.keys()):
        bitmap_idx[key] = 1 << len(bitmap_idx)

    valves = {
        bitmap_idx[valve]: (flow_rate, tuple(map(bitmap_idx.get, lead_to))) for valve, (flow_rate, lead_to) in valves.items()
    }

    return valves, bitmap_idx


def calculate_solution(config):
    valves, bitmap_idx = get_valves(config)
    
    TOTAL_TIME = 30

    states = [(bitmap_idx['AA'], 0, 0)]

    best = {}

    for t in range(1, TOTAL_TIME + 1):
        new_states = []
        for loc, opened, pressure in states:
            key = (loc, opened)
            if key in best and pressure <= best[key]:
                continue

            best[key] = pressure

            flow_rate, lead_to = valves[loc]
            if loc & opened == 0 and flow_rate > 0:
                new_states.append((loc, opened | loc, pressure + flow_rate * (TOTAL_TIME - t)))
            
            for dest in lead_to:
                new_states.append((dest, opened, pressure))

        states = new_states

    return max(pressure for _, _, pressure in states)


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

result = run_test(test_list, 1651)

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
