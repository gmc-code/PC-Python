import turtle
import math


def square(t, length=50, x=0, y=0, penc="blue", fillc="red", penw=1):
    """draw a square

    Args:
        t (turtle): turtle object
        length (int, optional): side length. Defaults to 50.
        x (int, optional): start x position. Defaults to 0.
        y (int, optional): start y position. Defaults to 0.
        penc (str, optional): pencolor. Defaults to "blue".
        fillc (str, optional): fillcolor. Defaults to "red".
        penw (int, optional): pensize. Defaults to 1.
    """
    t.pu()
    t.goto(x, y)
    t.pd()
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



def rectangle(t, length=40, width=30, x=0, y=0, x=0, y=0, penc="blue", fillc="red", penw=1):
    t.pu()
    t.goto(x, y)
    t.pd()
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



def equilateral(t, side, start_pos, start_h, penc="blue", fillc=None, penw=1):
    """draw a triangle with 3 equal sides

    Args:
        t (turtle): turtle
        side (int): side length
        start_pos (tuple): tuple of x and y position
        start_h (int): starting angle
        pencolor (str, optional): line color. Defaults to "blue".
        fillcolor (_type_, optional): triangle fill color. Defaults to None.
        pensize (int, optional): line width. Defaults to 1.
"""

    t.seth(start_h)
    t.pu()
    t.goto(start_pos)
    t.pd()
    t.pensize(pensize)
    t.pencolor(pencolor)

    if fillcolor is not None:
        t.fillcolor(fillcolor)
        t.begin_fill()

    start_pos = t.pos()
    for _ in range(3):
        t.fd(side)
        t.lt(120)

    if fillcolor is not None:
        t.end_fill()


