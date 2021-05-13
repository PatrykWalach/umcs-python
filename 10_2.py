import tkinter as tk
import random

window = tk.Tk()


canvas = tk.Canvas(window)
canvas.pack()

oval = None

colors = ["red", "orange", "yellow", "green", "blue", "violet"]


def draw_circle_start(event):
    global oval
    fill = random.choice(colors)
    oval = {
        'start': event,
        'fill': fill,
        'obj': canvas.create_oval(event.x, event.y, event.x, event.y, fill=fill)
    }


def draw_circle(event):
    global oval
    if oval != None:
        canvas.delete(oval['obj'])
        oval['obj'] = canvas.create_oval(
            oval['start'].x, oval['start'].y, event.x, event.y, fill=oval['fill'])


def draw_circle_end(event):
    global oval
    oval = None


def clear_canvas(*args):
    canvas.delete("all")


canvas.bind('<Button>', draw_circle_start)
canvas.bind('<Motion>', draw_circle)
canvas.bind('<ButtonRelease>', draw_circle_end)

window.bind('<Delete>', clear_canvas)
window.mainloop()
