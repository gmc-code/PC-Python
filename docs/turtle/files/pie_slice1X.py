"""draw_centered_pie_slice
"""
import turtle


def draw_centered_pie_slice(t, centre=(0, 0), angle=0, radius=10, extent=330, penw=1, penc="black", fillc=None):
    t.pu()
    t.goto(centre)
    t.seth(angle)
    t.pensize(penw)
    t.pencolor(penc)
    t.pd()
    
    if fillc is not None:
        t.fillcolor(fillc)
        t.begin_fill()
    t.fd(radius)
    t.seth(angle + 90)   
    t.circle(radius, extent=extent)
    t.goto(centre)
    if fillc is not None:
        t.end_fill()
   


s = turtle.Screen()
s.bgcolor("white")
s.title("pie")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(0)
t.ht()

centres = [(-250, 0),(-80, 0),(90, 0),(260, 0)]
radii = [80, 80, 80, 80]
angles = [15, 45, 205, 200]
extents = [330, 270, 300, 330]
pensizes =  [1, 1, 1, 1]
pencolors = ["blue", "red", "green", "orange"]
fillcolors = ["light blue", "pink", "light green", "yellow"]

for i in range(len(radii)):
    draw_centered_pie_slice(t, centre=centres[i], angle=angles[i], radius=radii[i], extent=extents[i], penw=1, penc=pencolors[i], fillc=fillcolors[i])

s.exitonclick()
