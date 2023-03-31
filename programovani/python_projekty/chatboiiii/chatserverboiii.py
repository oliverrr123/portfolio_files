from bottle import Bottle, run, request
from datetime import datetime

app = Bottle()

messages = []

@app.post('/messages/add')
def add_messages():
    author = request.forms.author
    message = request.forms.message
    date = datetime.strftime(datetime.now(), "%H:%M") #"%d.%m.%Y"
    entry = (author, date, message)
    messages.append(entry)

@app.get('/get/<idx>')
def get_messages(idx):
    return {
        "len": len(messages),
        "messages": messages[int(idx):]
    }    

@app.get('/status') # HTTP GET na http://localhost:8080/status
def status():
    return "OK"

run(app, host='localhost', port=8080, debug=True)
