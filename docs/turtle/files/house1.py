import turtle
import shapes as sh

s = turtle.Screen()
s.bgcolor("white")
s.title("Simple Houses")
s.setup(width=800, height=600, startx=200, starty=100)
s.tracer(0, 0)

t = turtle.Turtle()
t.speed(0)


def house_door(t, length, height, start_pos):
    """draw door 1/3 along length of house, 1/5 of length of house, 1/1.6 of height of house
    """
    d_pos = (start_pos[0] + length//3, start_pos[1])
    d_height = height//1.6
    d_length = length//5
    sh.rectangle(t, length=d_length, width=d_height, start_pos=d_pos, penw=1, penc="black", fillc="green")


def house_roof(t, length, height, start_pos):
    """draw roof with overhang of 1/20 length of house over left side and right side of house
    """
    r_height = length//3
    r_length = length * 1.1
    r_overhang = length//20
    r_pos = (start_pos[0] - r_overhang, start_pos[1] + height)
    sh.isosceles(t, base=r_length, height=r_height, start_pos=r_pos, penw=1, penc="black", fillc="brown")


def simple_house(t, length=60, height=40, start_pos=(0, 0)):
    # main house
    sh.rectangle(t, length=length, width=height, start_pos=start_pos, penw=1, penc="black", fillc="snow")
    # door
    house_door(t, length, height, start_pos)
    # roof
    house_roof(t, length, height, start_pos)


simple_house(t, length=210, height=160, start_pos=(-200, 20))
simple_house(t, length=150, height=120, start_pos=(200, 20))
simple_house(t, length=60, height=40, start_pos=(-100, 0))
simple_house(t, length=80, height=50, start_pos=(-10, 0))
simple_house(t, length=120, height=100, start_pos=(90, 0))
simple_house(t, length=210, height=160, start_pos=(-390, 0))

t.ht()
s.update()
s.exitonclick()