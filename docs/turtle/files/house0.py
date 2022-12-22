import turtle
import houses as h

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=200, starty=100)

t = turtle.Turtle()
h.rectangle(t, length=200, width=80, start_pos=(0,0), fillc="light green")

s.exitonclick()