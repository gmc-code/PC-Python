====================================================
Turtle rectangle progressions
====================================================

| The code progressions below draw a rectangle.
| With each version, an improvement in code structure is made.
| Firstly, only sequencing is used, with no iteration.
| Secondly, iteration, using a for-loop, reduces code duplication.
| Thirdly, a definition block with parameters allows for code reuse via the use of arguments.

----

Sequencing: steps to draw a rectangle
------------------------------------------

| The code below uses sequencing only.
| The code below draws a rectangle of side length 120 and width 50 at coordinates (20, 30).
| The starting direction, eastwards, is set by: ``t.seth(0)``
| The starting position, at (20, 30), is set by: ``t.goto(20, 30)``. 
| ``t.pu()`` and ``t.pd()`` are used either side of it to avoid line drawing when repositioning the turtle.
| A line is drawn forwards by: ``t.fd(120)``.
| The turtle then turns to the left by: ``t.lt(90)``.
| A line is drawn forwards by: ``t.fd(50)``.
| The turtle then turns to the left by: ``t.lt(90)``.
| Then the last 2 sides are drawn by doing the same 4 steps again.


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
    t.goto(20, 30)
    t.pd()

    t.fd(120)
    t.lt(90)
    t.fd(50)
    t.lt(90)
    t.fd(120)
    t.lt(90)
    t.fd(50)
    t.lt(90)

    s.exitonclick()

----

.. admonition:: Tasks

    1. From the code above, list the 8 lines that do the actual drawing.
    2. From the 8 lines, list the simplest amount of code that is repeated to form a rectangle.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    From the code above, list the lines that do the actual drawing. 

                    .. code-block:: python

                        t.fd(120)
                        t.lt(90)
                        t.fd(50)
                        t.lt(90)
                        t.fd(120)
                        t.lt(90)
                        t.fd(50)
                        t.lt(90)

                .. tab-item:: Q2

                    From the 8 lines, list the simplest amount of code that is repeated to form a rectangle.

                    .. code-block:: python

                        t.fd(120)
                        t.lt(90)
                        t.fd(50)
                        t.lt(90)


----

Iteration: using a for-loop to draw a rectangle 
------------------------------------------------

| The code below uses iteration to reduce code duplication that was present when only sequencing was used.
| The code below draws a rectangle of side side length 120 and width 50 at coordinates (20, 30).
| Firstly, 2 sides are drawn, then this is repeated.
| The iterator used is "_". This is the standard choice in python when the iterator is not referenced in the for-loop block.

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
    t.goto(20, 30)
    t.pd()

    for _ in range(2):
        t.fd(120)
        t.lt(90)
        t.fd(50)
        t.lt(90)
        
    s.exitonclick()

----

.. admonition:: Tasks

    1. Modify the code above to draw a rectangle of 80 by 150.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the code above to draw a rectangle of 80 by 150.

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
                        t.goto(20, 30)
                        t.pd()

                        for _ in range(2):
                            t.fd(80)
                            t.lt(90)
                            t.fd(150)
                            t.lt(90)
                            
                        s.exitonclick()

----

Definitions: using a def block to draw a rectangle
----------------------------------------------------

| The code below uses a definition block to draw a rectangle.
| The function has parameters to specify the side length and the staring position of the bottom left vertex.
| The function also requires the turtle to be passed as an argument so it can be referred to.
| Before the for-loop, the turtle is repositioned without drawing the movement; **penup** and **pendown** are needed for that.
| The initial heading has been left out of the rectangle function, but it can be set prior to using the rectangle function.

.. py:function:: rectangle(t, length=40, width=30, x=0, y=0)

    | **t** - the turtle object to draw the rectangle
    | **length** - side length, default 40
    | **width** - side width, default 30
    | **x** - starting x position, default 0
    | **y** - starting y position, default 0
    
| In the code below, ``rectangle(t)`` draws a default rectangle.
| ``rectangle(t, length=120, width=50, x=20, y=30)`` draws a rectangle of 120 by 50 at (x=20, y=30).
| ``rectangle(t, length=400, width=300, x=-300, y=-200)`` draws a rectangle of 400 by 300 at (x=-300, y=-100).
    
