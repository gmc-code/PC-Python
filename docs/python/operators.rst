==========================
Operators
==========================

| Assignment operators are used to assign values to variables.
| The compound assignment operators consist of two operators as a shorthand.
| Comparison operators are used to compare two values.
| Membership operators are used to test if a sequence is presented in an object.
| Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
| Booleans represent one of two values: True or False.
| Logical operators are used to combine conditional statements.

----

Arithmetic operators
--------------------------

Arithmetic operators are used with numbers to perform common mathematical operations

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    *   - **Operator** 
        - **Description**  
        - **Example**
    *   - \+
        - Addition    
        - x + y
    *   - \-
        - Subtraction    
        - x - y
    *   - \*    
        - Multiplication    
        - x * y
    *   - /    
        - Division    
        - x / y
    *   - %    
        - Modulus    
        - x % y
    *   - //    
        - Floor division    
        - x // y
    *   - \**    
        - Exponentiation    
        - x ** y



| Modulus gives the remainder from a division.
| Floor division rounds down the result from a division to the nearest integer.
| Exponentiation raises to a power.

.. code-block:: python

    a=9
    b=2

    print(f'a + b = {a} + {b} = {a + b}')  
    # a + b = 9 + 2 = 11
    print(f'a - b = {a} - {b} = {a - b}')  
    # a - b = 9 - 2 = 7
    print(f'a * b = {a} * {b} = {a * b}')  
    # a / b = 9 / 2 = 4.5
    print(f'a / b = {a} / {b} = {a / b}')  
    # a / b = 9 / 2 = 4.5
    print(f'a // b = {a} // {b} = {a // b}')  
    # a / b = 9 / 2 = 4.5
    print(f'a % b = {a} % {b} = {a % b}')  
    # a / b = 9 / 2 = 4.5
    print(f'a ** b = {a} ** {b} = {a ** b}')  
    # a / b = 9 / 2 = 4.5


| Basic arithmetic operators: ``+, -, *, /`` are used in the same way as with a calculator. 
| e.g. converting Celsius to Fahrenheit.

.. code-block:: python

    celsius_temp = 30
    fahrenheit_temp = celsius_temp * 9 / 5 + 32
    print(fahrenheit_temp)
    # 86.0

| The ``%`` operator, called ``mod`` is used to calculate the remainder when one value is divided by another. 
| For example: finding out if a number is odd or even, divide it by 2, and if the remainder is zero, then it was even.
| When dividing an integer by 2, the remainder will be 1 for odd numbers and 0 for even numbers.

.. code-block:: python

    number = 3
    if number % 2 == 1:
        print(f"The number {number} is odd.")
    else:
        print(f"The number {number} is even.")

----

Compound_assignment
--------------------------

.. csv-table:: Compound_assignment
    :file: Compound_assignment.csv
    :widths: 80, 30, 90, 30
    :header-rows: 1

.. code-block:: python

    a = 9
    b = 2
    a += b
    print(a)

    a = 9
    b = 2
    a -= b
    print(a)

    a = 9
    b = 2
    a *= b
    print(a)

    a = 9
    b = 2
    a /= b
    print(a)

----

Strings
--------------------------

| Strings (``str`` type in Python) are sequences of characters.
| Strings can be concatenated or joined using a ``+`` symbol.

.. code-block:: python

    name = "Alice"
    quote = "'And what is the use of a book,' thought " + name + ", 'without pictures or conversation?'"
    print(quote)

----

Strings and numbers
--------------------------

| To join numbers and strings together, the number must be convereted to a string using the ``str()`` function.

.. code-block:: python

    temperature = 24
    if temperature < 10:
        print("A cold " + str(temperature))
    else:
        print("A warm " + str(temperature))


----

Booleans
---------
| A Boolean value is a value that is either ``True`` or ``False``, also represented by `1` and `0`. 

| Booleans represent one of two values: True or False.
| Almost any value is evaluated to True if it has some sort of content.
| Any string is True, except empty strings.
| Any number is True, except 0.
| Any list, tuple, set, and dictionary is True, except empty ones.

