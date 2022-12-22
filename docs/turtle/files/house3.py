import turtle
import houses as h

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=200, starty=100)
s.tracer(0, 0)

t = turtle.Turtle()
t.speed(0)

h.windowed_house(t, length=210, height=160, start_pos=(-200, 20), windows="R")
h.windowed_house(t, length=150, height=120, start_pos=(200, 20), windows="R")
h.windowed_house(t, length=210, height=160, start_pos=(-390, 0), windows="LR")
h.windowed_house(t, length=60, height=40, start_pos=(-100, 0), windows=None)
h.windowed_house(t, length=80, height=50, start_pos=(-10, 0), windows="L")
h.windowed_house(t, length=120, height=100, start_pos=(90, 0), windows="LR")
    
t.ht()
turtle.update()
s.exitonclick()
