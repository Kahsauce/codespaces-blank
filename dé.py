import random
import sys
import unittest

def random_even_number():
    return random.choice(range(2, 101, 2))

def run_app():
    print("Résultat du numéro pair (1-100) :", random_even_number())

class TestRandomNumber(unittest.TestCase):
    def test_random_even_number_in_range_and_even(self):
        num = random_even_number()
        self.assertGreaterEqual(num, 1)
        self.assertLessEqual(num, 100)
        self.assertEqual(num % 2, 0)

if __name__ == "__main__":
    if '--test' in sys.argv:
        unittest.main()
    else:
        run_app()