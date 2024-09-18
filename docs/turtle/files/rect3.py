"""draw rectangle
"""
import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("Rectangle")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)


def rectangle(t, length=40, width=30, start_pos=(0, 0), start_h=0):
    t.pu()
    t.goto(start_pos)
    t.pd()
    t.seth(start_h)
    
    for _ in range(2):
        t.fd(length)
        t.lt(90)
        t.fd(width)
        t.lt(90)


rectangle(t)
rectangle(t, length=120, width=50, start_pos=(20, 30))
rectangle(t, length=400, width=300, start_pos=(-300, -100), start_h=10)


s.exitonclick()
