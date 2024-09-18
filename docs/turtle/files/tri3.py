"""draw triangle
"""
import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("triangle")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)

# --begin triangle
side = 100
start_pos = (20, 30)
start_h = 10

t.pu()
t.goto(start_pos)
t.pd()
t.seth(start_h)

start_pos = t.pos()
for _ in range(3):
    t.fd(side)
    t.lt(120)
# --end triangle

s.exitonclick()
