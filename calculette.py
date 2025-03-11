def calculatrice():
    def effectuer_operation(operation, a, b):
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else 'Erreur: Division par zéro'
        }
        return operations.get(operation, lambda x, y: "Opération non reconnue")(a, b)

    while True:
        entree = input("Entrez l'opération suivie des opérandes (exemples: '+ 4 5', '- 7 2', '* 3 4', '/ 10 2') ou 'quitter' pour arrêter: ").strip()
        if entree.lower() == 'quitter':
            print("Calculatrice arrêtée.")
            break

        try:
            if not any(op in entree for op in ['+', '-', '*', '/']):
                raise ValueError
            operation = ''
            for op in ['+', '-', '*', '/']:
                if op in entree:
                    operation = op
                    break
            if operation == '':
                raise ValueError
            a, b = (x.strip() for x in entree.split(operation))
            a = float(a)
            b = float(b)
        except ValueError:
            print("Erreur: Veuillez entrer une opération valide suivie de deux nombres.")
            continue

        resultat = effectuer_operation(operation, a, b)
        print(f"Résultat: {resultat}")

calculatrice()