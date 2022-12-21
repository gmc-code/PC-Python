import turtle
import math

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)

t.seth(30)
t.pu()
t.goto(-20, -100)
t.pd()

base = 200
height = 300
start_pos = t.pos()
b = math.sqrt(height**2 + (base**2) / 4)
angle_B = math.degrees(math.atan(2 * height / base))
t.fd(base)
t.lt(180 - angle_B)
t.fd(b)
t.goto(start_pos)

s.exitonclick()
