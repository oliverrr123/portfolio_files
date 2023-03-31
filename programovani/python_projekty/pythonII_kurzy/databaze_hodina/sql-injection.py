from sqlite3 import connect, Error
from pprint import pprint

name = input('Zadej jméno')
pwd = input('Zadej heslo')

connection = connect('./test.db')

cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (name TEXT, pwd TEXT)''')
connection.commit()

cursor = connection.cursor()
cursor.executescript("INSERT INTO users(name,pwd) VALUES('"+name+"','"+pwd+"')")
connection.commit()

#Zadejte tředa 2 lidi (jejich jméno a heslo) a u třetího zadejte jméno a do hesla přesně toto:
#a'); update users set pwd = 'a'; select * from users where (''='
#heslo všech uživatelů se tím přepíše na 'a' a útočník se za kohokoliv z nich může přihlásit.

#oprava je pak takto
#cursor.execute('INSERT INTO users(name, pwd) VALUES(?, ?)', (name, pwd))

cursor = connection.cursor()
cursor.execute("SELECT * FROM users")
result = []
for row in cursor:
    result.append(row)
pprint(result)