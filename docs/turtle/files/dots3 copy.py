"""draw_dot
"""
import turtle


def draw_dot(t, centre=(0, 0), size=20, color="blue"):
    t.pu()
    t.goto(centre)
    t.pd()
    t.dot(size, color)


def draw_dot_stack(t, x, y, yadd, size_0, size_dec, colors):
    for i in range(len(colors)):
        centre_xy = (x, y + yadd*i)
        size = size_0 - size_dec*i
        draw_dot(t, centre=centre_xy, size=size, color=colors[i])


s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=850, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)
t.ht()

colors = ["light blue", "pink", "light green", "yellow"]

draw_dot_stack(t,x=-300, y=-80, yadd=10, size_0=200, size_dec=50, colors=colors)
draw_dot_stack(t,x=-100, y=-80, yadd=25, size_0=200, size_dec=40, colors=colors)
draw_dot_stack(t,x=100, y=-80, yadd=40, size_0=200, size_dec=30, colors=colors)
draw_dot_stack(t,x=300, y=-80, yadd=55, size_0=200, size_dec=20, colors=colors)

s.exitonclick()
