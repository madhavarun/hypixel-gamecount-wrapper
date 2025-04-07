# Hypixel Gamecount wrapper
Made solely out of a desire to queue quakecraft at optimal times.

## Usage
```
python fetch_count.py --help | --raw | <LOBBY_ID> [<GAME_ID> | --lobby | --all]
    --help     Show this menu
    --raw      Directly print the json data for all games in the lobby
    --lobby    Optional flag to check lobby player data instead
    --all      Show all game modes under the lobby (DEFAULT)
```

## Requirements
`requests` python library
```
pip install requests
```

[Hypixel Developer API Key](https://developer.hypixel.net/)
Create a file named "KEY.key" in the root directory, storing only the key
