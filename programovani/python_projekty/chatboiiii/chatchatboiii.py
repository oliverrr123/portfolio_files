import tkinter as tk
import requests

server_url = "http://localhost:8080/"
last_index = 0

def display_message(author, date, text):
    message_listbox.insert(tk.END, '[' + date + '] ' + author + ': ' + text)
    message_listbox.yview_moveto(1)

def load_messages():
    global last_index
    response = requests.get(server_url + "get/" + str(last_index))
    print(response)
    data = response.json()
    print(data)

    for message in data["messages"]:
      display_message(message[0], message[1], message[2])

    last_index = int(data["len"])

def button_pressed():
    message = {
      "author": name.get(),
      "message": input.get("1.0", tk.END)
    }
    response = requests.post(server_url + "messages/add", data=message)  
    print(response)
    input.delete("1.0", tk.END)
    load_messages()

def refresh():
    load_messages()
    message_frame.after(2000, refresh)  

def on_enter(evt = None):
    button_pressed()

def new_line(evt = None):
  input.insert(tk.INSERT, '')

window = tk.Tk()
window.bind('<Return>', on_enter)
window.bind('<Shift-Return>', new_line)

title = tk.Label()
title.pack()

message_frame = tk.Frame()
message_frame.pack(fill=tk.BOTH, expand=True)
scroll_bar = tk.Scrollbar(message_frame)
scroll_bar.pack(side = tk.RIGHT, fill=tk.Y)

message_listbox = tk.Listbox(message_frame, yscrollcommand = scroll_bar.set)
message_listbox.pack(side = tk.LEFT, fill=tk.BOTH, expand=True)
scroll_bar.config(command = message_listbox.yview)

name_frame = tk.Frame()
name_frame.pack(fill=tk.X, expand=True)
name_label = tk.Label(name_frame, text="Jméno: ")
name_label.pack(side=tk.LEFT, expand=False)

name = tk.Entry(name_frame)
name.pack(side=tk.LEFT, fill=tk.X, expand=True)

input = tk.Text()
input.configure(height=3)
input.pack(fill=tk.X, expand = False)

button_add = tk.Button(text="Poslat", command=button_pressed)
button_add.pack()

refresh()

tk.mainloop()


#a
#aa
#aaa
#aaaa
#aaaaa
#aaaaaa
#aaaaaaa
#aaaaaaaa
#aaaaaaaaa
#aaaaaaaaaa
#aaaaaaaaaaa
#aaaaaaaaaaaa
#aaaaaaaaaaaaa
#aaaaaaaaaaaaaa
#aaaaaaaaaaaaaaa
#aaaaaaaaaaaaaaaa
#aaaaaaaaaaaaaaaaa
#aaaaaaaaaaaaaaaaaa
#aaaaaaaaaaaaaaaaaaa
#aaaaaaaaaaaaaaaaaaaa
#aaaaaaaaaaaaaaaaaaaaa
#aaaaaaaaaaaaaaaaaaaaaa
#aaaaaaaaaaaaaaaaaaaaaaa
#aaaaaaaaaaaaaaaaaaaaaaaa


#http://vtuma.pythonanywhere.com/get/0