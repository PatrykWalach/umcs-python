import tkinter as tk


window = tk.Tk()


radius = tk.IntVar(window, 12)

canvas = tk.Canvas(window)
canvas.pack()

def update_canvas(*args):
    canvas.delete("all")
    canvas.create_oval(1, 1, radius.get(), radius.get(),fill="green")

update_canvas()
tk.Scale(window, orient=tk.HORIZONTAL, variable=radius).pack()


radius.trace_add('write',update_canvas)

window.mainloop()
