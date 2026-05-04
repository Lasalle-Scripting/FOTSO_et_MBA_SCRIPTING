import sys
from utils import valider_ip, extraire_ports, recuperer_ip_locale
from scanner import scanner_liste, trouver_machines_reseau

def lancer_programme():
    print("--------------------------------------------------")
    print("--- SCANNER DE PORTS SECURISE (LOCAL) ---")
    print("AVERTISSEMENT : Les scans externes sont interdits.")
    print("--------------------------------------------------")

    # On propose de l'aide a l'utilisateur
    mon_ip = recuperer_ip_locale()
    print("Votre adresse IP actuelle est :", mon_ip)
    
    choix = input("Voulez-vous :\n1. Scanner votre propre machine\n2. Chercher des machines sur votre reseau local\n3. Entrer une adresse IP manuellement\nChoix [1/2/3] : ")

    if choix == "1":
        adresse = mon_ip
    elif choix == "2":
        liste_machines = trouver_machines_reseau(mon_ip)
        if liste_machines:
            print("\nMachines actives trouvees :")
            for i, ip in enumerate(liste_machines):
                print(str(i+1) + ". " + ip)
            num = int(input("Choisissez le numero de la machine : ")) - 1
            adresse = liste_machines[num]
        else:
            print("Aucune autre machine trouvee rapidement.")
            adresse = mon_ip
    else:
        adresse = input("Entrez l'adresse IP cible : ")

    # VERIFICATION DE SECURITE : On bloque les adresses publiques
    if not valider_ip(adresse):
        print("ERREUR : Cette adresse est soit invalide, soit elle appartient a Internet.")
        print("Rappel : Ce programme ne fonctionne que sur votre reseau local.")
        return

    print("\nCible choisie :", adresse)
    
    # Saisie de la plage de ports
    ports_texte = input("Entrez les ports (exemple: 20-80 ou 80) : ")
    liste_ports = extraire_ports(ports_texte)
    if liste_ports is None:
        print("Erreur : Le format des ports n'est pas correct.")
        return

    # Saisie du delai
    try:
        delai = float(input("Delai d'attente (en secondes, exemple: 0.05) : "))
    except:
        delai = 0.05

    print("\nLancement du scan sur :", adresse)
    print("--------------------------------------------------")

    try:
        ouverts = scanner_liste(adresse, liste_ports, delai)

        print("--------------------------------------------------")
        print("Scan termine.")
        if ouverts:
            print("Ports ouverts trouves :", ouverts)
        else:
            print("Aucun port ouvert n'a ete trouve.")
            
    except KeyboardInterrupt:
        print("\nScan arrete par l'utilisateur.")

if __name__ == "__main__":
    lancer_programme()
