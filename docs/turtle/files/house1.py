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
    """return bottom left position of door 1/3 along length of house
    """
    return (start_pos[0] + length//3, start_pos[1])


def roof_pos(start_pos, height):
    """return bottom left position of roof allows for an overhang of 5 pixels over left side of house
    """
    return (start_pos[0] -5, start_pos[1] + height)


def simple_house(t, hlength=60, hheight=40, hstart_pos=(0, 0)):
    # main house
    sh.rectangle(t, length=hlength, width=hheight, start_pos=hstart_pos, penw=1, penc="black", fillc="snow")
    # door
    sh.rectangle(t, length=hlength//5, width=hheight//1.6, start_pos=door_pos(hstart_pos, hlength), penw=1, penc="black", fillc="green")
    # roof
    sh.isosceles(t, base=hlength + 10, height=hlength//3, start_pos=roof_pos(hstart_pos, hheight), penw=1, penc="black", fillc="brown")


simple_house(t, hlength=210, hheight=160, hstart_pos=(-200, 20))
simple_house(t, hlength=150, hheight=120, hstart_pos=(200, 20))
simple_house(t, hlength=60, hheight=40, hstart_pos=(-100, 0))
simple_house(t, hlength=80, hheight=50, hstart_pos=(-10, 0))
simple_house(t, hlength=120, hheight=100, hstart_pos=(90, 0))
simple_house(t, hlength=210, hheight=160, hstart_pos=(-390, 0))


t.ht()
s.update()
s.exitonclick()
