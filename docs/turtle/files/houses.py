import turtle
import math

import turtle

s = turtle.Screen()
s.bgcolor("white")
s.title("Grid")
s.setup(width=800, height=600, startx=0, starty=0)

t = turtle.Turtle()
t.speed(0)


def square(t, length=50, start_pos=(0, 0), start_h=0, penw=1, penc="blue", fillc=None):
    """draw a square

    Args:
        t (turtle): turtle instance
        length (int, optional): side length. Defaults to 50.
        start_pos (tuple, optional): start position. Defaults to (0, 0).
        start_h (int, optional): initial heading. Defaults to 0.
        penw (int, optional): pensize. Defaults to 1.
        penc (str, optional): pencolor. Defaults to "blue".
        fillc (str, optional): fillcolor. Defaults to "red".

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


def rectangle(t, length=40, width=30, start_pos=(0, 0), start_h=0, penw=1, penc="blue", fillc=None):
    """Draw a rectangle

    Args:
        t (turtle): turtle instance
        length (int, optional): side length. Defaults to 40.
        width (int, optional): side width. Defaults to 30.
        start_pos (tuple, optional): start position. Defaults to (0, 0).
        start_h (int, optional): initial heading. Defaults to 0.
        penw (int, optional): pensize. Defaults to 1.
        penc (str, optional): pencolor. Defaults to "blue".
        fillc (_type_, optional): fillcolor. Defaults to None.
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



def scalene(t, side_a, angle_C, side_b, start_pos, start_h=0, penw=1, penc="blue", fillc=None):
    """_summary_

    Args:
        t (_type_): _description_
        side_a (_type_): _description_
        angle_C (_type_): _description_
        side_b (_type_): _description_
        start_pos (_type_): _description_
        start_h (int, optional): _description_. Defaults to 0.
        penw (int, optional): _description_. Defaults to 1.
        penc (str, optional): _description_. Defaults to "blue".
        fillc (_type_, optional): _description_. Defaults to None.
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




def isosceles(t, base, height, start_pos, start_h=0, penw=1, penc="blue", fillc=None):
    """_summary_

    Args:
        t (_type_): _description_
        base (_type_): _description_
        height (_type_): _description_
        start_pos (_type_): _description_
        start_h (int, optional): _description_. Defaults to 0.
        penw (int, optional): _description_. Defaults to 1.
        penc (str, optional): _description_. Defaults to "blue".
        fillc (_type_, optional): _description_. Defaults to None.
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


def equilateral(t, side, start_pos, start_h=0, penw=1, penc="blue", fillc=None):
    """_summary_

    Args:
        t (_type_): _description_
        side (_type_): _description_
        start_pos (_type_): _description_
        start_h (int, optional): _description_. Defaults to 0.
        penw (int, optional): _description_. Defaults to 1.
        penc (str, optional): _description_. Defaults to "blue".
        fillc (_type_, optional): _description_. Defaults to None.
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

