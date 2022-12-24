====================================================
Turtle houses module
====================================================

| The houses are built from squares, rectangles and triangles.
| To reduce the code in the main file, separate modules are used which group the code together.
| Definitions for the base shapes, squares, rectangles and triangles, are placed in a module, ``shapes.py``.
| Definitions for house shapes will be placed in a module, ``houses.py``.

| Download the python file :download:`shapes.py module <files/shapes.py>`
| Create the module, ``houses.py``, by following the steps below to build a basic house shape by combining together various shapes from the shapes module.

.. image:: images/house_measurements.png
    :scale: 40 %
    :align: center
    :alt: simple_houses1


----

Importing the shapes module
----------------------------------

| See: https: // www.w3schools.com/python/ref_keyword_as.asp
| The code below shows importing the shapes module as an alias via ``import shapes as sh``.
| This makes it shorter to refer to functions in the shapes module.
| Instead of needing ``shapes.rectangle``, only ``sh.rectangle`` is needed.

.. code-block:: python

    import turtle
    import shapes as sh

----

Simple houses
------------------

| Write a definition that produces a house of given length, height and position.
| Use the functions from the ``shapes.py`` module.
| Use the function to make several houses as shown below.

.. image:: images/simple_houses1.png
    :scale: 40 %
    :align: center
    :alt: simple_houses1


.. py:function:: simple_house(t, hlength=60, hheight=40, hstart_pos=(0, 0))

    | **t** - the turtle object to draw the rectangle
    | **hlength** - the length of the house; default 60
    | **hheight** - the height of the house (not including the roof); default 40
    | **hstart_pos** - start position in bottom left of house; default (0, 0)




