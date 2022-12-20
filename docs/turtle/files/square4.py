"""
draw squares 
"""
import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(0)


def square(t, l=50, x=0, y=0, penc="blue", fillc="white", penw=1):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.pensize(penw)
    t.pencolor(penc)
    if fillc is not None:
        t.fillcolor(fillc)
        t.begin_fill()
    for _ in range(4):
        t.fd(l)
        t.lt(90)
    if fillc is not None:
        t.end_fill()

def window(t, l=10, x=20, y=40, penc="black", fillc="snow", penw=2):
    for _ in range(4):
        square(t, l, x, y, penc, fillc, penw)
        t.lt(90 )

def house(t, l, x, y, penc="black", fillc="snow", penw=2):  
    square(t, l, x, y, penc, fillc, penw)
    window(t, l/10, x+l/5, y+l/2.5, penc, fillc, penw)


t.seth(0)

square(t, l=200, x=-100, y=-100, penc="blue", fillc="snow", penw=2)

# window(t, l=10, x=20, y=40, penc="blue", fillc="white", penw=2)
# house(t, l=100, x=0, y=0, penc="blue", fillc="PowderBlue", penw=1)
# house(t, l=70, x=-200, y=0, penc="blue", fillc="PowderBlue", penw=1)
# house(t, l=40, x=-300, y=0, penc="blue", fillc="PowderBlue", penw=1)
# house(t, l=20, x=-400, y=0, penc="blue", fillc="PowderBlue", penw=1)

s.exitonclick()
