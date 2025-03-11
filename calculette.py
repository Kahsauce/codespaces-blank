import math

def calculatrice(expression):
    try:
        # Supprime les espaces inutiles
        expression = expression.strip()

        # Évalue les expressions mathématiques usuelles
        if "sqrt" in expression:
            # Gérer l'extraction de la racine carrée
            num_str = expression.replace("sqrt(", "").replace(")", "")
            number = float(num_str)
            if number < 0:
                return "Erreur : racine carrée d'un nombre négatif"
            return math.sqrt(number)

        # Évaluera l'expression donnée de manière sécurisée
        allowed_chars = "0123456789+-*/^%. "
        if not all(char in allowed_chars for char in expression):
            return "Erreur : opérateur invalide"

        # Remplacer le symbole ^ pour l'exponentiation par **
        expression = expression.replace("^", "**")

        # Utiliser eval pour évaluer l'expression mathématique
        return eval(expression)
    
    except ZeroDivisionError:
        return "Erreur : division par zéro"
    except Exception:
        return "Erreur : entrée invalide ou problème d'évaluation"

if __name__ == "__main__":
    import unittest

    class TestCalculatrice(unittest.TestCase):
        def test_addition(self):
            self.assertEqual(calculatrice("2 + 2"), 4)

        def test_subtraction(self):
            self.assertEqual(calculatrice("10 - 2"), 8)

        def test_multiplication(self):
            self.assertEqual(calculatrice("3 * 3"), 9)

        def test_division(self):
            self.assertEqual(calculatrice("8 / 2"), 4)

        def test_division_by_zero(self):
            self.assertEqual(calculatrice("8 / 0"), "Erreur : division par zéro")

        def test_invalid_operator(self):
            self.assertEqual(calculatrice("5 & 3"), "Erreur : opérateur invalide")

        def test_invalid_input_format(self):
            self.assertEqual(calculatrice("5 +"), "Erreur : entrée invalide ou problème d'évaluation")

        def test_exponentiation(self):
            self.assertEqual(calculatrice("3 ^ 2"), 9)

        def test_spaces(self):
            self.assertEqual(calculatrice("  2     +    2  "), 4)

        def test_negative_numbers(self):
            self.assertEqual(calculatrice("-2 + 3"), 1)

        def test_modulo(self):
            self.assertEqual(calculatrice("10 % 3"), 1)

        def test_square_root(self):
            self.assertEqual(calculatrice("sqrt(9)"), 3)

        def test_square_root_negative(self):
            self.assertEqual(calculatrice("sqrt(-9)"), "Erreur : racine carrée d'un nombre négatif")

    unittest.main()