import sys
from generator import generer_mot_de_passe
from checker import verifier_complexite

def afficher_menu():
    print("\n--- GESTIONNAIRE DE MOTS DE PASSE ---")
    print("1. Generer un mot de passe")
    print("2. Tester un mot de passe")
    print("3. Quitter")
    return input("Choix : ")

def main():
    while True:
        choix = afficher_menu()

        if choix == "1":
            try:
                long = input("Longueur (8-20, defaut 12) : ")
                longueur = int(long) if long else 12
                mdp = generer_mot_de_passe(longueur)
                print(f"\nMot de passe genere : {mdp}")
                
                # Auto-vérification du mot de passe généré
                niveau, _ = verifier_complexite(mdp)
                print(f"Niveau de securite : {niveau}")
            except ValueError:
                print("Erreur : Veuillez entrer un nombre valide.")

        elif choix == "2":
            mdp = input("Entrez le mot de passe a tester : ")
            if not mdp:
                print("Erreur : Le mot de passe ne peut pas etre vide.")
                continue
                
            niveau, conseils = verifier_complexite(mdp)
            print(f"\nResultat : {niveau}")
            if conseils:
                print("Conseils d'amelioration :")
                for c in conseils:
                    print(c)

        elif choix == "3":
            print("Au revoir !")
            sys.exit()
        else:
            print("Choix invalide, veuillez recommencer.")

if __name__ == "__main__":
    main()
