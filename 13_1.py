# %%
from vpython import *
import random


t = box(size=vector(16, 8, 1), pos=vector(0, 0, -0.5), texture=textures.wood)

ball = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.yellow)

velocity = vector(random.uniform(0.1, 0.5), random.uniform(0.1, 0.5), 0)

while True:
    rate(100)
    ball.pos = ball.pos+velocity
    if ball.pos.x+ball.radius > t.pos.x+t.size.x/2:
        velocity.x *= -1

    if ball.pos.x-ball.radius < t.pos.x-t.size.x/2:
        velocity.x *= -1

    if ball.pos.y+ball.radius > t.pos.y+t.size.y/2:
        velocity.y *= -1

    if ball.pos.y-ball.radius < t.pos.y-t.size.y/2:
        velocity.y *= -1

# %%
