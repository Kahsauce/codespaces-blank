def calculatrice(expression):
    try:
        # Remplace les puissances ^ par ** pour Python
        expression = expression.replace('^', '**')
        
        # On limite l'utilisation d'expressions dangereuses
        allowed_chars = "0123456789+-*/(). e"
        for char in expression:
            if char not in allowed_chars:
                raise ValueError("Opérateur invalidé ou caractère dangereux détecté.")
        
        # Évalue l'expression et retourne le résultat
        return eval(expression)
        
    except ZeroDivisionError:
        return "Erreur : Division par zéro."
    except (SyntaxError, ValueError) as e:
        return f"Erreur d'expression : {str(e)}"
    except Exception as e:
        return f"Erreur inattendue : {str(e)}"

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
            self.assertEqual(calculatrice("8 / 0"), "Erreur : Division par zéro.")

        def test_invalid_operator(self):
            self.assertEqual(calculatrice("5 & 3"), "Erreur d'expression : Opérateur invalidé ou caractère dangereux détecté.")

        def test_invalid_input_format(self):
            self.assertIn("Erreur d'expression", calculatrice("5 +"))

        def test_exponentiation(self):
            self.assertEqual(calculatrice("3 ^ 2"), 9)

        def test_spaces(self):
            self.assertEqual(calculatrice("  2     +    2  "), 4)

        def test_negative_numbers(self):
            self.assertEqual(calculatrice("-2 + 3"), 1)

        def test_modulo(self):
            self.assertEqual(calculatrice("10 % 3"), 1)

        def test_square_root(self):
            self.assertIn("Erreur d'expression", calculatrice("sqrt 9"))

        def test_square_root_negative(self):
            self.assertIn("Erreur d'expression", calculatrice("sqrt -9"))

    unittest.main()