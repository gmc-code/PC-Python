import turtle
import math
import random

s = turtle.Screen()
s.bgcolor("white")
s.title("stars")
s.setup(width=800, height=600, startx=0, starty=0)
s.tracer(0, 0)

t = turtle.Turtle()
turtle.colormode(255)
t.speed(0)
t.width(1)
t.color("red", "yellow")  # outline, fill


def star(t, x, y, n_points, r_inner, r_outer):
    # Calculate coordinates of the points on the inner and outer circle
    points_x_inner = []
    points_y_inner = []
    points_x_outer = []
    points_y_outer = []

    for i in range(n_points):
        angle = 2 * math.pi * i / n_points
        points_x_inner.append(x + r_inner * math.cos(angle))
        points_y_inner.append(y + r_inner * math.sin(angle))
        angle2 = angle + math.pi / n_points
        points_x_outer.append(x + r_outer * math.cos(angle2))
        points_y_outer.append(y + r_outer * math.sin(angle2))

    # Connect the points with lines
    t.penup()
    t.goto([points_x_outer[-1], points_y_outer[-1]])
    t.pendown()
    t.begin_fill()

    for x_in, y_in, x_out, y_out in zip(
        points_x_inner, points_y_inner, points_x_outer, points_y_outer
    ):
        t.goto([x_in, y_in])
        t.goto([x_out, y_out])

    t.end_fill()


for _ in range(200):
    for n_points in range(7, 4, -1):
        x = -400 + random.randrange(0, 800, 20)
        y = -300 + random.randrange(0, 600, 20)
        r_inner = random.randrange(10, 45, 5)
        r_outer = r_inner + random.randrange(20, 75, 5)
        colp = (
            random.randrange(128, 172, 16),
            random.randrange(128, 172, 16),
            random.randrange(128, 172, 16),
        )
        colf = (
            random.randrange(202, 255, 16),
            random.randrange(202, 255, 16),
            random.randrange(202, 255, 16),
        )
        t.color(colp, colf)
        star(t, x, y, n_points, r_inner, r_outer)

s.exitonclick()
