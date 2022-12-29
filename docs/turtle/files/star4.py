"""draw stars
"""
import turtle


def star(t, length=50, points=5, start_pos=(0, 0), start_h=0, penw=1, penc="black", fillc=None):
    ang = (360 * ((points-1)/2))/points
    t.pu()
    t.goto(start_pos)
    t.pd()
    t.seth(start_h)

    t.pensize(penw)
    t.pencolor(penc)

    if fillc is not None:
        t.fillcolor(fillc)
        t.begin_fill()

    for _ in range(points):
        t.fd(length)
        t.lt(ang)
        
    if fillc is not None:
        t.end_fill()


s = turtle.Screen()
s.bgcolor("white")
s.title("star")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(9)


star(t, length=300, points=7, start_pos=(-100, 0), start_h=0, penw=3, penc="grey90", fillc="yellow")

t.ht()
s.exitonclick()
