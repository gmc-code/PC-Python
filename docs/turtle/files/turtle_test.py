import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)
s.tracer(1)
s.delay(1000)

t = turtle.Turtle()
t.speed(0)


def square(t, l=50, x=0, y=0):
    for _ in range(4):
        t.fd(l)
        t.rt(90)


for i in range(32):
    square(t, l=100)
    t.rt(6)

s.update()
s.exitonclick()