==========================
Variables
==========================

| A variable is a name used to refer to a memory location where a value is stored. 
| It can be thought of as a box that stores data. 
| In Python, the same variable can be reused to store values of any type.
| e.g In ``rectangle_length = 2.3``, the variable names is ``rectangle_length``, the type is ``float`` (decimal) and the value is ``2.3``.
| e.g In ``user_name = Annie``, the variable names is ``user_name``, the type is ``str`` (string) and the value is ``Annie``.

Rules for Python variable names:
    • A variable name must start with a letter or the underscore character
    • A variable name cannot start with a number
    • A variable name can only contain alpha-numeric characters (A-z, 0-9) and underscores ( _ )
    • Variable names are case-sensitive (``age``, ``Age`` and ``AGE`` are three different variables)

----

Python Reserved Words
--------------------------

Reserved Words are keywords that have a set meaning and can't be used for other purposes such as for variable names. Reserved words are case-sensitive and must be used exactly as shown. They are all entirely lowercase, except for False, None, and True.

| The list of reserved words is:

| False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

| A list of keywords can be shown by using ``print(help("keywords"))``.
| A second method for listing keywords uses the keyword library. (see: https://docs.python.org/3/library/keyword.html)

.. code-block:: python

    import keyword

    print(keyword.kwlist)

----

Python conventions
--------------------------

| It is helpful to use meaningful variable names that indicate what the variable is. e.g. ``height`` instead of ``x`` for the height of an object.

Snake case
---------------

| Snake case is used for variables and functions.
| Snake case uses underscores between words. e.g. player_count, player_1_score, player_2_score

ALL_CAPS
---------------

| ALL_CAPS are used for constants, such as ``PI = 3.14``, ``GRAVITY = 9.8``, ``MILES_TO_METRES = 1609``.

CapWords
---------------

| CapWords, such as ``AnimalFeatures``, are used for Class names in python.

camelCase
---------------

| camelCase variables, such as ``playerScore``, are not recommended in python.

KebabCase
---------------

| KebabCase variables, such as ``player-score``, are not recommended in python.

----

Sample code
--------------------------

| The print statement below can be generalised using a variable for the team name and a variable for the number of premierships.
| This is good practice since it separates the data from the output.

.. code-block:: python

    print('Federer has won 20 Grand Slams.')

Generalised to:

.. code-block:: python

    player_name = 'Federer'
    wins = '20'
    print(player_name + ' has won ' + wins + ' Grand Slams.')

----

Tasks
--------------------------

.. admonition:: Questions

    #. Write ``AGE`` in snake case.
    #. Write ``MyName`` in snake case.
    #. Write ``MyFirstNameLastName`` in snake case.
    #. Write ``rectangleArea`` in snake case.
    #. Write ``cm_in_an_inch = 2.14`` as ALL_CAPS.
    #. Write ``lbs_in_a_kg = 2.2`` as ALL_CAPS.
    #. A program asks for a person's age and stores it. What would be a good variable to use: ``x``, ``variable1``, ``AGE``, ``age``, ``Years_Old``?
    #. A program uses a person's first name and last name. What would be a good variable to use for their last name: ``x``, ``variable1``, ``SURNAME``, ``last_name``, ``Name``?
    #. A program calculates the area of a rectangle. What would be two good variables to use for the length and width of the rectangle: ``x``, ``y``, ``LENGTH``, ``length``, ``Width``, ``width``?

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1
                
                Write ``AGE`` in snake case.

                .. code-block:: python

                    age

            .. tab-item:: Q2
                
                Write ``MyName`` in snake case.

                .. code-block:: python

                    my_name

            .. tab-item:: Q3
                
                Write ``MyFirstNameLastName`` in snake case.

                .. code-block:: python

                    my_first_name_last_name

            .. tab-item:: Q4
                
                Write ``rectangleArea`` in snake case.

                .. code-block:: python

                    rectangle_area

            .. tab-item:: Q5
                
                Write ``cm_in_an_inch = 2.14`` as ALL_CAPS.

                .. code-block:: python

                    CM_IN_AN_INCH = 2.14

            .. tab-item:: Q6
                
                Write ``lbs_in_a_kg = 2.2`` as ALL_CAPS.

                .. code-block:: python

                    LBS_IN_A_KG = 2.2

            .. tab-item:: Q7
                
                A program asks for a person's age and stores it. What would be a good variable to use: ``x``, ``variable1``, ``AGE``, ``age``, ``Years_Old``?

                .. code-block:: python

                    age

            .. tab-item:: Q8
                
                A program uses a person's first name and last name. What would be a good variable to use for their last name: ``x``, ``variable1``, ``SURNAME``, ``last_name``, ``Name``?

                .. code-block:: python

                    last_name                   

            .. tab-item:: Q9
                
                A program calculates the area of a rectangle. What would be two good variables to use for the length and width of the rectangle: ``x``, ``y``, ``LENGTH``, ``length``, ``Width``, ``width``?

                .. code-block:: python

                    length, width
