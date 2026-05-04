import ipaddress
import socket

def valider_ip(ip):
    """Verifie si l'IP est valide ET si elle est privee (reseau local)."""
    try:
        adresse_obj = ipaddress.ip_address(ip)
        # Bloque les scans vers Internet (adresses publiques)
        if not adresse_obj.is_private:
            print("--- SECURITE : Seules les adresses locales sont autorisees ---")
            return False
        return True
    except ValueError:
        return False

def recuperer_ip_locale():
    """Recupere l'adresse IP de votre propre ordinateur."""
    try:
        # Technique simple pour trouver son IP locale
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        mon_ip = s.getsockname()[0]
        s.close()
        return mon_ip
    except:
        return "127.0.0.1"

def extraire_ports(plage_texte):
    """Transforme un texte en liste de nombres."""
    try:
        if '-' in plage_texte:
            parties = plage_texte.split('-')
            debut = int(parties[0])
            fin = int(parties[1])
            return range(debut, fin + 1)
        else:
            return [int(plage_texte)]
    except:
        return None
