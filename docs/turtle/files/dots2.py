"""draw dots
"""
import turtle

def do_dot(t, start_pos=(0, 0), size=30, color="white"):
    t.pu()
    t.goto(start_pos)
    t.pd()
    t.dot(200, color)




s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(5)


t.pu()
t.goto(20, 30)
t.pd()
t.seth(0)

# t.dot(200, "light blue")
# t.dot(150, "pink")
# t.dot(100, "light green")
# t.dot(50, "yellow")
do_dot(t, start_pos=(-100, -150), size=200, color="light green")



s.exitonclick()
