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

| Setup the screen for drawing in.
| Start by importing the inbuilt turtle library.

See: https://docs.python.org/3/library/turtle.html#turtle.Screen

| The class **Screen()** defines graphics windows as a playground for the drawing turtles. 
| This function should be used when turtle is used as a standalone tool for doing graphics.
| The last line, ``turtle.done()``, has been included here so the window stays open.

.. code-block:: python

    import turtle

    s = turtle.Screen()

    # turtle drawing to go here

    turtle.done()

----

Screen colours
-----------------

| Set the screen color mode.
| If colormode is 1, a colour as a rgb tuple is written with values form 0 to 1, such as (0.2, 0.8, 0.55),
| If colormode is 255, a colour as a rgb tuple is written with values form 0 to 255, such as (50, 193, 143)

| See: https://docs.python.org/3/library/turtle.html#turtle.bgcolor
| See: https://docs.python.org/3/library/turtle.html#turtle.colormode

.. py:function:: turtle.colormode(cmode=None)

    | **cmode** - one of the values 1.0 or 255.
    | The default config starts with a cmode of 1.0


| Set the screen color.

.. py:function:: turtle.bgcolor(*args)

    | **args** - a color string or three numbers in the range 0 to colormode or a 3-tuple of such numbers.
    | Color stings can be a named color such as "orange" or a hex color such as "#800080".
    | If colormode is 1, a colour is a rgb tuple such as (0.2, 0.8, 0.55),
    | If colormode is 255, a colour is a rgb tuple such as (50, 193, 143)

.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgcolor("black")

    # turtle drawing to go here

    turtle.done()


| Change the colormode to 255, so that the background can be set using the rgb tuple (50, 193, 143).

.. code-block:: python

    import turtle

    s = turtle.Screen()
    turtle.colormode(cmode=255)
    s.bgcolor((50, 193, 143))

    # turtle drawing to go here

    turtle.done()

----

.. admonition:: Tasks

    1. Modify the code above to draw a yellow background.
    2. Draw a cyan background using rgb value of (0, 255, 255).

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the code above to draw a yellow background.

                    .. code-block:: python

                        import turtle

                        s = turtle.Screen()
                        s.bgcolor("yellow")

                        # turtle drawing to go here

                        turtle.done()

                .. tab-item:: Q2

                    Draw a cyan background using rgb value of (0, 255, 255).

                    .. code-block:: python

                        import turtle

                        s = turtle.Screen()
                        turtle.colormode(cmode=255)
                        s.bgcolor((0, 255, 255))

                        # turtle drawing to go here

                        turtle.done()
----

Screen title
-----------------

| Set the screen title.

See: https://docs.python.org/3/library/turtle.html#turtle.title

.. py:function:: turtle.title(titlestring)

    | **titlestring** - a string that is shown in the titlebar of the turtle graphics window

.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgcolor("black")
    s.title("Turtle Screen")

    # turtle drawing to go here

    turtle.done()

----

.. admonition:: Tasks

    1. Modify the code above to create the screen title "Turtle Race".

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the code above to create the screen title "Turtle Race".

                    .. code-block:: python

                        import turtle

                        s = turtle.Screen()
                        s.bgcolor("black")
                        s.title("Turtle Screen")

                        # turtle drawing to go here

                        turtle.done()

----

Screen size and position
----------------------------

| Set the screen size and position.

See: https://docs.python.org/3/library/turtle.html#turtle.setup

.. py:function:: turtle.setup(width=0.5, height=0.75, startx=None, starty=None)

    | Set the size and position of the main window.
    | **width** - if an integer, a size in pixels; if a float, a fraction of the screen
    | **height** - if an integer, the height in pixels; if a float, a fraction of the screen
    | **startx** - if positive, starting position in pixels from the left edge of the screen; if negative from the right edge, if None, center window horizontally
    | **starty** - if positive, starting position in pixels from the top edge of the screen; if negative from the bottom edge, if None, center window vertically
    | Default values are: width = 0.5; height = 0.75; startx = None; starty = None


.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgcolor("black")
    s.title("Turtle Screen")
    s.setup(width=800, height=600, startx=None, starty=None)

    # turtle drawing to go here

    turtle.done()

----

.. admonition:: Tasks

    1. Modify the code above to have a screen of 600 by 400, with the left edge 40 pixels from the screen edge and the top edge at the top of the screen.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the code above to have a screen of 600 by 400, with the left edge 40 pixels from the screen edge and the top edge at the top of the screen.

                    .. code-block:: python

                        import turtle

                        s = turtle.Screen()
                        s.bgcolor("black")
                        s.title("Turtle Screen")
                        s.setup(width=600, height=400, startx=40, starty=0)

                        # turtle drawing to go here

                        turtle.done()

----

Using screen events
----------------------------------------

See: https://docs.python.org/3/library/turtle.html#turtle.mainloop


| Use **turtle.mainloop()** or **turtle.done()** to keep the window open.
| When used, it must be the last statement in the file.
| The close icon must be clicked to close the window.

.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgcolor("black")
    s.title("Turtle Screen")
    s.setup (width=800, height=600, startx=0, starty=0)

    # turtle drawing to go here

    turtle.done()

----

Exit on click
-----------------------

| Close the Turtle window when the mouse is clicked.
| Use **turtle.exitonclick()** instead of **turtle.done()**

| See: https://docs.python.org/3/library/turtle.html#turtle.exitonclick

.. py:function:: turtle.exitonclick()

    | Also **turtle.bye()**
    | Shut the turtle graphics window when the mouse is clicked on the Screen.


.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgcolor("black")
    s.title("Turtle Screen")
    s.setup (width=800, height=600, startx=0, starty=0)

    # turtle drawing to go here

    s.exitonclick()
    # turtle.done()


