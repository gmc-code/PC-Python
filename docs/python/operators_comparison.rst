==========================
Comparison operations 
==========================

| **Comparison** operators are used to compare two values.

| Comparison operations are useful to test variable values in conditional statements or loops. 

| Here are some examples of comparisons written in English::

    score is greater than 100
    name equals "Harry"
    acceleration is not equal to 0

Rewriting the comparisons above in Python would be.

.. code-block:: python

    score > 100
    name ==  "Harry"
    acceleration  != 0

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
    print(f'{a} == {b} is {a == b}')    # 7 == 3 is False
    print(f'{a} != {b} is {a != b}')    # 7 != 3 is True
    print(f'{a} > {b} is {a > b}')      # 7 > 3 is True
    print(f'{a} < {b} is {a < b}')      # 7 < 3 is False
    print(f'{a} >= {b} is {a >= b}')    # 7 >= 3 is True
    print(f'{a} <= {b} is {a <= b}')    # 7 <= 3 is False

