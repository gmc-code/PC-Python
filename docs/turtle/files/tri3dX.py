"""draw triangle
"""
import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("triangle")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)


# --begin triangle
def equilateral(t, side, start_pos=(0, 0), start_h=0, penw=1, penc="black", fillc=None):
    t.pu()
    t.goto(start_pos)
    t.pd()
    t.seth(start_h)
    
    t.pensize(penw)
    t.pencolor(penc)

    if fillc is not None:
        t.fillcolor(fillc)
        t.begin_fill()
  
    start_pos = t.pos()
    for _ in range(3):
        t.fd(side)
        t.lt(120)

    if fillc is not None:
        t.end_fill()


equilateral(t, side=100, start_pos=(20, 30), start_h=10, penw=2, penc="purple", fillc="light green")
# --end triangle

s.exitonclick()
