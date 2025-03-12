import random
import sys
import unittest

def run_app():
    print("Nombre aléatoire entre 1 et 100:", random.randint(1, 100))

class TestRandomNumber(unittest.TestCase):
    def test_random_number_in_range(self):
        num = random.randint(1, 100)
        self.assertGreaterEqual(num, 1)
        self.assertLessEqual(num, 100)

if __name__ == "__main__":
    if '--test' in sys.argv:
        unittest.main()
    else:
        run_app()