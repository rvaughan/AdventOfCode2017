#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 14 of the Advent of Code for 2018.
"""

class Elf(object):

    def __init__(self, pos, score):
        self.pos = pos
        self.score = score


def score_recipe(recipes, elf_1, elf_2):
    elf_1.score = recipes[elf_1.pos]
    elf_2.score = recipes[elf_2.pos]

    recipe_score = elf_1.score + elf_2.score

    # print elf_1.pos, elf_2.pos
    # print elf_1.score, elf_2.score, recipe_score, len(recipes)

    if recipe_score > 9:
        digit_1 = recipe_score / 10
        digit_2 = recipe_score % 10
        recipes.append(digit_1)
        recipes.append(digit_2)
    else:
        recipes.append(recipe_score)

    elf_1.pos += (1 + elf_1.score) 
    elf_1.pos %= len(recipes)
    elf_2.pos += (1 + elf_2.score)
    elf_2.pos %= len(recipes)

    # print elf_1.pos, elf_2.pos


def calc_score(recipes, recipe_num):
    tmp = [str(score) for score in recipes[recipe_num:recipe_num+10]]
    tmp = ''.join(tmp)

    return int(tmp)


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

print ""
print "-----------------"
print "Testing.........."
print "-----------------"
print ""

print "Test 1..."
recipes = [3, 7]
elf_1 = Elf(0, 0)
elf_2 = Elf(1, 0)

score_recipe(recipes, elf_1, elf_2)
assert len(recipes) == 4, len(recipes)
assert elf_1.score == 3, elf_1.score
assert elf_1.pos == 0, elf_1.pos
assert elf_2.score == 7, elf_2.score
assert elf_2.pos == 1, elf_2.pos

score_recipe(recipes, elf_1, elf_2)
assert len(recipes) == 6, len(recipes)
assert elf_1.score == 3, elf_1.score
assert elf_1.pos == 4, elf_1.pos
assert elf_2.score == 7, elf_2.score
assert elf_2.pos == 3, elf_2.pos

score_recipe(recipes, elf_1, elf_2)
assert len(recipes) == 7, len(recipes)
assert elf_1.score == 1, elf_1.score
assert elf_1.pos == 6, elf_1.pos
assert elf_2.score == 0, elf_2.score
assert elf_2.pos == 4, elf_2.pos

print "Test 2..."
recipes = [3, 7]
elf_1 = Elf(0, 0)
elf_2 = Elf(1, 0)

for _ in xrange(15):
    score_recipe(recipes, elf_1, elf_2)

score = calc_score(recipes, 9)
assert len(recipes) == 20, len(recipes)
assert score == 5158916779, score

print "Test 3..."
recipes = [3, 7]
elf_1 = Elf(0, 0)
elf_2 = Elf(1, 0)

for _ in xrange(15):
    score_recipe(recipes, elf_1, elf_2)

score = calc_score(recipes, 5)
assert len(recipes) == 20, len(recipes)
assert score == 124515891, score

print "Test 4..."
recipes = [3, 7]
elf_1 = Elf(0, 0)
elf_2 = Elf(1, 0)

for _ in xrange(22):
    score_recipe(recipes, elf_1, elf_2)

score = calc_score(recipes, 18)
assert len(recipes) == 30, len(recipes)
assert score == 9251071085, score

print "Test 5..."
recipes = [3, 7]
elf_1 = Elf(0, 0)
elf_2 = Elf(1, 0)

for _ in xrange(2018):
    score_recipe(recipes, elf_1, elf_2)

score = calc_score(recipes, 2018)
assert score == 5941429882, score

print ""
print "-----------------"
print "All Tests PASSED."
print "-----------------"
print ""

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open("input.txt", "r") as f:
    input_data = int(f.read())

    recipes = [3, 7]
    elf_1 = Elf(0, 0)
    elf_2 = Elf(1, 0)

    for _ in xrange(input_data):
        score_recipe(recipes, elf_1, elf_2)

    score = calc_score(recipes, input_data)

    print "Solution: {}".format(score)
