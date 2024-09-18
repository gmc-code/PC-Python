"""draw_centered_circle
"""
import turtle


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


s = turtle.Screen()
s.bgcolor("white")
s.title("circle")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(0)
t.ht()

centres = [(0, 0),(0, 50),(0, 100),(0, 150)]
radii = [200, 150, 100, 50]
pensizes =  [16, 8, 4, 2]  # [1, 1, 1, 1]  #
pencolors = ["blue", "red", "green", "orange"]
fillcolors = ["light blue", "pink", "light green", "yellow"]

for i in range(len(radii)):
    draw_centered_circle(t, centre=centres[i], radius=radii[i], penw=pensizes[i], penc=pencolors[i], fillc=fillcolors[i])

s.exitonclick()
