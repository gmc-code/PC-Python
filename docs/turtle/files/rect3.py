"""draw square
"""
import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)


def square(t, l=50, x=0, y=0):
    t.pu()
    t.goto(x, y)
    t.pd()
    for _ in range(4):
        t.fd(l)
        t.lt(90)


t.seth(0)
square(t)
square(t, l=50, x=20, y=30)
square(t, l=250, x=-300, y=-200)
s.exitonclick()
