====================================================
Turtle screen advanced
====================================================

| The code below shows more code options for Turtle scrrens.

----

Screen background gif
-----------------------

See: https://docs.python.org/3/library/turtle.html#turtle.bgpic


.. py:function:: turtle.bgpic(picname=None)
    
    | picname - a string, name of a gif-file or "nopic", or None
    | Set background image or return the name of current background image.
    | If picname is a filename, set the corresponding image as background. 
    | If picname is "nopic", delete background image, if present. 
    | If picname is None, return the filename of the current background image.

| The code belwo sets the gackground image to a gif.

.. code-block:: python

    import turtle

    s = turtle.Screen()
    s.bgpic("docs/turtle/images/mario.gif")
    s.title("Mario")
    s.setup (width=800, height=600, startx=0, starty=0)

    # turtle drawing to go here

    turtle.done()


----

Clear screen
-----------------------

See: https://docs.python.org/3/library/turtle.html#turtle.clearscreen

    resetscreen = reset
    clearscreen = clear

.. py:function:: turtle.clearscreen()

    | Also clear()
    | Delete all drawings and all turtles from the TurtleScreen.
    | Reset the now empty Screen to its initial state: white background, no background image, no event bindings and tracing on.


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

Reset screen
-----------------------

See: https://docs.python.org/3/library/turtle.html#turtle.resetscreen

.. py:function:: turtle.resetscreen()

    | Also reset()
    | Reset all Turtles on the Screen to their initial state, clearing their drawings.

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
    t.penup(); t.setpos(-400, -250); t.pendown()
    t.fd(800)

    s.resetscreen()

    # same turtle - new drawing
    t.color("red")
    t.pensize(10)
    t.penup(); t.setpos(-400, -285); t.pendown()
    t.fd(800)


    turtle.done()


----

Reset screensize
-----------------------

See: https://docs.python.org/3/library/turtle.html#turtle.screensize

.. py:function:: turtle.screensize(canvwidth=None, canvheight=None, bg=None)

    | canvwidth - positive integer, new width of canvas in pixels
    | canvheight - positive integer, new height of canvas in pixels
    | bg - colorstring or color-tuple, new background color
    | If no arguments are given, return current (canvaswidth, canvasheight). 
    | Else resize the canvas the turtles are drawing on. Do not alter the drawing window. 
    | To observe hidden parts of the canvas previously outside the canvas, use the scrollbars.

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
    t.penup(); t.setpos(-400, -250); t.pendown()
    t.fd(800)

    s.resetscreen()

    # same turtle - new drawing
    t.color("red")
    t.pensize(10)
    t.penup(); t.setpos(-400, -285); t.pendown()
    t.fd(800)


    turtle.done()



