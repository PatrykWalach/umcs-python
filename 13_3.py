import math
from vpython import *


scene.camera.axis = vector(0, 0, -5)
scene.camera.pos = vector(0, 0, 20)

t = text(pos=vector(0, 0, 0), align='center', text='Python')


print(scene.camera.pos)
while True:
    # pass

    while scene.center.z > t.pos.z:
        rate(100)
        scene.camera.pos += vector(0, 0, -0.5)


# tu jest jakiś problem
    x = 0
    while x < 180:
        rate(100)
        scene.camera.rotate(angle=radians(
            1),  axis=vector(0, 1, 0), origin=t.pos)
        x += 1

    while scene.center.z < 20:
        rate(100)
        scene.camera.pos += vector(0, 0, 0.5)
