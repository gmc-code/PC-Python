"""draw triangle
"""
import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("triangle")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)


def scalene(t, side_a, angle_C, side_b, start_pos=(0, 0), start_h=0):
    t.pu()
    t.goto(start_pos)
    t.pd()
    t.seth(start_h)

    t.fd(side_a)
    t.lt(180 - angle_C)
    t.fd(side_b)
    t.goto(start_pos)


scalene(t, side_a=100, angle_C=60, side_b=150, start_pos=(20, 30), start_h=15)

s.exitonclick()
