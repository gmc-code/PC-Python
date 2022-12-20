====================================================
Turtle rectangle progressions
====================================================

| The code progressions below draw a rectangle.
| With each version, an improvement is made.
| Firstly, only sequencing is used, with no iteration.
| Iteration, using a for loop, reduces the code lines.
| Placing the code in a function allows for code reuse with the use of arguments.

----

Turtle rectangle in steps
----------------------------------------

| The code below draws a rectangle of side lengths 120 and 40 at coordinates (20,30).
| The starting direction, eastwards, is set by: ``t.seth(0)``
| The starting position, at (20, 30), is set by: ``t.goto(20,30)``. ``t.pu()`` and ``t.pd()`` are used either side of it to avoid line drawing by the turtle repositioning.
| A line is drawn upwards by: ``t.fd(120)``.
| The turtle then turns to the left by: ``t.lt(90)``.
| Then the other 3 sides are added.


.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgcolor("white")
    s.title("Grid")
    s.setup(width=800, height=600, startx=0, starty=0)

    t = turtle.Turtle()
    t.speed(5)

    t.seth(0)
    t.pu()
    t.goto(50, 50)
    t.pd()

    t.fd(120)
    t.lt(90)
    t.fd(40)
    t.lt(90)
    t.fd(120)
    t.lt(90)
    t.fd(40)
    t.lt(90)

    s.exitonclick()

----

Turtle rectangle using for loop
----------------------------------------

| The code below draws a rectangle of side length 50 at coordinates (20, 20).
| What code is repeated above? Each line is foolowed by a right angled turn.
| The fd(50) and lt(90) are placed in a for loop with 4 repeats for the 4 sides.
| The iterator used is "_". This is the standard choice in python whne the iterator is not used in the for loop block.

.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgcolor("white")
    s.title("Grid")
    s.setup(width=800, height=600, startx=0, starty=0)

    t = turtle.Turtle()
    t.speed(5)

    t.seth(0)
    t.pu()
    t.goto(20, 20)
    t.pd()

    for _ in range(4):
        t.fd(50)
        t.lt(90)

    s.exitonclick()

----

Turtle rectangle function
----------------------------------------

| The rectangle function draws a rectangle.
| The function has parameters to specify the side length and the staring position of the bottom left vertex.
| The function also requires the turtle to be passed as an argument.
| The initial heading has been left out of the function.

.. pyfunction:: rectangle(t, l=50, x=0, y=0)

    | t - the turtle object to draw the rectangle
    | l - side length, default 50
    | x - starting x position, default 0
    | y - starting y position, default 0
    
| In the code below, a default rectangle is drawn using ``rectangle(t)``.
| A second rectangle of length 100 is drawn at (x=200, y=100).
| A third rectangle of length 250 is drawn at (x=-300, y=-200).

.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgcolor("white")
    s.title("Grid")
    s.setup(width=800, height=600, startx=0, starty=0)

    t = turtle.Turtle()
    t.speed(5)

    def rectangle(t, l=50, x=0, y=0):
        t.pu()
        t.goto(x, y)
        t.pd()
        for _ in range(4):
            t.fd(l)
            t.lt(90)

    t.seth(0)
    rectangle(t)
    rectangle(t, l=100, x=200, y=100)
    rectangle(t, l=250, x=-300, y=-200)
    s.exitonclick()

----

Adding pen colour and fill colour parameters
-----------------------------------------------

| The code adds parameters for pen and fill colours.

.. pyfunction:: rectangle(t, l=50, x=0, y=0, penc="blue", fillc=None, penw=1)

    | t - the turtle object to draw the rectangle
    | l - side length, default 50
    | x - starting x position, default 0
    | y - starting y position, default 0
    | penc - pencolor, default is blue
    | fillc - fillcolor, default is None
    | penw - pensize, default 1
   
| In the code below, a rectangle of length 200 is drawn at (x=-100, y=-100) with a blue pencolor, a green fillcolor, with a pensize of 2.
| The code needs to check the **fillc** argument since setting a fillcolor to **None** will throw an error.

.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgcolor("white")
    s.title("Grid")
    s.setup(width=800, height=600, startx=0, starty=0)

    t = turtle.Turtle()
    t.speed(0)

    def rectangle(t, l=50, x=0, y=0, penc="blue", fillc="red", penw=1):
        t.pu()
        t.goto(x, y)
        t.pd()
        t.pensize(penw)
        t.pencolor(penc)
        if fillc is not None:
            t.fillcolor(fillc)
            t.begin_fill()
        for _ in range(4):
            t.fd(l)
            t.lt(90)
        if fillc is not None:
            t.end_fill()

    rectangle(t, l=200, x=-100, y=-100, penc="blue", fillc="snow", penw=2)

    s.exitonclick()

