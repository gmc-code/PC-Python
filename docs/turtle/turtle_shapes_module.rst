====================================================
Turtle shapes module
====================================================

| The shapes module is designed to be used for making turtle pictures of houses.
| The houses are built from squares, rectangles and triangles.
| To reduce the code in the main file, separate modules are used which group the code together.
| Definitions for the base shapes are placed in a module, ``shapes.py``.
| Definitions for house shapes will be placed in a module, ``houses.py``.

| Download the python file :download:`shapes.py module <files/shapes.py>`

----

Importing the module
-----------------------

| See: https://www.w3schools.com/python/ref_keyword_as.asp
| The code below shows importing the shapes module as an alias via ``import shapes as sh``.
| This makes it shorter to refer to functions in the shapes module.
| Instead of needing ``shapes.rectangle``, only ``sh.rectangle`` is needed.

| The code below imports the shapes module, then draws a light green filled rectangle.

.. code-block:: python

    import turtle
    import shapes as sh

    s = turtle.Screen()
    s.bgcolor("white")
    s.title("rectangle")
    s.setup(width=800, height=600, startx=200, starty=100)

    t = turtle.Turtle()
    sh.rectangle(t, length=200, width=80, start_pos=(0,0), fillc="light green")

    s.exitonclick()

----

Shape module functions
-----------------------

| The syntax of the basic shapes in the shapes module is below.

| When using this, there is no need to include all the parameters that have default values, since this makes them optional.
| e.g. ``square(t, length=100, start_pos=(10, 20), fillc="light green")`` can be used 
| rather than the full ``square(t, length=50, start_pos=(0, 0), start_h=0, penw=1, penc="black", fillc=None)``.

----
Documenting the module
-----------------------

| Documentation in the module follows the standard Google python docs format.

| The first line describes the use of the function.
| The arguments are described under the heading: Args.
| Consider the string: ``length (int, optional): side lengths. Defaults to 50.``
| The name of the argument is followed by its type in brackets along with "optional" if a default value has been given. A short description of the argument follows. Any default values are stated.
| None of the functions below return values, so there is no need for a Return section in the doc strings.

----

Square
----------

| Syntax for the square function.

.. py:function:: square(t, length=50, start_pos=(0, 0), start_h=0, penw=1, penc="black", fillc=None)

    | **t** - the turtle object to draw the square
    | **length** - side length; default 50
    | **start_pos** - start position; default (0, 0)
    | **start_h** - start heading; default 0
    | **penw** - pen size; default 1
    | **penc** - pen color; default "black"
    | **fillc** - fill color; default None


| The code snippet below shows the doc string for the square function.

.. code-block:: python

    def square(t, length=50, start_pos=(0, 0), start_h=0, penw=1, penc="black", fillc=None):
        """draw a square

        Args:
            t (turtle): turtle object
            length (int, optional): side lengths. Defaults to 50.
            start_pos (tuple, optional): start position. Defaults to (0, 0).
            start_h (int, optional): start heading. Defaults to 0.
            penw (int, optional): pen size. Defaults to 1.
            penc (str, optional): pen color. Defaults to "black".
            fillc (str, optional): fill color. Defaults to "red".

        """
----

Rectangle
------------

| Syntax for the rectangle function.


.. py:function:: rectangle(t, length=40, width=30, start_pos=(0, 0), start_h=0, penw=1, penc="black", fillc=None)

    | **t** - the turtle object to draw the rectangle
    | **length** - side length; default 40
    | **width** - side width; default 30
    | **start_pos** - start position; default (0, 0)
    | **start_h** - start heading; default 0 degrees
    | **penw** - pen size; default 1
    | **penc** - pen color; default "black"
    | **fillc** - fill color; default None

