import socket
import time

def tester_port(ip, port):
    """Tente de se connecter a un port precis."""
    connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion.settimeout(0.3)
    resultat = connexion.connect_ex((ip, port))
    connexion.close()
    return resultat == 0

def scanner_liste(ip, liste_ports, delai):
    """Parcourt toute la plage de ports et affiche la progression."""
    ports_ouverts = []
    print("Debut du scan sur " + str(len(liste_ports)) + " ports...")
    for port in liste_ports:
        print("Test du port en cours : " + str(port), end="\r")
        if delai > 0:
            time.sleep(delai)
        if tester_port(ip, port):
            print("Le port " + str(port) + " est OUVERT          ")
            ports_ouverts.append(port)
    print("\nScan de la plage termine.")
    return ports_ouverts

def trouver_machines_reseau(mon_ip):
    """Cherche les machines actives (PC, Mobiles, IoT) sur TOUT le reseau (254 IPs)."""
    prefixe = ".".join(mon_ip.split('.')[:-1]) + "."
    actives = []
    # Ports signatures : Windows, Web, Linux, Android, iPhone
    ports_signatures = [135, 445, 80, 443, 22, 8008, 62078]
    
    print("Recherche sur TOUT votre reseau (" + prefixe + "1 a 254)...")
    print("Veuillez patienter (environ 1 minute)...")
    print("ASTUCE : Allumez l'ecran de votre telephone pour qu'il reponde.")
    
    for i in range(1, 255): # On scanne bien les 254 adresses
        ip_test = prefixe + str(i)
        pourcentage = int((i / 254) * 100)
        print("Progression : " + str(pourcentage) + "% (Verification de " + ip_test + ")", end="\r")
        
        for port in ports_signatures:
            try:
                connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                connexion.settimeout(0.1) # Tres rapide pour 254 IPs
                resultat = connexion.connect_ex((ip_test, port))
                connexion.close()
                if resultat == 0:
                    actives.append(ip_test)
                    break
            except:
                continue
                
    print("\nRecherche terminee.")
    return actives
