import tkinter as tk
from random import randrange

root = tk.Tk()

iv=tk.IntVar(0)
iv.set(0)
sv=tk.StringVar()
sv.set('parzysta')

# miejsce na kod:
def generate():
    global iv, sv
    r= randrange(0,1000)
    iv.set(r)
    sv.set('nieparzysta' if r%2 else 'parzysta')

tk.Button(root,text="Generate number",command=lambda: generate()).pack()
tk.Label(root, textvariable=iv ).pack()
tk.Label(root, textvariable=sv ).pack()

# koniec  

root.mainloop()    
