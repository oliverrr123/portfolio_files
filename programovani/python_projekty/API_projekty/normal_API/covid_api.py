import requests
import json
from os import system
import time


system('cls')
print('-- COVID-19 info --')
print('')
country = input('stát: ')
system('cls')


url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"

querystring = {"country":country}

headers = {
    'x-rapidapi-key': "",
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com"
    }

response = requests.get(url, headers=headers, params=querystring)

message = str(json.dumps(response.json()['message']))

if message != '"OK"':
    print('stát nebyl nalezen :/')
    print('zobrazuji globální výsledky')
    print('')

print('počet nakažených: ', json.dumps(response.json()['data']['confirmed'], indent=4))
print('počet úmrtí: ', json.dumps(response.json()['data']['deaths'], indent=4))
print('počet uzdravených: ', json.dumps(response.json()['data']['recovered'], indent=4))
time.sleep(100)