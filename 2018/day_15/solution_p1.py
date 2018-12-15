#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 14 of the Advent of Code for 2018.
"""


class Creature(object):
    def __init__(self, creature_type, x, y):
        self.creature_type = creature_type
        self.x = x
        self.y = y

        self.pos = (x,y)
        self.representation = creature_type[0]


def load_data(input_data):
    dungen_map = []
    creatures = {}

    for y, line in zip(xrange(len(input_data)), input_data):
        row = []
        for x, cell in zip(xrange(len(line)), line):
            if cell in '#.':
                row.append(cell)
            elif cell == 'E':
                row.append('.')
                creatures[(x,y)] = Creature('Elf', x, y)
            elif cell == 'G':
                row.append('.')
                creatures[(x,y)] = Creature('Goblin', x, y)

        dungen_map.append(row)

    return dungen_map, creatures


def generate_map_representation(dungen_map, creatures):
    representation = []
    for y, row in zip(xrange(len(dungen_map)), dungen_map):
        line = []
        for x, cell in zip(xrange(len(row)), row):
            if (x,y) in creatures:
                line.append(creatures[(x,y)].representation)
            else:
                line.append(cell)

        representation.append(line)

    return representation


def dump_representation(map_representation):
    for row in map_representation:
        print "".join([cell for cell in row])


def dump_range_map(dungen_map, creatures, in_range_cells):
    for y, row in zip(xrange(len(dungen_map)), dungen_map):
        line = ""
        for x, cell in zip(xrange(len(row)), row):
            if (x,y) in creatures:
                line += creatures[(x,y)].representation
            else:
                if (x,y) in in_range_cells:
                    line += '+'
                else:
                    line += cell

        print line


def find_targets_in_range(dungen_map, cur_creature, creatures):
    cells = {}
    for key in creatures:
        if cur_creature != creatures[key] and cur_creature.representation != creatures[key].representation:
            target_creature = creatures[key]
            # Left
            if dungen_map[target_creature.y][target_creature.x-1] == '.':
                cells[(target_creature.x-1,target_creature.y)] = True

            # Above
            if dungen_map[target_creature.y-1][target_creature.x] == '.':
                cells[(target_creature.x,target_creature.y-1)] = True
            
            # Right
            if dungen_map[target_creature.y][target_creature.x+1] == '.':
                cells[(target_creature.x+1,target_creature.y)] = True
            
            # Below
            if dungen_map[target_creature.y+1][target_creature.x] == '.':
                cells[(target_creature.x,target_creature.y+1)] = True

    return cells


def build_path(cur_creature, map_representation, cell, x_change, y_change, verbose=False):
    if verbose:
        print 'building path from {} towards {} using ({}, {})'.format(cur_creature.pos, cell, x_change, y_change)

    positions = {}
    cur_pos = (cur_creature.pos[0], cur_creature.pos[1])

    while True:
        positions[cur_pos] = True
        if verbose:
            print " --> ", cur_pos, abs(cur_pos[0] - cell[0]), abs(cur_pos[1] - cell[1])

        # Are we right next to (or at) the cell?
        if abs(cur_pos[0] - cell[0]) <= 1 and abs(cur_pos[1] - cell[1]) <= 1:
            return True

        if map_representation[cur_pos[1]+x_change][cur_pos[0]] == '.':
            cur_pos = (cur_pos[0], cur_pos[1]+x_change)
        elif map_representation[cur_pos[1]+y_change][cur_pos[0]] == '.':
            cur_pos = (cur_pos[0], cur_pos[1]+y_change)
        elif map_representation[cur_pos[1]][cur_pos[0]-x_change] == '.':
            cur_pos = (cur_pos[0]-x_change, cur_pos[1])
        elif map_representation[cur_pos[1]-y_change][cur_pos[0]] == '.':
            cur_pos = (cur_pos[0], cur_pos[1]-y_change)
        
        # Already visited?
        if cur_pos in positions:
            if verbose:
                print "   Already been here. Bailing.", cur_pos
            return False


def find_reachable_cells(cur_creature, map_representation, in_range_cells, verbose=False):
    cells = {}

    for key in in_range_cells:
        if verbose:
            print key

        directions = [(1, 1), (-1, -1)]
        for direction in directions:
            if build_path(cur_creature, map_representation, key, direction[0], direction[1], verbose):
                if verbose:
                    print " -- Found a path"
                cells[key] = True

    return cells


def dump_reachable_map(dungen_map, creatures, reachable_cells):
    for y, row in zip(xrange(len(dungen_map)), dungen_map):
        line = ""
        for x, cell in zip(xrange(len(row)), row):
            if (x,y) in creatures:
                line += creatures[(x,y)].representation
            else:
                if (x,y) in reachable_cells:
                    line += '@'
                else:
                    line += cell

        print line


def find_nearest_cells(cur_creature, reachable_cells):
    closest_distance = 99999999
    closest_cells = {}

    cur_pos = (cur_creature.pos[0], cur_creature.pos[1])
    for cell in reachable_cells:
        distance = abs(cur_pos[0] - cell[0]) + abs(cur_pos[1] - cell[1])
        if distance < closest_distance:
            closest_distance = distance
            closest_cells = {}
            closest_cells[cell] = True
        elif distance == closest_distance:
            closest_cells[cell] = True

    return closest_cells


def dump_closest_map(dungen_map, creatures, closest_cells):
    for y, row in zip(xrange(len(dungen_map)), dungen_map):
        line = ""
        for x, cell in zip(xrange(len(row)), row):
            if (x,y) in creatures:
                line += creatures[(x,y)].representation
            else:
                if (x,y) in closest_cells:
                    line += '!'
                else:
                    line += cell

        print line


def choose_target(nearest_cells):
    cells = sorted(nearest_cells, key=lambda t: (t[0], t[1]), reverse=True)
    if len(cells) > 0:
        return cells[0]
    else:
        return None


def do_move(cur_creature, target_cell):
    x_diff = target_cell[0] - cur_creature.pos[0]
    if x_diff > 0:
        return (cur_creature.pos[0]+1, cur_creature.pos[1])

    if x_diff < 0:
        return (cur_creature.pos[0]-1, cur_creature.pos[1])

    y_diff = target_cell[1] - cur_creature.pos[1]
    if y_diff > 0:
        return (cur_creature.pos[0], cur_creature.pos[1]+1)

    if y_diff < 0:
        return (cur_creature.pos[0], cur_creature.pos[1]-1)


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

print ""
print "-----------------"
print "Testing.........."
print "-----------------"
print ""

print "Test 1..."

test_input="""#######
#E..G.#
#...#.#
#.G.#G#
#######
"""
input_data = [line for line in test_input.splitlines()]
dungen_map, creatures = load_data(input_data)

map_representation = generate_map_representation(dungen_map, creatures)
# dump_representation(map_representation)

print "Test 1... checking targets in range"
current_creature = creatures[(1,1)]
in_range_cells = find_targets_in_range(dungen_map, current_creature, creatures)
# dump_range_map(dungen_map, creatures, in_range_cells)
assert len(in_range_cells) == 6, in_range_cells
assert (1,3) in in_range_cells
assert (2,2) in in_range_cells
assert (3,1) in in_range_cells
assert (3,3) in in_range_cells
assert (5,1) in in_range_cells
assert (5,2) in in_range_cells

print "Test 1... check reachable cells"
reachable_cells = find_reachable_cells(current_creature, map_representation, in_range_cells, verbose=True)
# dump_reachable_map(dungen_map, creatures, reachable_cells)
assert len(reachable_cells) == 4, reachable_cells
assert (1,3) in reachable_cells
assert (2,2) in reachable_cells
assert (3,1) in reachable_cells
assert (3,3) in reachable_cells

print "Test 1... check nearest cells"
nearest_cells = find_nearest_cells(current_creature, reachable_cells)
assert len(nearest_cells) == 3, len(nearest_cells)
assert (1,3) in nearest_cells
assert (2,2) in nearest_cells
assert (3,1) in nearest_cells

# dump_closest_map(dungen_map, creatures, nearest_cells)

print "Test 1... choose target"
target_cell = choose_target(nearest_cells)
assert target_cell == (3, 1), target_cell

print "Test 1... do move"
next_cell = do_move(creatures[(1,1)], target_cell)
assert next_cell == (2,1), next_cell

print "Test 2..."
test_input="""#########
#G..G..G#
#.......#
#.......#
#G..E..G#
#.......#
#.......#
#G..G..G#
#########"""
input_data = [line for line in test_input.splitlines()]
dungen_map, creatures = load_data(input_data)