.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgcolor("white")
    s.title("Grid")
    s.setup(width=800, height=600, startx=0, starty=0)

    t = turtle.Turtle()
    t.speed(5)

    def rectangle(t, length=40, width=30, x=0, y=0):
        t.pu()
        t.goto(x, y)
        t.pd()
        for _ in range(2):
            t.fd(length)
            t.lt(90)
            t.fd(width)
            t.lt(90)


    t.seth(0)
    rectangle(t)
    rectangle(t, length=120, width=50, x=50, y=30)
    rectangle(t, length=400, width=300, x=-300, y=-200)

    s.exitonclick()

----

.. admonition:: Tasks

    1. Modify the code above to draw a rectangle of 80 by 150 at (-80, -150).

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the code above to draw a rectangle of 80 by 150 at (-80, -150).

                    .. code-block:: python

                        import turtle

                        s = turtle.Screen()
                        s.bgcolor("white")
                        s.title("Grid")
                        s.setup(width=800, height=600, startx=0, starty=0)

                        t = turtle.Turtle()
                        t.speed(5)

                        def rectangle(t, length=40, width=30, x=0, y=0):
                            t.pu()
                            t.goto(x, y)
                            t.pd()
                            for _ in range(2):
                                t.fd(length)
                                t.lt(90)
                                t.fd(width)
                                t.lt(90)


                        t.seth(0)
                        rectangle(t, length=80, width=150, x=-80, y=-150)

                        s.exitonclick()

----

Adding pen colour and fill colour parameters
-----------------------------------------------

| The syntax below adds parameters for pen and fill colours.

.. py:function:: rectangle(t, length=40, width=30, x=0, y=0, penc="blue", fillc=None, penw=1)

    | **t** - the turtle object to draw the rectangle
    | **length** - side length; default 40
    | **width** - side width; default 30
    | **x** - starting x position; default 0
    | **y** - starting y position; default 0
    | **penc** - pencolor; default is blue
    | **fillc** - fillcolor; default is None
    | **penw** - pensize; default 1
   
| In the code below, ``rectangle(t, length=400, width=300, x=-100, y=-150, penc="blue", fillc="green", penw=5)`` draws a rectangle of 400 by 300 at (x=-100, y=-150) with a blue pencolor, a green fillcolor, using a pensize of 5.
| The code needs to check the **fillc** argument since setting a fillcolor to **None** will throw an error.

.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgcolor("white")
    s.title("Grid")
    s.setup(width=800, height=600, startx=0, starty=0)

    t = turtle.Turtle()
    t.speed(0)

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

    rectangle(t, length=400, width=300, x=-100, y=-150, penc="blue", fillc="green", penw=5)

    s.exitonclick()

----

.. admonition:: Tasks

    1. Use the definition provided above to draw a rectangle of side lengths 150 and 250 at (x=-150, y=-250) with a purple pencolor, a bisque fillcolor, with a pensize of 10.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Use the definition provided above to draw a rectangle of side lengths 150 and 250 at (x=-150, y=-250) with a purple pencolor, a bisque fillcolor, with a pensize of 10. 

                    .. code-block:: python

                        import turtle

                        s = turtle.Screen()
                        s.bgcolor("white")
                        s.title("Grid")
                        s.setup(width=800, height=600, startx=0, starty=0)

                        t = turtle.Turtle()
                        t.speed(0)

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

                        rectangle(t, length=150, width=250, x=-150, y=-250, penc="purple", fillc="bisque", penw=10)

----

.. admonition:: Tasks

    1. Using sequencing only, draw a rectangle of side lengths 500 and 400 at (-250, -250).
    2. Using a repeat loop (without a function), draw a rectangle of side lengths 50 and 40 at (-25, -25).
    3. Use the definition provided above to draw a rectangle of side lengths 400 and 300 at (x=-300, y=-200) with a blue pencolor, a snow fillcolor, with a pensize of 6.
