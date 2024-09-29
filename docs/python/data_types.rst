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
    :file: files/modified_data_with_structure.csv
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
    - Example of a docstring:
      .. code-block:: python
      '''n is an integer'''
      ```
    - Example of a multi-line string:
      .. code-block:: python
      """angle is a float from 0 to 90"""
      ```

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

| Data types can't be mixed.
| They need to be converted to the same type so that they can be used together.
| The conversion of one type to another is called type casting.

| An integer can be converted to a string using the str() function.
| The premierships integer is converted to a string so it can be combined with the rest of the strings for printing.

.. code-block:: python

    team = 'Richmond'
    premierships = 11
    print(team + ' has won ' + str(premierships) + ' premierships.')

int() converts a string consisting of an integer to an integer number

.. code-block:: python

    c = int("3")      # c will be 3

float() converts a string consisting of a decimal to a decimal number

.. code-block:: python

    g = float("4.23") # g will be 4.23

str() converts a number to a string with a number in it

.. code-block:: python

    j = str(3.01) # j will be "3.01"

----

.. admonition:: Questions

    #. Predict the output from ``print(int(2.5))``.
    #. Predict the output from ``print(int("3"))``.
    #. Predict the output from ``print(float(1))``.
    #. Predict the output from ``print(float("4.23"))``.
    #. Predict the output from ``print(str(3.01))``.
