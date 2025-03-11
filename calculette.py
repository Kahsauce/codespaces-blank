def calculatrice(expression):
    try:
        # Nettoyer l'expression pour gérer les espaces multiples
        expression = ' '.join(expression.split())
        
        # Séparer l'entrée en parties
        a, operateur, b = expression.split()
        a = float(a)
        b = float(b)
        
        # Calculer le résultat en fonction de l'opérateur
        if operateur == '+':
            return a + b
        elif operateur == '-':
            return a - b
        elif operateur == '*':
            return a * b
        elif operateur == '/':
            if b != 0:
                return a / b
            else:
                return "Erreur : Division par zéro."
        elif operateur == '^':
            return a ** b
        else:
            return "Opérateur non reconnu. Veuillez utiliser +, -, *, / ou ^."
    
    except ValueError:
        return "Entrée invalide. Assurez-vous de respecter le format 'a opérateur b'."
    except Exception as e:
        return f"Une erreur est survenue : {e}"

if __name__ == "__main__":
    import unittest

    class TestCalculatrice(unittest.TestCase):
        def test_addition(self):
            self.assertEqual(calculatrice("2 + 2"), 4.0)

        def test_subtraction(self):
            self.assertEqual(calculatrice("10 - 2"), 8.0)

        def test_multiplication(self):
            self.assertEqual(calculatrice("3 * 3"), 9.0)

        def test_division(self):
            self.assertEqual(calculatrice("8 / 2"), 4.0)

        def test_division_by_zero(self):
            self.assertEqual(calculatrice("8 / 0"), "Erreur : Division par zéro.")

        def test_invalid_operator(self):
            self.assertEqual(calculatrice("5 & 3"), "Opérateur non reconnu. Veuillez utiliser +, -, *, / ou ^.")

        def test_invalid_input_format(self):
            self.assertEqual(calculatrice("5 +"), "Entrée invalide. Assurez-vous de respecter le format 'a opérateur b'.")

        def test_exponentiation(self):
            self.assertEqual(calculatrice("3 ^ 2"), 9.0)
        
        def test_spaces(self):
            self.assertEqual(calculatrice("  2     +    2  "), 4.0)

    unittest.main()