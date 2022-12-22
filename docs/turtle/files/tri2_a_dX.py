import turtle
import math

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)

# --begin triangle
def isosceles(t, base, height, start_pos, start_h, 
                penc="blue", fillc=None, penw=1):
    t.seth(start_h)
    t.pu()
    t.goto(start_pos)
    t.pd()
    t.pensize(pensize)
    t.pencolor(pencolor)

    b = math.sqrt(height**2 + (base**2) / 4)
    angle_B = math.degrees(math.atan(2 * height / base))

    if fillcolor is not None:
        t.fillcolor(fillcolor)
        t.begin_fill()
     
    t.fd(base)
    t.lt(180 - angle_B)
    t.fd(b)
    t.goto(start_pos)

    if fillcolor is not None:
        t.end_fill()

isosceles(t, base=100, height=50, start_pos=(20, 30), start_h=15, 
                penc="blue", fillc="pink", penw=2)
# --end triangle

s.exitonclick()
