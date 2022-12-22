====================================================
Turtle houses module
====================================================

| The houses will be built from squares, rectangles and triangles.
| To reduce the code in the main file, defintions for the base shapes will be placed in a module which will need to be imported.

----

Documenting the module
-----------------------

| Documentation in the module follows the standard Google python docs format.
| The code snippet below shows the doc string for the square function.

| The first line describes the use of the function.
| The arguments are decribed under the heading: Args.
| Consider the string: ``length (int, optional): side length. Defaults to 50.``
| The name of the argument is followed by its type in brackets along with "optional" if a default value has been given. A short description of the argument follows. Any default values are stated.

.. code-block:: python

    def square(t, length=50, start_pos=(0, 0), start_h=0, penw=1, penc="blue", fillc=None):
        """draw a square

        Args:
            t (turtle): turtle object
            length (int, optional): side length. Defaults to 50.
            start_pos (tuple, optional): start position. Defaults to (0, 0).
            start_h (int, optional): initial heading. Defaults to 0.
            penw (int, optional): pensize. Defaults to 1.
            penc (str, optional): pencolor. Defaults to "blue".
            fillc (str, optional): fillcolor. Defaults to "red".

        """

----

.. admonition:: Tasks

    1. Complete the doc string for the rectangle function using the template provided.

        .. code-block:: python

            def rectangle(t, length=40, width=30, start_pos=(0, 0), start_h=0, penw=1, penc="blue", fillc=None):
                """Draw a rectangle

                Args:
                    t (turtle): turtle instance
                    length (_type_, optional): side length. Defaults to _value_.
                    width (_type_, optional): side width. Defaults to _value_.
                    start_pos (_type_, optional): start position. Defaults to _value_.
                    start_h (_type_, optional): initial heading. Defaults to _value_.
                    penw (_type_, optional): pensize. Defaults to _value_.
                    penc (str, optional): pencolor. Defaults to "blue".
                    fillc (str, optional): fillcolor. Defaults to None.
                """

    2. Complete the doc string for the scalene triangle function using the template provided.

        .. code-block:: python

            def scalene(t, side_a, angle_C, side_b, start_pos, start_h=0, penw=1, penc="blue", fillc=None):
                """_summary_

                Args:
                    t (_type_): _description_
                    side_a (_type_): _description_
                    angle_C (_type_): _description_
                    side_b (_type_): _description_
                    start_pos (_type_): _description_
                    start_h (int, optional): _description_. Defaults to 0.
                    penw (int, optional): _description_. Defaults to 1.
                    penc (str, optional): _description_. Defaults to "blue".
                    fillc (_type_, optional): _description_. Defaults to None.
                """

    3. Complete the doc string for the isosceles triangle function using the template provided.

        .. code-block:: python

            def isosceles(t, base, height, start_pos, start_h=0, penw=1, penc="blue", fillc=None):
                """_summary_

                Args:
                    t (_type_): _description_
                    base (_type_): _description_
                    height (_type_): _description_
                    start_pos (_type_): _description_
                    start_h (int, optional): _description_. Defaults to 0.
                    penw (int, optional): _description_. Defaults to 1.
                    penc (str, optional): _description_. Defaults to "blue".
                    fillc (_type_, optional): _description_. Defaults to None.
                """

    4. Complete the doc string for the equilateral triangle function using the template provided.

        .. code-block:: python

            def equilateral(t, side, start_pos, start_h=0, penw=1, penc="blue", fillc=None):
                """_summary_

                Args:
                    t (_type_): _description_
                    side (_type_): _description_
                    start_pos (_type_): _description_
                    start_h (int, optional): _description_. Defaults to 0.
                    penw (int, optional): _description_. Defaults to 1.
                    penc (str, optional): _description_. Defaults to "blue".
                    fillc (_type_, optional): _description_. Defaults to None.
                """

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Complete the doc string for the rectangle function using the template provided.

                    .. code-block:: python

                        def rectangle(t, length=40, width=30, start_pos=(0, 0), start_h=0, penw=1, penc="blue", fillc=None):
                            """Draw a rectangle

                            Args:
                                t (turtle): turtle instance
                                length (int, optional): side length. Defaults to 40.
                                width (int, optional): side width. Defaults to 30.
                                start_pos (tuple, optional): start position. Defaults to (0, 0).
                                start_h (int, optional): initial heading. Defaults to 0.
                                penw (int, optional): pensize. Defaults to 1.
                                penc (str, optional): pencolor. Defaults to "blue".
                                fillc (_type_, optional): fillcolor. Defaults to None.
                            """

                .. tab-item:: Q2

                    Complete the doc string for the scalene triangle function using the template provided.

                    .. code-block:: python

                        def scalene(t, side_a, angle_C, side_b, start_pos, start_h=0, penw=1, penc="blue", fillc=None):
                            """_summary_

                            Args:
                                t (_type_): _description_
                                side_a (_type_): _description_
                                angle_C (_type_): _description_
                                side_b (_type_): _description_
                                start_pos (_type_): _description_
                                start_h (int, optional): _description_. Defaults to 0.
                                penw (int, optional): _description_. Defaults to 1.
                                penc (str, optional): _description_. Defaults to "blue".
                                fillc (_type_, optional): _description_. Defaults to None.
                            """

                .. tab-item:: Q3

                    Complete the doc string for the iscosceles triangle function using the template provided.

                    .. code-block:: python

                        def isosceles(t, base, height, start_pos, start_h=0, penw=1, penc="blue", fillc=None):
                            """_summary_

                            Args:
                                t (_type_): _description_
                                base (_type_): _description_
                                height (_type_): _description_
                                start_pos (_type_): _description_
                                start_h (int, optional): _description_. Defaults to 0.
                                penw (int, optional): _description_. Defaults to 1.
                                penc (str, optional): _description_. Defaults to "blue".
                                fillc (_type_, optional): _description_. Defaults to None.
                            """

                .. tab-item:: Q4

                    Complete the doc string for the equilateral triangle function using the template provided.

                    .. code-block:: python

                        def equilateral(t, side, start_pos, start_h=0, penw=1, penc="blue", fillc=None):
                            """_summary_

                            Args:
                                t (_type_): _description_
                                side (_type_): _description_
                                start_pos (_type_): _description_
                                start_h (int, optional): _description_. Defaults to 0.
                                penw (int, optional): _description_. Defaults to 1.
                                penc (str, optional): _description_. Defaults to "blue".
                                fillc (_type_, optional): _description_. Defaults to None.
                            """


