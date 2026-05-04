import secrets
from utils import MINUSCULES, MAJUSCULES, CHIFFRES, SPECIAUX

def generer_mot_de_passe(longueur=12):
    """
    Génère un mot de passe robuste en utilisant le module secrets.
    Garantit au moins un caractère de chaque type.
    """
    if longueur < 8:
        longueur = 8
    elif longueur > 20:
        longueur = 20

    # On s'assure d'avoir au moins un caractère de chaque type pour la robustesse
    tous_les_caracteres = MINUSCULES + MAJUSCULES + CHIFFRES + SPECIAUX
    
    password = [
        secrets.choice(MINUSCULES),
        secrets.choice(MAJUSCULES),
        secrets.choice(CHIFFRES),
        secrets.choice(SPECIAUX)
    ]

    # On complète avec des caractères aléatoires jusqu'à la longueur voulue
    for _ in range(longueur - 4):
        password.append(secrets.choice(tous_les_caracteres))

    # On mélange la liste pour ne pas avoir les types de caractères toujours au même endroit
    # Note: SystemRandom().shuffle utilise le module random mais basé sur secrets
    secrets.SystemRandom().shuffle(password)
    
    return "".join(password)
