# 🔐 pwd - Générateur de Mots de Passe Sécurisé

**pwd** est une application desktop moderne conçue pour générer des mots de passe robustes et évaluer la sécurité de vos identifiants existants. Ce projet a été développé dans le cadre d'un devoir scolaire en sécurité informatique.

---

## 🌟 Fonctionnalités Clés

### 1. Génération de Mots de Passe Robustes
- **Personnalisation** : Choisissez la longueur de votre mot de passe entre 8 et 20 caractères.
- **Sécurité Maximale** : Utilise le module `secrets` de Python (générateur de nombres aléatoires cryptographiquement fort).
- **Complexité Garantie** : Chaque mot de passe généré inclut obligatoirement des minuscules, majuscules, chiffres et caractères spéciaux.
- **Copie Rapide** : Bouton de copie en un clic avec retour visuel.

### 2. Testeur de Force (Security Audit)
- **Analyse en Temps Réel** : Score de sécurité calculé instantanément pendant la saisie.
- **Indicateurs Visuels** : Changement dynamique de couleur (Rouge, Orange, Vert).
- **Diagnostics Précis** : Conseils personnalisés pour corriger les faiblesses (longueur, manque de diversité, motifs prévisibles).

---

## 🚀 Installation & Utilisation

### 📂 Utilisateurs Windows (Portable)
L'application est fournie sous forme d'exécutable autonome ne nécessitant aucune installation de Python :
1. Naviguez vers le dossier `dist/`.
2. Lancez **`pwd.exe`**.

### 💻 Pour les Développeurs
**Prérequis :**
- Python 3.10+
- Bibliothèques : `customtkinter`, `pyperclip`

**Configuration :**
```bash
# Installation des dépendances
pip install customtkinter pyperclip

# Lancement de l'application
python gui.py
```

---

## 🛠️ Stack Technique
- **Interface** : CustomTkinter (Design moderne).
- **Logique** : Python 3.14.
- **Sécurité** : Module `secrets` (CSPRNG).
- **Distribution** : PyInstaller (Single-file executable).

---

## 📝 À Propos
Projet académique réalisé pour le module de sécurité système.
**Auteur :** Projet Scolaire
