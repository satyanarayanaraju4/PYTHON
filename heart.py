import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2*k) - 2*math.cos(3*k) - math.cos(4*k)

bgcolor("black")
color("red")
speed(0)
tracer(0)  


penup()
for i in range(6000):
    x = hearta(i) * 20
    y = heartb(i) * 20
    goto(x, y)
    pendown()

update()  


penup()
goto(0, -20)  
color("white")
write("CHINTA.KIRANMAI", align="center", font=("Arial", 28, "bold"))

hideturtle()
done()