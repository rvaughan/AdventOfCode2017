#!/usr/bin/env python3
"""
This code holds the solution for part 2 of day 5 of the Advent of Code for 2023.
"""
import sys


def get_dest(map, seed):
    return map[seed] if seed in map else seed


def get_dest_2(map, seed):
    for x in map:
        if seed >= x[1]:
            if seed < x[1] + x[2]:
                return x[0] + (seed - x[1])
        
    return seed


class Processor:
    """
    Provides processing of range intervals.
    """
    def __init__(self, definition) -> None:
        # Build up the list of starting points.
        self.definitions = [[int(x) for x in line] for line in definition]

    def process_range(self, data_range):
        answers = []

        for (dest, src, size) in self.definitions:
            src_end = src + size
            next_range = []
            while data_range:
                (start, end) = data_range.pop()

                # We need to split the data into 3 parts identifying where (if)
                # the intersection appears between the range being sought, and
                # the defined range.

                # [start                                            end]
                #                 [src               src_end]
                # (BEFORE        )(INTERSECTION             )(AFTER     )

                before = (start, min(end, src))
                intersection = (max(start, src), min(src_end, end))
                after = (max(src_end, start), end)

                if before[1] > before[0]:
                    next_range.append(before)

                if intersection[1] > intersection[0]:
                    # We found an interval, so include it in our answers as we
                    # know there's only a single transform to be performed for
                    # this puzzle.
                    answers.append((intersection[0]-src+dest, intersection[1]-src+dest))

                if after[1] > after[0]:
                    next_range.append(after)

            data_range = next_range
        
        return answers + data_range


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

        map_data.append(parts)


    if len(map_data) > 0:
        maps.append(map_data)

    # Turn the list of seeds into a list of seed pairs
    seed_pairs = list(zip(seeds[::2], seeds[1::2]))

    Fs = [Processor(s) for s in maps]

    solutions = []

    for start, end in seed_pairs:
        # Inclusive on the left, exclusive on the right. i.e. a range of (1,3) = [1, 2]
        data_range = [(start, start+end)]
        for f in Fs:
            data_range = f.process_range(data_range)

        # data_range gives us back an interval, whilst data_range[0] gives us the starting point,
        # which is the correct value for the given seed range.
        solutions.append(min(data_range)[0])
    
    # Just return the minimum of all of the found solutions
    return min(solutions)


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
