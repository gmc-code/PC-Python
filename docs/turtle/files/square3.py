"""draw square
"""
import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("square")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)


def square(t, length=50, start_pos=(0, 0), start_h=0):
    t.pu()
    t.goto(start_pos)
    t.pd()
    t.seth(start_h)
    for _ in range(4):
        t.fd(length)
        t.lt(90)


square(t)
square(t, length=50, start_pos=(20, 30))
square(t, length=250, start_pos=(-300, -200), start_h=20)

s.exitonclick()
