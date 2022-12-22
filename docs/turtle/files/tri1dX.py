"""draw triangle
"""
import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width = 800, height = 600, startx = 0, starty = 0)
t = turtle.Turtle()
t.speed(5)

def scalene(t, side_a, angle_C, side_b, heading, start_pos, 
                pencolor="blue", fillcolor =None, pensize=1): 
    t.seth(heading)
    t.pu()
    t.goto(start_pos)
    t.pd()
    t.pensize(pensize)
    t.pencolor(pencolor)

    if fillcolor is not None:
        t.fillcolor(fillcolor)
        t.begin_fill()

    t.fd(side_a)
    t.lt(180 - angle_C)
    t.fd(side_b)
    t.goto(start_pos)

    if fillcolor is not None:
        t.end_fill()

scalene(t, side_a=100, angle_C=60, side_b=150, heading=15, start_pos=(20, 30),
         pencolor="blue", fillcolor="light green", pensize=3)
       
s.exitonclick()
