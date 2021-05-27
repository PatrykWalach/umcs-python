# %%
import math
from vpython import *
import random


s1 = sphere(pos=vector(0, 0, 0), radius=0.8, color=color.yellow)
s2 = sphere(pos=vector(random.randint(-6, 6), random.randint(-6, 6), random.randint(-6, 6)), radius=0.5, color=color.red)

r = (s1.pos-s2.pos).mag
theta = math.atan(math.sqrt(s2.pos.x**2+s2.pos.y**2)/s2.pos.z)
omega = math.atan(s2.pos.y/s2.pos.x)

velocity = random.uniform(0.01,0.03)

while True:
    rate(100)
    x = r*math.cos(theta)*math.sin(omega)
    y = r*math.sin(theta)*math.sin(omega)
    z = r*math.cos(omega)
    s2.pos = vector(x, y, z)
    omega+=velocity


# %%
