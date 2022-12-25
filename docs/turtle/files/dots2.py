"""draw dots
"""
import turtle


def draw_dot(t, centre=(0, 0), size=20, color="blue"):
    t.pu()
    t.goto(centre)
    t.pd()
    t.dot(size, color)


s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)

sizes = [200, 150, 100, 50]
colors = ["light blue", "pink", "light green", "yellow"]
centres = [(0, -100), (0, -50), (0, 0), (0, 30)]
for i in range(len(sizes)):
    draw_dot(t, centre=centres[i], size=sizes[i], color=colors[i])

s.exitonclick()
