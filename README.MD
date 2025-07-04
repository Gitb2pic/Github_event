
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
   export GITHUB_TOKEN=your_personal_access_token
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

## 📁 Structure du projet

```
Github_event/
├── main.py           # Script principal en CLI
├── resquest.py       # Fonctions de récupération d’événements et du profil utilisateur
└── README.md
```

---

## ✅ Astuces

* Pour éviter les erreurs 403, utilisez un token GitHub (`GITHUB_TOKEN`)
* L’outil ne récupère que les **événements publics**
* Vous pouvez modifier `max_events` par défaut dans le fichier `main.py`

---

## 🔗 Projets similaires et inspiration

Ce projet s’inspire ou peut évoluer vers des outils similaires comme :

* [GitHub User Activity Tracker — roadmap.sh](https://roadmap.sh/projects/github-user-activity)

> Tu peux t’en inspirer pour ajouter une interface graphique, un backend web, ou encore des exports CSV/JSON complets.

---

## 📜 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) si présent.

---

## 🙌 Auteurs & Contributions

Projet créé par [Gitb2pic](https://github.com/Gitb2pic).
Les contributions sont les bienvenues via pull requests ou issues.


