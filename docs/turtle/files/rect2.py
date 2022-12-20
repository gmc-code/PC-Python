"""draw rectangle
"""
import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)

t.seth(0)
t.pu()
t.goto(20, 30)
t.pd()

for _ in range(2):
    t.fd(120)
    t.lt(90)
    t.fd(50)
    t.lt(90)

s.exitonclick()
