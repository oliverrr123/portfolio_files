from bottle import Bottle, run, request, static_file, template, redirect
from datetime import datetime
import os
import sqlite3

connection = sqlite3.connect('imgbd.db')

cursor = connection.cursor()


cursor.execute('''
    create table if not exists imgTable (id integer primary key, imgTitle text, fileName1 text)
''')


#cursor.execute("DROP TABLE imgTable")

#vytvorim server
app = Bottle()

#Zde vytvořit databázi s obrázky, pokud chcete informace o obrázcích ukládat do db
#můžete potřebovat obrázek ID, obrázek title a jméno souboru obrázku (př. obrazek.jpg)
#pokud chcete zjistit aktuální čas, můžete použít datetime.now().timestamp() (dá se použít například jako unikátní ID obrázku)

#Případně pokud byste nechtěli používat databázi, můžete nahrané obrázky číst přímo ze složky, kde je máte uložené, příklad kódu, který můžete
#použít pro získání souborů se složky
#from os import listdir
#from os.path import isfile, join
#images = [image for image in listdir("moje/cest/k/obrázkům") #načte soubobry z definované složky

connection.commit()

cursor = connection.cursor()
# cursor.execute(f"insert into imgTable (id, imgTitle, fileName1) values ({hash(*imgName*)}, {*imgName*}, {*fileName1*})")
cursor.execute(f"insert into imgTable (id, imgTitle, fileName1) values ({hash('Python')}, 'Python', '1.jpeg')")
cursor.execute(f"insert into imgTable (id, imgTitle, fileName1) values ({hash('Bottle')}, 'Bottle', '2.jpeg')")
cursor.execute(f"insert into imgTable (id, imgTitle, fileName1) values ({hash('Make IT Today')}, 'Make IT Today', '3.jpeg')")
connection.commit()

# cursor.execute("SELECT * FROM imageTable")

# for row in cursor:
#     print(row[0], " ", row[1], " ", row[2], " ", row[3])
# connection.close()

@app.get('/')
def home():
    return show_list()
    #return show_list() #použít tuto funkci, kde budete načítat svoje obrázky

# def show_list_test(filter=None):
#     #cursor.execute("SELECT * FROM imageTable")

#     imgs = [
#         {
#             'title': 'Python',
#             'url': '/img/1.jpeg'
#         },
#         {
#             'title': 'Bottle',
#             'url': '/img/2.jpeg'
#         },
#         {
#             'title': 'Make IT Today',
#             'url': '/img/3.jpeg'
#         }
#     ]
#     return template('list', {'imgs': imgs})


def show_list():
    #funkce pro získání obrázků a předání obrázků do šablony list
    imgs = load_pictures()
    print(imgs)
    for img in imgs:
        print(img['title'])
        print(img['url'])
    return template('list.tpl', {'imgs': imgs})



# ------------------------------- DONE -------------------------------


@app.get('/add')
def add_form():
    #funkce která vykresluje formulář pro přidání obrázku
    return template('addform')




# ------------------------------- DONE -------------------------------


@app.post('/add')
def add_form_post():
    #funkce pro zpracování nahraného obrázku  z formuláře

    title = request.forms.get('txtitle') #získání title z web formuláře, doplnte váš title, který je v html
    upload = request.files.get('upload') #získání vloženého souboru, doplnte váš upload file name, který je v html v formuláři

    upload.save(os.path.join('imgs', upload.filename)) #uloz soubor do slozky imgs
    add_picture_to_db(upload.filename, title) #funkce pro přidání obrázku do databáze

    redirect('/', 302) #přesměruju zpátky na hlavní stránku 



# ------------------------------- DONE -------------------------------

def add_picture_to_db(filename, title):
    #funkce na přidání obrázku do databáze, pokud používáte databázi

    cursor = connection.cursor()
    cursor.execute("insert into imgTable (id, imgTitle, fileName1) values (?, ?, ?)", (hash(filename), title, filename))
    connection.commit()





def load_pictures():
    #funkce pro načtení obrázků z databáze nebo ze složky a vrácení v poli

    connection.commit()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM imgTable")

    imgsList = []

    for row in cursor:
        imgsList.append({'id': row[0], 'title': row[1], 'url': row[2]})
    

    # print(id, title, filename)

    return imgsList





@app.get('/img/<file_name>')
def images(file_name):
    #funkce pro načtení souboru obrázku
    return static_file(file_name, 'imgs')





#spustim server na adrese localhost a portu 8080...url tedy bude http://localhost:8080
run(app, host='localhost', port=8080, debug=True)