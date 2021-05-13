import tkinter as tk
import math
import time

window = tk.Tk()


canvas = tk.Canvas(window)
canvas.pack()


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def __sub__(self, v):
        return Vector(self.x - v.x, self.y - v.y)

    def __mul__(self, n):
        return Vector(self.x * n, self.y * n)

    def __truediv__(self, n):
        return Vector(self.x / n, self.y / n)

    def mag(self):
        return math.sqrt(self.x * self.x + self.y + self.y)

    def normalize(self):
        m = self.mag()
        if not m == 0:
            return self / m
        return self


class Tank:
    def __init__(self, pos: Vector, fill="green"):
        self.fill = fill

        self.pos = pos
        self.diagonal = Vector(40, 30)
        canvas.create_rectangle(pos.x+0, pos.y+0, pos.x +
                                self.diagonal.x, pos.y+self.diagonal.y, fill=fill)
        self.cannon_drawing = None
        self.cannon_length = 80
        self.cannon_angle = 0
        self.draw_cannon()

        self.shot_strength = 10

    def set_cannon_angle(self, angle):
        self.cannon_angle = angle
        self.draw_cannon()

    def increment_cannon_angle(self):
        self.set_cannon_angle(self.cannon_angle+0.1)

    def decrement_cannon_angle(self):
        self.set_cannon_angle(self.cannon_angle-0.1)

    def cannon_vector(self):
        x = self.cannon_length*math.cos(self.cannon_angle)
        y = self.cannon_length*math.sin(self.cannon_angle)
        return Vector(x, y)

    def cannon_start(self):
        return self.pos+self.diagonal/2

    def cannon_end(self):
        return self.cannon_start() + self.cannon_vector()

    def shoot(self, i=0, prev=None):
        if prev != None:
            canvas.delete(prev)

        if i > 100:
            return

        x = self.shot_strength*math.cos(self.cannon_angle)
        y = self.shot_strength*math.sin(self.cannon_angle)
        velocity = Vector(x, y)

        start = velocity*i+self.cannon_end()

        g = 2
        start.y += g*(i**2)/2
        end = start + Vector(10, 10)

        missile = canvas.create_oval(
            start.x, start.y, end.x, end.y, fill=self.fill)

        window.after(100, self.shoot, i+1,missile)

    def increment_shot_strength(self):
        self.shot_strength += 1

    def decrement_shot_strength(self):
        self.shot_strength = max([0, self.shot_strength-1])

    def draw_cannon(self):
        if self.cannon_drawing != None:
            canvas.delete(self.cannon_drawing)

        start = self.cannon_start()
        end = self.cannon_end()

        self.cannon_drawing = canvas.create_line(
            start.x, start.y, end.x, end.y, fill=self.fill)


green = Tank(Vector(20, 80), 'green')


tk.Button(window, text="Lower cannon",
          command=green.increment_cannon_angle).pack()
tk.Button(window, text="Raise cannon",
          command=green.decrement_cannon_angle).pack()

tk.Button(window, text="Increment shot strength",
          command=green.increment_shot_strength).pack()
tk.Button(window, text="Decrement shot strength",
          command=green.decrement_shot_strength).pack()

tk.Button(window, text="strzał", command=green.shoot).pack()


window.mainloop()
