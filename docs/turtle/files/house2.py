import turtle
import houses as h

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=200, starty=100)
s.tracer(0, 0)

t = turtle.Turtle()
t.speed(0)


def door_pos(start_pos, length):
    """calculate door bottom left position

    Args:
        start_pos (tuple): bottom left of house
        length (int): house length

    Returns:
        tuple: bottom left position of door
    """
    return (start_pos[0] + length//3, start_pos[1])


def roof_pos(start_pos, length, height):
    """calculate roof bottom left position allowing a hang of 5 pixels over house

    Args:
        start_pos (tuple): bottom left of house
        length (int): house length
        height (int): house height

    Returns:
        tuple: bottom left position of roof
    """
    return (start_pos[0] -5, start_pos[1] + height)


def window_pos(start_pos, x_add, y_add):
    """calculate the bottom left of window or square making up a window

    Args:
        start_pos (tuple): bottom left of house
        x_add (int): amount to add to the x coordinate of the house start_pos to locate the window
        y_add (int): amount to add to the y coordinate of the house start_pos to locate the window

    Returns:
        tuple: bottom left position of roof
    """
    return (start_pos[0] + x_add, start_pos[1] + y_add)


def window(t, length=10, start_pos=(0, 0), fillc="light blue"):
    """draw a 4 pane square window.
    Uses the window_pos function.

    Args:
        t (class turtle.Turtle): turtle instance.
        length (int, optional): full length of window. Defaults to 10.
        start_pos (tuple, optional): bottom left of window. Defaults to (0, 0).
        fillc (str, optional): window colour. Defaults to "light blue".
    """
    h.square(t, length=length//2, start_pos=start_pos, fillc="light blue")
    h.square(t, length=length//2, start_pos=window_pos(start_pos, length//2, 0), fillc="light blue")
    h.square(t, length=length//2, start_pos=window_pos(start_pos, 0, length//2), fillc="light blue")
    h.square(t, length=length//2, start_pos=window_pos(start_pos, length//2, length//2), fillc="light blue")


def windowed_house(t, length=60, height=40, start_pos=(0, 0), windows=0):
    """draw a house with 0-2 windows

    Args:
        t (class turtle.Turtle): turtle instance.
        length (int, optional): length of house. Defaults to 60.
        height (int, optional): height of house. Defaults to 40.
        start_pos (tuple, optional): bottom left of house. Defaults to (0, 0).
        windows (int, optional): number of windows, 0, 1 or 2. Defaults to 0.
    """
    # front of house
    h.rectangle(t, length=length, width=height, start_pos=start_pos, penw=1, penc="black", fillc="snow")
    # door
    h.rectangle(t, length=length//5, width=height//1.6, start_pos=door_pos(start_pos, length), penw=1, penc="black", fillc="green")
    # roof
    h.isosceles(t, base=length + 10, height=length//3, start_pos=roof_pos(start_pos, length, height), penw=1, penc="black", fillc="brown")
    # windows
    if windows > 0:
        # right hand window
        window(t, length=length//5, start_pos=window_pos(start_pos, length//1.5, height/3))
    if windows > 1:
        # left hand window
        window(t, length=length//5, start_pos=window_pos(start_pos, length//20, height/3))


windowed_house(t, length=210, height=160, start_pos=(-200, 20))
windowed_house(t, length=150, height=120, start_pos=(200, 20))
windowed_house(t, length=60, height=40, start_pos=(-100, 0))
windowed_house(t, length=80, height=50, start_pos=(-10, 0))
windowed_house(t, length=120, height=100, start_pos=(90, 0))
windowed_house(t, length=210, height=160, start_pos=(-390, 0))


windowed_house(t, length=210, height=160, start_pos=(-200, -270), windows=0)
windowed_house(t, length=150, height=120, start_pos=(200, -270), windows=2)
windowed_house(t, length=60, height=40, start_pos=(-100, -290), windows=1)
windowed_house(t, length=80, height=50, start_pos=(-10, -290), windows=2)
windowed_house(t, length=120, height=100, start_pos=(90, -290), windows=1)
windowed_house(t, length=210, height=160, start_pos=(-390, -290), windows=2)


t.ht()
turtle.update()
s.exitonclick()
