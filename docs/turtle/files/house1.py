import turtle
import shapes as sh

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=200, starty=100)
s.tracer(0, 0)

t = turtle.Turtle()
t.speed(0)


def house_door(t, h_length, h_height, h_start_pos):
    """draw door 1/3 along length of house, 1/5 of length of house, 1/1.6 of height of house
    """
    d_pos = (h_start_pos[0] + h_length//3, h_start_pos[1])
    d_height = h_height//1.6
    d_length = h_length//5
    sh.rectangle(t, length=d_length, width=d_height, start_pos=d_pos, penw=1, penc="black", fillc="green")


def house_roof(t, h_length, h_height, h_start_pos):
    """draw roof with overhang of 5 pixels over left side and right side of house
    """
    r_pos = (h_start_pos[0] - 5, h_start_pos[1] + h_height)
    r_height = h_length//3
    r_length = h_length + 10
    sh.isosceles(t, base=r_length, height=r_height, start_pos=r_pos, penw=1, penc="black", fillc="brown")


def simple_house(t, h_length=60, h_height=40, h_start_pos=(0, 0)):
    # main house
    sh.rectangle(t, length=h_length, width=h_height, start_pos=h_start_pos, penw=1, penc="black", fillc="snow")
    # door
    house_door(t, h_length, h_height, h_start_pos)
    # roof
    house_roof(t, h_length, h_height, h_start_pos)


simple_house(t, h_length=210, h_height=160, h_start_pos=(-200, 20))
simple_house(t, h_length=150, h_height=120, h_start_pos=(200, 20))
simple_house(t, h_length=60, h_height=40, h_start_pos=(-100, 0))
simple_house(t, h_length=80, h_height=50, h_start_pos=(-10, 0))
simple_house(t, h_length=120, h_height=100, h_start_pos=(90, 0))
simple_house(t, h_length=210, h_height=160, h_start_pos=(-390, 0))

t.ht()
s.update()
s.exitonclick()