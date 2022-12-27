"""draw_dot_stack_cone
"""
import turtle


def draw_dot(t, centre=(0, 0), size=20, color="blue"):
    t.pu()
    t.goto(centre)
    t.pd()
    t.dot(size, color)


def draw_dot_stack_cone(t, centre, pos_step, angle, size, size_step, colors):
    # based on size and size_step
    # use  counter % len(colors)  to be able to loop though colors more than once.
    counter = 0
    for i in range(size, 0, -size_step):
        t.pu()
        t.goto(centre)
        t.seth(angle)
        t.fd(counter*pos_step)
        dot_centre = t.pos()
        draw_dot(t, centre=dot_centre, size=size - counter*size_step, color=colors[counter % len(colors)])
        counter += 1


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

draw_dot_stack_cone(t, centre=(-200, 100), pos_step=50, angle=270, size=200, size_step =50, colors=colors[0:2])
draw_dot_stack_cone(t, centre=(0, 100), pos_step=30, angle=270, size=200, size_step=30, colors=colors[2:5])
draw_dot_stack_cone(t, centre=(200, 100), pos_step=10,  angle=270, size=200, size_step=10, colors=colors)

s.update()
s.exitonclick()
