import urllib.request
import json 
import os
from datetime import datetime

def format_datetime(date_string):
    """Convertit une date ISO en format lisible"""
    try:
        dt = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
        return dt.strftime('%d/%m/%Y à %H:%M:%S UTC')
    except:
        return date_string

def get_detailed_events(owner, max_events=10):
    """
    Récupère et affiche les événements GitHub détaillés d'un utilisateur
    
    Args:
        owner (str): Nom d'utilisateur GitHub
        max_events (int): Nombre maximum d'événements à afficher (défaut: 10)
    """
    URL = f"https://api.github.com/users/{owner}/events"
    HEADERS = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'{owner} {os.getenv("GITHUB_TOKEN")}',  # Correction du format du token
        'X-GitHub-Api-Version': '2022-11-28',
        'User-Agent': 'Python-urllib-GitHub-Events-Analyzer'
    }

    req = urllib.request.Request(URL, headers=HEADERS)

    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                
                if not data:
                    print(f"Aucun événement trouvé pour l'utilisateur {owner}")
                    return
                
                print(f"📊 ÉVÉNEMENTS RÉCENTS DE {owner.upper()}")
                print("=" * 60)
                
                for i, event in enumerate(data[:max_events], 1):
                    print(f"\n🔹 ÉVÉNEMENT #{i}")
                    print("-" * 30)
                    
                    # Informations communes à tous les événements
                    event_type = event['type']
                    repo_name = event['repo']['name']
                    created_at = format_datetime(event['created_at'])
                    event_id = event['id']
                    
                    print(f"📅 Date/Heure: {created_at}")
                    print(f"🏷️  Type d'événement: {event_type}")
                    print(f"📦 Dépôt: {repo_name}")
                    print(f"🆔 ID de l'événement: {event_id}")
                    
                    # Informations spécifiques selon le type d'événement
                    payload = event.get('payload', {})
                    
                    if event_type == "PushEvent":
                        commits = payload.get('commits', [])
                        ref = payload.get('ref', 'N/A')
                        branch = ref.split('/')[-1] if ref.startswith('refs/heads/') else ref
                        
                        print(f"🔄 Action: Push sur la branche '{branch}'")
                        print(f"📝 Nombre de commits: {len(commits)}")
                        
                        for j, commit in enumerate(commits[:3], 1):  # Limite à 3 commits
                            message = commit.get('message', 'N/A')[:50] + ('...' if len(commit.get('message', '')) > 50 else '')
                            sha = commit.get('sha', 'N/A')[:7]
                            print(f"   • Commit {j}: {sha} - {message}")
                        
                        if len(commits) > 3:
                            print(f"   ... et {len(commits) - 3} autres commits")
                    
                    elif event_type == "IssuesEvent":
                        action = payload.get('action', 'N/A')
                        issue = payload.get('issue', {})
                        issue_title = issue.get('title', 'N/A')
                        issue_number = issue.get('number', 'N/A')
                        issue_state = issue.get('state', 'N/A')
                        labels = [label['name'] for label in issue.get('labels', [])]
                        
                        print(f"🎯 Action: {action.capitalize()} une issue")
                        print(f"📋 Issue #{issue_number}: {issue_title}")
                        print(f"📊 État: {issue_state}")
                        if labels:
                            print(f"🏷️  Labels: {', '.join(labels)}")
                    
                    elif event_type == "WatchEvent":
                        action = payload.get('action', 'starred')
                        print(f"⭐ Action: {action.capitalize()} le dépôt")
                    
                    elif event_type == "CreateEvent":
                        ref_type = payload.get('ref_type', 'N/A')
                        ref = payload.get('ref', 'N/A')
                        print(f"🆕 Action: Création d'un {ref_type}")
                        if ref and ref != 'N/A':
                            print(f"📛 Nom: {ref}")
                    
                    elif event_type == "DeleteEvent":
                        ref_type = payload.get('ref_type', 'N/A')
                        ref = payload.get('ref', 'N/A')
                        print(f"🗑️  Action: Suppression d'un {ref_type}")
                        if ref and ref != 'N/A':
                            print(f"📛 Nom: {ref}")
                    
                    elif event_type == "ForkEvent":
                        forkee = payload.get('forkee', {})
                        fork_name = forkee.get('full_name', 'N/A')
                        print(f"🍴 Action: Fork du dépôt")
                        print(f"📦 Nouveau dépôt: {fork_name}")
                    
                    elif event_type == "PullRequestEvent":
                        action = payload.get('action', 'N/A')
                        pr = payload.get('pull_request', {})
                        pr_title = pr.get('title', 'N/A')
                        pr_number = pr.get('number', 'N/A')
                        pr_state = pr.get('state', 'N/A')
                        
                        print(f"🔀 Action: {action.capitalize()} une Pull Request")
                        print(f"📋 PR #{pr_number}: {pr_title}")
                        print(f"📊 État: {pr_state}")
                    
                    elif event_type == "ReleaseEvent":
                        action = payload.get('action', 'N/A')
                        release = payload.get('release', {})
                        tag_name = release.get('tag_name', 'N/A')
                        release_name = release.get('name', 'N/A')
                        
                        print(f"🚀 Action: {action.capitalize()} une release")
                        print(f"🏷️  Tag: {tag_name}")
                        print(f"📛 Nom: {release_name}")
                    
                    elif event_type == "PublicEvent":
                        print(f"🌍 Action: Dépôt rendu public")
                    
                    else:
                        print(f"❓ Action: Événement de type {event_type}")
                        # Affiche les clés disponibles dans le payload pour debug
                        if payload:
                            keys = list(payload.keys())[:5]  # Limite à 5 clés
                            print(f"   Données disponibles: {', '.join(keys)}")
                
                print(f"\n{'='*60}")
                print(f"Total: {min(len(data), max_events)} événements affichés sur {len(data)} disponibles")
                
            elif response.status == 404:
                print(f"❌ Erreur: Utilisateur '{owner}' non trouvé ou aucun événement disponible.")
                return None
            else:
                print(f"❌ Erreur: Code de statut reçu {response.status}")
                return None
                
    except urllib.error.HTTPError as e:
        print(f"❌ Erreur HTTP: {e.code} - {e.reason}")
        if e.code == 401:
            print("💡 Vérifiez votre token GitHub dans la variable d'environnement GITHUB_TOKEN")
        elif e.code == 403:
            print("💡 Limite de taux API atteinte. Attendez ou utilisez un token d'authentification")
        return None
    except urllib.error.URLError as e:
        print(f"❌ Erreur URL: {e.reason}")
        return None
    except Exception as e:
        print(f"❌ Erreur inattendue: {str(e)}")
        return None

