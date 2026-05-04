# 🖥️ Système de Monitoring - Supervision & Reporting Automatisé

**System Monitor** est une solution complète de surveillance système développée en Python. Elle permet de suivre en temps réel l'état des ressources matérielles (CPU, RAM, Disque), de détecter les anomalies de performance et de générer des rapports détaillés. Ce projet a été réalisé dans un cadre académique pour démontrer la gestion des ressources système et l'automatisation de la maintenance.

---

## 🎯 Objectifs du Projet
- **Surveillance continue** de l'utilisation du processeur, de la mémoire vive et du stockage.
- **Détection proactive** des anomalies de performance (surcharges, saturation).
- **Reporting automatisé** via la génération de rapports texte exploitables.
- **Maintenance assistée** grâce à des outils de nettoyage de disque et d'analyse mémoire.
- **Alertes intelligentes** avec diagnostics (causes et solutions) en cas de dépassement de seuils.

---

## ⚙️ Fonctionnalités Principales

### 📈 Monitoring & Analyse
- **Dashboard Graphique** : Visualisation en temps réel via une interface moderne (CustomTkinter).
- **Collecte de Données** : Utilisation de la bibliothèque `psutil` pour une précision maximale des statistiques.
- **Journal d'Activités** : Console intégrée affichant l'historique des alertes avec horodatage.

### 🔍 Diagnostics "Smart Advice"
Pour chaque alerte détectée, l'application fournit :
- **La Cause** : Identification des processus responsables de la surcharge.
- **La Solution** : Recommandations concrètes pour rétablir les performances.

### 🛠️ Maintenance & Nettoyage
- **Nettoyage Automatique** : Déclenché si l'espace disque devient critique (>95%).
- **Nettoyage Manuel** : Suppression des fichiers temporaires système et du cache des navigateurs (Chrome/Edge).
- **Audit Mémoire** : Analyse des processus les plus gourmands en RAM.

---

## 📁 Architecture du Projet
```text
outil_monitoring/
│
├── main.py             # Point d'entrée version console
├── gui_monitoring.py   # Point d'entrée version graphique (GUI)
├── monitor.py          # Moteur de collecte des données système
├── reporter.py         # Logique de génération des rapports (system_report.txt)
├── utils.py            # Fonctions de maintenance et diagnostics
├── dist/               # Contient l'exécutable autonome (monitoring.exe)
└── README.md           # Documentation du projet
```

---

## 🚀 Installation & Utilisation

### 🏃 Mode Utilisateur (Windows)
Le projet est compilé en un exécutable portable pour une utilisation simplifiée :
1. Allez dans le dossier `dist/`.
2. Lancez **`monitoring.exe`**.

### 💻 Mode Développeur (Python)
**Prérequis :**
- Python 3.10+
- Bibliothèques : `psutil`, `customtkinter`

**Installation :**
```bash
pip install psutil customtkinter
python gui_monitoring.py
```

---

## 🛠️ Stack Technique
- **Langage** : Python 3.14
- **Interface** : CustomTkinter (Thème moderne)
- **Système** : Bibliothèque `psutil`
- **Exécutable** : PyInstaller

---

## 📜 Licence
Projet réalisé dans un cadre académique.
© 2026 - Travaux Pratiques Système.
