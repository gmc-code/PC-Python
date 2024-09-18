==========================
Data Types
==========================

See: https://www.w3schools.com/python/python_datatypes.asp

.. csv-table::
    :file: Date_types.csv
    :widths: 70, 120, 200
    :header-rows: 1

Some common built-in data types are:

.. list-table::
    :widths: 200, 200
    :header-rows: 0

    *   - Text Type:
        - str
    *   - Numeric Types:
        - int, float
    *   - Sequence Types:
        - list, tuple, range
    *   - Mapping Type:
        - dict
    *   - Set Types:
        - set, frozenset
    *   - Boolean Type:
        - bool
    *   - None Type:
       	- NoneType

----

Strings
--------------------------

| A string is a sequence of characters surrounded by either single quotation marks (' '), or double quotation marks (" "). 
| Text with quotes within it can use done using the other quote mark.
| e.g. "it's"
| e.g. 'Jim said "Go home", then left.'

| Text with both quotes within it can use done using triple quotes.
| '''My favourite quote from Jim's essay was "Go home". Short and sharp.'''

| Escaping via \ can be used to force the quote to be used literally.
| e.g. 'it\'s'

| Triple quotes are used for documentation strings. Triple single or triple double quotes can be used.
| Triple quotes can also be used for multi line strings.
| e.g. '''n is an integer'''
| e.g. """angle is a float from 0 to 90"""

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
