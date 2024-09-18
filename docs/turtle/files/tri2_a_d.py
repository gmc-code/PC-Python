import turtle
import math

s = turtle.Screen()
s.bgcolor("white")
s.title("triangle")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)

# --begin triangle
def isosceles(t, base, height, start_pos=(0, 0), start_h=0):
    t.pu()
    t.goto(start_pos)
    t.pd()
    t.seth(start_h)

    b = math.sqrt(height**2 + (base**2) / 4)
    angle_B = math.degrees(math.atan(2 * height / base))

    t.fd(base)
    t.lt(180 - angle_B)
    t.fd(b)
    t.goto(start_pos)


isosceles(t, base=100, height=50, start_pos=(20, 30), start_h=15)
# --end triangle

s.exitonclick()