.. code-block:: python

    # True  evaluates to 1.
    print(int(True))
    # 1
    print((1 + True))
    # 2

    # False evaluates to 0.
    print(int(False))
    # 0
    print((1 + False))
    # 1

    # These all print # False
    print(bool(False))  
    print(bool(None))
    print(bool(0))
    print(bool(""))
    print(bool(()))
    print(bool([]))
    print(bool({}))

    These all print # True
    print(bool(1))
    print(bool(" "))
    print(bool((1)))
    print(bool([2]))
    print(bool({3}))

----

Comparison
--------------------------

| Comparison operations are useful to test variable values in conditional statements or loops. 

.. tabularcolumns:: |L|l|

+--------------------------------+----------------------------------------+
| **Comparison Operator**        | **Meaning**                            |
+================================+========================================+
| ==                             | Equal to                               |
+--------------------------------+----------------------------------------+
| <                              | Less than                              |
+--------------------------------+----------------------------------------+
| <=                             | Less than or equal to                  |
+--------------------------------+----------------------------------------+
| >                              | Greater than                           |
+--------------------------------+----------------------------------------+
| >=                             | Greater than or equal to               |
+--------------------------------+----------------------------------------+
| !=                             | not equal to                           |
+--------------------------------+----------------------------------------+

Examples of comparisons in Python:

.. code-block:: python

    # score is greater than 10
    score = 40
    print(score > 10)

    # name equals "Anne"
    name = "Anne"
    print(name ==  "Anne")

    # speed is not equal to 0
    speed = 2
    print(speed != 0)

.. code-block:: python

    a = 7
    b = 3
    print(f'{a} == {b} is {a == b}')
    # 7 == 3 is False
    print(f'{a} != {b} is {a != b}')
    # 7 != 3 is True
    print(f'{a} > {b} is {a > b}')
    # 7 > 3 is True
    print(f'{a} < {b} is {a < b}')
    # 7 < 3 is False
    print(f'{a} >= {b} is {a >= b}')
    # 7 >= 3 is True
    print(f'{a} <= {b} is {a <= b}')
    # 7 <= 3 is False

----

Logical operations
--------------------------

Logical operators test the truth value of their operands.

+--------------+---------------------------------+-------------------+
| **Operator** |  **Evaluates to ``True`` if:**  | **Example**       |
+==============+=================================+===================+
| and          |  Both operands are true         | ``True and True`` |
+--------------+---------------------------------+-------------------+
| or           |  At least one operand is true   | ``True or False`` |
+--------------+---------------------------------+-------------------+
| not          |  Operand is false               | ``not False``     |
+--------------+---------------------------------+-------------------+

| Examples of logical operations in Python:

.. code-block:: python

    score = 40
    user = "Anne"
    level = 2

    print(score > 10 and user == "Anne")
    print(score > 10 or level == 3)
    print(not(level == 1))

----

Membership operations
--------------------------

| Membership operators are useful to determine the presence of an element in a sequence, such as a string or list.

+--------------+----------------------------------------------------------+--------------------------+
| **Operator** | **Evaluates to ``True`` if:**                            | **Example**              | 
+==============+==========================================================+==========================+
|   in         | A variable value is in a sequence                        | ``x in [1, 2, 3, 4]``    |
+--------------+----------------------------------------------------------+--------------------------+
| not in       | A variable value is not in a sequence                    | ``x not in [1, 2, 3, 4]``|
+--------------+----------------------------------------------------+-----+--------------------------+

| Example of membership operation in strings:

.. code-block:: python
    
    a = 'o'
    b = 'John'
    print(f'{a} in {b} is {a in b}') # o in John is True
    print(f'{a} not in {b} is {a not in b}') # o not in John is False

| Example of membership operation in lists:

.. code-block:: python

    x = 7
    value_list = [1, 2, 3, 4]

    print(x in value_list)
    print(x not in value_list)


----

Using Boolean operations
--------------------------

| The code below uses 2 booleans with nested selection.

.. code-block:: python

    is_condition1 = True
    is_condition2 = False
    if is_condition1 or is_condition2:
        if is_condition1 and is_condition2:
            my_val = 1
        elif is_condition1 and not is_condition2:
            my_val = 2
        else:
            my_val = 3
    else:
        my_val = 4
    print(my_val)
