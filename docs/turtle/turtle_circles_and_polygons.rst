====================================================
Turtle circles and polygons
====================================================

| The code below draws circles, parts of circles and regular polygons.

----


Turtle Circles
------------------------------------------

| The turtle syntax for drawing circles in below:

.. py:function:: turtle.circle(radius, extent=None, steps=None)

    | radius - radius; a positive number draws anticlockwise, a negative number draws clockwise. 
    | extent - an angle; a number (or None for whole circle), which determines how many degrees of the circle is drawn.
    | steps - an integer (or None for a circle) which allows polygons to be drawn.

| The center is radius units left of the turtle at right angles from its heading if the radius is positive.
| The direction of the turtle is changed by the amount of extent.
| The pensize increases the circle line inwards and outwards from the radius distance. So a pensize of 41 draws the circle 20 pixels inwards and 20 pixels outwards from the exact radius position. This is important for predicting circle edges with large pensizes. 

----

Circles at a specified location
------------------------------------------

| Adding a starting position, the centre of the circle, will provide some convenience.
| The ``draw_centered_circle`` syntax is below:

.. py:function:: draw_centered_circle(t, centre=(0, 0), size=20, color="blue", penw=1, penc="black", fillc=None)

    | **t** - the turtle object to draw the rectangle
    | **centre** - start position; default (0, 0)
    | **size** - the dot diameter, an integer >= 1 (if given)
    | **color** - a colorstring or a numeric color tuple (r, g, b,)

| The ``draw_centered_circle`` definition code is below.

