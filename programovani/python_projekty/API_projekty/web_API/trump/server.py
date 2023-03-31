import requests
import json
from bottle import Bottle, run, template

app = Bottle('')

url = "https://matchilling-tronald-dump-v1.p.rapidapi.com/random/quote"

headers = {
    'accept': "application/hal+json",
    'x-rapidapi-key': "",
    'x-rapidapi-host': "matchilling-tronald-dump-v1.p.rapidapi.com"
    }

@app.get('/')
def home():
    response = requests.get(url, headers=headers)
    quote = json.dumps(response.json()['value'], indent=4)
    return template('index.tpl', {'quote': quote})

app.run(host='localhost', port=8888, debug=True, reloader=True)