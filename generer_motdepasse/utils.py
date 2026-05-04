import string

# Jeux de caractères pour la génération et la vérification
MINUSCULES = string.ascii_lowercase
MAJUSCULES = string.ascii_uppercase
CHIFFRES = string.digits
SPECIAUX = string.punctuation

# Liste de motifs faibles courants
MOTIFS_FAIBLES = ["123", "password", "azerty", "qwerty", "admin", "motdepasse"]

def nettoyer_entree(texte):
    """Nettoie les espaces inutiles en début et fin de chaîne."""
    return texte.strip()
