====================================
Python Fundamentals: Working with Lists
====================================

A **list** in Python is an ordered collection of items stored in a single variable. Lists are mutable, meaning you can change, add, or remove elements after creation.

.. contents:: Lesson Outline
   :depth: 2
   :local:

----

Creating Lists
=================

Lists are defined using square brackets ``[]``, with items separated by commas.

Creating Empty and Populated Lists
----------------------------------------------

.. code-block:: python

    # Empty lists
    empty_list = []

    # A list of strings (fruits)
    fruits = ["apple", "banana", "cherry", "date"]

    # A list of numbers
    scores = [85, 92, 78, 90, 88]

    # Displaying list contents and length
    print(fruits)       # Output: ['apple', 'banana', 'cherry', 'date']
    print(len(scores))  # Output: 5

----

Adding Elements to a List
============================

Python provides multiple methods to add items to an existing list.

Using ``append()``, ``insert()``, and ``extend()``
------------------------------------------------------------------

* **``append(item)``**: Adds an item to the **end** of the list.
* **``insert(index, item)``**: Inserts an item at a **specific position**.
* **``extend(iterable)``**: Appends all items from another collection to the end.

.. code-block:: python

    fruits = ["apple", "banana"]

    # 1. Append to the end
    fruits.append("cherry")
    print(fruits)  # Output: ['apple', 'banana', 'cherry']

    # 2. Insert at index 1 (second position)
    fruits.insert(1, "blueberry")
    print(fruits)  # Output: ['apple', 'blueberry', 'banana', 'cherry']

    # 3. Extend with another list of numbers
    numbers = [1, 2, 3]
    numbers.extend([4, 5])
    print(numbers)  # Output: [1, 2, 3, 4, 5]

----

Removing Elements from a List
================================

Items can be removed by value or by position.

Using ``remove()``, ``pop()``, and ``clear()``
-------------------------------------------------------------

* **``remove(value)``**: Deletes the **first match** of a specific value.
* **``pop(index)``**: Removes and **returns** the item at the given index (defaults to the last item).
* **``clear()``**: Removes **all** items from the list.

.. code-block:: python

    basket = ["apple", "banana", "cherry", "banana", "elderberry"]

    # 1. Remove by value (removes the first 'banana')
    basket.remove("banana")
    print(basket)  # Output: ['apple', 'cherry', 'banana', 'elderberry']

    # 2. Pop by index (removes item at index 2)
    removed_item = basket.pop(2)
    print(removed_item)  # Output: 'banana'
    print(basket)        # Output: ['apple', 'cherry', 'elderberry']

    # 3. Pop the last element (no argument passed)
    last_item = basket.pop()
    print(last_item)     # Output: 'elderberry'

    # 4. Clear all elements from a number list
    nums = [10, 20, 30]
    nums.clear()
    print(nums)          # Output: []

----

List Slicing
===============

Slicing extracts a sub-section of a list using the syntax ``list[start:stop:step]``.

* **``start``**: The index where the slice begins (inclusive).
* **``stop``**: The index where the slice ends (**exclusive**).
* **``step``**: The increment between indices (optional).

Slicing Examples
---------------------

.. code-block:: python

    numbers = [0, 10, 20, 30, 40, 50, 60, 70]
    fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig"]

    # Basic slicing [start:stop]
    print(fruits[1:4])     # Output: ['banana', 'cherry', 'date']

    # From start up to index
    print(numbers[:4])     # Output: [0, 10, 20, 30]

    # From index to the end
    print(fruits[3:])      # Output: ['date', 'elderberry', 'fig']

    # Using step [start:stop:step]
    print(numbers[::2])    # Output: [0, 20, 40, 60] (every second item)

    # Negative indexing and reversing
    print(fruits[-3:])     # Output: ['date', 'elderberry', 'fig'] (last 3 items)
    print(numbers[::-1])   # Output: [70, 60, 50, 40, 30, 20, 10, 0] (reversed)

----

Iterating Over Lists
=======================

You can loop through elements directly, with index counters, or through multiple lists simultaneously.

