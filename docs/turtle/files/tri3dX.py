"""draw triangle
"""
import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)


# --begin triangle
def equilateral(t, side, start_pos, start_heading, 
                    pencolor="blue", fillcolor=None, pensize=1):
    t.seth(start_heading)
    t.pu()
    t.goto(start_pos)
    t.pd()
    t.pensize(pensize)
    t.pencolor(pencolor)

    if fillcolor is not None:
        t.fillcolor(fillcolor)
        t.begin_fill()
  
    start_pos = t.pos()
    for _ in range(3):
        t.fd(side)
        t.lt(120)

    if fillcolor is not None:
        t.end_fill()


equilateral(t, side=100, start_pos=(20, 30), start_heading=10, 
                pencolor="purple", fillcolor="light green", pensize=2)
# --end triangle

s.exitonclick()
