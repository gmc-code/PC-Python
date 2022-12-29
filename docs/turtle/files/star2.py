"""draw restarctangle
"""
import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("star")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(9)


t.pu()
t.goto(20, 30)
t.pd()
t.seth(0)

for _ in range(5):
    t.fd(120)
    t.lt(144)

s.exitonclick()
