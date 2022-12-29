"""draw_dot stacked hexagon
"""
import turtle
import random

def draw_dot(t, centre=(0, 0), size=20, color="blue"):
    t.pu()
    t.goto(centre)
    t.pd()
    t.dot(size, color)


def draw_dot_hexagon(t, centre, angle, size, colors):
    for i in range(6):
        t.pu()
        t.goto(centre)
        t.seth(angle + 60 * i)
        t.fd(size)
        dot_centre = t.pos()
        draw_dot(t, centre=dot_centre, size=size, color=colors[i])


def rand_color():
    cmin = 40
    cmax = 240
    return (random.randrange(cmin, cmax), random.randrange(cmin, cmax), random.randrange(cmin, cmax))


def rand_colors_list(num):
    clrs = []
    for _ in range(num):
        clrs.append(rand_color())
    return clrs

def rand_colors_list_same(num):
    clrs = []
    newc = rand_color()
    for _ in range(num):
        clrs.append(newc)
    return clrs

s = turtle.Screen()
s.bgcolor("white")
s.title("dots")
s.setup(width=800, height=600, startx=0, starty=0)
s.tracer(0, 0)
s.colormode(255)

t = turtle.Turtle()
t.speed(0)
t.ht()

colors = ["light blue", "pink", "light green", "yellow", "MediumPurple1", "bisque"]

for i in range(200, 5, -10):
    colors = rand_colors_list_same(6)
    draw_dot_hexagon(t, centre=(0, 0), angle=0, size=i, colors=colors)


s.update()
s.exitonclick()
