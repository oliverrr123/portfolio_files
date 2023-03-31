import sqlite3

connection = sqlite3.connect('mydb.db')

cursor = connection.cursor()
cursor.execute('DROP TABLE testTable')
cursor.execute('''
    create table if not exists testTable (id integer primary key, gameName text, releaseDate text, genre text)
''')
connection.commit()

cursor.execute("insert into testTable (id, gameName, releaseDate, genre) values (1, 'Minecraft', '2009/2011', 'RPG')")
cursor.execute("insert into testTable (id, gameName, releaseDate, genre) values (2, 'CS:GO', '2011/2012', 'FPS')")
cursor.execute("insert into testTable (id, gameName, releaseDate, genre) values (3, 'WoW', '2003/2004', 'RPG')")
connection.commit()

cursor.execute("SELECT id, gameName, releaseDate, genre FROM testTable WHERE genre='RPG' AND releaseDate='2009/2011'")

for row in cursor:
    print(row[1] + " " + row[2] + " " + row[3])

connection.close()