.. admonition:: Code Completion: rectangle doc string

    .. tab-set::

        .. tab-item:: Q

            | Complete the doc string for the rectangle function using the template provided.
            | Replace _summary_, _type_, _description_ and _value_ with suitable text.

            .. code-block:: python

                def rectangle(t, length=40, width=30, start_pos=(0, 0), start_h=0, 
                                penw=1, penc="black", fillc=None):
                    """Draw a rectangle

                    Args:
                        t (turtle): turtle instance
                        length (_type_, optional): side lengths. Defaults to _value_.
                        width (_type_, optional): side widtsh. Defaults to _value_.
                        start_pos (_type_, optional): start position. Defaults to _value_.
                        start_h (_type_, optional): start heading. Defaults to _value_.
                        penw (_type_, optional): pen size. Defaults to _value_.
                        penc (str, optional): pen color. Defaults to "black".
                        fillc (str, optional): fill color. Defaults to None.
                    """

        .. tab-item:: Ans

            Completed doc string for the rectangle function.

            .. code-block:: python

                def rectangle(t, length=40, width=30, start_pos=(0, 0), start_h=0, 
                                penw=1, penc="black", fillc=None):
                    """Draw a rectangle

                    Args:
                        t (turtle): turtle instance
                        length (_type_, optional): side lengths. Defaults to _value_.
                        width (_type_, optional): side widtsh. Defaults to _value_.
                        start_pos (_type_, optional): start position. Defaults to _value_.
                        start_h (_type_, optional): start heading. Defaults to _value_.
                        penw (_type_, optional): pen size. Defaults to _value_.
                        penc (str, optional): pen color. Defaults to "black".
                        fillc (str, optional): fill color. Defaults to None.
                    """
----

Scalene
----------

| Syntax for the scalene function.

.. py:function:: scalene(t, side_a, angle_C, side_b, start_pos=(0, 0), start_h=0, penw=1, penc="black", fillc=None)

    | **t** - the turtle object to draw the scalene triangle
    | **side_a** - side length a
    | **angle_C** - angle_C
    | **side_b** - side length b
    | **start_pos** - start position; default (0, 0)
    | **start_h** - start heading; default 0 degrees
    | **penw** - pen size; default 1
    | **penc** - pen color; default "black"
    | **fillc** - fill color; default None

.. admonition:: Code Completion: scalene doc string

    .. tab-set::

        .. tab-item:: Q

            | Complete the doc string for the scalene triangle function using the template provided.
            | Replace _summary_, _type_, _description_ and _value_ with suitable text.

            .. code-block:: python

                def scalene(t, side_a, angle_C, side_b, start_pos=(0, 0), start_h=0, 
                            penw=1, penc="black", fillc=None):
                    """_summary_

                    Args:
                        t (_type_): _description_
                        side_a (_type_): _description_
                        angle_C (_type_): _description_
                        side_b (_type_): _description_
                        start_pos (_type_, optional): start position. Defaults to _value_.
                        start_h (int, optional): _description_. Defaults to 0.
                        penw (int, optional): _description_. Defaults to 1.
                        penc (str, optional): _description_. Defaults to "black".
                        fillc (_type_, optional): _description_. Defaults to None.
                        """

        .. tab-item:: Ans

            Completed doc string for the scalene triangle function using the template provided.

            .. code-block:: python

                def scalene(t, side_a, angle_C, side_b, start_pos=(0, 0), start_h=0, 
                            penw=1, penc="black", fillc=None):
                    """Draw a scalene triangle given SAS (side angle side).

                    Args:
                        t (class turtle.Turtle): turtle instance.
                        side_a (int): side length before angle.
                        angle_C (int): angle between 2 sides.
                        side_b (int): side length after angle.
                        start_pos (tuple, optional): start position. Defaults to (0, 0).
                        start_h (int, optional): start heading. Defaults to 0.
                        penw (int, optional): pen size. Defaults to 1.
                        penc (str, optional): pen color. Defaults to "black".
                        fillc (str, optional): fill color. Defaults to None.
                    """

----

Isosceles
----------

| Syntax for the isosceles function.

