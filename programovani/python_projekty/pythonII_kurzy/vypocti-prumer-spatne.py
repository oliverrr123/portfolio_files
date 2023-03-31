from tkinter import Tk, Label, Button, mainloop, X, Frame, END, Entry


# funkce pro pridavani predmetu
def count_average():
    subject = get_subject.get()
    marks_str = get_marks.get()
    marks = marks_str.split(',')
    get_subject.delete(0, END)
    get_marks.delete(0, END)

    marks_sum = 0
    for mark in marks:
        marks_sum += mark

        average = round(marks_sum / len(marks), 2)

    # zobrazeni
    lbl = Label(text = subject + ': ' + str(average), master=frame, bg='#F0FFF0)
    lbl.pack(fill=X)


# funkce po stisku klavesy enter - rozsirujici
def on_enter(evt = None):
    count_average()


# vytvoreni uzivatelskeho rozhrani
window = Tk()
window.bind('<Return>', on_enter)

Label(text = 'Předmět:').pack()
get_subject = Entry
get_subject,pack(fill=X)

Label(text = 'Známky:').pack()
get_marks = Entry()
get_marks.pack(fill=X

# tlacitko Vypočti průměr vola funkci count_average, ma modre pozadi a bily text
button = Button(text='Vypočti průměr', command=count_averag, bg='#000080', fg='white')
button.pack(fill=X)

frame = Frame()
frame.pack(fill=X)

mainloop()

