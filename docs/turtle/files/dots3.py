"""draw_dot
"""
import turtle


def draw_dot(t, centre=(0, 0), size=20, color="blue"):
    t.pu()
    t.goto(centre)
    t.pd()
    t.dot(size, color)


def draw_dot_stack(t, centre, pos_step, angle, size, size_step, colors):
    # based on number of colours
    for i in range(len(colors)):
        t.pu()
        t.goto(centre)
        t.seth(angle)
        t.fd(i*pos_step)
        dot_centre = t.pos()
        draw_dot(t, centre=dot_centre, size=size - i*size_step, color=colors[i])


s = turtle.Screen()
s.bgcolor("white")
s.title("dots")
s.setup(width=850, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(0)
t.ht()

colors = ["light blue", "pink", "light green", "yellow"]

draw_dot_stack(t, centre=(-300, -80), pos_step=10, angle=45, size=200, size_step=50, colors=colors)
draw_dot_stack(t, centre=(-100, -80), pos_step=25, angle=60, size=200, size_step=40, colors=colors)
draw_dot_stack(t, centre=(100, -80), pos_step=40, angle=75, size=200, size_step=30, colors=colors)
draw_dot_stack(t, centre=(300, -80), pos_step=55, angle=90, size=200, size_step=20, colors=colors)

s.exitonclick()
