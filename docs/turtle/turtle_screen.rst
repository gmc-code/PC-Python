====================================================
Turtle screen
====================================================

| The code below shows code to set up a window for a turtle to draw in.
| The use of each line is detailed below.

.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgcolor("black")
    s.title("Turtle Screen")
    s.setup (width=800, height=600, startx=0, starty=0)

    # turtle drawing to go here

    turtle.done()


----

Screen class
--------------

| Start by importing the inbuilt turtle library.
| Then set up the screen for drawing on.

See: https://docs.python.org/3/library/turtle.html#turtle.Screen

| The class Screen() defines graphics windows as a playground for the drawing turtles. This function should be used when turtle is used as a standalone tool for doing graphics.


.. code-block:: python

    import turtle

    s = turtle.Screen()

----

Screen colours
-----------------

| Set the screen color.

See: https://docs.python.org/3/library/turtle.html#turtle.bgcolor
See: https://docs.python.org/3/library/turtle.html#turtle.colormode

.. py:function:: turtle.colormode(cmode=None)

    | cmode - one of the values 1.0 or 255.
    | The default config starts with a cmode of 1.0


.. py:function:: turtle.bgcolor(*args)

    | args - a color string or three numbers in the range 0..colormode or a 3-tuple of such numbers.
    | Color stings can be a named color such as "orange" or a hex color such as "#800080".
    | If colormode is 1, a colour is a rgb tuple such as (0.2, 0.8, 0.55),
    | If colormode is 255, a colour is a rgb tuple such as (50, 193, 143)

.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgcolor("black")

| s.bgcolor(color)
| s.title(string) show the string in the titlebar of the turtle graphics window

----

Screen title
-----------------

| Set the screen title.

See: https://docs.python.org/3/library/turtle.html#turtle.title

.. py:function:: turtle.title(titlestring)

    | titlestring - a string that is shown in the titlebar of the turtle graphics window

.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgcolor("black")
    s.title("Turtle Screen")

----

Screen size and position
----------------------------

| Set the screen size and position.

See: https://docs.python.org/3/library/turtle.html#turtle.setup

.. py:function:: turtle.setup(width=0.5, height=0.75, startx=None, starty=None)

    | Set the size and position of the main window.
    | width - if an integer, a size in pixels; if a float, a fraction of the screen
    | height - if an integer, the height in pixels; if a float, a fraction of the screen
    | startx - if positive, starting position in pixels from the left edge of the screen; if negative from the right edge, if None, center window horizontally
    | starty - if positive, starting position in pixels from the top edge of the screen; if negative from the bottom edge, if None, center window vertically
    | Default values are: width = 0.5; height = 0.75; startx = None; starty = None


.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgcolor("black")
    s.title("Turtle Screen")
    s.setup(width=800, height=600, startx=None, starty=None)

----

Screen setup
-----------------

| Set the screen size and position.

See: https://docs.python.org/3/library/turtle.html#turtle.setup

.. py:function:: turtle.setup(width=0.5, height=0.75, startx=None, starty=None)

    | Set the size and position of the main window.

----

Using screen events
----------------------------------------

See: https://docs.python.org/3/library/turtle.html#turtle.mainloop


| Use turtle.mainloop() or turtle.done() to keep the window open.
| When used, it must be the last statement in the file.

.. code-block:: python

    import turtle

    s = turtle.Screen()
    # s.bgcolor("black")
    s.bgpic("spiro_d.gif")
    s.title("Turtle Screen")
    s.setup (width=600, height=400, startx=0, starty=0)
    s.tracer(10, 0)

    # turtle drawing to go here

    turtle.done()

