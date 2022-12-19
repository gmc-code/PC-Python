"""draw square
"""
import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(0)

def square(t, l=50, x=0, y=0):
    t.seth(90)
    t.pu()
    t.goto(x, y)
    t.pd()
    for _ in range(4):
        t.fd(l)
        t.rt(90)

square(t)
square(t, l=100, x=200, y=0)
square(t, l=100, x=0, y=100)
s.exitonclick()