.. py:function:: isosceles(t, base, height, start_pos=(0, 0), start_h=0, penw=1, penc="black", fillc=None)

    | **t** - the turtle object to draw the isosceles triangle
    | **base** - base length
    | **height** - height
    | **start_pos** - start position; default (0, 0)
    | **start_h** - start heading; default 0 degrees
    | **penw** - pen size; default 1
    | **penc** - pen color; default "black"
    | **fillc** - fill color; default None

.. admonition:: Code Completion: isosceles doc string

    .. tab-set::

        .. tab-item:: Q

            | Complete the doc string for the isosceles triangle function using the template provided.
            | Replace _summary_, _type_, _description_ and _value_ with suitable text.

            .. code-block:: python

                def isosceles(t, base, height, start_pos=(0, 0), start_h=0, 
                                penw=1, penc="black", fillc=None):
                    """_summary_

                    Args:
                        t (_type_): _description_
                        base (_type_): _description_
                        height (_type_): _description_
                        start_pos (_type_, optional): start position. Defaults to _value_.
                        start_h (int, optional): _description_. Defaults to 0.
                        penw (int, optional): _description_. Defaults to 1.
                        penc (str, optional): _description_. Defaults to "black".
                        fillc (_type_, optional): _description_. Defaults to None.
                    """

        .. tab-item:: Ans

            Completed doc string for the iscosceles triangle function.

            .. code-block:: python

                def isosceles(t, base, height, start_pos=(0, 0), start_h=0, 
                                penw=1, penc="black", fillc=None):
                    """Draw an isosceles triangle given base and height.

                    Args:
                        t (class turtle.Turtle): turtle instance.
                        base (int): base of triangle.
                        height (int): height of triangle.
                        start_pos (tuple, optional): start position. Defaults to (0, 0).
                        start_h (int, optional): start heading. Defaults to 0.
                        penw (int, optional): pen size. Defaults to 1.
                        penc (str, optional): pen color. Defaults to "black".
                        fillc (str, optional): fill color. Defaults to None.
                    """

----

Equilateral
----------

| Syntax for the equilateral function.

.. py:function:: equilateral(t, side, start_pos=(0, 0), start_h=0, penw=1, penc="black", fillc=None)

    | **t** - the turtle object to draw the equilateral triangle
    | **side** - side length
    | **start_pos** - start position; default (0, 0)
    | **start_h** - start heading; default 0 degrees
    | **penw** - pen size; default 1
    | **penc** - pen color; default "black"
    | **fillc** - fill color; default None


.. admonition:: Code Completion: equilateral doc string

    .. tab-set::

        .. tab-item:: Q

            | Complete the doc string for the equilateral triangle function using the template provided.
            | Replace _summary_, _type_, _description_ and _value_ with suitable text.

            .. code-block:: python

                def equilateral(t, side, start_pos=(0, 0), start_h=0, 
                                penw=1, penc="black", fillc=None):
                    """_summary_

                    Args:
                        t (_type_): _description_
                        side (_type_): _description_
                        start_pos (_type_, optional): start position. Defaults to _value_.
                        start_h (int, optional): _description_. Defaults to 0.
                        penw (int, optional): _description_. Defaults to 1.
                        penc (str, optional): _description_. Defaults to "black".
                        fillc (_type_, optional): _description_. Defaults to None.
                    """

        .. tab-item:: Ans

            Completed doc string for the equilateral triangle function.

            .. code-block:: python

                def equilateral(t, side, start_pos=(0, 0), start_h=0, 
                                penw=1, penc="black", fillc=None):
                    """Draw an equilateral triangle

                    Args:
                        t (class turtle.Turtle): turtle instance.
                        side (int): side lengths.
                        start_pos (tuple, optional): start position. Defaults to (0, 0).
                        start_h (int, optional): start heading. Defaults to 0.
                        penw (int, optional): pen size. Defaults to 1.
                        penc (str, optional): pen color. Defaults to "black".
                        fillc (str, optional): fill color. Defaults to None.
                    """               
