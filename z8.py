from vpython import *
import math

ball1=sphere(pos=vector(0,0,0), radius=1) 
ball2=sphere(pos=vector(8,0,0), radius=1) 

# miejsce na kod:
while True:
    rate(100)
    ball1.rotate(angle=math.pi/90,axis=vec(0,1,1) ,origin=ball2.pos)

# koniec      