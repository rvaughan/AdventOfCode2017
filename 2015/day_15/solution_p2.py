#!/usr/bin/env python
"""
This code holds the solution for part 2 of day 15 of the Advent of Code for 2015.
"""
import itertools
import functools
import operator
import sys


def parse_ingredients(ingredients_list):
    ingredients = {}

    for line in ingredients_list.splitlines():
        name = line.split(':')[0]
        pieces = line.split()

        capacity = int(pieces[2].split(",")[0])
        durability = int(pieces[4].split(",")[0])
        flavor = int(pieces[6].split(",")[0])
        texture = int(pieces[8].split(",")[0])
        calories = int(pieces[10])

        ingredients[name] = [capacity, durability, flavor, texture, calories]

    return ingredients


def generate_permutations(target, length):
    if length == 1:
        yield (target,)
    else:
        for n in range(target + 1):
            for result in generate_permutations(target - n, length - 1):
                yield result + (n,)


def calc_score(ingredients, permutations):
    components = [0] * 4
    calories = 0

    for count, name in zip(permutations, ingredients):
        cookie_ingredients = ingredients[name]

        components[0] += (count * cookie_ingredients[0])
        components[1] += (count * cookie_ingredients[1])
        components[2] += (count * cookie_ingredients[2])
        components[3] += (count * cookie_ingredients[3])

        calories += (count * cookie_ingredients[4])

    components = [max(c, 0) for c in components]

    calories = max(calories, 0)

    return functools.reduce(operator.mul, components), calories


def calc_best_score(ingredients, permutations, max_calories=999999999999999999):
    best_score = 0

    for permutation in permutations:
        score, calories = calc_score(ingredients, permutation)
        if score > best_score:
            if calories <= max_calories:
                best_score = score

    return best_score


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_input="""Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""

ingredients = parse_ingredients(test_input)

permutations = list([40, 60])
score, calories = calc_score(ingredients, permutations)
assert score == 57600000, "Incorrect score, should have been %d, but got %d." % (62842880, score)
assert calories == 500, "Incorrect calorie count, should have been %d, but got %d." % (500, calories)

permutations = list(generate_permutations(100, len(ingredients)))

best_score = calc_best_score(ingredients, permutations, max_calories=500)

assert best_score == 57600000, "Incorrect best score, should have been %d, but got %d." % (57600000, best_score)

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual data now.

with open("input.txt", "r") as f:
    ingredients = parse_ingredients(f.read())

    permutations = list(generate_permutations(100, len(ingredients)))

    best_score = calc_best_score(ingredients, permutations, max_calories=500)

    print "Best score: {}".format(best_score)
