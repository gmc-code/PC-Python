"""draw triangle
"""
import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)

# --begin triangle
side = 100
start_pos = (20, 30)
start_heading = 10

t.seth(start_heading)
t.pu()
t.goto(start_pos)
t.pd()

start_pos = t.pos()
for _ in range(3):
    t.fd(side)
    t.lt(120)
# --end triangle

s.exitonclick()
