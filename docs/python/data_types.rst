==========================
Data Types
==========================

See: https://www.w3schools.com/python/python_datatypes.asp

Data type categories
--------------------------

.. csv-table::
    :file: files/data_type_categories.csv
    :widths: 200, 400
    :header-rows: 1

----

Data type examples
--------------------------

.. csv-table::
    :file: files/data_type_examples.csv
    :widths: 350, 50, 300, 50, 50, 50
    :header-rows: 1

----

Strings
--------------------------

A string is a sequence of characters surrounded by either single quotation marks (``' '``) or double quotation marks (``" "``).

- **Using Quotes Within Strings**:
  - If your text contains single quotes, you can use double quotes to enclose the string.
    - Example: ``"It's a nice day."``
  - If your text contains double quotes, you can use single quotes to enclose the string.
    - Example: ``'Jane said "Go now", then left.'```

- **Using Both Quotes Within Strings**:
  - If your text contains both single and double quotes, you can use triple quotes to enclose the string.
    - Example: ``'''My favourite quote from Jane's essay was "Go now". Short and sweet.'''``

- **Escaping Quotes**:
  - You can use the backslash (`\`) to escape quotes within a string, forcing them to be used literally.
    - Example: `'It\'s a nice day.'`

- **Triple Quotes for Documentation and Multi-line Strings**:
  - Triple quotes (either ``'''`` or ``"""``) are used for documentation strings (docstrings) and multi-line strings.
    - Example of a docstring for a function:

      .. code-block:: python

        def square_number(n):
            """
            This function returns the square of a given number.

            Parameters:
            n (int or float): The number to be squared.

            Returns:
            int or float: The square of the input number.
            """
            return n ** 2

    - Example of a multi-line string:

      .. code-block:: python

        """This is a multiline string.
        It can span multiple lines.
        You can include line breaks."""


----

Numbers
--------------------------

| Numbers are written without quotes.
| An integer is a whole number.
| e.g. 2
| A float is a decimal.
| e.g. 3.5

----

Booleans
--------------------------

Booleans have the value ``True`` or ``False``.

----

Types
--------------------------

The type() function can be used to get the data type for a variable.

.. code-block:: python

    # String
    print(type('hello'))   # <class 'str'>

    # Integer
    print(type(1))         # <class 'int'>

    # Float
    print(type(1.64))      # <class 'float'>

    # Boolean
    print(type(True))      # <class 'bool'>

    # None
    print(type(None))      # <class 'NoneType'>

----

.. admonition:: Questions

    #. Predict the output from ``print(type('123'))``.
    #. Predict the output from ``print(type(123))``.
    #. Predict the output from ``print(type('False'))``.

----

Type casting
--------------------------

See: https://www.w3schools.com/python/python_casting.asp

| The conversion of one type to another is called type casting.
| Data types can't be mixed so type casting is needed to convert data to the same type so that they can be used together.

Converting numbers to strings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

str() converts a number to a string with a number in it

.. code-block:: python

    j = str(3.01) # j will be "3.01"

| An integer can be converted to a string using the str() function.
| The premierships integer is converted to a string so it can be combined with the rest of the strings for printing.

.. code-block:: python

    team = 'Richmond'
    premierships = 11
    print(team + ' has won ' + str(premierships) + ' premierships.')

Converting numbers as strings to numbers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

int() converts a string consisting of an integer to an integer number

.. code-block:: python

    c = int("3")      # c will be 3

float() converts a string consisting of a decimal to a decimal number

.. code-block:: python

    g = float("4.23") # g will be 4.23


----

.. admonition:: Questions

    #. Predict the output from ``print(int(2.5))``.
    #. Predict the output from ``print(int("3"))``.
    #. Predict the output from ``print(float(1))``.
    #. Predict the output from ``print(float("4.23"))``.
    #. Predict the output from ``print(str(3.01))``.