Looping Techniques
------------------------

**Standard ``for`` Loop**

.. code-block:: python

    fruits = ["apple", "banana", "cherry"]

    for fruit in fruits:
        print(f"I like {fruit}s!")

**Using ``enumerate()`` for Index and Value**

.. code-block:: python

    scores = [88, 95, 72]

    for index, score in enumerate(scores, start=1):
        print(f"Student {index}: {score}")

**List Comprehension (Concise Iteration)**

.. code-block:: python

    numbers = [1, 2, 3, 4, 5]

    # Square each number in a new list
    squares = [n ** 2 for n in numbers]
    print(squares)  # Output: [1, 4, 9, 16, 25]

    # Filter items during iteration
    even_numbers = [n for n in numbers if n % 2 == 0]
    print(even_numbers)  # Output: [2, 4]

----

Summary Table
=============

.. list-table:: Common Python List Operations
   :widths: 25 35 40
   :header-rows: 1

   * - Operation
     - Syntax Example
     - Result / Description
   * - Create
     - ``items = [1, 2, 3]``
     - Initializes a list.
   * - Append
     - ``items.append(4)``
     - Adds ``4`` to the end.
   * - Insert
     - ``items.insert(0, 99)``
     - Inserts ``99`` at index 0.
   * - Remove Value
     - ``items.remove(2)``
     - Removes first instance of ``2``.
   * - Pop Index
     - ``val = items.pop(1)``
     - Removes and returns item at index 1.
   * - Slice
     - ``subset = items[1:3]``
     - Copies elements from index 1 up to 2.
   * - Iterate
     - ``for x in items:``
     - Loops through each element.


6. Test Your Understanding
===========================

Check your knowledge of Python lists using the interactive questions below.

Fill-in-the-Blanks (Cloze)
---------------------------

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. To add a new item to the end of a list, use the @@.append()@@ method.
    2. In Python lists, the very first item is always at index @@0@@.
    3. To remove an item by name (value) rather than by index number, use the @@.remove()@@ method.
    4. The function @@len()@@ tells you total number of items in a list.
    5. A basic @@for@@ loop lets you look at every item in a list one by one.


Code Ordering Examples
----------------------

**Example 1:** Create a list of animals, add a new animal to the end, and print the list.

.. ordering::

    animals = ["cat", "dog"]
    animals.append("rabbit")
    print(animals)

----

**Example 2:** Create a fruit list, insert a fruit at the start, and print each fruit on a new line.

.. ordering::

    fruits = ["apple", "banana"]
    fruits.insert(0, "mango")
    for fruit in fruits:
        print(fruit)

----

**Example 3:** Build a score list, remove a low score, and display how many scores are left.

.. ordering::

    scores = [10, 50, 20, 80]
    scores.remove(10)
    print(len(scores))

----

**Example 4:** Create a list of colors, remove the last item using pop, and print the removed color.

.. ordering::

    colors = ["red", "blue", "green"]
    last_color = colors.pop()
    print(last_color)

----

**Example 5:** Create a numbers list, slice the first two numbers into a new list, and print them.

.. ordering::

    numbers = [5, 10, 15, 20]
    first_two = numbers[0:2]
    print(first_two)


