==========================
Python Intro
==========================

Python can be used for: AI and machine learning, Data analytics, Data visualisation, Programming applications, Game development, Web development and system scripting.

Python has syntax that allows developers to write programs with fewer lines than most other programming languages.

VSCode is a popular IDE (Integrated Development Environment) used to edit and run python files.

----

Python Indentation
----------------------

| Python uses **indentation** to indicate a **block of code** for selection and iteration and definition.
| Indentation refers to the spaces at the beginning of a code line.
| The number of spaces is flexible, but is usually 4 spaces for each indentation.
| A tab press can be used instead of 4 spaces, with editors converting the tab to 4 spaces.
| Errors results from not using the same number of spaces in the same block of code or for not applying indentation in blocks after a colon (:).
| Indentation is required in any block of code where the header line starts with a keyword: (**if**, **elif**, **else**, **for**, **while**, **def**, class, try, except, finally, with) and ends with a colon (:).


Code examples showing indentation:

.. image:: images/indenting.png
    :scale: 50 %
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
    :scale: 50 %
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
