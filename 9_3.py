
from tkinter import Tk, Canvas, Label, Button, StringVar, Entry, Radiobutton, IntVar


licznik = 0
krok = 1


window = Tk()


def update_licznik_text():
    global licznik_text
    licznik_text.set(f"Licznik: {licznik}")


def set_licznik(next_licznik):
    global licznik
    licznik = next_licznik
    update_licznik_text()


def increment():
    global licznik
    set_licznik(licznik + 1)


def decrement():
    global licznik
    set_licznik(licznik - 1)


licznik_text = StringVar()
update_licznik_text()

e = Entry(window)
e.pack()

Button(window, text="set", command=lambda: set_licznik(int(e.get()))).pack()


Label(window, textvariable=licznik_text).pack()
Label(window, text=f"Krok: {krok}").pack()
Button(window, text="+", command=increment).pack()
Button(window, text="-", command=decrement).pack()


v = IntVar()

Radiobutton(window, text="set licznik to 1", variable=v,
            command=lambda: set_licznik(1), value=1).pack()
Radiobutton(window, text="set licznik to 3", variable=v,
            command=lambda: set_licznik(3), value=3).pack()
Radiobutton(window, text="set licznik to 10", variable=v,
            command=lambda: set_licznik(10), value=10).pack()

window.mainloop()
