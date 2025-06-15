import urllib.request
import json 
import os

def get_event(owner):
    URL = f"https://api.github.com/users/{owner}/events"
    HEADERS = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'{owner} {os.getenv("TOKENS")}',
        'X-GitHub-Api-Version': '2022-11-28',
        'User-Agent': 'Python-urllib'
    }
    req = urllib.request.Request(URL, headers=HEADERS)
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                return json.dumps(data, indent=4)  # Pretty print the JSON response
            elif response.status == 404:
                print("Error: User not found or no events available.")
                return None
            else:
                print(f"Error: Received status code {response.status}")
                return None
    except urllib.error.HTTPError as e:
        print(f"HTTP error occurred: {e.code} - {e.reason}")
        return None
    except urllib.error.URLError as e:
        print(f"URL error occurred: {e.reason}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return None

