====================================================
Introduction to turtle
====================================================

| Turtles are objects that can be directed to move about on a screen.
| The turtle can draw on the screen as it moves.

| This section begins with some basic syntax for the screen and turtles.
| Basic shapes, squares, rectangles and triangles, are drawn via **sequencing**, **iteration** and **definitions**.
| The houses section puts together **modules** that group similar code together.
| Module code is **documented** using a standard documentation layout.

----

turtle documentation
----------------------------------------

| Docs: https://docs.python.org/3.11/library/turtle.html#module-turtle
| See the docs for a full listing of methods.

----

Tutorial
--------------

| Tutorial: https://www.geeksforgeeks.org/python-turtle-tutorial/
| This has a large number of examples for specific syntax.
----

Academy
--------------

| Academy: https://pythonturtle.academy/
| Excellent, extensive challenges from easy to very hard, with images of what to make, with some sample code.

----

turtle uses tkinter
----------------------

| The turtle module uses tkinter for the underlying graphics.
| Some of the methods have dual use depending on whether arguments are passed or not.
| e.g s.bgcolor("black") sets the screen colour, while s.bgcolor() returns "black".

----

Import turtle
---------------

| Import the turtle library.

.. code-block:: python

    import turtle

----

Screen and turtles
-------------------------

| For standalone usage, not within a tkinter based script, there are 2 classes used to set up the screen and to set up a turtle to draw with.
| ``screen = turtle.Screen()`` sets up the window to draw in.
| ``turtle = turtle.Turtle()`` sets up a turtle to draw with.

.. code-block:: python

    import turtle

    screen = turtle.Screen()
    turtle = turtle.Turtle()

----

| In the sample code, the **screen** object is shortened to **s**. ``s = turtle.Screen()``
| In the sample code, the **turtle** object is shortened to **t**. ``t = turtle.Turtle()``
| Shortening object variables makes method calls on these objects shorter to type and read.
| e.g. ``s.bgcolor("black")`` instead of ``screen.bgcolor("black")``
| e.g. ``t.pendown()`` instead of ``turtle.pendown()``


.. code-block:: python

    import turtle

    s = turtle.Screen()
    t = turtle.Turtle()
