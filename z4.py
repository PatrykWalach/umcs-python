import tkinter as tk
import math


class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.t_step = 50
        self.s_step = 10
        self.master = master

        self.Cv = tk.Canvas(master, width=400, height=300)
        self.Cv.pack(side=tk.TOP)
        self.BStart = tk.Button(self, text='Start', command=self.run)
        self.BStart.pack(side=tk.LEFT)
        self.BQuit = tk.Button(self, text='Quit', command=master.quit)
        self.BQuit.pack(side=tk.LEFT)

        self.Cv.create_line(0, 250, 400, 250, width=3)
        self.start_par(10, 250, 45, 50)
        self.Cv.create_oval(self.x-3, self.y-3, self.x+3,
                            self.y+3, tag='bullet', fill='red')

    def start_par(self, x, y, angle, v):
        self.x = x
        self.y = y
        self.angle = angle
        self.vx = math.cos(math.radians(self.angle)) * v
        self.vy = math.sin(math.radians(self.angle)) * v

    def new_pos(self, t=0):
        self.x += self.vx*t/1000
        self.y -= self.vy*t/1000
        self.vy = self.vy-9.8*t/1000

# miejsce na kod:
    def run(self, t=1):
        
        V=9
        G = 2

        alpha = math.pi/4

        x = V*t*math.cos(alpha)
        y = -V*t*math.sin(alpha) + G*(t**2)/2

        print(x)
        print(y)

        self.Cv.move('bullet', x,y)

        x1, y1, x2, y2 = self.Cv.coords('bullet')
        
        if y1 + 3 < self.y:
            self.master.after(100, self.run, t+1)
            return

        self.Cv.coords('bullet', self.x-3, self.y-3, self.x+3,
                         self.y+3)
        self.master.after(100, self.run)
            

# koniec


root = tk.Tk()

MainFrame(root).pack()

root.mainloop()
