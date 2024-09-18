"""draw_dot stacked hexagon
"""
import turtle
import random

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
    t.circle(radius)  
    if fillc is not None:
        t.end_fill()


def draw_circles_in_hexagon(t, centre, angle, size, colors):
    for i in range(6):
        t.pu()
        t.goto(centre)
        t.seth(angle + 60 * i)
        t.fd(2 * size)
        dot_centre = t.pos()
        draw_centered_circle(t, centre=dot_centre, radius=size, fillc=colors[i])


s = turtle.Screen()
s.bgcolor("white")
s.title("circle")
s.setup(width=1000, height=1000, startx=0, starty=0)
s.tracer(0, 0)
s.colormode(255)

t = turtle.Turtle()
t.speed(0)
t.ht()

const = 2.58  #2.589961639
size0 = 8
sizes = [int(size0 * (const **i)) for i in range(4) ]
colors = ["light blue", "pink", "light green", "yellow", "MediumPurple1", "bisque"]
angles = [0, 30, 0, 30, 0]
# sizes = [20, 50, 125, 315]
for i in range(4): 
    random.shuffle(colors)
    draw_circles_in_hexagon(t, centre=(0, 0), angle=angles[i], size=sizes[i], colors=colors)


s.update()
s.exitonclick()
