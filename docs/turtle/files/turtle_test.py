"""draw_circle_of_circles
"""
import turtle
from math import sin, radians


def draw_centered_circle(t, centre=(0, 0), radius=10, penw=1, penc="black", fillc=None):
    t.pu()
    t.goto(centre)
    t.seth(0)
    t.fd(radius)
    t.seth(90)
    t.pensize(penw)
    t.pencolor(penc)
    t.pd()
    if fillc is not None:
        t.fillcolor(fillc)
        t.begin_fill()   
    t.circle(radius, steps=4)  
    if fillc is not None:
        t.end_fill()


def draw_circle_of_circles(t, centre, angle, size, sides, colors=None):
    circum_r = (sin(radians(180/sides)) / (1 - sin(radians(180/sides)))) * size
    for i in range(sides):
        t.pu()
        t.goto(centre)
        t.seth(angle + i*360//sides)
        t.fd(size + circum_r)
        dot_centre = t.pos()
        if colors is None:  
            draw_centered_circle(t, centre=dot_centre, radius=circum_r, penw=1, penc="blue", fillc=None)
        else:  
            dot_color = colors[i]
            draw_centered_circle(t, centre=dot_centre, radius=circum_r, penw=1, penc="blue", fillc=dot_color)


s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=1000, height=1000, startx=0, starty=0)
s.tracer(0, 0)
s.colormode(255)

t = turtle.Turtle()
t.speed(0)
t.ht()


colorlist=["light blue", "pink", "light green", "yellow", "MediumPurple1", "bisque"]*4
draw_circle_of_circles(t, centre=(0, 0), angle=0, size=20, sides=4, colors=colorlist)
draw_circle_of_circles(t, centre=(0, 0), angle=45, size=100, sides=8, colors=colorlist)

s.update()
s.exitonclick()