.. admonition:: Code Completion

    .. tab-set::

        .. tab-item:: Q

            | Complete the code to build a series of houses.
            | Starter code is provided with ``XXX`` where the code has to be completed.

            .. code-block:: python

                import turtle
                import shapes as sh

                s = turtle.Screen()
                s.bgcolor("white")
                s.title("Grid")
                s.setup(width=800, height=600, startx=200, starty=100)
                s.tracer(0, 0)

                t = turtle.Turtle()
                t.speed(0)


                def house_door(t, h_length, h_height, h_start_pos):
                    """draw door 1/3 along length of house, 1/5 of length of house, 1/1.6 of height of house
                    """
                    d_pos = (h_start_pos[0] + h_length//3, h_start_pos[1])
                    d_height = h_height//1.6
                    d_length = h_length//5
                    sh.rectangle(t, length=d_length, width=d_height, start_pos=d_pos, penw=1, penc="black", fillc="green")


                def house_roof(t, h_length, h_height, h_start_pos):
                    """draw roof with overhang of 5 pixels over left side and right side of house
                    """
                    r_pos = (h_start_pos[0] - 5, h_start_pos[1] + h_height)
                    r_height = h_length//3
                    r_length = h_length + 10
                    sh.isosceles(t, base=r_length, height=r_height, start_pos=r_pos, penw=1, penc="black", fillc="brown")


                def simple_house(t, h_length=60, h_height=40, h_start_pos=(0, 0)):
                    # main house
                    sh.rectangle(t, length=h_length, width=h_height, start_pos=h_start_pos, penw=1, penc="black", fillc="snow")
                    # door
                    house_door(t, h_length, h_height, h_start_pos)
                    # roof
                    house_roof(t, h_length, h_height, h_start_pos)


                simple_house(t, h_length=210, h_height=160, h_start_pos=(-200, 20))
                simple_house(t, h_length=150, h_height=120, h_start_pos=(200, 20))
                simple_house(t, h_length=60, h_height=40, h_start_pos=(-100, 0))
                simple_house(t, h_length=80, h_height=50, h_start_pos=(-10, 0))
                simple_house(t, h_length=120, h_height=100, h_start_pos=(90, 0))
                simple_house(t, h_length=210, h_height=160, h_start_pos=(-390, 0))

                t.ht()
                s.update()
                s.exitonclick()

        .. tab-item:: Ans

            Completed code to build a series of houses.

            .. code-block:: python

                import turtle
                import shapes as sh

                s = turtle.Screen()
                s.bgcolor("white")
                s.title("Grid")
                s.setup(width=800, height=600, startx=200, starty=100)
                s.tracer(0, 0)

                t = turtle.Turtle()
                t.speed(0)


                def house_door(t, h_length, h_height, h_start_pos):
                    """draw door 1/3 along length of house, 1/5 of length of house, 1/1.6 of height of house
                    """
                    d_pos = (h_start_pos[0] + h_length//3, h_start_pos[1])
                    d_height = h_height//1.6
                    d_length = h_length//5
                    sh.rectangle(t, length=d_length, width=d_height, start_pos=d_pos, penw=1, penc="black", fillc="green")


                def house_roof(t, h_length, h_height, h_start_pos):
                    """draw roof with overhang of 5 pixels over left side and right side of house
                    """
                    r_pos = (h_start_pos[0] - 5, h_start_pos[1] + h_height)
                    r_height = h_length//3
                    r_length = h_length + 10
                    sh.isosceles(t, base=r_length, height=r_height, start_pos=r_pos, penw=1, penc="black", fillc="brown")


                def simple_house(t, h_length=60, h_height=40, h_start_pos=(0, 0)):
                    # main house
                    sh.rectangle(t, length=h_length, width=h_height, start_pos=h_start_pos, penw=1, penc="black", fillc="snow")
                    # door
                    house_door(t, h_length, h_height, h_start_pos)
                    # roof
                    house_roof(t, h_length, h_height, h_start_pos)


                simple_house(t, h_length=210, h_height=160, h_start_pos=(-200, 20))
                simple_house(t, h_length=150, h_height=120, h_start_pos=(200, 20))
                simple_house(t, h_length=60, h_height=40, h_start_pos=(-100, 0))
                simple_house(t, h_length=80, h_height=50, h_start_pos=(-10, 0))
                simple_house(t, h_length=120, h_height=100, h_start_pos=(90, 0))
                simple_house(t, h_length=210, h_height=160, h_start_pos=(-390, 0))

                t.ht()
                s.update()
                s.exitonclick()

----

windows
---------------------

| Write a definition, ``window(t, length=10, start_pos=(0, 0))``, that produces a 4 pane square window given the window length and start position.
| Combine 4 squares to make the 4 pane square window.
| Write a helper function, ``window_pos(start_pos, x_add, y_add)``, to get the bottom left coordinates of each square.
| The module syntax is ``square(t, length=50, start_pos=(0, 0), start_h=0, penw=1, penc="black", fillc=None)``.
| Some default arguments, ``start_h=0, penw=1, penc="black"``, can be left out for convenience in the code below.


.. image:: images/window.png
    :scale: 100 %
    :align: center
    :alt: window


.. py:function:: window(t, length=10, start_pos=(0, 0))

    | **t** - the turtle object to draw the rectangle
    | **length** - the length of the window; default 10
    | **start_pos** - start position in bottom left of the window; default (0, 0)


| Starter code is provided with ``XXX`` where the code has to be completed.

.. code-block:: python

    import turtle
    import houses as h

    s = turtle.Screen()
    s.bgcolor("white")
    s.title("Grid")
    s.setup(width=800, height=600, startx=200, starty=100)
    s.tracer(0, 0)

    t = turtle.Turtle()
    t.speed(0)
        

    def window_pos(start_pos, x_add, y_add):
        return (start_pos[0] + XXX, start_pos[1] + XXX)


    def window(t, length=10, start_pos=(0, 0)):
        h.square(t, length=length/2, start_pos=start_pos, fillc="light blue")
        h.square(t, length=length/2, start_pos=window_pos(XXX), fillc="light blue")
        h.square(t, length=length/2, start_pos=window_pos(XXX), fillc="light blue")
        h.square(t, length=length/2, start_pos=window_pos(XXX), fillc="light blue")


    t.ht()
    s.update()
    s.exitonclick()

----

Houses with windows
---------------------

