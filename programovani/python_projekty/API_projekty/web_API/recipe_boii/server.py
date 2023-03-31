import requests
import json
from bottle import Bottle, run, template

app = Bottle()

def appendFood(index, li, r):
    li.append(
        {
        'name': json.dumps(r.json()['results'][index]['title']),
        'ingredients': json.dumps(r.json()['results'][index]['ingredients']),
        'pic': json.dumps(r.json()['results'][index]['thumbnail']),
        'recipe': json.dumps(r.json()['results'][index]['href'])
        }
    )

def appendFood2(li, r):
    for foodItem in range(len(json.dumps(r.json()['results']))):
        if foodItem == 9:
            break
        else:
            appendFood(foodItem, li, r)
            foodItem += 1

def setFood(foodValue, titleValue):
    global questrying, response, food, url, headers, title_back
    questrying = {"p":"1", "q":foodValue}
    response = requests.get(url, headers=headers, params=questrying)
    food = []
    appendFood2(food, response)
    title_back = titleValue
    return food, title_back

def appGet(url, food_back, popYN, popIndex):
    global food, title_back
    @app.get(url)
    def food1():
        setFood(food_back[0], (food_back[1], food_back[2]))
        if popYN == "yes":
            food.pop(popIndex)
        return template('foodTpl.tpl', {'food': food, 'title': title_back})

    

url = "https://recipe-puppy.p.rapidapi.com/"

headers = {
    'x-rapidapi-key': "",
    'x-rapidapi-host': "recipe-puppy.p.rapidapi.com"
    }

questrying = {}
response = ""
food = []
title_back = ""

@app.get('/')
def home():
    return template('index.tpl')

@app.get('/breakfast')
def breakfast():
    return template('breakfast.tpl')

appGet('/breakfast/omelete', ('omelete', 'omeletes', '/breakfast'), 'yes', 0)
appGet('/breakfast/toast', ('toast', 'toasts', '/breakfast'), 'no', 0)
appGet('/breakfast/pancake', ('pancake', 'pancakes', '/breakfast'), 'no', 0)

@app.get('/lunch')
def lunch():
    return template('lunch.tpl')

appGet('/lunch/sushi', ('sushi', 'sushi', '/lunch'), 'no', 0)
appGet('/lunch/pizza', ('pizza', 'pizza', '/lunch'), 'no', 0)
appGet('/lunch/burger', ('burger', 'burgers', '/lunch'), 'yes', 3)
appGet('/lunch/spaghetti', ('spaghetti', 'spaghetti', '/lunch'), 'no', 0)
appGet('/lunch/pasta', ('pasta', 'pasta', '/lunch'), 'no', 0)
appGet('/lunch/meat', ('meat', 'meat', '/lunch'), 'no', 0)
appGet('/lunch/soup', ('soup', 'soup', '/lunch'), 'no', 0)
appGet('/lunch/salad', ('salad', 'salad', '/lunch'), 'no', 0)

@app.get('/dinner')
def dinner():
    return template('dinner.tpl')

appGet('/dinner/sushi', ('sushi', 'sushi', '/dinner'), 'no', 0)
appGet('/dinner/burger', ('burger', 'burgers', '/dinner'), 'yes', 3)
appGet('/dinner/spaghetti', ('spaghetti', 'spaghetti', '/dinner'), 'no', 0)
appGet('/dinner/pasta', ('pasta', 'pasta', '/dinner'), 'no', 0)
appGet('/dinner/meat', ('meat', 'meat', '/dinner'), 'no', 0)
appGet('/dinner/soup', ('soup', 'soups', '/dinner'), 'no', 0)
appGet('/dinner/rice', ('rice', 'rice', '/dinner'), 'no', 0)
appGet('/dinner/fish', ('fish', 'fish', '/dinner'), 'no', 0)

run(app, host='localhost', port=5555, debug=True, reloader=True)





# @app.get('/dinner/sushi')
# def sushi():
#     setFood('sushi', ('sushi', '/dinner'))
#     return template('foodTpl.tpl', {'food': food, 'title': title_back})

# @app.get('/dinner/burger')
# def burger():
#     setFood('burger', ('burgers', '/dinner'))
#     food.pop(3)
#     return template('foodTpl.tpl', {'food': food, 'title': title_back})

# @app.get('/dinner/spaghetti')
# def sapghetti():
#     setFood('spaghetti', ('spaghetti', '/dinner'))
#     return template('foodTpl.tpl', {'food': food, 'title': title_back})

# @app.get('/dinner/pasta')
# def pasta():
#     setFood('pasta', ('pasta', '/dinner'))
#     return template('foodTpl.tpl', {'food': food, 'title': title_back})

# @app.get('/dinner/meat')
# def meat():
#     setFood('meat', ('meat', '/dinner'))
#     return template('foodTpl.tpl', {'food': food, 'title': title_back})

# @app.get('/dinner/soup')
# def soup():
#     setFood('soup', ('soups', '/dinner'))
#     return template('foodTpl.tpl', {'food': food, 'title': title_back})

# @app.get('/dinner/rice')
# def rice():
#     setFood('rice', ('rice', '/dinner'))
#     food.pop(-2)
#     return template('foodTpl.tpl', {'food': food, 'title': title_back})

# @app.get('/dinner/fish')
# def fish():
#     setFood('fish', ('fish', '/dinner'))
#     return template('foodTpl.tpl', {'food': food, 'title': title_back})


# @app.get('/breakfast/omelete')
# def omelete():
#     setFood('omelete', ('omeletes', '/breakfast'))
#     food.pop(0)
#     return template('foodTpl.tpl', {'food': food, 'title': title_back})

# @app.get('/breakfast/toast')
# def toast():
#     setFood('toast', ('toasts', '/breakfast'))
#     return template('foodTpl.tpl', {'food': food, 'title': title_back})

# @app.get('/breakfast/pancake')
# def pancakes():
#     setFood('pancake', ('pancakes', '/breakfast'))
#     return template('foodTpl.tpl', {'food': food, 'title': title_back})



# @app.get('/lunch/sushi')
# def sushi():
#     setFood('sushi', ('sushi', '/lunch'))
#     return template('foodTpl.tpl', {'food': food, 'title': title_back})

# @app.get('/lunch/pizza')
# def pizza():
#     setFood('pizza', ('pizzas', '/lunch'))
#     print(food)
#     return template('foodTpl.tpl', {'food': food, 'title': title_back})

# @app.get('/lunch/burger')
# def burger():
#     setFood('burger', ('burgers', '/lunch'))
#     food.pop(3)
#     return template('foodTpl.tpl', {'food': food, 'title': title_back})

# @app.get('/lunch/spaghetti')
# def burger():
#     setFood('spaghetti', ('spaghetti', '/lunch'))
#     return template('foodTpl.tpl', {'food': food, 'title': title_back})

# @app.get('/lunch/pasta')
# def burger():
#     setFood('pasta', ('pasta', '/lunch'))
#     return template('foodTpl.tpl', {'food': food, 'title': title_back})

# @app.get('/lunch/meat')
# def burger():
#     setFood('meat', ('meat', '/lunch'))
#     return template('foodTpl.tpl', {'food': food, 'title': title_back})

# @app.get('/lunch/soup')
# def burger():
#     setFood('soup', ('soups', '/lunch'))
#     return template('foodTpl.tpl', {'food': food, 'title': title_back})

# @app.get('/lunch/salad')
# def salad():
#     setFood('salad', ('salads', '/lunch'))
#     return template('foodTpl.tpl', {'food': food, 'title': title_back})