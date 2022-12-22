import turtle
import math


def square(t, length=50, start_pos=(0, 0), start_h=0, penw=1, penc="black", fillc=None):
    """Draw a square given side length.

    Args:
        t (class turtle.Turtle): turtle instance.
        length (int, optional): side length. Defaults to 50.
        start_pos (tuple, optional): start position. Defaults to (0, 0).
        start_h (int, optional): initial heading. Defaults to 0.
        penw (int, optional): pensize. Defaults to 1.
        penc (str, optional): pencolor. Defaults to "black".
        fillc (str, optional): fillcolor. Defaults to None.

    """
    t.pu()
    t.goto(start_pos)
    t.pd()
    t.seth(start_h)

    t.pensize(penw)
    t.pencolor(penc)

    if fillc is not None:
        t.fillcolor(fillc)
        t.begin_fill()

    for _ in range(4):
        t.fd(length)
        t.lt(90)

    if fillc is not None:
        t.end_fill()


def rectangle(t, length=40, width=30, start_pos=(0, 0), start_h=0, penw=1, penc="black", fillc=None):
    """Draw a rectangle given side lengths.

    Args:
        t (class turtle.Turtle): turtle instance.
        length (int, optional): side length. Defaults to 40.
        width (int, optional): side width. Defaults to 30.
        start_pos (tuple, optional): start position coordinates. Defaults to (0, 0).
        start_h (int, optional): initial heading. Defaults to 0.
        penw (int, optional): pen size. Defaults to 1.
        penc (str, optional): pen color. Defaults to "black".
        fillc (_type_, optional): fill color. Defaults to None.
    """

    t.pu()
    t.goto(start_pos)
    t.pd()
    t.seth(start_h)

    t.pensize(penw)
    t.pencolor(penc)

    if fillc is not None:
        t.fillcolor(fillc)
        t.begin_fill()

    for _ in range(2):
        t.fd(length)
        t.lt(90)
        t.fd(width)
        t.lt(90)

    if fillc is not None:
        t.end_fill()



def scalene(t, side_a, angle_C, side_b, start_pos=(0, 0), start_h=0, penw=1, penc="black", fillc=None):
    """Draw a scalene triangle given SAS (side angle side).

    Args:
        t (class turtle.Turtle): turtle instance.
        side_a (int): side length before angle.
        angle_C (int): angle between 2 sides.
        side_b (int): side length after angle.
        start_pos (tuple, optional): start position. Defaults to (0, 0).
        start_h (int, optional): initial heading. Defaults to 0.
        penw (int, optional): pen size. Defaults to 1.
        penc (str, optional): pen color. Defaults to "black".
        fillc (str, optional): fill color. Defaults to None.
    """
    t.pu()
    t.goto(start_pos)
    t.pd()
    t.seth(start_h)

    t.pensize(penw)
    t.pencolor(penc)

    if fillc is not None:
        t.fillcolor(fillc)
        t.begin_fill()

    t.fd(side_a)
    t.lt(180 - angle_C)
    t.fd(side_b)
    t.goto(start_pos)

    if fillc is not None:
        t.end_fill()




def isosceles(t, base, height, start_pos=(0, 0), start_h=0, penw=1, penc="black", fillc=None):
    """Draw an isosceles triangle given base and height.

    Args:
        t (class turtle.Turtle): turtle instance.
        base (int): base of triangle.
        height (int): height of triangle.
        start_pos (tuple, optional): start position. Defaults to (0, 0).
        start_h (int, optional): initial heading. Defaults to 0.
        penw (int, optional): pen size. Defaults to 1.
        penc (str, optional): pen color. Defaults to "black".
        fillc (str, optional): fill color. Defaults to None.
    """
    t.pu()
    t.goto(start_pos)
    t.pd()
    t.seth(start_h)

    t.pensize(penw)
    t.pencolor(penc)

    b = math.sqrt(height**2 + (base**2) / 4)
    angle_B = math.degrees(math.atan(2 * height / base))

    if fillc is not None:
        t.fillcolor(fillc)
        t.begin_fill()

    t.fd(base)
    t.lt(180 - angle_B)
    t.fd(b)
    t.goto(start_pos)

    if fillc is not None:
        t.end_fill()


def equilateral(t, side, start_pos=(0, 0), start_h=0, penw=1, penc="black", fillc=None):
    """Draw an equilateral triangle

    Args:
        t (class turtle.Turtle): turtle instance.
        side (int): side length.
        start_pos (tuple, optional): start position. Defaults to (0, 0).
        start_h (int, optional): initial heading. Defaults to 0.
        penw (int, optional): pen size. Defaults to 1.
        penc (str, optional): pen color. Defaults to "black".
        fillc (str, optional): fill color. Defaults to None.
    """
    t.pu()
    t.goto(start_pos)
    t.pd()
    t.seth(start_h)

    t.pensize(penw)
    t.pencolor(penc)

    if fillc is not None:
        t.fillcolor(fillc)
        t.begin_fill()

    start_pos = t.pos()
    for _ in range(3):
        t.fd(side)
        t.lt(120)

    if fillc is not None:
        t.end_fill()

