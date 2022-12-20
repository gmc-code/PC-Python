"""draw rectangle
"""
import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)


def rectangle(t, length=40, width=30, x=0, y=0):
    t.pu()
    t.goto(x, y)
    t.pd()
    for _ in range(2):
        t.fd(length)
        t.lt(90)
        t.fd(width)
        t.lt(90)


t.seth(0)
rectangle(t)
rectangle(t, length=120, width=50, x=50, y=30)
rectangle(t, length=400, width=300, x=-300, y=-200)

s.exitonclick()
