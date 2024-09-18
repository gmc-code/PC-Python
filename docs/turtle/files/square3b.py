"""
draw squares 
"""
import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("square")
s.setup(width=800, height=600, startx=0, starty=0)
s.tracer(0, 0)

t = turtle.Turtle()
t.speed(0)


def square(t, length=50, start_pos=(0, 0), start_h=0):
    t.pu()
    t.goto(start_pos)
    t.pd()
    t.seth(start_h)
    for _ in range(4):
        t.fd(length)
        t.lt(90)


for i in range(16):
    square(t, length=100, start_h=i * 6)
    t.lt(6)

s.update()
s.exitonclick()
