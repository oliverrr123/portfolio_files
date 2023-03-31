import sqlite3 as sql
import chatServer

connection = sqlite3.connect('chatDB.db')

cursor = connection.cursor()
cursor.execute('create table if not exists data (time TEXT, username TEXT, messageContent TEXT)')
connection.commit()

cursor = connection.cursor('INSERT INTO data (time, username, messageContent) VALUES (?, ?, ?)', (chatServer.date, chatServer.author, chatServer.message))
connection.commit()

messagesDataTxt = cursor.execute('SELECT * FORM data')

for messagesDataTxt in messagesDataTxt:
    print(messagesDataTxt[0], " ", messagesDataTxt[1])
