"""draw_dot stacked hexagon
"""
import turtle


def draw_dot(t, centre=(0, 0), size=20, color="blue"):
    t.pu()
    t.goto(centre)
    t.pd()
    t.dot(size, color)


def draw_dot_stack(t, centre, angle, size, color):
    t.pu()
    t.goto(centre)
    t.seth(angle)
    t.fd(size)
    dot_centre = t.pos()
    draw_dot(t, centre=dot_centre, size=size, color=color)


s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=850, height=600, startx=0, starty=0)
s.tracer(0, 0)
s.colormode(255)

t = turtle.Turtle()
t.speed(0)
t.ht()

colors = ["light blue", "pink", "light green", "yellow", "MediumPurple1", "bisque"]

for i in range(200, 5, -50):
    draw_dot_stack(t, centre=(-200, -100), angle=90, size=i, color=colors[0])
for i in range(200, 5, -30):
    draw_dot_stack(t, centre=(0, -100), angle=90, size=i, color=colors[1])
for i in range(200, 5, -10):
    draw_dot_stack(t, centre=(200, -100), angle=90, size=i, color=colors[2])

s.update()
s.exitonclick()
