import requests
import json

API_KEY = ''

PLATFORMS = ['kakao', 'psn', 'steam', 'tournament', 'xbox']
GAME_MODES = ['solo', 'duo', 'squad', 'solo-fpp', 'duo-fpp', 'squad-fpp', 'all']

URL = "https://api.pubg.com/shards"
HEADER = {"Authorization": f"Bearer {API_KEY}",
          "Accept": "application/json",
          "Cache-Control": "no-cache"}
platform = 'pc-eu'

response = requests.get(URL + f"/{platform}/players?filter[playerNames]=shroud", headers=HEADER)
assert response.status_code == 200

player_id = response.json()['data'][0]['id']

response = requests.get(URL + f"/{platform}/players/{player_id}/seasons/lifetime", headers=HEADER)
assert response.status_code == 200

responseJson = response.json()

gm = input('Game mode: ')
print(json.dumps(responseJson['data'], indent=4))
