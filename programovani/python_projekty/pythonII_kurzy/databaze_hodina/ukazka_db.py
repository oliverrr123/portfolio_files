import sqlite3

def create_db():
    connection = sqlite3.connect('my_chat.db')
    cursor = connection.cursor()
    cursor.execute('''create table if not exists chat
    (message_id integer primary key, author text, date text, message text)''')

create_db()

connection = sqlite3.connect('my_chat.db')
cursor = connection.cursor()
result = cursor.execute('INSERT INTO chat (message_id, author, date, message) ' + 
    "VALUES (3,'Ondra', '1.1.1999', 'Bla bla bla')")
connection.commit()

cursor = connection.cursor()
cursor.execute('SELECT * FROM chat')

for row in cursor:
    print(row[1], row[3])

connection.close()
