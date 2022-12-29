import turtle
import shapes as sh


def house_door(t, length, height, start_pos):
    """draw door centered along length of houseat 4/10 of length, 2/10 of length of house, 1/1.6 of height of house
    
    Args:
        t (class turtle.Turtle): turtle instance.
        length (int, optional): length of house.
        height (int, optional): height of house.
        start_pos (tuple, optional): bottom left of house.
    """
    d_height = height//1.6
    d_length = length//5
    d_pos = (start_pos[0] + 4*length//10, start_pos[1])
    sh.rectangle(t, length=d_length, width=d_height, start_pos=d_pos, penw=1, penc="black", fillc="green")


def house_door_v1(t, length, height, start_pos):
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


def house_roof(t, length, height, start_pos):
    """draw roof height 1/3 of house length
    with overhang of 1/20 length of house over left side and right side of house
    
    Args:
        t (class turtle.Turtle): turtle instance.
        length (int, optional): length of house.
        height (int, optional): height of house.
        start_pos (tuple, optional): bottom left of house.
    """
    r_height = length//3
    r_length = length * 1.1
    r_overhang = length//20
    r_pos = (start_pos[0] - r_overhang, start_pos[1] + height)
    sh.isosceles(t, base=r_length, height=r_height, start_pos=r_pos, penw=1, penc="black", fillc="brown")


def house_window4_v1(t, length, height, start_pos, w_side, fillc="light blue"):
    """draw a 4 pane square window.
        each window pane is half the total length of the window.
        right hand window; 1/5 of house length; 2/3 of house length from left of house up 1/3 of height of house
        left hand window; 1/5 of house length; 1/20 of house length from left of house up 1/3 of height of house

    Args:
        t (class turtle.Turtle): turtle instance.
        length (int, optional): length of house.
        height (int, optional): height of house.
        start_pos (tuple, optional): bottom left of house.
        w_side (str): L for left side of house; R for right and LR for both.
        fillc (str, optional): window pane colour. Defaults to "light blue".
    """
    w_length = length//10
    if "L" in w_side:
        w_pos = (start_pos[0] + length//20, start_pos[1] + height//3)
    elif "R" in w_side:
        w_pos = (start_pos[0] + 2*length//3, start_pos[1] + height//3)
    else:
        w_pos = (start_pos[0] + length//20, start_pos[1] + height//3)

    sh.square(t, length=w_length, start_pos=w_pos, fillc="light blue")
    sh.square(t, length=w_length, start_pos=(w_pos[0] + w_length, w_pos[1]), fillc="light blue")
    sh.square(t, length=w_length, start_pos=(w_pos[0], w_pos[1] + w_length), fillc="light blue")
    sh.square(t, length=w_length, start_pos=(w_pos[0] + w_length, w_pos[1] + w_length), fillc="light blue")


def house_window4(t, length, height, start_pos, w_side, fillc="light blue"):
    """draw a 4 pane square window.
        each window pane is half the total length of the window.
        right hand window; 1/5 of house length; 7/10 of house length from left of house up 1/3 of height of house
        left hand window; 1/5 of house length; 1/10 of house length from left of house up 1/3 of height of house

    Args:
        t (class turtle.Turtle): turtle instance.
        length (int, optional): length of house.
        height (int, optional): height of house.
        start_pos (tuple, optional): bottom left of house.
        w_side (str): L for left side of house; R for right and LR for both.
        fillc (str, optional): window pane colour. Defaults to "light blue".
    """
    w_length = length//10
    if "L" in w_side:
        w_pos = (start_pos[0] + length//10, start_pos[1] + height//3)
    elif "R" in w_side:
        w_pos = (start_pos[0] + 7*length//10, start_pos[1] + height//3)
    else:
        w_pos = (start_pos[0] + length//20, start_pos[1] + height//3)

    sh.square(t, length=w_length, start_pos=w_pos, fillc="light blue")
    sh.square(t, length=w_length, start_pos=(w_pos[0] + w_length, w_pos[1]), fillc="light blue")
    sh.square(t, length=w_length, start_pos=(w_pos[0], w_pos[1] + w_length), fillc="light blue")
    sh.square(t, length=w_length, start_pos=(w_pos[0] + w_length, w_pos[1] + w_length), fillc="light blue")



def house(t, length=60, height=40, start_pos=(0, 0), w_sides=None):
    """draw a house with 0-2 windows

    Args:
        t (class turtle.Turtle): turtle instance.
        length (int, optional): length of house. Defaults to 60.
        height (int, optional): height of house. Defaults to 40.
        start_pos (tuple, optional): bottom left of house. Defaults to (0, 0).
        w_sides (str, optional): window sides - L for windows on left side of house; R for right and LR for both. Defaults to None.
    """
    # front of house
    sh.rectangle(t, length=length, width=height, start_pos=start_pos, penw=1, penc="black", fillc="snow")
    # door
    house_door(t, length, height, start_pos)
    # roof
    house_roof(t, length, height, start_pos)
    # windows
    if w_sides is not None:
        if "R" in w_sides:
            # right hand window
            house_window4(t, length, height, start_pos, "R")
        if "L" in w_sides:
            # left hand window
            house_window4(t, length, height, start_pos, "L")


def house2(t, length=60, height=40, start_pos=(0, 0), w_sides=None):
    """draw a house with 0-2 windows

    Args:
        t (class turtle.Turtle): turtle instance.
        length (int, optional): length of house. Defaults to 60.
        height (int, optional): height of house. Defaults to 40.
        start_pos (tuple, optional): bottom left of house. Defaults to (0, 0).
        w_sides (str, optional): window sides - L for windows on left side of house; R for right and LR for both. Defaults to None.
    """
    # front of house
    sh.rectangle(t, length=length, width=height, start_pos=start_pos, penw=1, penc="black", fillc="snow")
    # door
    house_door(t, length, height, start_pos)
    # roof
    house_roof(t, length, height, start_pos)
    # windows
    if w_sides is not None:
        if "R" in w_sides:
            # right hand window
            house_window4(t, length, height, start_pos, "R")
        if "L" in w_sides:
            # left hand window
            house_window4(t, length, height, start_pos, "L")
