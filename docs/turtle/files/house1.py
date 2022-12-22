import turtle
import math
import houses as h

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(0)

def simple_house(t, base=60, height=30, start_pos=(-105, 50), start_h=0, penw=1, penc="black", fillc=None):
    h.square(t, length=50, start_pos=(-100, 0), start_h=0, penw=1, penc="black", fillc="snow")
    h.rectangle(t, length=10, width=30, start_pos=(-80, 0), start_h=0, penw=1, penc="black", fillc="green")
    h.isosceles(t, base=60, height=30, start_pos=(-105, 50), start_h=0, penw=1, penc="black", fillc="brown")

simple_house(t, base=60, height=30, start_pos=(-105, 50), start_h=0, penw=1, penc="black", fillc=None)

s.exitonclick()
