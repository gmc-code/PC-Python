import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)

# --begin triangle
side_a = 100
angle_C = 70
side_b = 100
heading = 15
start_pos = (20, 30)

t.seth(heading)
t.pu()
t.goto(start_pos)
t.pd()

t.fd(side_a)
t.lt(180 - angle_C)
t.fd(side_b)
t.goto(start_pos)
# --end triangle

s.exitonclick()
