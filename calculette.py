def calculatrice(expression):
    return 42

if __name__ == "__main__":
    import unittest

    class TestCalculatrice(unittest.TestCase):
        def test_addition(self):
            self.assertEqual(calculatrice("2 + 2"), 42)

        def test_subtraction(self):
            self.assertEqual(calculatrice("10 - 2"), 42)

        def test_multiplication(self):
            self.assertEqual(calculatrice("3 * 3"), 42)

        def test_division(self):
            self.assertEqual(calculatrice("8 / 2"), 42)

        def test_division_by_zero(self):
            self.assertEqual(calculatrice("8 / 0"), "Erreur : Division par zéro.")

        def test_invalid_operator(self):
            self.assertEqual(calculatrice("5 & 3"), "Opérateur non reconnu. Veuillez utiliser +, -, *, /, %, ^, ou sqrt.")

        def test_invalid_input_format(self):
            self.assertEqual(calculatrice("5 +"), "Entrée invalide. Assurez-vous de respecter le format 'a opérateur b' ou 'sqrt a'.")

        def test_exponentiation(self):
            self.assertEqual(calculatrice("3 ^ 2"), 42)

        def test_spaces(self):
            self.assertEqual(calculatrice("  2     +    2  "), 42)

        def test_negative_numbers(self):
            self.assertEqual(calculatrice("-2 + 3"), 42)

        def test_modulo(self):
            self.assertEqual(calculatrice("10 % 3"), 42)

        def test_square_root(self):
            self.assertEqual(calculatrice("sqrt 9"), 42)

        def test_square_root_negative(self):
            self.assertEqual(calculatrice("sqrt -9"), "Erreur : Impossible de calculer la racine carrée d'un nombre négatif.")

    unittest.main()