"""draw dots
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
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(0)

centres = [(150, -148), (150, 14), (150, 136), (150, 227)]
radii = [92, 69, 52, 39]
# pensizes = [30, 30, 30, 30]
pensizes = [80, 80, 80, 80]
pencolors = ["blue", "red", "green", "orange"]
fillcolors = ["light blue", "pink", "light green", "yellow"]

for i in range(len(radii)):
    draw_centered_circle(t, centre=centres[i], radius=radii[i], penw=pensizes[i], penc=pencolors[i], fillc=fillcolors[i])


centres = [(-150, -112), (-150, 80), (-150, 176), (-150, 224)]
radii = [128, 64, 32, 16]
pensizes = [1, 1, 1, 1]
pencolors = ["blue", "red", "green", "orange"]
fillcolors = ["light blue", "pink", "light green", "yellow"]

for i in range(len(radii)):
    draw_centered_circle(t, centre=centres[i], radius=radii[i], penw=pensizes[i], penc=pencolors[i], fillc=fillcolors[i])



s.exitonclick()
