"""draw square
"""
import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("square")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)

t.pu()
t.goto(20, 30)
t.pd()
t.seth(0)

for _ in range(4):
    t.fd(50)
    t.lt(90)

s.exitonclick()
