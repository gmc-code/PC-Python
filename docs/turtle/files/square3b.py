"""
draw squares 
"""
import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)
s.tracer(0, 0)

t = turtle.Turtle()
t.speed(0)


def square(t, l=50, x=0, y=0):
    for _ in range(4):
        t.fd(l)
        t.lt(90)


for i in range(16):
    square(t, l=100)
    t.lt(6)

turtle.update()
s.exitonclick()
