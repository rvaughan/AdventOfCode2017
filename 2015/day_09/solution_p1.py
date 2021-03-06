#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 9 of the Advent of Code for 2015.
"""
import itertools
import sys


def process_routes(routes):
    locations = []
    paths = {}

    for route in routes.split('\n'):
        print route
        parts = route.split(' ')

        city1 = parts[0]
        city2 = parts[2]
        distance = int(parts[4])

        locations.append(city1)
        locations.append(city2)

        paths[city1 + city2] = distance
        paths[city2 + city1] = distance

    return set(locations), paths


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

route_input="""London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""

locations, paths = process_routes(route_input)

shortest_route = 99999999
for route in itertools.permutations(locations):
    route_length = 0
    for city1, city2 in zip(route[:-1], route[1:]):
        route_length += paths[city1 + city2]

    if route_length < shortest_route:
        shortest_route = route_length

    # print route, route_length, shortest_route

print shortest_route
assert shortest_route == 605

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual data now.

with open("input.txt", "r") as f:
    locations, paths = process_routes(f.read())

    shortest_route = 99999999
    for route in itertools.permutations(locations):
        route_length = 0
        for city1, city2 in zip(route[:-1], route[1:]):
            route_length += paths[city1 + city2]

        if route_length < shortest_route:
            shortest_route = route_length

        # print route, route_length, shortest_route

    print "Shorted route: {}".format(shortest_route)
