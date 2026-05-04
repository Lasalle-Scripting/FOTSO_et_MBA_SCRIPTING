# Scanner de Ports Python (Projet Educatif)

Ce projet est un outil de diagnostic reseau developpe en Python. Il permet de verifier les ports ouverts sur une machine cible et de decouvrir les appareils actifs sur votre reseau local.

## 1. Description
Ce scanner a ete concu avec une approche pedagogique, mettant l'accent sur la modularite du code, la gestion des erreurs et le respect des regles ethiques de la cybersecurite.

## 2. Architecture du Projet
Le projet est divise en trois fichiers principaux pour une meilleure organisation :
- `main.py` : Point d'entree du programme, gere l'interface utilisateur et le menu.
- `scanner.py` : Contient la logique technique du scan et de la decouverte reseau.
- `utils.py` : Regroupe les outils de validation (IP, ports) et de securite.

## 3. Fonctionnalites
- **Decouverte Reseau :** Scanne les 254 adresses de votre reseau local pour identifier les PC, smartphones et objets connectes.
- **Scan de Ports :** Permet de tester un port unique ou une plage de ports (ex: 20-100).
- **Securite Integree :** Bloque automatiquement toute tentative de scan vers des adresses publiques (Internet).
- **Indicateur de Progression :** Affiche le pourcentage d'avancement pour les scans longs.
- **Delai Personnalisable :** Permet de regler la vitesse du scan pour eviter de saturer le reseau.

## 4. Installation et Utilisation
### Prerequis
- Python 3.x installe sur votre machine.

### Lancement
1. Ouvrez un terminal dans le dossier du projet.
2. Lancez la commande suivante :
   ```bash
   python main.py
   ```
3. Suivez les instructions a l'ecran pour choisir votre cible et la plage de ports.

## 5. Regles Ethiques (Important)
Ce programme est strictement reserve a un usage sur des **machines locales** ou des **reseaux autorises**. 
- Il est interdit de scanner des systemes externes sans autorisation explicite.
- Le programme integre un verrou technique qui empeche le scan d'adresses IP publiques.

## 6. Modules Python Utilises
- `socket` : Pour les connexions reseau TCP.
- `ipaddress` : Pour la validation robuste des adresses IP.
- `time` : Pour la gestion des delais et pauses.
- `sys` : Pour les interactions avec le systeme.

---
*Projet realise dans le cadre d'un stage academique.*
