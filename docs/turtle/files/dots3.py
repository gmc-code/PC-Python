"""draw_dot
"""
import turtle


def draw_dot(t, centre=(0, 0), size=20, color="blue"):
    t.pu()
    t.goto(centre)
    t.pd()
    t.dot(size, color)


def draw_dot_stack(t, x, y, yadd, sizes, colors):
    for i in range(len(sizes)):
        centre_xy = (x, y+yadd*i)
        draw_dot(t, centre=centre_xy, size=sizes[i], color=colors[i])


s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=850, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)
t.ht()

colors = ["light blue", "pink", "light green", "yellow"]

sizes = [200, 150, 100, 50]
draw_dot_stack(t,-300, -80, 10, sizes, colors)

sizes = [200, 160, 120, 80]
draw_dot_stack(t,-100, -80, 25, sizes, colors)

sizes = [200, 170, 140, 110]
draw_dot_stack(t,100, -80, 40, sizes, colors)

sizes = [200, 180, 160, 140]
draw_dot_stack(t,300, -80, 55, sizes, colors)

s.exitonclick()
