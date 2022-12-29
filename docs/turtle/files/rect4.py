"""
draw rectangle 
"""
import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("Rectangle")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(0)


def rectangle(t, length=40, width=30, start_pos=(0, 0), start_h=0, penw=1, penc="black", fillc=None):
    t.pu()
    t.goto(start_pos)
    t.pd()
    t.seth(start_h)
    
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


rectangle(t, length=400, width=300, start_pos=(-100, -150), start_h=10, penw=5, penc="black", fillc="light green")

s.exitonclick()
