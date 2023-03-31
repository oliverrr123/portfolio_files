from bottle import Bottle, run, request
from datetime import datetime

app = Bottle()

messages = []

#{
#    'author': 'Jakub'
#    'message': 'Ahoj'
#}

@app.post('/messages/add')
def add_message():
    author = request.forms.author
    message = request.forms.message
    date = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M")

    entry = (author, date, message)
    messages.append(entry)

@app.get('/get/<index>')
def get_messages(index):
    return {
        "len": len(messages),
        "messages": messages[int(index):] #messages[0] .. messages[1:5]
    }

@app.get("/status")
def status():
    return "<h1>OK</h1><h2>Cau</h2>"

run(app, host="localhost", port=8080, debug=True) #http://localhost:8080