"""draw triangle
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

start_pos = t.pos()
for _ in range(3):
    t.fd(100)
    t.lt(120)

s.exitonclick()
