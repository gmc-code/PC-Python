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
    ytranslate = -200
    xtranslate = -300

    t.width(pensize)
    t.color(tcolor, tcolor)
    xmax = width // 2
    ymax = height // 2
    # x axis
    t.pu()
    t.goto(-xmax, ytranslate)
    t.pd()
    t.seth(0)
    t.fd(width)
    # y axis
    t.pu()
    t.goto(xtranslate, -ymax)
    t.pd()
    t.seth(90)
    t.fd(height)


def label_axes(t, width, height, spacing, tcolor):
    ytranslate = +200
    xtranslate = +300
    
    t.color(tcolor, tcolor)
    xmax = width // 2
    ymax = height // 2
    # x axis
    for i in range(-xmax + spacing, xmax, spacing):
        if i == 0 - xtranslate:
            continue
        t.pu()
        t.goto(i, -20 - ytranslate)
        t.pd()
        t.write(i + xtranslate, align="center", font=("Arial", 12, "normal"))
     # y axis
    for i in range(-ymax + spacing, ymax, spacing):
        if i == 0 - ytranslate:
            continue
        t.pu()
        t.goto(-25 - xtranslate, i - 10)
        t.pd()
        t.write(i + ytranslate, align="center", font=("Arial", 12, "normal"))


def manual_labels(t, start_pos, tcolor):
    t.color(tcolor, tcolor)
    t.pensize(1)
    x0 = start_pos[0]
    y = start_pos[1]
    # x axis
    for i in range(1, 11):
        t.pu()
        t.goto(x0 + i * 50, y)
        t.seth(-90)
        t.pd()
        t.write(str(i) + "/10" , align="center", font=("Arial", 12, "normal"))
        t.pu()
        t.goto(x0 + i * 50, y)
        t.pd()
        t.fd(20)
        t.pu()


s = turtle.Screen()
s.bgcolor("white")
s.title("circle")
s.setup(width=800, height=600, startx=0, starty=0)
s.tracer(10, 0)

grid_turtle = turtle.Turtle()
grid_turtle.speed(0)
draw_grid(grid_turtle, 800, 600, 50, "green")
draw_axes(grid_turtle, 800, 600, 4, "red")
label_axes(grid_turtle, 800, 600, 100, "red")
grid_turtle.ht()


"""drawing code below"""
import houses as h

s.tracer(0, 0)
t = turtle.Turtle()
t.speed(0)
ytranslate = -200
xtranslate = -300
h.house(t, length=500, height=300, start_pos=(0 + xtranslate, 0 + ytranslate), w_sides="LR")
manual_labels(grid_turtle, (0 + xtranslate, 250 + ytranslate), "blue")
    
t.ht()

"""drawing code above"""

s.update()
s.exitonclick()

