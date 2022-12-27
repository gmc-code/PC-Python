"""draw_dot stacked hexagon
"""
import turtle


def draw_dot(t, centre=(0, 0), size=20, color="blue"):
    t.pu()
    t.goto(centre)
    t.pd()
    t.dot(size, color)


def draw_dot_stack(t, centre, angle, size, step, colors):
    col_i = 0
    for i in range(size, 0, -step):
        t.pu()
        t.goto(centre)
        t.seth(angle)
        t.fd(i)
        dot_centre = t.pos()
        draw_dot(t, centre=dot_centre, size=i, color=colors[col_i])
        col_i = (col_i + 1) % len(colors)
        print(col_i, end=" ")

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

draw_dot_stack(t, centre=(-200, -100), angle=90, size=200, step = 50, colors=colors[0:2])
draw_dot_stack(t, centre=(0, -100), angle=90, size=200, step = 30, colors=colors[2:5])
draw_dot_stack(t, centre=(200, -100), angle=90, size=200, step = 10, colors=colors)

s.update()
s.exitonclick()
