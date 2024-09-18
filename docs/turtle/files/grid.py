"""draw axes and grid
"""
import turtle


def draw_grid(t, width, height, spacing, tcolor):
    t.color(tcolor, tcolor)
    xmax = width // 2
    ymax = height // 2
    for i in range(-xmax, xmax + 1, spacing):
        t.pu()
        t.goto(i, -ymax)
        t.pd()
        t.seth(90)
        t.fd(height)
    for i in range(-ymax, ymax + 1, spacing):
        t.pu()
        t.goto(-xmax, i)
        t.pd()
        t.seth(0)
        t.fd(width)


def draw_axes(t, width, height, pensize, tcolor):
    t.width(pensize)
    t.color(tcolor, tcolor)
    xmax = width // 2
    ymax = height // 2
    # x axis
    t.pu()
    t.goto(-xmax, 0)
    t.pd()
    t.seth(0)
    t.fd(width)
    # y axis
    t.pu()
    t.goto(0, -ymax)
    t.pd()
    t.seth(90)
    t.fd(height)


def label_axes(t, width, height, spacing, tcolor):
    t.color(tcolor, tcolor)
    xmax = width // 2
    ymax = height // 2
    # x axis
    for i in range(-xmax + spacing, xmax, spacing):
        if i == 0:
            continue
        t.pu()
        t.goto(i, -20)
        t.pd()
        t.write(i, align="center", font=("Arial", 12, "normal"))
    for i in range(-ymax + spacing, ymax, spacing):
        if i == 0:
            continue
        t.pu()
        t.goto(25, i - 10)
        t.write(i, align="center", font=("Arial", 12, "normal"))


s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)
s.tracer(10, 0)

grid_turtle = turtle.Turtle()
grid_turtle.speed(0)
draw_grid(grid_turtle, 800, 600, 50, "green")
draw_axes(grid_turtle, 800, 600, 4, "red")
label_axes(grid_turtle, 800, 600, 100, "red")
grid_turtle.ht()
"""drawing code below"""


    


"""drawing code above"""

s.update()
s.exitonclick()