Multiple Choice Questions
-------------------------

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 10


    .. multichoice::

        Given the list ``colors = ["red", "blue", "green"]``, what is ``colors[1]``?

        [ ] "red" | Incorrect. "red" is at index 0 because counting starts at 0.
        [x] "blue" | Correct! Index 1 is the second item in the list.
        [ ] "green" | Incorrect. "green" is at index 2.
        [ ] ["red", "blue"] | Incorrect. Using a single index returns one item, not a list.


    .. multichoice::

        Which code adds the string ``"pizza"`` to the end of a list named ``food``?

        [x] food.append("pizza") | Correct! .append() adds new items to the very end of a list.
        [ ] food.add("pizza") | Incorrect. Python lists do not use .add().
        [ ] food.insert("pizza") | Incorrect. .insert() needs an index number to know where to put the item.
        [ ] food.push("pizza") | Incorrect. .push() is used in other languages, not Python.


    .. multichoice::

        What happens when you run ``numbers = [1, 2, 3]`` followed by ``numbers.pop(0)``?

        [ ] The number 3 is removed. | Incorrect. pop(0) targets index 0, which is the first item.
        [x] The number 1 is removed. | Correct! Index 0 is the first element (1).
        [ ] The entire list is cleared. | Incorrect. pop() only removes one item at a time.
        [ ] Nothing, because pop needs a name not a number. | Incorrect. pop() takes index numbers.


    .. multichoice::

        What will be printed by the following code?

        ``fruits = ["apple", "banana", "cherry"]``
        ``print(len(fruits))``

        [ ] 2 | Incorrect. Count all items starting from 1.
        [x] 3 | Correct! There are 3 items in total in the list.
        [ ] 4 | Incorrect. There are only 3 items in this list.
        [ ] 0 | Incorrect. len() counts the items, it does not use zero-based indexing.


    .. multichoice::

        If ``items = ["book", "pen", "pencil", "pen"]``, what does ``items.remove("pen")`` do?

        [ ] Removes both "pen" items from the list. | Incorrect. .remove() only deletes the first matching item it finds.
        [x] Removes the first "pen" at index 1. | Correct! .remove() scans from left to right and stops after deleting the first match.
        [ ] Removes the last "pen" at index 3. | Incorrect. It removes the first matching item it reaches.
        [ ] Gives an error message. | Incorrect. "pen" is in the list, so it works fine.


    .. multichoice::

        What is the output of ``letters = ["a", "b", "c", "d"]`` followed by ``print(letters[1:3])``?

        [ ] ['a', 'b'] | Incorrect. Index 1 is 'b', so it does not start with 'a'.
        [x] ['b', 'c'] | Correct! Slicing starts at index 1 ('b') and goes up to, but does not include, index 3 ('d').
        [ ] ['b', 'c', 'd'] | Incorrect. Slicing stops right before the second index number.
        [ ] ['a', 'b', 'c'] | Incorrect. Index 0 ('a') is excluded because the slice starts at 1.


    .. multichoice::

        What error occurs if you try to print ``names[5]`` when ``names = ["Alex", "Sam"]``?

        [ ] NameError | Incorrect. The variable exists, but the index is out of range.
        [ ] TypeError | Incorrect. Using numbers for indices is correct syntax.
        [x] IndexError | Correct! The list only has indices 0 and 1, so index 5 is out of bounds.
        [ ] ValueError | Incorrect. Accessing a missing position in a list raises an IndexError.


    .. multichoice::

        Where does ``pets.insert(0, "fish")`` place the word ``"fish"`` in the list?

        [x] At the very beginning of the list | Correct! Index 0 is the starting position.
        [ ] At the very end of the list | Incorrect. To add to the end, you would use .append().
        [ ] At index 1 (second place) | Incorrect. Index 0 is the first position.
        [ ] It replaces the item currently at index 0 | Incorrect. .insert() pushes existing items to the right rather than overwriting them.


    .. multichoice::

        How many times will the print command run in this loop?

        ``nums = [5, 10, 15, 20]``
        ``for n in nums:``
        ``    print(n)``

        [ ] 3 times | Incorrect. The loop visits every single item in the list.
        [x] 4 times | Correct! Since there are 4 items in the list, the loop runs 4 times.
        [ ] 5 times | Incorrect. There are only 4 items in the list.
        [ ] 1 time | Incorrect. The loop iterates through all items, not just one.


    .. multichoice::

        Which code block correctly creates an empty list and then adds the number ``10`` to it?

        [ ] ``data = []`` then ``data.insert(10)`` | Incorrect. .insert() requires a position index as well.
        [x] ``data = []`` then ``data.append(10)`` | Correct! Creates an empty list [] and appends 10 to it.
        [ ] ``data = [10]`` then ``data.clear()`` | Incorrect. .clear() would make the list empty again.
        [ ] ``data = 10`` then ``data.append()`` | Incorrect. ``data = 10`` creates an integer, not a list.

