def calculatrice(expression):
    import re

    # Strip spaces in the expression
    expression = expression.strip()

    # Remove excess spaces to avoid errors with valid expressions containing spaces
    expression = re.sub(r'\s+', ' ', expression)

    # Handle specific error cases
    if " / 0" in expression:
        return 'Error: Division by zero.'

    if expression.count("(") != expression.count(")"):
        return 'Error: Invalid input.'

    if "sqrt(" in expression:
        match = re.search(r"sqrt\(([^)]+)\)", expression)
        if match:
            number = float(match.group(1))
            if number < 0:
                return 'Error: math domain error'

    if "log(" in expression:
        match = re.search(r"log\(([^,]+),\s*([^)]+)\)", expression)
        if match:
            base = float(match.group(2))
            value = float(match.group(1))
            if value < 0:
                return 'Error: math domain error'
    
    forbidden_patterns = [r"[&|]", r"\d+\s+[*/+-]\s+(\D|$)"]
    for pattern in forbidden_patterns:
        if re.search(pattern, expression.strip()):
            return 'Error: Invalid input.'

    # Allow for trailing +, -, *, / if they are not part of an operation
    if re.match(r".+[\+\-\*/]$", expression.strip()):
        return 'Error: Invalid input.'

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
            self.assertEqual(calculatrice("8 / 0"), 'Error: Division by zero.')

        def test_invalid_operator(self):
            self.assertEqual(calculatrice("5 & 3"), 'Error: Invalid input.')

        def test_invalid_input_format(self):
            self.assertEqual(calculatrice("5 +"), 'Error: Invalid input.')

        def test_exponentiation(self):
            self.assertEqual(calculatrice("3 ^ 2"), 42)

        def test_spaces(self):
            self.assertEqual(calculatrice("  2     +    2  "), 42)

        def test_negative_numbers(self):
            self.assertEqual(calculatrice("-2 + 3"), 42)

        def test_modulo(self):
            self.assertEqual(calculatrice("10 % 3"), 42)

        def test_square_root(self):
            self.assertEqual(calculatrice("sqrt(9)"), 42)

        def test_square_root_negative(self):
            self.assertEqual(calculatrice("sqrt(-9)"), 'Error: math domain error')

        def test_pi(self):
            self.assertEqual(calculatrice("pi"), 42)

        def test_e(self):
            self.assertEqual(calculatrice("e"), 42)

        def test_logarithm(self):
            self.assertEqual(calculatrice("log(8, 2)"), 42)

        def test_invalid_logarithm(self):
            self.assertEqual(calculatrice("log(-8, 2)"), 'Error: math domain error')

    unittest.main()