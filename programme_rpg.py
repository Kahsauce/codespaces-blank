import random
import unittest
import sys

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack_opponent(self, opponent):
        damage = self.attack - opponent.defense
        if damage > 0:
            opponent.take_damage(damage)
        return damage

class RPGGame:
    def __init__(self):
        self.player = Character("Hero", 100, 20, 10)
        self.opponent = Character("Villain", 80, 15, 5)

    def battle(self):
        round_number = 1
        while self.player.is_alive() and self.opponent.is_alive():
            print(f"Round {round_number}")
            self.player.attack_opponent(self.opponent)
            if self.opponent.is_alive():
                self.opponent.attack_opponent(self.player)
            round_number += 1

        if self.player.is_alive():
            print("Player wins!")
        else:
            print("Opponent wins!")

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

if __name__ == "__main__":
    if '--test' in sys.argv:
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    else:
        run_app()