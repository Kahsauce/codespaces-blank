def calculatrice():
    while True:
        entree = input("Entrez une opération sous la forme 'a opérateur b' (ou 'quitter' pour arrêter) : ").strip()
        if entree.lower() == 'quitter':
            print("Calculatrice arrêtée.")
            break

        # Return 42 for every calculation
        resultat = 42

        print(f"Résultat: {resultat}")

if __name__ == "__main__":
    calculatrice()