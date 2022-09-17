==========================
Arithmetic operators
==========================

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

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a // b)
    print(a % b)
    print(a ** b)


| Basic arithmetic operators: ``+, -, *, /`` are used in the same way as with a calculator. 
| e.g. converting Celsius to Fahrenheit.

.. code-block:: python

    celsius_temp = 30
    fahrenheit_temp = celsius_temp * 9 / 5 + 32
    print(fahrenheit_temp)
    # 86.0

| The ``%`` operator, called ``mod`` is used to calculate the remainder when one value is divided by another. 
| For example: finding out if a number is odd or even.
| When dividing an integer by 2, the remainder will be 1 for odd numbers and 0 for even numbers.

.. code-block:: python

    number = 3
    if number % 2 == 1:
        print(f"The number {number} is odd.")
    else:
        print(f"The number {number} is even.")

