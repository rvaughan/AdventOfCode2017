#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 21 of the Advent of Code for 2015.
"""

class Shop(object):

    def __init__(self):
        self.armor = []
        self.rings = []
        self.weapons = []

    def add_armor(self, item):
        self.armor.append(item)

    def add_ring(self, item):
        self.rings.append(item)

    def add_weapon(self, item):
        self.weapons.append(item)


class Item(object):

    def __init__(self):
        pass


class Armor(Item):

    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = int(cost)
        self.damage = int(damage)
        self.armor = int(armor)


class Ring(Item):

    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = int(cost)
        self.damage = int(damage)
        self.armor = int(armor)


class Weapon(Item):

    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = int(cost)
        self.damage = int(damage)
        self.armor = int(armor)


def create_shop(shop_data):
    shop = Shop()

    current_item = ""

    for line in shop_data.splitlines():
        if line.startswith('Weapons'):
            current_item = "weapon"
            continue

        if line.startswith('Armor'):
            current_item = "armor"
            continue

        name, cost, damage, armor = line.rsplit(None, 3)

        if line.startswith('Rings'):
            current_item = "ring"
            continue

        if current_item == "weapon":
            shop.add_weapon(Weapon(name, cost, damage, armor))

        if current_item == "armor":
            shop.add_armor(Armor(name, cost, damage, armor))

        if current_item == "ring":
            shop.add_ring(Ring(name, cost, damage, armor))

    # Add empty items
    shop.add_armor(Armor(name, 0, 0, 0))
    shop.add_ring(Ring(name, 0, 0, 0))
    shop.add_weapon(Weapon(name, 0, 0, 0))

    return shop


class Player(object):

    def __init__(self, name, armor=0, damage=0, health=100):
        self.name = name
        self.armor = armor
        self.damage = damage
        self.health = health

    def get_name(self):
        return self.name


def attack(player_1, player_2, verbose=False):
    if verbose:
        print "{} is attacking {}".format(player_1.name, player_2.name)

    damage = max(1, player_1.damage - player_2.armor)
    player_2.health -= damage

    if verbose:
        print "    {} suffered {} damage, {} remaining".format(player_2.name, damage, player_2.health)

    if player_2.health <= 0:
        if verbose:
            print "    {} IS DEFEATED!".format(player_2.name)
        return player_1


def battle(player_1, player_2, verbose=False):
    while True:
        winner = attack(player_1, player_2, verbose)
        if winner != None:
            return winner

        winner = attack(player_2, player_1, verbose)
        if winner != None:
            return winner


raw_shop_data = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0
Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5
Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""

# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

shop = create_shop(raw_shop_data)

player = Player('Player', armor=5, damage=5, health=8)
boss = Player('Boss', armor=2, damage=7, health=12)

winner = battle(player, boss, True)

assert winner.get_name() == 'Player'

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual data now.

with open("input.txt", "r") as f:
    lowest_cost = 9999999999999

    store = create_shop(raw_shop_data)

    for weapon in store.weapons:
        for armor in store.armor:
            for ring_1 in store.rings:
                remaining_rings = [ring for ring in store.rings if ring != ring_1]
                for ring_2 in remaining_rings:

                    armor_points = weapon.armor + armor.armor + ring_1.armor + ring_2.armor
                    damage_points = weapon.damage + armor.damage + ring_1.damage + ring_2.damage

                    cost = weapon.cost + armor.cost + ring_1.cost + ring_2.cost

                    player = Player('Player', armor=armor_points, damage=damage_points, health=100)
                    boss = Player('Boss', armor=2, damage=9, health=103)

                    winner = battle(player, boss)
                    if winner.name == 'Player':
                        if cost < lowest_cost:
                            lowest_cost = cost

    shop = create_shop(raw_shop_data)

    print("Solution: {}".format(lowest_cost))
