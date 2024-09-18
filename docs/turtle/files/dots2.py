import turtle


def draw_dot(t, centre=(0, 0), size=20, color="blue"):
    t.pu()
    t.goto(centre)
    t.pd()
    t.dot(size, color)


s = turtle.Screen()
s.bgcolor("white")
s.title("dots")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)
t.ht()

centres = [(0, -100), (0, -50), (0, 0), (0, 50)]
sizes = [200, 160, 120, 80]
colors = ["light blue", "pink", "light green", "yellow"]

for i in range(len(sizes)):
    draw_dot(t, centre=centres[i], size=sizes[i], color=colors[i])

s.exitonclick()