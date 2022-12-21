import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)

base = 100
height = 50
start_pos = (20, 30)

t.seth(0)
t.pu()
t.goto(start_pos)
t.pd()

start_x = t.xcor()
start_y = t.ycor()
t.fd(base)
t.goto(start_x + base/2, start_y + height)
t.goto(start_x, start_y)

s.exitonclick()