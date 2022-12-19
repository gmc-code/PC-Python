====================================================
Turtle square progressions
====================================================

| The code progressions below draw a simple square.
| With each version, an improvement is made.
| Firstly, sequencing only is used with no iteration.
| Iteration using a for loop reduce the code lines.
| Placing the code in a function allows code reuse with the use of arguments.

----

Turtle square in steps
----------------------------------------

| The code below draws a square of side length 50 at coordinates (50,50).
| The starting direction, directly upwards, is set by: ``t.seth(90)``
| The starting position, at (50, 50), is set by: ``t.goto(50,50)``. ``t.pu()`` and ``t.pd()`` are used either side of it to avoid line drawing by the turtle repositioning.
| A line is drawn upwards by: ``t.fd(50)``.
| The turtle then turns to the right by: ``t.rt(90)``.
| The fd(50) and rt(90) are then repeated 3 more times for the other three sides.


.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgcolor("white")
    s.title("Grid")
    s.setup(width=800, height=600, startx=0, starty=0)

    t = turtle.Turtle()
    t.speed(2)

    t.seth(90)
    t.pu()
    t.goto(50,50)
    t.pd()

    t.fd(50)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(50)
    t.rt(90)

    s.exitonclick()

----

Turtle square using for loop
----------------------------------------

| The code below draws a square of side length 50 at coordinates (50,50).
| The fd(50) and rt(90) are placed in a for loop.
| The iterator used is "_". This is the standard choice in python whne the iterator is not used in the for loop block.

.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgcolor("white")
    s.title("Grid")
    s.setup(width=800, height=600, startx=0, starty=0)

    t = turtle.Turtle()
    t.speed(2)

    t.seth(90)
    t.pu()
    t.goto(50, 50)
    t.pd()

    for _ in range(4):
        t.fd(50)
        t.rt(90)

    s.exitonclick()

----

Turtle square function
----------------------------------------

| The code below draws a square of side length 50 at coordinates (50,50).
| The function has parameters to specify the staring position and the side length.
| The function also requires the turtle to be passed as an argument.

.. pyfunction:: square(t, l=50, x=0, y=0)

    | t - the turtle object to draw the square
    | l - side length, default 50
    | x - starting x position, default 0
    | y - starting y position, default 0
    

.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgcolor("white")
    s.title("Grid")
    s.setup(width=800, height=600, startx=0, starty=0)

    t = turtle.Turtle()
    t.speed(0)

    def square(t, l=50, x=0, y=0):
        t.seth(90)
        t.pu()
        t.goto(x, y)
        t.pd()
        for _ in range(4):
            t.fd(l)
            t.rt(90)

    square(t)
    square(t, l=100, x=200, y=0)
    square(t, l=100, x=0, y=100)
    s.exitonclick()