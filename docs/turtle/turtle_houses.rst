====================================================
Turtle houses
====================================================

| The houses will be built from squares, rectangles and triangles.
| To reduce the code in the main file, definitions for the base shapes will be placed in a module which will need to be imported.

----

Simple houses
------------------

| Write a definition that produces a house of given length, height and position.
| Use the functions from the houses.py module.
| Use the function to make several houses as shown below.

.. image:: images/simple_houses1.png
    :scale: 40 %
    :align: center
    :alt: simple_houses1


.. py:function:: def simple_house(t, length=60, height=40, start_pos=(0, 0))

    | **t** - the turtle object to draw the rectangle
    | **length** - the length of the house; default 60
    | **height** - the height of the house (not including the roof); default 40
    | **start_pos** - start position in bottom left of house; default (0, 0)

| Starter code is provided with ``?`` where the code has to be completed.

.. code-block:: python

    import turtle
    import math
    import houses as h

    s = turtle.Screen()
    s.bgcolor("white")
    s.title("Grid")
    s.setup(width=800, height=600, startx=200, starty=100)
    s.tracer(0, 0)

    t = turtle.Turtle()
    t.speed(0)

    def door_pos(start_pos, length):
        return (start_pos[0] + ?, start_pos[1])

    def roof_pos(start_pos, length, height):
        return (start_pos[0] -?, start_pos[1] + ?)

    def simple_house(t, length=60, height=40, start_pos=(0, 0)):
        # main house
        h.rectangle(t, length=length, width=height, start_pos=start_pos, fillc="snow")
        # door
        h.rectangle(t, length=?, width=?, start_pos=door_pos(?), fillc="green")
        # roof
        h.isosceles(t, base=?, height=?, start_pos=roof_pos(?), fillc="brown")

    simple_house(t, length=210, height=160, start_pos=(-200, 20))
    simple_house(t, length=150, height=120, start_pos=(200, 20))
    simple_house(t, length=60, height=40, start_pos=(-100, 0))
    simple_house(t, length=80, height=50, start_pos=(-10, 0))
    simple_house(t, length=120, height=100, start_pos=(90, 0))
    simple_house(t, length=210, height=160, start_pos=(-390, 0))


    t.ht()
    turtle.update()
    s.exitonclick()


