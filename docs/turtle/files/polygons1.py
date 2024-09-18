"""draw_centered_circle
"""
import turtle


def draw_centered_regular_polygon(t, centre=(0, 0), radius=10, sides=4, penw=1, penc="black", fillc=None):
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
    t.circle(radius, steps=sides)  
    if fillc is not None:
        t.end_fill()


s = turtle.Screen()
s.bgcolor("white")
s.title("polygon")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(0)
t.ht()

centres = [(-250, 0),(-80, 0),(80, 0),(250, 0)]
radii = [80, 80, 80, 80]
polysides = [8, 6, 5, 4]
pensizes =  [1, 1, 1, 1]
pencolors = ["blue", "red", "green", "orange"]
fillcolors = ["light blue", "pink", "light green", "yellow"]

for i in range(len(radii)):
    draw_centered_regular_polygon(t, centre=centres[i], radius=radii[i], sides=polysides[i], penw=pensizes[i], penc=pencolors[i], fillc=fillcolors[i])

s.exitonclick()
