import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)


def square(t, length=50, start_pos=(0, 0), start_h=0, penw=1, penc="black", fillc=None):
    t.pu()
    t.goto(start_pos)
    t.pd()
    t.seth(start_h)

    t.pensize(penw)
    t.pencolor(penc)

    if fillc is not None:
        t.fillcolor(fillc)
        t.begin_fill()

    for _ in range(4):
        t.fd(length)
        t.lt(90)

    if fillc is not None:
        t.end_fill()


square(t, length=250, start_pos=(-100, -150), start_h=0, penw=2, penc="black", fillc="green")

s.exitonclick()