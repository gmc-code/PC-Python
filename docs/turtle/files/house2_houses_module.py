import turtle
import houses as h

s = turtle.Screen()
s.bgcolor("white")
s.title("Houses")
s.setup(width=800, height=600, startx=200, starty=100)
s.tracer(0, 0)

t = turtle.Turtle()
t.speed(0)

h.house(t, length=210, height=160, start_pos=(-200, 20), w_sides="LR")
h.house(t, length=150, height=120, start_pos=(200, 20), w_sides="LR")
h.house(t, length=60, height=40, start_pos=(-100, 0), w_sides=None)
h.house(t, length=80, height=50, start_pos=(-10, 0), w_sides="R")
h.house(t, length=120, height=100, start_pos=(90, 0), w_sides="L")
h.house(t, length=210, height=160, start_pos=(-390, 0), w_sides="LR")

t.ht()
s.update()
s.exitonclick()
