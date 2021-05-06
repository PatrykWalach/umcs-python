
from tkinter import Tk, Menu, filedialog, BOTH,  END, scrolledtext

window = Tk()


content = scrolledtext.ScrolledText(window)
content.pack(fill=BOTH)


def open_file():
    path = filedialog.askopenfilename()

    if path == '':
        return

    with open(path) as f:
        content.delete('1.0', END)
        content.insert(END, f.read())


def save_file():
    path = filedialog.asksaveasfilename()

    if path == '':
        return

    with open(path, 'w') as f:
        f.write(content.get("1.0", "end-1c"))


menubar = Menu(window)
window.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(
    label='Open',
    command=open_file,
)
file_menu.add_command(
    label='Save',
    command=save_file,
)

menubar.add_cascade(
    label="File",
    menu=file_menu,
)


window.mainloop()
