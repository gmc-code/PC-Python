import turtle
import shapes as sh

s = turtle.Screen()
s.bgcolor("white")
s.title("Houses")
s.setup(width=800, height=600, startx=200, starty=100)

t = turtle.Turtle()
t.speed(9)

def house_door(t, length, height, start_pos):
    """draw door 1/3 along length of house, 1/5 of length of house, 1/1.6 of height of house

    Args:
        t (class turtle.Turtle): turtle instance.
        length (int, optional): length of house.
        height (int, optional): height of house.
        start_pos (tuple, optional): bottom left of house.
    """
    d_pos = (start_pos[0] + length//3, start_pos[1])
    d_height = height//1.6
    d_length = length//5
    sh.rectangle(t, length=d_length, width=d_height, start_pos=d_pos, penw=1, penc="black", fillc="green")


def house(t, length=60, height=40, start_pos=(0, 0), w_sides=None):
    """draw a house with 0-2 windows

    Args:
        t (class turtle.Turtle): turtle instance.
        length (int, optional): length of house. Defaults to 60.
        height (int, optional): height of house. Defaults to 40.
        start_pos (tuple, optional): bottom left of house. Defaults to (0, 0).
        w_sides (str, optional): L for left side of house; R for right and LR for both. Defaults to None.
    """
    # front of house
    sh.rectangle(t, length=length, width=height, start_pos=start_pos,
                    penw=1, penc="black", fillc="snow")
    # door
    house_door(t, length, height, start_pos)

    # roof

    # windows

house(t, length=600, height=300, start_pos=(-300, -200), w_sides="LR")

s.exitonclick()