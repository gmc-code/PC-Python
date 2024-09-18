====================================================
Turtle screen advanced
====================================================

| The code below shows some more useful methods for Turtle screens.

----

Screen background gif
-----------------------

| See: https://docs.python.org/3/library/turtle.html#turtle.bgpic

| Set a background image (gif file).

.. py:function:: turtle.bgpic(picname=None)
    
    | **picname** - a string, name of a **gif**-file or "nopic", or None; default None
    | Set background image or return the name of current background image.
    | If picname is a filename, set the corresponding image as background. 
    | If picname is "nopic", delete background image, if present. e.g s.bgpic("nopic")
    | If picname is None, return the filename of the current background image.
    | e.g print(s.bgpic(picname=None))
    | When ``s = turtle.Screen()``, ``s.bgpic(...)`` can be used as below.

| The code below sets the gackground image to a gif.

.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgpic("docs/turtle/images/mario.gif")
    s.title("Mario")
    s.setup(width=800, height=600, startx=0, starty=0)

    # turtle drawing to go here

    turtle.done()

----

.. admonition:: Tasks

    1. Modify the code above to use a different gif of your own choice.
    2. Modify the code below to clear the gif while keeping the drawing.

    .. code-block:: python

        import turtle

        s = turtle.Screen()
        s.bgpic("docs/turtle/images/mario.gif")
        s.title("Turtle Screen")
        s.setup(width=800, height=600, startx=0, starty=0)

        # turtle drawing
        t = turtle.Turtle()
        t.speed(10)
        t.color("blue", "red")
        t.pensize(10)
        t.pu()
        t.goto(110, -290)
        t.pd()
        t.begin_fill()
        t.circle(200)
        t.end_fill()

        turtle.done()

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q2

                Modify the code below to clear the gif while keeping the drawing.

                .. code-block:: python

                    import turtle

                    s = turtle.Screen()
                    s.bgpic("docs/turtle/images/mario.gif")
                    s.title("Turtle Screen")
                    s.setup(width=800, height=600, startx=0, starty=0)

                    # turtle drawing
                    t = turtle.Turtle()
                    t.speed(10)
                    t.color("blue", "red")
                    t.pensize(10)
                    t.pu()
                    t.goto(110, -290)
                    t.pd()
                    t.begin_fill()
                    t.circle(200)
                    t.end_fill()

                    s.bgpic("nopic")

                    turtle.done()
                        
----

Clear screen
-----------------------

| See: https://docs.python.org/3/library/turtle.html#turtle.clearscreen

| Clear the screen.

.. py:function:: turtle.clearscreen()

    | Also **turtle.clear()**
    | Delete all drawings and all turtles from the TurtleScreen.
    | Reset the now empty Screen to its initial state: white background, no background image, no event bindings and tracing on.
    | When ``s = turtle.Screen()``, ``s.clearscreen()`` can be used as below.

.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgpic("docs/turtle/images/mario.gif")
    s.title("Turtle Screen")
    s.setup(width=800, height=600, startx=0, starty=0)

    # turtle drawing
    t = turtle.Turtle()
    t.color("#285078", "#a0c8f0")
    t.pensize(5)
    t.fd(300)

    s.clearscreen()

    turtle.done()

----

.. admonition:: Tasks

    1. Suggest a use case for ``s.clearscreen()``.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                ``s.clearscreen()`` could be used to clear the screen between stages in a game that uses a different background and different turtles.

----

Reset screen
-----------------------

| See: https://docs.python.org/3/library/turtle.html#turtle.resetscreen

| Reset all turtles on the Screen.

.. py:function:: turtle.resetscreen()

    | Also **turtle.reset()**
    | Reset all turtles on the Screen to their initial state, clearing their drawings.
    | When ``s = turtle.Screen()``, ``s.resetscreen()`` can be used as below.

.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgpic("docs/turtle/images/mario.gif")
    s.title("Turtle Screen")
    s.setup(width=800, height=600, startx=0, starty=0)

    # turtle drawing
    t = turtle.Turtle()
    t.shapesize(10, 10, 12)
    t.color("blue")
    t.pensize(10)
    t.penup(); t.setpos(-400, -230); t.pendown()
    t.fd(800)

    s.resetscreen()

    # same turtle - new drawing
    t.shapesize(5, 5, 6)
    t.color("red")
    t.pensize(10)
    t.penup(); t.setpos(-400, -255); t.pendown()
    t.fd(800)

    turtle.done()


----

.. admonition:: Tasks

    1. Adjust the code so that only one circle is drawn on the screen at any time.

    .. code-block:: python

        import turtle

        s = turtle.Screen()
        s.bgpic("docs/turtle/images/mario.gif")
        s.title("Turtle Screen")
        s.setup(width=800, height=600, startx=0, starty=0)

        # turtle drawing
        t = turtle.Turtle()
        t.speed(10)
        t.color("blue", "red")
        t.pensize(10)
        t.begin_fill()
        t.circle(120)
        t.end_fill()


        # same turtle - new drawing
        t.color("green", "yellow")
        t.pensize(5)
        t.begin_fill()
        t.circle(50)
        t.end_fill()

        turtle.done()

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Adjust the code so that only one circle is drawn on the screen at any time.

                .. code-block:: python

                    import turtle

                    s = turtle.Screen()
                    s.bgpic("docs/turtle/images/mario.gif")
                    s.title("Turtle Screen")
                    s.setup(width=800, height=600, startx=0, starty=0)

                    # turtle drawing
                    t = turtle.Turtle()
                    t.speed(10)
                    t.color("blue", "red")
                    t.pensize(10)
                    t.begin_fill()
                    t.circle(120)
                    t.end_fill()

                    s.resetscreen()

                    # same turtle - new drawing
                    t.color("green", "yellow")
                    t.pensize(5)
                    t.begin_fill()
                    t.circle(50)
                    t.end_fill()

                    turtle.done()

