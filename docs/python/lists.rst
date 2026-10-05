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

    1. To add an item to the end of a list, use the @@.append()@@ method.
    2. List indices start at index @@0@@, which represents the first element.
    3. The slice syntax ``fruits[1:4]`` extracts items starting at index 1 up to index @@3@@.
    4. To delete the first matching instance of an element by value, call the @@.remove()@@ method.
    5. To get both the index and value while looping over a list, use the @@enumerate()@@ function.


Code Ordering Examples
----------------------

**Example 1:** Create a fruit list, add to front, drop last, and print uppercase

.. ordering::

    fruits = ["apple", "banana", "cherry"]
    fruits.insert(0, "mango")
    fruits.pop()
    for fruit in fruits:
        print(fruit.upper())


 **Example 2:** Find all even numbers, square them, and print results

.. ordering::

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = [n for n in numbers if n % 2 == 0]
    squared_evens = [n ** 2 for n in evens]
    for val in squared_evens:
        print(val)

**Example 3:** Build a shopping cart by extending and removing an out-of-stock item

.. ordering::

     cart = ["apples", "bananas"]
    cart.extend(["milk", "bread"])
    cart.remove("bananas")
    print(f"Items to buy: {len(cart)}")


**Example 4:** Extract middle elements using slicing and reverse them

.. ordering::

    values = [10, 20, 30, 40, 50, 60]
    middle_three = values[1:4]
    reversed_middle = middle_three[::-1]
    print(reversed_middle)

**Example 5:** Number a ranked list of top scores using enumerate

.. ordering::

     scores = [95, 88, 79, 64]
    scores.sort(reverse=True)
    for rank, score in enumerate(scores, start=1):
        print(f"Rank {rank}: {score}")


Multiple Choice Questions
-------------------------


.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 10


    .. multichoice::

        What is the output of ``numbers = [10, 20, 30, 40, 50]`` followed by ``print(numbers[1:3])``?

        [ ] [10, 20] | Incorrect. Slicing starts at index 1 (inclusive), which is 20.
        [x] [20, 30] | Correct! Index 1 is 20, and index 2 is 30. Index 3 (40) is excluded because the stop bound is non-inclusive.
        [ ] [20, 30, 40] | Incorrect. Slicing stops before reaching the stop index. Index 3 is excluded.
        [ ] [10, 20, 30] | Incorrect. Index 0 is excluded because the start index is 1.


    .. multichoice::

        Which method removes and returns an element from a specific index in a list?

        [ ] remove() | Incorrect. remove() deletes by value, not by index, and does not return the item.
        [ ] delete() | Incorrect. Python uses the del statement or pop() method, not a .delete() method.
        [x] pop() | Correct! pop(index) removes and returns the element at the specified index (or the last item if no index is passed).
        [ ] clear() | Incorrect. clear() empties the entire list and returns None.


    .. multichoice::

        Given ``fruits = ["apple", "banana", "cherry"]``, what will ``fruits[::-1]`` return?

        [x] ["cherry", "banana", "apple"] | Correct! A step of -1 reverses the list order.
        [ ] ["apple", "banana"] | Incorrect. Negative step values reverse the slice rather than trimming from the end.
        [ ] ["cherry"] | Incorrect. Slicing with [::-1] reverses the entire list.
        [ ] SyntaxError | Incorrect. Step parameters in slices can legally take negative integer values.


    .. multichoice::

        What happens if you attempt to access ``fruits[5]`` when ``fruits = ["apple", "banana"]``?

        [ ] Returns None | Incorrect. Python does not return None for out-of-bounds indices.
        [ ] Returns "" | Incorrect. An empty string is not returned.
        [x] Raises IndexError | Correct! Accessing an index outside the list's bounds raises an IndexError.
        [ ] Returns ["apple", "banana"] | Incorrect. Indexing retrieves a single item, not the full list.


    .. multichoice::

        How do you add all elements from list ``b = [3, 4]`` to list ``a = [1, 2]`` so that ``a`` becomes ``[1, 2, 3, 4]``?

        [ ] a.append(b) | Incorrect. append(b) produces a nested list: [1, 2, [3, 4]].
        [x] a.extend(b) | Correct! extend() iterates over its argument and appends each element.
        [ ] a.insert(b) | Incorrect. insert() requires two arguments: an index and an item.
        [ ] a.add(b) | Incorrect. Lists do not have an .add() method (sets do).


    .. multichoice::

        What is the result of ``len([5, 10, 15, 20][::2])``?

        [ ] 4 | Incorrect. The slice [::2] selects every second element, reducing the total length.
        [x] 2 | Correct! Slicing with step 2 extracts [5, 15], which has a length of 2.
        [ ] 3 | Incorrect. Index 0 (5) and index 2 (15) are taken, yielding 2 elements.
        [ ] 1 | Incorrect. Both the first and third items are included.


    .. multichoice::

        If ``items = ["a", "b", "c", "b"]``, what does ``items.remove("b")`` do?

        [ ] Removes both "b" elements | Incorrect. remove() only deletes the first occurrence.
        [x] Removes the first "b" at index 1 | Correct! remove() finds and deletes only the first matching value.
        [ ] Removes the last "b" at index 3 | Incorrect. It works from left to right.
        [ ] Raises a ValueError | Incorrect. "b" exists in the list, so no error is raised.


    .. multichoice::

        Which expression creates a copy of the list ``data = [1, 2, 3]`` using slicing?

        [ ] data[0:2] | Incorrect. This drops the last element [3].
        [ ] data[1:] | Incorrect. This drops the first element [1].
        [x] data[:] | Correct! Omitted start and stop indices copy the entire list.
        [ ] data[:-1] | Incorrect. This excludes the final item.


    .. multichoice::

        What will ``list(range(2, 10, 3))`` evaluate to?

        [ ] [2, 3, 4, 5, 6, 7, 8, 9, 10] | Incorrect. The third argument specifies a step of 3.
        [x] [2, 5, 8] | Correct! Starts at 2, increments by 3 (5, 8), and stops before reaching 10.
        [ ] [2, 5, 8, 11] | Incorrect. 11 exceeds the stop bound of 10.
        [ ] [3, 6, 9] | Incorrect. The start value is 2, not 3.


    .. multichoice::

        Which function provides loop count indices alongside list items during iteration?

        [ ] range() | Incorrect. range() generates numbers but does not pair them with list values directly.
        [ ] zip() | Incorrect. zip() pairs items from multiple iterables together.
        [x] enumerate() | Correct! enumerate() yields (index, item) pairs during iteration.
        [ ] index() | Incorrect. index() is a list method that returns the position of a specific value.

