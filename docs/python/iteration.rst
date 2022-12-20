==========================
Iteration
==========================

The three basic control structures are:

#. Sequence (steps in order)
#. Selection (branching using ``if`` ... ``elif`` ... ``else``)
#. Iteration (repetition or looping using ``while`` or ``for``)

Loops
------------------

| Loops are very useful structures which enable repeating of a certain block of code several times over.
| There are two types of loops: 
| ``for`` loops, that keep count of the number of times a block of code is executed, and 
| ``while`` loops which perform an action until a specified condition is no longer true. 

----

For loops with the range function
------------------------------------

| Use the range() function to loop through a set of code a specified number of times.
| The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
| ``range(8)`` means the values 0 to 7 (8 not included).

.. code-block:: python

    for number in range(8):
        print(number, end = ' ')
    # 0 1 2 3 4 5 6 7

| ``range(2, 8)`` means values from 2 to 8 but not including 8.

.. code-block:: python

    for number in range(2,8):
        print(number, end = ' ')
    # 2 3 4 5 6 7

| The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter.
| range(1, 15, 3) means values from 1 up to but not including 15, in steps of 3.

.. code-block:: python

    for number in range(1, 15, 3):
        print(number, end = ' ')
    # 1 4 7 10 13

----

Nested For loops
------------------------------------

| In the example below, x and y are assigned the values by the range function:

.. code-block:: python

    for x in range(2, 5):
        for y in range(3, 6):
            print(x, y)

----

For loops with sequences
------------------------------------

| A for-loop can be used to iterate over a sequence that is either a string, a list, a tuple, , a set or a dictionary.
| The for-loop can execute a set of statements, once for each item in a sequence.

.. code-block:: python

    for letter in 'Common Operating Machine Particularly Used for Technical, Education and Research':
        print(letter, end = '-')

.. code-block:: python

    for network in ['DNS','VPN','PoP','VoIP']:
        print(network, end = ' ' )

----

While True loops
------------------

| One of the most common things you might want to do with a ``while`` loop is to do something forever. Here is an example of some code to repeat forever:

.. code-block:: python

    while True:
        print("Hello..."")

This code will repeatedly print the text ``Hello...``.

----

While loops
------------------

| The while loop requires relevant variables to be ready, and incremented in the loop to avoid it running for ever.
| In the example below, the variable num is increased by one each loop.
| The loops stops when ``num`` gets to 5.

.. code-block:: python

    num = 0
    while num < 5:
        num += 1
        print(num)

| In the example below, the variable num is decreased by one each loop.
| The loops stops when ``num`` gets to 0.

.. code-block:: python

    num = 5
    while num > 0:
        print(num)
        num -= 1

| In the example below, a final clock of code can run as part of the ``else`` statement.
| The loops stops when ``num`` gets to 0, then the ``else`` block is run.

.. code-block:: python

    num = 5
    while num > 0:
        print(num)
        num -= 1
    else:
        print("Blastoff")



| The break statement stops the loop even if the while condition is true:
| Example. Exit the loop when i is 3:

.. code-block:: python

    i = 1
    while i < 6:
        print(i)
        if i == 3:
            break
        i += 1


| The continue statement stops the current iteration (the current run through the loop), and continues with the next iteration of the loop.
| Example. Continue to the next iteration if i is 3:

.. code-block:: python

    i = 0
    while i < 6:
        i += 1
        if i == 3:
            continue
        print(i)



