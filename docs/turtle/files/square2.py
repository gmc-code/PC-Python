"""draw square
"""
import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(2)

t.seth(90)
t.pu()
t.goto(50, 50)
t.pd()

for _ in range(4):
    t.fd(50)
    t.rt(90)

s.exitonclick()
