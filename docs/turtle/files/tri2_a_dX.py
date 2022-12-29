import turtle
import math

s = turtle.Screen()
s.bgcolor("white")
s.title("triangle")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)

# --begin triangle
def isosceles(t, base, height, start_pos=(0, 0), start_h=0, penw=1, 
                penc="black", fillc=None):
    t.seth(start_h)
    t.pu()
    t.goto(start_pos)
    t.pd()
    t.pensize(penw)
    t.pencolor(penc)

    b = math.sqrt(height**2 + (base**2) / 4)
    angle_B = math.degrees(math.atan(2 * height / base))

    if fillc is not None:
        t.fillcolor(fillc)
        t.begin_fill()
     
    t.fd(base)
    t.lt(180 - angle_B)
    t.fd(b)
    t.goto(start_pos)

    if fillc is not None:
        t.end_fill()

isosceles(t, base=100, height=50, start_pos=(20, 30), start_h=15, penw=2, 
                penc="black", fillc="pink")
# --end triangle

s.exitonclick()
