#!/usr/bin/env python3
"""
This code holds the solution for part 1 of day 5 of the Advent of Code for 2023.
"""
import sys


def get_dest(map, seed):
    return map[seed] if seed in map else seed


def get_dest_2(map, seed):
    for x in map:
        # print(x)
        if seed >= x[1]:
            # print('a', seed, x[1], x[1] + x[2])
            if seed < x[1] + x[2]:
                # print('b', x[0], (x[1] + x[2]), (seed - x[1]))
                return x[0] + (seed - x[1])
        
    return seed


def calculate_solution(items):
    maps = []

    seeds = [int(x) for x in items[0].split()[1:]]

    # First build up the map data
    first = True
    map_data = []
    for line in items[2:]:
        if first:
            first = False
            continue

        if line == '':
            maps.append(map_data)
            # print(map_data)
            map_data = []
            first = True
            continue

        parts = [int(x) for x in line.split()]
        
        # # print(parts)
        # for dest, seed in zip(range(parts[0], parts[0] + parts[2]), range(parts[1], parts[1] + parts[2])):
        #     map_data[seed] = dest

        map_data.append(parts)


    if len(map_data) > 0:
        maps.append(map_data)

    # print(get_dest_2(maps[0], 98))
    # assert(get_dest_2(maps[0], 98)) == 50
    # assert(get_dest_2(maps[0], 99)) == 51
    # assert(get_dest_2(maps[0], 10)) == 10

    min_location = 9999999999
    # print(seeds)
    for x in range(0, len(seeds), 2):
        # print('a', x, seeds[x], seeds[x+1])
        for seed in range(seeds[x], seeds[x] + seeds[x+1]):
            loc = seed
            for map in maps:
                loc = get_dest_2(map, loc)

            min_location = min(min_location, loc)

    # assert(min_location == 82)
    x

    return min_location


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'))

    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

result = run_test(test_list, 46)

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
