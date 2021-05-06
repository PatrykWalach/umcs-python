
from tkinter import Tk, Canvas, Label, Button, StringVar


licznik = 0
krok = 1


window = Tk()


def update_licznik_text():
    global licznik_text
    licznik_text.set(f"Licznik: {licznik}")


def increment():
    global licznik
    licznik += 1
    update_licznik_text()


def decrement():
    global licznik
    licznik -= 1
    update_licznik_text()


licznik_text = StringVar()
update_licznik_text()
Label(window, textvariable=licznik_text).pack()
Label(window, text=f"Krok: {krok}").pack()
Button(window, text="+", command=increment).pack()
Button(window, text="-", command=decrement).pack()


window.mainloop()
