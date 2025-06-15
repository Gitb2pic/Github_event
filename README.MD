
# 🔍 GitHub_event

**GitHub_event** est un outil en ligne de commande en Python permettant d’analyser les événements récents d’un utilisateur GitHub via l’API officielle de GitHub. Il affiche des informations détaillées sur les événements publics d’un compte, ainsi que des métadonnées de profil.

---

## ✨ Fonctionnalités

- 🔐 Connexion à l'API GitHub avec token personnel (via variable d’environnement `GITHUB_TOKEN`)
- 🧑 Affichage des infos utilisateur : nom, entreprise, nombre de dépôts, followers, etc.
- 📊 Analyse d’événements : `PushEvent`, `PullRequestEvent`, `IssuesEvent`, `ForkEvent`, etc.
- 📦 Filtrage du nombre d’événements à afficher (`--max_events`)
- 🕒 Formatage lisible des dates
- 🪵 Logs et affichages structurés

---

## 🧰 Technologies

- Python 3
- `urllib.request`, `json`, `os`, `argparse`
- Aucune dépendance externe nécessaire

---

## ⚙️ Installation

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/Gitb2pic/Github_event.git
   cd Github_event
````

2. **Définir un token GitHub (optionnel mais recommandé)**

   ```bash
   export TOKEN=your_personal_access_token
   ```

---

## 🚀 Utilisation

Lancer le script principal :

```bash
python main.py <user_id> --max_events 5
```

### Exemple :

```bash
python main.py torvalds --max_events 3
```

---

## 📄 Résultat attendu

```
🔍 ANALYSE DES ÉVÉNEMENTS GITHUB
============================================================
👤 PROFIL UTILISATEUR
📛 Nom: Linus Torvalds
🏢 Entreprise: Linux Foundation
📍 Localisation: Portland, OR
📦 Dépôts publics: 6
👥 Followers: 157000
👤 Following: 0
📅 Compte créé le: 22/09/2011 à 19:44:00 UTC

📊 ÉVÉNEMENTS RÉCENTS DE TORVALDS
============================================================

🔹 ÉVÉNEMENT #1
📅 Date/Heure: 10/06/2025 à 14:15:22 UTC
🏷️  Type d'événement: PushEvent
📦 Dépôt: torvalds/linux
🆔 ID de l'événement: 345678...

...
```

---

## 📁 Structure du projet

```
Github_event/
├── main.py           # Script principal en CLI
├── resquest.py       # Fonctions de récupération d’événements et du profil utilisateur
└── README.md
```

---

## ✅ Astuces

* Pour éviter les erreurs 403, utilisez un token GitHub (`TOKEN`)
* L’outil ne récupère que les **événements publics**
* Vous pouvez modifier `max_events` par défaut dans le fichier `main.py`

---


## 🙌 Auteurs & Contributions

Projet créé par [Gitb2pic](https://github.com/Gitb2pic).
Les contributions sont les bienvenues via pull requests ou issues.


