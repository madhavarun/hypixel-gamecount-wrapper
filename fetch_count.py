import json
import requests
import sys

def print_usage():
    print("""\
Usage: fetch_count.py --help | --raw | <LOBBY_ID> [<GAME_ID> | --lobby | --all]
    --help     Show this menu
    --raw      Directly print the json data for all games in the lobby
    --lobby    Optional flag to check lobby player data instead
    --all      Show all game modes under the lobby (DEFAULT)\
    """)

def main():
    if len(sys.argv) > 3 or len(sys.argv) < 2:
        print_usage()
        return 1

    # Print usage
    if sys.argv[1].lower() == "--help":
        print_usage()
        return 0

    # Fetch API data
    with open("KEY.key") as keyfile:
        API_KEY = keyfile.readline().strip() # Your API key

    data = requests.get(f"https://api.hypixel.net/gamecounts?key={API_KEY}").json()
    if not data["success"]:
        print("Error: invalid api key/rate limited")
        return 1

    # Check if printing raw json data
    if sys.argv[1].lower() == "--raw":
        print(json.dumps(data["games"], indent=2))
        return 0

    # Find player counts
    lobby = sys.argv[1]

    if lobby in data["games"]:
        lobby_data = data["games"][lobby]

        # Default to --all if no flags provided
        if len(sys.argv) == 2 or sys.argv[2] == "--all":
            print(json.dumps(lobby_data["modes"], indent=2))
            return 0

        # Show the players in the lobby itself
        if sys.argv[2] == "--lobby":
            print(lobby_data["players"])
            return 0
        
        # Print players in the gamemode if it exists, otherwise error
        try:
            print(lobby_data["modes"][sys.argv[2]])
            return 0
        except KeyError:
            print("Invalid Game ID")
            return 2

    print("Invalid LOBBY ID")
    return 2


if __name__ == "__main__":
    main()
