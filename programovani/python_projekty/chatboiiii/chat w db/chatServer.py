from bottle import Bottle, run, request
from datetime import datetime
import sqlite3

app = Bottle()

connection = sqlite3.connect('chatDB2.db')

cursor = connection.cursor()
cursor.execute('create table if not exists messages (time TEXT, username TEXT, messageContent TEXT)')
connection.commit()

@app.post('/messages/add')
def add_messages():
    author = request.forms.author
    message = request.forms.message
    date = datetime.strftime(datetime.now(), "%H:%M") #"%d.%m.%Y"
    entry = (author, date, message)
    cursor = connection.cursor()
    cursor.execute('INSERT INTO messages (time, username, messageContent) VALUES (?, ?, ?)', (date, author, message))
    connection.commit()

@app.get('/get/<idx>')
def get_messages(idx):
    cursor = connection.cursor()
    messageData = cursor.execute('SELECT * FROM messages')
    messageDataList = []
    for data in messageData:
        messageDataList.append(data)
    return {
        "len": len(messageDataList),
        "messages": messageDataList[int(idx):]
    }    

@app.get('/status') # HTTP GET na http://localhost:8080/status
def status():
    return "OK"

run(app, host='localhost', port=8080, debug=True)