----

Reset screensize
-----------------------

| See: https://docs.python.org/3/library/turtle.html#turtle.screensize

| Reset the screensize.

.. py:function:: turtle.screensize(canvwidth=None, canvheight=None, bg=None)

    | **canvwidth** - positive integer, new width of canvas in pixels; default None
    | **canvheight** - positive integer, new height of canvas in pixels; default None
    | **bg** - colorstring or color-tuple, new background color; default None
    | If no arguments are given, return current (canvaswidth, canvasheight). 
    | Else, resize the canvas the turtles are drawing on without altering the drawings. 
    | Scrollbars are added, to observe hidden parts of the canvas previously outside the canvas.
    | When ``s = turtle.Screen()``, ``s.screensize(...)`` can be used as below.

| The code line below, ``s.screensize(canvwidth=1200, canvheight=800, bg="yellow")``, creates scrollbars and extends the canvas which is drawn in yellow around the background gif.

.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgpic("docs/turtle/images/mario.gif")
    s.title("Turtle Screen")
    s.setup(width=800, height=600, startx=40, starty=20)

    # turtle drawing
    t = turtle.Turtle()
    t.shapesize(10, 10, 12)
    t.color("blue")
    t.pensize(10)
    t.penup(); t.setpos(-400, -250); t.pendown()
    t.fd(800)

    s.screensize(canvwidth=1200, canvheight=800, bg="yellow")

    # same turtle - new drawing
    t.color("red")
    t.pensize(10)
    t.penup(); t.setpos(-400, -285); t.pendown()
    t.fd(800)

    turtle.done()

----

.. admonition:: Tasks

    1. Replace the screensize line above with ``s.setup(width=1200, height=800, startx=0, starty=0)``. What happens instead?

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Replace the screensize line above with ``s.setup(width=1200, height=800, startx=0, starty=0)``. What happens instead?

                No scroll bars are required as the screen window resizes and repositions to the topleft of the screen.

----

Animation control
-------------------------

| See: https://docs.python.org/3/library/turtle.html#animation-control

| Turn turtle animation on/off and set the delay for update drawings.

.. py:function:: turtle.tracer(n=None, delay=None)
 
    | n - nonnegative integer; higher is faster; 0 to turn off tracing; default None
    | delay - nonnegative integer; default None
    | If n is given, only each n-th regular screen update is really performed. When called without arguments, returns the currently stored value of n. Second argument sets delay value (see delay()).
    | When ``s = turtle.Screen()``, ``s.tracer(0, 0)`` can be used as below.

----

| Set the delay for update drawings.

.. py:function:: turtle.delay(delay=None)
 
    | Set or return the drawing delay in milliseconds. This is approximately the time interval between two consecutive canvas updates.
    | delay - positive integer; default None
    | When ``s = turtle.Screen()``, ``s.delay(1000)`` can be used as below.

----

| Update the screen. Use when tracing has been set to 0 to turn it off. 

.. py:function:: turtle.update()
 
    | Perform a TurtleScreen update. To be used when tracer is turned off.
    | When ``s = turtle.Screen()``, ``s.update()`` can be used as below.

----

| The code below turns off turtle animation and produces the image rapidly.
| Try changing the tracer to ``s.tracer(1, 100)`` to compare.

.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgcolor("white")
    s.title("square")
    s.setup(width=800, height=600, startx=0, starty=0)
    s.tracer(0, 0)

    t = turtle.Turtle()
    t.speed(0)


    def square(t, l=50, x=0, y=0):
        for _ in range(4):
            t.fd(l)
            t.rt(90)


    for i in range(32):
        square(t, l=100)
        t.rt(6)

    s.update()
    s.exitonclick()

----

.. admonition:: Tasks

    1. Add 2 lines of code to display the drawing without animation.

    .. code-block:: python

        import turtle

        s = turtle.Screen()
        s.bgcolor("white")
        s.title("square")
        s.setup(width=800, height=600, startx=0, starty=0)

        t = turtle.Turtle()
        t.pencolor("blue")
        t.speed(0)

        def square(t, side, x=0, y=0):
            for _ in range(4):
                t.fd(side)
                t.rt(90)

        for i in range(60):
            square(t, side=200)
            t.rt(6)

        s.exitonclick()

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Add 2 lines of code to display the drawing without animation.

                .. code-block:: python

                    import turtle

                    s = turtle.Screen()
                    s.bgcolor("white")
                    s.title("square")
                    s.setup(width=800, height=600, startx=0, starty=0)
                    s.tracer(0, 0)

                    t = turtle.Turtle()
                    t.pencolor("blue")
                    t.speed(0)


                    def square(t, side, x=0, y=0):
                        for _ in range(4):
                            t.fd(side)
                            t.rt(90)


                    for i in range(60):
                        square(t, side=200)
                        t.rt(6)

                    s.update()
                    s.exitonclick()

----

Using screen events
-----------------------

| Several other screen events are available.

| listen()
| onkey(); onkeyrelease()
| onkeypress()
| onclick(); onscreenclick()
| ontimer()

| See: https://docs.python.org/3/library/turtle.html#using-screen-events




