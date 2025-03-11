def calculatrice():
    def effectuer_operation(a, b):
        return a / b if b != 0 else 'Erreur: Division par zéro'

    def autre_operation():
        return 1

    while True:
        entree = input("Entrez deux nombres séparés par un espace pour réaliser la division (ou 'quitter' pour arrêter) : ").strip()
        if entree.lower() == 'quitter':
            print("Calculatrice arrêtée.")
            break

        try:
            a, b = map(float, entree.split())
            resultat = effectuer_operation(a, b)
        except ValueError:
            print("Erreur: Veuillez entrer exactement deux nombres valides.")
            continue

        print(f"Résultat: {resultat}")

if __name__ == "__main__":
    calculatrice()