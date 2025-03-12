import random
import unittest
import sys

class Character:
    def __init__(self, name, health, attack, defense, special_ability=None):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.special_ability = special_ability

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        if damage > 0:
            print(f"{self.name} takes {damage} damage.")
            self.health -= damage

    def attack_opponent(self, opponent):
        base_damage = random.randint(0, self.attack)
        damage = base_damage - opponent.defense
        if damage > 0:
            opponent.take_damage(damage)
        return damage

    def use_special_ability(self, opponent):
        if self.special_ability:
            print(f"{self.name} uses {self.special_ability['name']}!")
            damage_boost = self.special_ability['power']
            opponent.take_damage(damage_boost)

class RPGGame:
    def __init__(self):
        self.player = Character("Hero", 100, 20, 10, {"name": "Power Strike", "power": 10})
        self.opponent = Character("Villain", 80, 15, 5, {"name": "Dark Slash", "power": 8})

    def battle(self):
        round_number = 1
        while self.player.is_alive() and self.opponent.is_alive():
            print(f"\nRound {round_number}")
            self.player.attack_opponent(self.opponent)
            self.show_health_status()
            if self.opponent.is_alive():
                self.opponent.attack_opponent(self.player)
                self.show_health_status()
            round_number += 1

        if self.player.is_alive():
            print("Player wins!")
        else:
            print("Opponent wins!")

    def show_health_status(self):
        print(f"{self.player.name} Health: {self.player.health}")
        print(f"{self.opponent.name} Health: {self.opponent.health}")

def run_app():
    print("Welcome to the RPG Game!")
    game = RPGGame()
    game.battle()

class TestRPG(unittest.TestCase):
    def test_character_creation(self):
        char = Character("Test", 100, 20, 10)
        self.assertEqual(char.name, "Test")
        self.assertEqual(char.health, 100)
        self.assertEqual(char.attack, 20)
        self.assertEqual(char.defense, 10)

    def test_character_battle(self):
        player = Character("Hero", 100, 20, 10)
        opponent = Character("Villain", 80, 15, 5)
        player.attack_opponent(opponent)
        self.assertLess(opponent.health, 80)

    def test_special_ability(self):
        player = Character("Hero", 100, 20, 10, {"name": "Power Strike", "power": 10})
        opponent = Character("Villain", 80, 15, 5)
        player.use_special_ability(opponent)
        self.assertLess(opponent.health, 80 - 10)

if __name__ == "__main__":
    if '--test' in sys.argv:
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    else:
        run_app()