
from tkinter import Tk, Canvas, Label, Button, StringVar, Entry, Radiobutton


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


licznik_text = StringVar(window)
update_licznik_text()

e = Entry(window)
e.pack()

Button(window, text="set", command=lambda: set_licznik(int(e.get()))).pack()


color = StringVar(window, "red")

Label(window, textvariable=licznik_text).pack()
Label(window, text=f"Krok: {krok}").pack()
increment_button = Button(window, text="+", command=increment, bg=color.get())
increment_button.pack()
decrement_button = Button(window, text="-", command=decrement, bg=color.get())
decrement_button.pack()

def update_buttons_colors(var, indx, mode):
    global color
    increment_button.configure(bg=color.get())
    decrement_button.configure(bg=color.get())

color.trace_add("write", update_buttons_colors)




Radiobutton(window, text="set licznik to 1", variable=color,
            command=lambda: set_licznik(1), bg="red", value="red").pack()
Radiobutton(window, text="set licznik to 3", variable=color,
            command=lambda: set_licznik(3), bg="green", value="green").pack()
Radiobutton(window, text="set licznik to 10", variable=color,
            command=lambda: set_licznik(10), bg="blue", value="blue").pack()

window.mainloop()