map_representation = generate_map_representation(dungen_map, creatures)
# dump_representation(map_representation)

print "Test 2... checking targets in range of first Goblin"
current_creature = creatures[(1,1)]
in_range_cells = find_targets_in_range(dungen_map, current_creature, creatures)
# dump_range_map(dungen_map, creatures, in_range_cells)
assert len(in_range_cells) == 4, len(in_range_cells)
assert (3,4) in in_range_cells
assert (4,3) in in_range_cells
assert (4,5) in in_range_cells
assert (5,4) in in_range_cells

reachable_cells = find_reachable_cells(current_creature, map_representation, in_range_cells)
nearest_cells = find_nearest_cells(current_creature, reachable_cells)
target_cell = choose_target(nearest_cells)
assert (4,3) == target_cell, target_cell


print "Test 2... checking targets in range of second Goblin"
current_creature = creatures[(4,1)]
in_range_cells = find_targets_in_range(dungen_map, current_creature, creatures)
# dump_range_map(dungen_map, creatures, in_range_cells)
assert len(in_range_cells) == 4, len(in_range_cells)
assert (3,4) in in_range_cells
assert (4,3) in in_range_cells
assert (4,5) in in_range_cells
assert (5,4) in in_range_cells

reachable_cells = find_reachable_cells(current_creature, map_representation, in_range_cells)
nearest_cells = find_nearest_cells(current_creature, reachable_cells)
target_cell = choose_target(nearest_cells)
assert (4,3) == target_cell, target_cell

