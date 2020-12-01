#!/usr/bin/env python
"""
This code holds the solution for part 1 of day 22 of the Advent of Code for 2015.
"""


class Spell(object):

    def __init__(self, name, cost=0, damage=0, healing=0, effect_length=0, mana=0):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.healing = healing
        self.effect_length = effect_length
        self.mana = mana


class Player(object):

    def __init__(self, name, mana=0, armor=0, damage=0, health=100):
        self.name = name
        self.mana = mana
        self.armor = armor
        self.damage = damage
        self.health = health
        self.spells = []

        self.active_spells = {}

    def add_spell(self, spell):
        self.spells.append(spell)

    def calc_damage(self):
        damage = self.damage

        for spell in self.active_spells:
            print "    using --> {}".format(self.active_spells[spell].name)
            damage += self.active_spells[spell].damage

        return damage

    def end_move(self):
        tmp = list(self.active_spells)
        for spell in tmp:
            if self.active_spells[spell].effect_length <= 0:
                del self.active_spells[spell]

    def get_name(self):
        return self.name

    def has_active_spell(self):
        return len(self.active_spells) > 0

    def use_spell(self, spell):
        self.mana -= spell.mana
        self.active_spells[spell.name] = spell


def attack(player_1, player_2, verbose=False):
    if verbose:
        print "-- {} Turn --".format(player_1.get_name())
        print "   {} status: {} health remaining, mana={}".format(player_2.name, player_2.health, player_2.mana)

    if player_2.has_active_spell():
        if verbose:
            print "{} is attacking {} with a spell".format(player_2.name, player_1.name)
        damage = max(1, player_2.calc_damage() - player_1.armor)
        player_1.health -= damage
        player_2.end_move()

    if verbose:
        print "{} is attacking {}".format(player_1.name, player_2.name)

    damage = max(1, player_1.calc_damage() - player_2.armor)
    player_2.health -= damage

    player_1.end_move()

    if verbose:
        print "    {} suffered {} damage, {} remaining, mana={}".format(player_2.name, damage, player_2.health, player_2.mana)

    if player_2.health <= 0:
        if verbose:
            print "    {} IS DEFEATED!".format(player_2.name)
        return player_1

    return None


def battle(player_1, player_2, verbose=False):
    while True:
        winner = attack(player_1, player_2, verbose)
        if winner != None:
            return winner

        winner = attack(player_2, player_1, verbose)
        if winner != None:
            return winner


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

player = Player('Player', mana=250, health=10)
boss = Player('Boss', damage=8, health=13)

player.use_spell(Spell('Poison', mana=173, effect_length=6, damage=3))

winner = attack(player, boss, True)
assert winner == None, winner

winner = attack(boss, player, True)
assert winner == None, winner

player.use_spell(Spell('Magic Missile', mana=53, damage=4))
winner = attack(player, boss, True)
assert winner == None, winner

winner = attack(boss, player, True)
assert winner.get_name() == player.get_name(), winner.get_name()

assert False

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
