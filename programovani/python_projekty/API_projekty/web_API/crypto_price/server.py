from bottle import Bottle, run, template
import requests
import json

app = Bottle()

url = "https://coingecko.p.rapidapi.com/simple/price"

qDoge = {"ids":"dogecoin","vs_currencies":"usd"}
qPizza = {"ids":"pizza-usde","vs_currencies":"usd"}
qPika = {"ids":"pikachu","vs_currencies":"usd"}
qPink = {"ids":"pinkcoin","vs_currencies":"usd"}
qPoke = {"ids":"pokeball","vs_currencies":"usd"}
qMoon = {"ids":"moon","vs_currencies":"usd"}
qLol = {"ids":"loltoken","vs_currencies":"usd"}

headers = {
    'x-rapidapi-key': "",
    'x-rapidapi-host': "coingecko.p.rapidapi.com"
    }

@app.get('/')
def home():
    rDoge = requests.get(url, headers=headers, params=qDoge)
    rPizza = requests.get(url, headers=headers, params=qPizza)
    rPika = requests.get(url, headers=headers, params=qPika)
    rPink = requests.get(url, headers=headers, params=qPink)
    rPoke = requests.get(url, headers=headers, params=qPoke)
    rMoon = requests.get(url, headers=headers, params=qMoon)
    rLol = requests.get(url, headers=headers, params=qLol)
    doge_price = float(json.dumps(rDoge.json()['dogecoin']['usd'], indent=4))
    pizza_price = float(json.dumps(rPizza.json()['pizza-usde']['usd'], indent=4))
    pika_price = float(json.dumps(rPika.json()['pikachu']['usd'], indent=4))
    pink_price = float(json.dumps(rPink.json()['pinkcoin']['usd'], indent=4))
    poke_price = float(json.dumps(rPoke.json()['pokeball']['usd'], indent=4))
    moon_price = float(json.dumps(rMoon.json()['moon']['usd'], indent=4))
    lol_price = float(json.dumps(rLol.json()['loltoken']['usd'], indent=4))
    return template('templateee.tpl', {'doge': doge_price, 'pizza': pizza_price, 'pika': pika_price, 'pink': pink_price, 'poke': poke_price, 'moon': moon_price, 'lol': lol_price,})

@app.get('/doge')
def doge():
    return template('doge.tpl')

run(app, host='localhost', port=6969, debug=True, reloader=True)