==========================
Indentation
==========================

Python Indentation
----------------------

| Python uses **indentation** to indicate a **block of code** for selection and iteration and definition.
| Indentation refers to the spaces at the beginning of a code line.
| The number of spaces is flexible, but is usually 4 spaces for each indentation.
| A tab press can be used instead of 4 spaces, with editors converting the tab to 4 spaces.
| Errors result from not using the same number of spaces in the same block of code or for not applying indentation in blocks after a colon (:).

| Indentation is required in any block of code where the header line starts with a keyword: (**if**, **elif**, **else**, **for**, **while**, **def**, class, try, except, finally, with) and ends with a colon (:).


Code examples showing indentation:

.. image:: images/indenting.png
    :scale: 52 %
    :align: left
    :alt: indenting

.. code-block:: python

    dice = "5"
    if dice == "6":
        print("Win")
    elif dice == "1":
        print("Loose")
    else:
        print("Roll again.")

    for x in "banana":
        print(x)

    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Go.")

    def my_function():
        print("Hello from a function")




Blocks of code nested within other blocks of code need to be indented to the same level of nesting.

.. image:: images/nested_indenting.png
    :scale: 40 %
    :align: left
    :alt: nested_indenting

.. code-block:: python

    num = 3
    if num < 0:
        print("Negative number")
    else:
        if num == 0:
            print("Zero")
        else:
            print("Positive number")

    for x in "ABC":
        for y in "123":
            print(x, y)

----




Indenting with Conditionals
----------------------------------

**Question:**
The following sequence of code is supposed to check if a number is positive, negative, or zero, but it has indentation errors. Fix the indentation.

.. code-block:: python

    n= 10
    if n > 0:
    print("Positive")
    elif n < 0:
    print("Negative")
    else:
    print("Zero")

**Solution:**

.. code-block:: python

    n= 10
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")


---

Practice Questions
~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Tasks

    #. The following code is supposed to check if a number is positive, but it has indentation errors. Fix the indentation.

        ::

            n = 5
            if n > 0:
            print("Positive")

    #. The following code is supposed to check if a number is positive, but it has indentation errors. Fix the indentation.

        ::
            n = 5
            if n > 0:
            print("Positive")

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                The following code is supposed to check if a number is positive, but it has indentation errors. Fix the indentation.

                .. code-block:: python

                    n = 5
                    if n > 0:
                        print("Positive")

            .. tab-item:: Q2

                The following code is supposed to check if a number is positive, but it has indentation errors. Fix the indentation.

                .. code-block:: python

                    n = 5
                    if n > 0:
                        print("Positive")
























----

Problem 3: Loop with Conditional
================================

**Question:**
The following function is supposed to print numbers from 1 to 5 and label them as even or odd, but it has indentation errors. Fix the indentation.

.. code-block:: python

    def print_numbers():
    for i in range(1, 6):
    if i % 2 == 0:
    print(f"{i} is even.")
    else:
    print(f"{i} is odd.")

**Solution:**
.. code-block:: python

    def print_numbers():
        for i in range(1, 6):
            if i % 2 == 0:
                print(f"{i} is even.")
            else:
                print(f"{i} is odd.")


Problem 4: Nested Loops
=======================

**Question:**
The following function is supposed to print a 3x3 grid of numbers, but it has indentation errors. Fix the indentation.

.. code-block:: python

    def print_grid():
    for i in range(1, 4):
    for j in range(1, 4):
    print(i * j, end=" ")
    print()

**Solution:**
.. code-block:: python

    def print_grid():
        for i in range(1, 4):
            for j in range(1, 4):
                print(i * j, end=" ")
            print()


Problem 1: Function Definition
==============================

**Question:**
The following function is supposed to print a greeting message, but it has indentation errors. Fix the indentation.

.. code-block:: python

    def greet(name):
    print(f"Hello, {name}!")

**Solution:**
.. code-block:: python

    def greet(name):
        print(f"Hello, {name}!")