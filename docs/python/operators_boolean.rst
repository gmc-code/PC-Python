==========================
Booleans
==========================

| **Booleans** represent one of two values: True or False.

Booleans
--------------------------

| A Boolean value is a value that is either ``True`` or ``False``, also represented by ``1`` and ``0``. 

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
