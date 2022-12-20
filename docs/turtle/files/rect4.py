"""
draw rectangle 
"""
import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(0)


def rectangle(t, length=40, width=30, x=0, y=0, penc="blue", fillc="white", penw=1):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.pensize(penw)
    t.pencolor(penc)
    if fillc is not None:
        t.fillcolor(fillc)
        t.begin_fill()
    for _ in range(2):
        t.fd(length)
        t.lt(90)
        t.fd(width)
        t.lt(90)
    if fillc is not None:
        t.end_fill()


t.seth(0)

rectangle(t, length=400, width=300, x=-100, y=-150, penc="blue", fillc="green", penw=5)

s.exitonclick()
