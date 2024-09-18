import turtle


def draw_dot(t, centre=(0, 0), size=20, color="blue"):
    t.pu()
    t.goto(centre)
    t.pd()
    t.dot(size, color)


def draw_dot_centre_hexagon(t, centre, angle, size, centre_color, colors):
    draw_dot(t, centre=centre, size=size, color=centre_color)
    for i in range(6):
        t.pu()
        t.goto(centre)
        t.seth(angle + 60 * i)
        t.fd(size)
        dot_centre = t.pos()
        draw_dot(t, centre=dot_centre, size=size, color=colors[i])


s = turtle.Screen()
s.bgcolor("white")
s.title("dots")
s.setup(width=800, height=600, startx=0, starty=0)
s.tracer(0, 0)
s.colormode(255)

t = turtle.Turtle()
t.speed(0)
t.ht()

colors = ["light blue", "pink", "light green", "orange", "MediumPurple1", "yellow"]
draw_dot_centre_hexagon(t, centre=(0, 0), angle=0, size=80, centre_color="ivory3", colors=colors)

s.update()
s.exitonclick()
