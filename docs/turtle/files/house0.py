import turtle
import shapes as sh

s = turtle.Screen()
s.bgcolor("white")
s.title("Houses")
s.setup(width=800, height=600, startx=200, starty=100)

t = turtle.Turtle()

def house(t, length=60, height=40, start_pos=(0, 0), w_sides=None):
    """draw a house with 0-2 windows

    Args:
        t (class turtle.Turtle): turtle instance.
        length (int, optional): length of house. Defaults to 60.
        height (int, optional): height of house. Defaults to 40.
        start_pos (tuple, optional): bottom left of house. Defaults to (0, 0).
        w_sides (str, optional): window sides - L for left side of house; R for right and LR for both. Defaults to None.
    """
    # front of house
    sh.rectangle(t, length=length, width=height, start_pos=start_pos,
                    penw=1, penc="black", fillc="snow")

house(t, length=600, height=300, start_pos=(-300, -200), w_sides="LR")

s.exitonclick()