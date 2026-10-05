===========================
Python Lists Guide (Year 7)
===========================

A **list** in Python is used to store multiple items in a single variable. Lists are ordered, changeable, and created using square brackets ``[]``.

.. code-block:: python

    # Creating a simple list of fruits
    fruits = ["apple", "banana", "cherry"]

--------------------------------------------------

1. Adding Items to a List
=========================

To add new items to an existing list, Python gives us two primary methods:

* ``.append(item)``: Adds a single item to the **very end** of the list.
* ``.insert(index, item)``: Adds an item at a **specific position (index)**. Remember that Python counts starting from ``0``.

.. code-block:: python

    inventory = ["sword", "shield"]

    # Adds "potion" to the end
    inventory.append("potion")  # Result: ["sword", "shield", "potion"]

    # Inserts "map" at index 1 (second position)
    inventory.insert(1, "map")   # Result: ["sword", "map", "shield", "potion"]

Quiz: Adding Items
------------------

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. To add an item to the end of a list, you use the @@.append()@@ method.
    2. The @@.insert()@@ method allows you to place an item at a specific position by index.
    3. Python list indices always start counting from the number @@0@@.
    4. Lists in Python are created using square @@brackets@@.
    5. Using ``.append("dragon")`` puts the new item at the very @@end@@ of your list.

--------------------------------------------------

2. Deleting Items from a List
=============================

Python provides several ways to remove items depending on whether you know the item's **value** or its **position**:

* ``.remove(item)``: Deletes the **first matching item** by value.
* ``.pop(index)``: Removes and returns the item at a specific index. If no index is given, it removes the **last item**.
* ``del list[index]``: Deletes an item at a specific index using the ``del`` keyword.

.. code-block:: python

    pets = ["dog", "cat", "fish", "cat"]

    # Removes the first occurrence of "cat"
    pets.remove("cat")  # Result: ["dog", "fish", "cat"]

    # Removes the item at index 0 ("dog")
    pets.pop(0)         # Result: ["fish", "cat"]

    # Deletes the item at index 1 ("cat")
    del pets[1]         # Result: ["fish"]

Quiz: Deleting Items
--------------------

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. The @@.remove()@@ method removes an item by its value, not its index position.
    2. If you don't specify an index inside ``.pop()``, it automatically removes the @@last@@ item in the list.
    3. To delete an item using its index position, you can use ``.pop()`` or the @@del@@ keyword.
    4. The ``.remove()`` method looks for the item's @@value@@ rather than its index number.
    5. Trying to ``.remove()`` an item that does not exist in the list will cause Python to raise an @@IndexError@@.

--------------------------------------------------

3. Sorting and Reversing Lists
==============================

You can reorder the items inside a list using these simple methods:

* ``.sort()``: Sorts the list in **ascending order** (alphabetical for text, smallest-to-largest for numbers).
* ``.sort(reverse=True)``: Sorts the list in **descending order**.
* ``.reverse()``: Reverses the current order of elements **without** alphabetizing or numerical sorting.

.. code-block:: python

    scores = [45, 12, 89, 33]

    # Sort in ascending order
    scores.sort()             # Result: [12, 33, 45, 89]

    # Sort in descending order
    scores.sort(reverse=True) # Result: [89, 45, 33, 12]

    colors = ["red", "blue", "green"]

    # Simply flip the list order
    colors.reverse()          # Result: ["green", "blue", "red"]

Quiz: Sorting and Reversing
---------------------------

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Calling ``.sort()`` on a list of words arranges them in @@alphabetical@@ order.
    2. To sort numbers from highest to lowest, set the parameter inside sort to ``reverse=`` @@True@@.
    3. The @@.reverse()@@ method flips the order of items without sorting them alphabetically or numerically.
    4. By default, ``.sort()`` arranges numbers in @@ascending@@ order.
    5. The method used to rearrange list elements in order is @@.sort()@@.

--------------------------------------------------

4. Iterating Through a List
===========================

Iterating means going through items in a list one by one. We use a **for loop** to do this efficiently.

.. code-block:: python

    team = ["Alex", "Sam", "Jordan"]

    # Loop through each item in the list
    for player in team:
        print("Welcome to the team, " + player + "!")

Quiz: Iterating Through Lists
-----------------------------

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. We use a @@for@@ loop to visit each item in a list one after another.
    2. The word following ``for`` in a loop acts as a temporary @@variable@@ to hold the current item.
    3. A ``for`` loop header in Python must end with a @@colon@@.
    4. Code inside the loop block must use correct @@indentation@@ to run properly.
    5. Iteration allows Python to step through every item in a @@sequence@@ like a list.

--------------------------------------------------

5. Code Ordering Examples
=========================

**Example 1:** Create an empty inventory list, add a shield to the end, and print the inventory.

.. ordering::

    inventory = []
    inventory.append("Shield")
    print(inventory)

----

**Example 2:** Create a list of student names, sort them alphabetically, and print the sorted list.