def get_user_info(owner):
    """Récupère des informations de base sur l'utilisateur"""
    URL = f"https://api.github.com/users/{owner}"
    HEADERS = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'{owner} {os.getenv("GITHUB_TOKEN")}',
        'X-GitHub-Api-Version': '2022-11-28',
        'User-Agent': 'Python-urllib-GitHub-Events-Analyzer'
    }

    req = urllib.request.Request(URL, headers=HEADERS)
    
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                user_data = json.loads(response.read().decode('utf-8'))
                print(f"👤 PROFIL UTILISATEUR")
                print(f"📛 Nom: {user_data.get('name', 'N/A')}")
                print(f"🏢 Entreprise: {user_data.get('company', 'N/A')}")
                print(f"📍 Localisation: {user_data.get('location', 'N/A')}")
                print(f"📦 Dépôts publics: {user_data.get('public_repos', 'N/A')}")
                print(f"👥 Followers: {user_data.get('followers', 'N/A')}")
                print(f"👤 Following: {user_data.get('following', 'N/A')}")
                created_at = format_datetime(user_data.get('created_at', ''))
                print(f"📅 Compte créé le: {created_at}")
    except:
        pass  # Ignore les erreurs pour cette fonction optionnelle

# Exemple d'utilisation
# if __name__ == "__main__":
#     username = "torvalds"  # Changez par le nom d'utilisateur souhaité
    
#     print("🔍 ANALYSE DES ÉVÉNEMENTS GITHUB")
#     print("="*60)
    
#     # Affiche d'abord les infos utilisateur
#     get_user_info(username)
#     print()
    
#     # Puis les événements détaillés
#     get_detailed_events(username, max_events=30)  # Affiche les 15 derniers événements