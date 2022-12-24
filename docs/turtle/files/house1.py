import turtle
import shapes as sh

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=200, starty=100)
s.tracer(0, 0)

t = turtle.Turtle()
t.speed(0)


def door_pos(start_pos, length):
    return (start_pos[0] + length/3, start_pos[1])


def roof_pos(start_pos, length, height):
    return (start_pos[0] -5, start_pos[1] + height)


def simple_house(t, length=60, height=40, start_pos=(0, 0)):
    # main house
    sh.rectangle(t, length=length, width=height, start_pos=start_pos, penw=1, penc="black", fillc="snow")
    # door
    sh.rectangle(t, length=length/5, width=height/1.6, start_pos=door_pos(start_pos, length), penw=1, penc="black", fillc="green")
    # roof
    sh.isosceles(t, base=length + 10, height=length/3, start_pos=roof_pos(start_pos, length, height), penw=1, penc="black", fillc="brown")


simple_house(t, length=210, height=160, start_pos=(-200, 20))
simple_house(t, length=150, height=120, start_pos=(200, 20))
simple_house(t, length=60, height=40, start_pos=(-100, 0))
simple_house(t, length=80, height=50, start_pos=(-10, 0))
simple_house(t, length=120, height=100, start_pos=(90, 0))
simple_house(t, length=210, height=160, start_pos=(-390, 0))


t.ht()
s.update()
s.exitonclick()
