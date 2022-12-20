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

a = 100
C = 60
b = 100

start_pos = t.pos()
t.fd(a)
t.lt(180 - C)
t.fd(b)
t.goto(start_pos)

s.exitonclick()
