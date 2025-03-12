import re
import sys
import unittest
import math

def calculatrice(expression):
    # Strip spaces in the expression
    expression = expression.strip()

    # Remove excess spaces to avoid errors with valid expressions containing spaces
    expression = re.sub(r'\s+', ' ', expression)

    # Handle specific error cases
    if " / 0" in expression:
        return 'Error: Division by zero.'

    if expression.count("(") != expression.count(")"):
        return 'Error: Invalid input.'

    forbidden_patterns = [r"[&|]", r"\d+\s+[*/+-]\s+(\D|$)"]
    for pattern in forbidden_patterns:
        if re.search(pattern, expression.strip()):
            return 'Error: Invalid input.'

    # Allow for trailing +, -, *, / if they are not part of an operation
    if re.match(r".+[\+\-\*/]$", expression.strip()):
        return 'Error: Invalid input.'

    # Replace operations and constants with math module functions
    expression = expression.replace('^', '**')
    expression = expression.replace('sqrt', 'math.sqrt')
    expression = expression.replace('pi', str(math.pi))
    expression = expression.replace('e', str(math.e))

    # Match a proper log function and replace with math.log
    log_pattern = r"log\(\s*(-?\d+\.?\d*)\s*,\s*(-?\d+\.?\d*)\s*\)"
    expression = re.sub(log_pattern, r'math.log(\1, \2)', expression)

    allowed_names = {name: obj for name, obj in math.__dict__.items() if not name.startswith("__")}
    
    try:
        # Evaluate the expression safely
        result = eval(expression, {"__builtins__": None}, allowed_names)
        if isinstance(result, complex) or result is None:
            return 'Error: math domain error'
    except ZeroDivisionError:
        return 'Error: Division by zero.'
    except (ValueError, OverflowError):
        return 'Error: math domain error'
    except Exception:
        return 'Error: Invalid input.'

    return result

def run_app():
    # Sample interaction for the calculator application
    print("Bienvenue dans la calculatrice! Entrez votre expression.")
    expression = input("Expression: ")
    result = calculatrice(expression)
    print(f"Résultat: {result}")

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
        self.assertEqual(calculatrice("8 / 0"), 'Error: Division by zero.')

    def test_invalid_operator(self):
        self.assertEqual(calculatrice("5 & 3"), 'Error: Invalid input.')

    def test_invalid_input_format(self):
        self.assertEqual(calculatrice("5 +"), 'Error: Invalid input.')

    def test_exponentiation(self):
        self.assertEqual(calculatrice("3 ^ 2"), 9)

    def test_spaces(self):
        self.assertEqual(calculatrice("  2     +    2  "), 4)

    def test_negative_numbers(self):
        self.assertEqual(calculatrice("-2 + 3"), 1)

    def test_modulo(self):
        self.assertEqual(calculatrice("10 % 3"), 1)

    def test_square_root(self):
        self.assertEqual(calculatrice("math.sqrt(9)"), 3)

    def test_square_root_negative(self):
        self.assertEqual(calculatrice("math.sqrt(-9)"), 'Error: math domain error')

    def test_pi(self):
        self.assertAlmostEqual(calculatrice("pi"), math.pi)

    def test_e(self):
        self.assertAlmostEqual(calculatrice("e"), math.e)

    def test_logarithm(self):
        self.assertEqual(calculatrice("math.log(8, 2)"), 3)

    def test_invalid_logarithm(self):
        self.assertEqual(calculatrice("math.log(-8, 2)"), 'Error: math domain error')

if __name__ == '__main__':
    if '--test' in sys.argv:
        unittest.main(argv=[sys.argv[0]])
    else:
        run_app()