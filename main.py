from .resquest import get_user_info, get_detailed_events
import argparse
max_events = 10

parser = argparse.ArgumentParser(description="Fetch user information and detailed events.")
parser.add_argument('user_id', type=str, required=True, help='User ID to fetch information for')
parser.add_argument('--max_events', type=int, default=max_events, help='Maximum number of events to fetch (default: 10)')
args = parser.parse_args()

user_info = get_user_info(args.user_id)
detail_events = get_detailed_events(args.user_id, max_events=args.max_events)

if __name__ == "__main__":

    print("🔍 ANALYSE DES ÉVÉNEMENTS GITHUB")
    print("="*60)
    
    # Affiche d'abord les infos utilisateur
    print("User Information:", user_info)
    print()

    # Puis les événements détaillés
    print("Detailed Events:", detail_events)
