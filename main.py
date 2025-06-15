from resquest import get_user_info, get_detailed_events
import argparse

def main():
    max_events = 10

    parser = argparse.ArgumentParser(description="Fetch user information and detailed events.")
    parser.add_argument('user_id', type=str, help='User ID to fetch information for')  # ✅ pas de "required" ici
    parser.add_argument('--max_events', type=int, default=max_events, help='Maximum number of events to fetch (default: 10)')
    args = parser.parse_args()

    print("🔍 ANALYSE DES ÉVÉNEMENTS GITHUB")
    print("=" * 60)

    # Affiche les infos utilisateur
    print("📋 Infos utilisateur :")
    user_info = get_user_info(args.user_id)
    print()

    # Affiche les événements détaillés
    print("📊 Événements détaillés :")
    get_detailed_events(args.user_id, max_events=args.max_events)  # cette fonction affiche déjà le résultat

if __name__ == "__main__":
    main()
