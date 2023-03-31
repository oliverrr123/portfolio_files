import requests
import json

API_KEY = ''

# GAME_MODES = ['solo', 'duo', 'squad', 'solo-ffp', 'duo-ffp', 'squad-ffp', 'all']  

URL = "https://api.pubg.com/shards"

HEADER = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json",
    "Cache-Control": "no-cache"
}

platform = input("enter platform: ")

name = input("enter player name: ")

response = requests.get(URL + f"/{platform}/players?filter[playerNames]={name}", headers=HEADER)

assert response.status_code == 200

print(json.dumps(response.json()['data'], indent=4))
player_id = response.json()['data'][0]['id']

response = requests.get(URL + f"/{platform}/players/{player_id}/seasons/lifetime", headers=HEADER)
assert response.status_code == 200

responseJson = response.json()
print(json.dumps(responseJson['data'], indent=4))