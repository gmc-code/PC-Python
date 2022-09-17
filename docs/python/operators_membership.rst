==========================
Membership operations
==========================


| **Membership** operators are used to test if a sequence is presented in an object.

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
    print(f'{a} in {b} is {a in b}')          # o in John is True
    print(f'{a} not in {b} is {a not in b}')  # o not in John is False

| Example of membership operation in lists:

.. code-block:: python

    x = 7
    value_list = [1, 2, 3, 4]

    print(x in value_list)
    print(x not in value_list)

