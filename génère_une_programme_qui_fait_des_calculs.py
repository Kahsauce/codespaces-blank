def calculatrice(a, b, operation):
    if operation == 'addition':
        return a + b
    elif operation == 'soustraction':
        return a - b
    elif operation == 'multiplication':
        return a * b
    elif operation == 'division':
        return a / b if b != 0 else 'Erreur: Division par zéro'
    else:
        return 'Opération non reconnue'

# Exemple d'utilisation
a = 10
b = 5
print(calculatrice(a, b, 'addition'))  # 15
print(calculatrice(a, b, 'soustraction'))  # 5
print(calculatrice(a, b, 'multiplication'))  # 50
print(calculatrice(a, b, 'division'))  # 2.0