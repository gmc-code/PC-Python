"""draw triangle
"""
import turtle
import houses as h
from PIL import ImageGrab

import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("Turtle Screen")
s.setup(width=800, height=600, startx=300, starty=300)
s.tracer(0, 0)

# turtle drawing to go here

t = turtle.Turtle()
t.speed(0)

h.windowed_house(t, length=210, height=160, start_pos=(-200, 20), windows="R")
h.windowed_house(t, length=150, height=120, start_pos=(200, 20), windows="R")
h.windowed_house(t, length=210, height=160, start_pos=(-390, 0), windows="LR")
h.windowed_house(t, length=60, height=40, start_pos=(-100, 0), windows=None)
h.windowed_house(t, length=80, height=50, start_pos=(-10, 0), windows="L")
h.windowed_house(t, length=120, height=100, start_pos=(90, 0), windows="LR")

t.ht()
s.update()  


def fxn():
    ImageGrab.grab((300, 300, 1100, 900)).save('test.png')
      
# call methods
turtle.onkey(fxn,'space')
  
# to listen by the turtle
turtle.listen()

s.exitonclick()