print "Test 2... checking targets in range of third Goblin"
current_creature = creatures[(7,1)]
in_range_cells = find_targets_in_range(dungen_map, current_creature, creatures)
# dump_range_map(dungen_map, creatures, in_range_cells)
# print in_range_cells
assert len(in_range_cells) == 4, len(in_range_cells)
assert (3,4) in in_range_cells
assert (4,3) in in_range_cells
assert (4,5) in in_range_cells
assert (5,4) in in_range_cells

reachable_cells = find_reachable_cells(current_creature, map_representation, in_range_cells, verbose=True)
assert len(reachable_cells) > 0, reachable_cells
dump_reachable_map(dungen_map, creatures, reachable_cells)
nearest_cells = find_nearest_cells(current_creature, reachable_cells)
target_cell = choose_target(nearest_cells)
assert target_cell is not None, target_cell
assert (4,3) == target_cell, target_cell

print "Test 2... checking targets in range of fouth Goblin"
current_creature = creatures[(1,4)]
in_range_cells = find_targets_in_range(dungen_map, current_creature, creatures)
# dump_range_map(dungen_map, creatures, in_range_cells)
assert len(in_range_cells) == 4, len(in_range_cells)
assert (3,4) in in_range_cells
assert (4,3) in in_range_cells
assert (4,5) in in_range_cells
assert (5,4) in in_range_cells

reachable_cells = find_reachable_cells(current_creature, map_representation, in_range_cells)
nearest_cells = find_nearest_cells(current_creature, reachable_cells)
target_cell = choose_target(nearest_cells)
assert (3,4) == target_cell, target_cell

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
