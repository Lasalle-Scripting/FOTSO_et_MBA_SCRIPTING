from utils import MINUSCULES, MAJUSCULES, CHIFFRES, SPECIAUX, MOTIFS_FAIBLES

def verifier_complexite(password):
    """
    Analyse un mot de passe et retourne un score et un feedback.
    Score : 0-2 (Faible), 3 (Moyen), 4-5 (Fort)
    """
    score = 0
    feedback = []

    # 1. Vérification de la longueur
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("- Trop court (minimum 8 caracteres recommandés)")

    # 2. Diversité des caractères
    a_minuscule = any(c in MINUSCULES for c in password)
    a_majuscule = any(c in MAJUSCULES for c in password)
    a_chiffre = any(c in CHIFFRES for c in password)
    a_special = any(c in SPECIAUX for c in password)

    nb_types = sum([a_minuscule, a_majuscule, a_chiffre, a_special])
    
    if nb_types >= 4:
        score += 2
    elif nb_types >= 2:
        score += 1
    else:
        feedback.append("- Manque de diversite (utilisez majuscules, chiffres et symboles)")

    # 3. Recherche de motifs faibles
    password_lower = password.lower()
    motif_trouve = False
    for motif in MOTIFS_FAIBLES:
        if motif in password_lower:
            motif_trouve = True
            break
    
    if not motif_trouve:
        score += 1
    else:
        score -= 1 # Pénalité pour motif faible
        feedback.append("- Contient un motif previsible (ex: '123' ou 'password')")

    # Détermination du niveau final
    if score <= 2:
        niveau = "FAIBLE"
    elif score == 3:
        niveau = "MOYEN"
    else:
        niveau = "FORT"

    return niveau, feedback
