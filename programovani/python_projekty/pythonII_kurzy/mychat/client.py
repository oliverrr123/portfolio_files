from tkinter import Tk, Label, Button, mainloop, Entry, X, Text, Frame, END, W, LEFT, BOTTOM
import requests

message_index = 0

server_url = "http://localhost:8080"

def send_message():
    messageData = {
        "author": author.get(),
        "message": message.get("1.0",END),
    }
    message.delete("1.0",END)
    #odeslani na serevr
    response = requests.post(server_url + "/messages/add", data=messageData)
    assert response.status_code == 200
    #aby se mi moje zprava zobrazila, nactu zpravy ze serveru
    load_messages()

def show_message(date, author, text):
    Label(text = text, master=frame, anchor=W, justify=LEFT).pack(fill=X, side=BOTTOM)
    Label(text = date + " " + author, master=frame, bg="#00FF00").pack(side=BOTTOM)

def load_messages():
    global message_index
    response = requests.get(server_url + "/get/" + str(message_index)) #http://localhost:8080/get/10
    #zkontroluju zda server vrátil správný kód (když server vrátí správné data, pak status_code je 200)
    assert response.status_code == 200

    response_data = response.json() #vrátí pole ["len": 1, "messages": [["Jakub", "21.1.", "Ahoj světě!"]]]

    #response_data["messages"]
    #response_data["len"]
    #
    #pole = [1,2,3,4]
    #for promenna in pole:
    #   print(promenna)
    #

    for message in response_data["messages"]:
        #message ["Jakub", "21.1.", "Ahoj světě!"]
        show_message(message[1], message[0], message[2])

    message_index = int(response_data["len"])
    #message_index = message_index + len(response_data["messages"])

def refresh():
    load_messages()
    frame.after(2000, refresh)

window = Tk()
window.geometry("400x500")

Label(text = "Prezdivka:").pack()
author = Entry()
author.pack(fill=X)

Label(text = "Nová zpráva:").pack()
message = Text(height=2)
message.pack(fill=X)

sendButton = Button(text="Odeslat", bg="white", fg="black", command=send_message)
sendButton.pack(fill=X)

frame = Frame()
frame.pack(fill=X)

refresh()

mainloop()