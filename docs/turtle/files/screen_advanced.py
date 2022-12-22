import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)
s.tracer(0, 0)

t = turtle.Turtle()
t.pencolor("blue")
t.speed(0)


def square(t, side, x=0, y=0):
    for _ in range(4):
        t.fd(side)
        t.rt(90)


for i in range(60):
    square(t, side=200)
    t.rt(6)

s.update()
s.exitonclick()