.. ordering::

    names = ["Charlie", "Alice", "Bob"]
    names.sort()
    print(names)

----

**Example 3:** Build a score list, remove the last score with pop, sort the rest, and print each score.

.. ordering::

    scores = [40, 10, 30, 20]
    scores.pop()
    scores.sort()
    for s in scores:
        print(s)

--------------------------------------------------

6. Multiple Choice Questions
============================

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 10


    .. multichoice::

        Which symbol is used to create a list in Python?

        [ ] {} | Incorrect. Curly braces {} are used for dictionaries and sets.
        [ ] () | Incorrect. Parentheses () are used for tuples and function calls.
        [x] [] | Correct! Square brackets [] define a list in Python.
        [ ] <> | Incorrect. Angle brackets <> are not list syntax in Python.


    .. multichoice::

        What is the index of the first item in a Python list?

        [ ] 1 | Incorrect. Counting in Python starts at 0, not 1.
        [x] 0 | Correct! Python uses 0-based indexing for lists.
        [ ] -1 | Incorrect. Index -1 targets the last item in a list.
        [ ] "first" | Incorrect. List indices must be integers.


    .. multichoice::

        What does ``items.append("gold")`` do?

        [ ] Replaces the first item with "gold" | Incorrect. .append() does not overwrite existing items.
        [ ] Adds "gold" to the beginning of the list | Incorrect. To add at the start, use .insert(0, "gold").
        [x] Adds "gold" to the end of the list | Correct! .append() always adds items to the very end.
        [ ] Deletes "gold" from the list | Incorrect. To delete items, use .remove() or .pop().


    .. multichoice::

        Given ``colors = ["red", "green", "blue"]``, what does ``colors.pop(1)`` remove?

        [ ] "red" | Incorrect. "red" is at index 0.
        [x] "green" | Correct! Index 1 corresponds to "green".
        [ ] "blue" | Incorrect. "blue" is at index 2.
        [ ] Nothing, it causes an error | Incorrect. Index 1 exists, so .pop(1) succeeds.


    .. multichoice::

        How do you remove the item ``"apple"`` from ``fruits = ["apple", "banana"]`` if you don't know its index?

        [x] fruits.remove("apple") | Correct! .remove() finds and deletes an item by its value.
        [ ] fruits.pop("apple") | Incorrect. .pop() expects an integer index, not a string value.
        [ ] del fruits("apple") | Incorrect. del uses bracket syntax with an index (e.g., del fruits[0]).
        [ ] fruits.delete("apple") | Incorrect. Python lists do not have a .delete() method.


    .. multichoice::

        What will be the value of ``numbers`` after running ``numbers = [3, 1, 4]`` and ``numbers.sort()``?

        [ ] [4, 3, 1] | Incorrect. .sort() defaults to ascending order (smallest to largest).
        [x] [1, 3, 4] | Correct! .sort() reorders elements from lowest to highest.
        [ ] [3, 1, 4] | Incorrect. .sort() modifies the list in place.
        [ ] [1, 4, 3] | Incorrect. All numbers are sorted, so 3 comes before 4.


    .. multichoice::

        How do you sort a list named ``scores`` from highest to lowest?

        [ ] scores.sort(descending=True) | Incorrect. The parameter name is reverse, not descending.
        [ ] scores.reverse(sort=True) | Incorrect. reverse() takes no sort argument.
        [x] scores.sort(reverse=True) | Correct! Setting reverse=True sorts in descending order.
        [ ] scores.sort_down() | Incorrect. There is no .sort_down() method in Python.


    .. multichoice::

        What does ``animals.reverse()`` do to ``animals = ["cat", "dog"]``?

        [ ] Sorts them alphabetically to ["cat", "dog"] | Incorrect. .reverse() flips current order without sorting.
        [x] Changes the list to ["dog", "cat"] | Correct! It reverses the order of items in place.
        [ ] Deletes all items in the list | Incorrect. To delete all items, use .clear().
        [ ] Prints the items backwards without changing the list | Incorrect. .reverse() mutates the list directly.


    .. multichoice::

        Which code correctly prints each item in ``tools = ["hammer", "saw"]``?

        [x] for t in tools: print(t) | Correct! A standard for loop iterates over each element in a list.
        [ ] loop tools as t: print(t) | Incorrect. "loop" is not a Python keyword for iteration.
        [ ] foreach (tools as t) { print(t); } | Incorrect. foreach syntax belongs to PHP/C#, not Python.
        [ ] print(tools.loop()) | Incorrect. Lists do not have a .loop() method.


    .. multichoice::

        What happens if you run ``nums = [10, 20]`` followed by ``print(nums[2])``?

        [ ] Prints 20 | Incorrect. 20 is at index 1.
        [ ] Prints None | Incorrect. Accessing an out-of-range index raises an error.
        [x] Raises an IndexError | Correct! Indices are 0 and 1, so index 2 is out of range.
        [ ] Prints 0 | Incorrect. Python does not return 0 for out-of-bounds indices.

