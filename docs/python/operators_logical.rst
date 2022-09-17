==========================
Logical operations
==========================

| **Logical** operators are used to combine conditional statements.

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

