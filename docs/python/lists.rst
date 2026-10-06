===========================
Lists
===========================

| A **list** in Python is used to store multiple items in a single variable.
| Lists are ordered, changeable, and created using square brackets ``[]``.
| Each item in a list is separated by a comma.
| Lists can contain items of different data types, including strings, integers, floats, and even other lists.

.. code-block:: python

    # Creating a simple list of fruits
    fruits = ["apple", "banana", "cherry"]

----

Adding Items to a List
======================

To add new items to an existing list, Python gives us three primary methods:

* ``.append(item)``: Adds a single item to the **very end** of the list.
* ``.insert(index, item)``: Adds an item at a **specific position (index)**. Remember that Python counts starting from ``0``.
* ``.extend(iterable)``: Appends **multiple items** from another list (or iterable) to the end of the current list.

The .append() Method
--------------------

The ``.append(item)`` method adds a single item to the **very end** of the list.

.. code-block:: python

    inventory = ["sword", "shield"]

    # Adds "potion" to the end
    inventory.append("potion")
    print(inventory)  # Output: ["sword", "shield", "potion"]

The .insert() Method
--------------------

The ``.insert(index, item)`` method adds an item at a **specific position (index)**. Remember that Python uses zero-based indexing, so ``0`` is the first position.

.. code-block:: python

    inventory = ["sword", "shield", "potion"]

    # Inserts "map" at index 1 (second position)
    inventory.insert(1, "map")
    print(inventory)  # Output: ["sword", "map", "shield", "potion"]

The .extend() Method
--------------------

The ``.extend(iterable)`` method appends **multiple items** from another list (or iterable) to the end of the current list.

.. code-block:: python

    inventory = ["sword", "map", "shield", "potion"]
    more_items = ["bow", "arrow"]

    # Adds multiple items from another list to the end
    inventory.extend(more_items)
    print(inventory)  # Output: ["sword", "map", "shield", "potion", "bow", "arrow"]

Quiz: Adding Items
------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. To add a single new item to the very end of a list, use the @@.append()@@ method.
    2. To place an item at a specific position in a list, use the @@.insert()@@ method.
    3. To add all items from another list to the end of your current list, use the @@.extend()@@ method.
    4. Python list indices always start counting from the number @@0@@.
    5. Lists in Python are defined using square @@brackets@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Create an inventory list, add a shield to the end, and print the result.

.. ordering::

    inventory = ["sword"]
    inventory.append("shield")
    print(inventory)

----

**Example 2:** Create a fruit list, insert a mango at the front (index 0), and print the list.

.. ordering::

    fruits = ["apple", "banana"]
    fruits.insert(0, "mango")
    print(fruits)

----

**Example 3:** Create a list of primary colors, extend it with secondary colors, and print the total list.

.. ordering::

    primary = ["red", "blue", "green"]
    secondary = ["yellow", "magenta", "cyan"]
    primary.extend(secondary)
    print(primary)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Which method adds a single item to the very end of a Python list?

        [x] .append() | Correct! .append() adds one element to the end.
        [ ] .insert() | Incorrect. .insert() requires a specific index position.
        [ ] .extend() | Incorrect. .extend() is used to combine another list into the current list.
        [ ] .add() | Incorrect. Python lists do not have an .add() method.


    .. multichoice::

        Where does ``inventory.insert(0, "map")`` place the string ``"map"``?

        [x] At index 0 (the very start of the list) | Correct! Index 0 is the first position.
        [ ] At index 1 (the second position) | Incorrect. Index 0 refers to the first position.
        [ ] At the end of the list | Incorrect. To add to the end, use .append().
        [ ] It replaces whatever was at index 0 | Incorrect. .insert() shifts existing items right without overwriting them.


    .. multichoice::

        What happens if you use ``.extend(["a", "b"])`` on a list named ``letters``?

        [ ] Only "a" is added to the list | Incorrect. .extend() adds all items from the passed list.
        [ ] A list containing ["a", "b"] is inserted as a single nested element | Incorrect. That would happen if you used .append(["a", "b"]).
        [x] "a" and "b" are added individually to the end of ``letters`` | Correct! .extend() unwraps the list and adds each element.
        [ ] An error is raised | Incorrect. .extend() takes an iterable like a list as its argument.


    .. multichoice::

        Which code block correctly adds ``"dragon"`` as the second item in a list named ``monsters``?

        [ ] monsters.append("dragon") | Incorrect. .append() places items at the end.
        [x] monsters.insert(1, "dragon") | Correct! Index 1 represents the second position in a list.
        [ ] monsters.extend("dragon") | Incorrect. .extend() with a string will unpack every character ('d', 'r', 'a'...) separately.
        [ ] monsters.insert(2, "dragon") | Incorrect. Index 2 represents the third position.


    .. multichoice::

        What is the difference between ``.append()`` and ``.extend()`` when passed a list ``[1, 2]``?

        [x] .append() adds the list as 1 single element, while .extend() adds 1 and 2 as separate elements | Correct! .append() keeps nested structures while .extend() flattens them.
        [ ] .append() adds elements to the start, while .extend() adds to the end | Incorrect. Both add to the end of the list.
        [ ] .append() works only on numbers, while .extend() works only on strings | Incorrect. Both work with any data type.
        [ ] There is no difference between them | Incorrect. They handle list arguments differently.


    .. multichoice::

        What will ``items = ["book"]; items.extend(["pen", "ruler"]); print(len(items))`` output?

        [ ] 1 | Incorrect. Two new items were added.
        [ ] 2 | Incorrect. The original item "book" remains in the list.
        [x] 3 | Correct! "book", "pen", and "ruler" make 3 items in total.
        [ ] 4 | Incorrect. Exactly 2 items were added to 1 existing item.


    .. multichoice::

        How do you add multiple items from ``new_scores`` into an existing list ``all_scores``?

        [ ] all_scores.add(new_scores) | Incorrect. .add() is not a list method.
        [ ] all_scores.insert(new_scores) | Incorrect. .insert() requires an index argument.
        [x] all_scores.extend(new_scores) | Correct! .extend() combines elements from new_scores into all_scores.
        [ ] all_scores.push(new_scores) | Incorrect. .push() is used in JavaScript, not Python.


    .. multichoice::

        What bracket symbol must be used when creating a new list?

        [ ] Curly braces {} | Incorrect. {} creates dictionaries or sets.
        [ ] Parentheses () | Incorrect. () creates tuples or surrounds function arguments.
        [x] Square brackets [] | Correct! Lists use square brackets [].
        [ ] Angle brackets <> | Incorrect. <> are comparison operators in Python.


    .. multichoice::

        Given ``nums = [10, 30]``, which command makes the list ``[10, 20, 30]``?

        [ ] nums.append(20) | Incorrect. .append(20) makes [10, 30, 20].
        [x] nums.insert(1, 20) | Correct! Index 1 places 20 between 10 and 30.
        [ ] nums.extend(20) | Incorrect. Integers are not iterable in .extend().
        [ ] nums.insert(20, 1) | Incorrect. The first argument of .insert() must be the index (1), not the value (20).


    .. multichoice::

        What happens if you run ``data = [1, 2]; data.extend("34")``?

        [x] ``data`` becomes ``[1, 2, '3', '4']`` | Correct! Strings are iterable, so .extend() adds each character as an item.
        [ ] ``data`` becomes ``[1, 2, '34']`` | Incorrect. .extend() iterates through the string characters.
        [ ] Raises a TypeError | Incorrect. Strings are valid iterables for .extend().
        [ ] ``data`` becomes ``[1, 2, 34]`` | Incorrect. The items added are strings ('3', '4'), not integers.

----

Deleting Items from a List
==========================

Python provides several ways to remove items depending on whether you know the item's **value**, its **position (index)**, or if you want to wipe the list completely.

* ``.remove(item)``: Deletes the **first matching item** by value.
* ``.pop(index)``: Removes and returns the item at a specific index. If no index is given, it removes the **last item**.
* ``del list[index]``: Deletes an item at a specific index using the ``del`` statement.
* ``.clear()``: Removes **all items** from the list, leaving it completely empty ``[]``.


The .remove() Method
--------------------

The ``.remove(item)`` method searches for an item by its value and deletes the **first matching occurrence** from the list.

.. code-block:: python

    pets = ["dog", "cat", "fish", "cat"]

    # Removes the first occurrence of "cat"
    pets.remove("cat")
    print(pets)  # Output: ["dog", "fish", "cat"]

The .pop() Method
-----------------

The ``.pop(index)`` method removes and returns the item at a specific index. If no index argument is provided, it automatically removes and returns the **very last item**.

.. code-block:: python

    pets = ["dog", "fish", "cat"]

    # Removes and returns the item at index 0 ("dog")
    removed_pet = pets.pop(0)
    print(removed_pet)  # Output: "dog"
    print(pets)         # Output: ["fish", "cat"]

The del Statement
-----------------

The ``del`` statement deletes an item at a specific index without returning its value. It can also be used to delete slices or entire variables.

.. code-block:: python

    pets = ["fish", "cat"]

    # Deletes the item at index 1 ("cat")
    del pets[1]
    print(pets)  # Output: ["fish"]

The .clear() Method
-------------------

The ``.clear()`` method removes **all items** from the list at once, leaving behind a completely empty list ``[]``.

.. code-block:: python

    pets = ["fish"]

    # Wipes all remaining items from the list
    pets.clear()
    print(pets)  # Output: []


Quiz: Deleting Items
--------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. To delete an item by value rather than position, use the @@.remove()@@ method.
    2. To delete and return an item by index, use the @@.pop()@@ method.
    3. If no argument is passed to ``.pop()``, it automatically removes the @@last@@ item.
    4. You can use the @@del@@ keyword followed by ``list[index]`` to delete an item at a specific position.
    5. Attempting to ``.remove()`` an item that does not exist in the list raises a @@ValueError@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Create a list of animals, remove `"dog"` by value, and print the remaining list.

.. ordering::

    animals = ["cat", "dog", "bird"]
    animals.remove("dog")
    print(animals)

----

**Example 2:** Create a scores list, pop the first score (index 0), and print the popped score.

.. ordering::

    scores = [100, 85, 90]
    removed_score = scores.pop(0)
    print(removed_score)

----

**Example 3:** Create a list of colors, delete the middle color using `del`, and print the list.

.. ordering::

    colors = ["red", "green", "blue"]
    del colors[1]
    print(colors)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Which method removes an item by its value rather than its index?

        [x] .remove() | Correct! .remove() searches for a matching value and deletes it.
        [ ] .pop() | Incorrect. .pop() uses index numbers.
        [ ] del | Incorrect. del uses index brackets.
        [ ] .clear() | Incorrect. .clear() deletes all items in a list.


    .. multichoice::

        What happens when you execute ``nums = [10, 20, 30]; nums.pop()``?

        [ ] 10 is removed | Incorrect. Without an argument, .pop() targets the last item.
        [ ] 20 is removed | Incorrect. Index 1 (20) is only removed if you pass .pop(1).
        [x] 30 is removed | Correct! Calling .pop() with no parameters removes the last item.
        [ ] An error occurs | Incorrect. .pop() works without parameters on non-empty lists.


    .. multichoice::

        If ``items = ["apple", "banana", "apple"]``, what does ``items.remove("apple")`` do?

        [ ] Removes all occurrences of "apple" | Incorrect. .remove() only deletes the first match it finds.
        [x] Removes only the first "apple" at index 0 | Correct! .remove() stops scanning after finding and deleting the first match.
        [ ] Removes the last "apple" at index 2 | Incorrect. It searches left-to-right and deletes the first match.
        [ ] Raises a ValueError | Incorrect. "apple" exists in the list.


    .. multichoice::

        How do you delete the item at index 2 using the ``del`` keyword?

        [x] del items[2] | Correct! Proper syntax is del list_name[index].
        [ ] del(items, 2) | Incorrect. del is a statement, not a function structured like this.
        [ ] items.del[2] | Incorrect. del is not a method attached to list objects.
        [ ] del items(2) | Incorrect. List indices must use square brackets [].


    .. multichoice::

        What error occurs if you run ``colors = ["red"]; colors.remove("blue")``?

        [ ] IndexError | Incorrect. IndexError occurs when an index is out of bounds.
        [x] ValueError | Correct! Searching for a non-existent item in .remove() raises a ValueError.
        [ ] TypeError | Incorrect. Passing a string to .remove() is valid syntax.
        [ ] NameError | Incorrect. NameError occurs when a variable name is not defined.


    .. multichoice::

        Given ``letters = ["a", "b", "c"]``, what does ``popped = letters.pop(1)`` store in ``popped``?

        [ ] "a" | Incorrect. "a" is at index 0.
        [x] "b" | Correct! .pop(1) removes and returns "b" at index 1.
        [ ] "c" | Incorrect. "c" is at index 2.
        [ ] None | Incorrect. .pop() returns the removed value.


    .. multichoice::

        Which statement about ``.pop()`` vs ``del`` is true?

        [x] .pop() returns the removed item, whereas del does not | Correct! .pop() can be assigned to a variable to save the removed item.
        [ ] del can take no arguments, whereas .pop() requires an index | Incorrect. .pop() can take no arguments; del requires a target.
        [ ] Both remove items exclusively by value | Incorrect. Both remove items by index.
        [ ] .pop() works on dictionaries only, while del works on lists | Incorrect. Both work on lists.


    .. multichoice::

        What will be the value of ``pets`` after ``pets = ["cat", "dog"]; del pets[0]``?

        [ ] ["cat", "dog"] | Incorrect. Index 0 was deleted.
        [x] ["dog"] | Correct! "cat" at index 0 is removed, leaving ["dog"].
        [ ] ["cat"] | Incorrect. "cat" was at index 0.
        [ ] [] | Incorrect. Only index 0 was deleted, not the whole list.


    .. multichoice::

        What does ``items = [1, 2, 3]; items.pop(-1)`` remove?

        [ ] The first item (1) | Incorrect. Index -1 refers to the last element.
        [ ] The second item (2) | Incorrect. Index -1 targets the last position.
        [x] The last item (3) | Correct! Negative indices count from the end; -1 is the last item.
        [ ] Raises an IndexError | Incorrect. Negative indexing is valid in Python.


    .. multichoice::

        How do you remove ALL items from a list named ``data`` so it becomes ``[]``?

        [ ] data.remove() | Incorrect. .remove() requires an argument.
        [ ] data.pop(all) | Incorrect. Invalid syntax for .pop().
        [x] data.clear() | Correct! .clear() removes all elements from a list.
        [ ] del data | Incorrect. del data deletes the variable entirely, not just its contents.

----

Sorting and Reversing Lists
===========================

You can reorder the items inside a list using methods that modify the list in place, or use functions that create a new sorted list:

* ``.sort()``: Sorts the list in **ascending order** in place (alphabetical for text, smallest-to-largest for numbers).
* ``.sort(reverse=True)``: Sorts the list in **descending order** in place.
* ``sorted(iterable)``: Returns a **new** sorted list without modifying the original list. Can also take ``reverse=True``.
* ``.reverse()``: Reverses the current order of elements in place **without** alphabetizing or numerical sorting.


The .sort() Method
------------------

The ``.sort()`` method reorders items in **ascending order** directly inside the original list (alphabetically for text, or smallest-to-largest for numbers).

.. code-block:: python

    scores = [45, 12, 89, 33]

    # Sorts the original list in ascending order
    scores.sort()
    print(scores)  # Output: [12, 33, 45, 89]

Sorting in Descending Order (.sort(reverse=True))
-------------------------------------------------

Passing the parameter ``reverse=True`` into the ``.sort()`` method reorders the list in **descending order** (largest-to-smallest or reverse alphabetical).

.. code-block:: python

    scores = [12, 33, 45, 89]

    # Sorts the original list in descending order
    scores.sort(reverse=True)
    print(scores)  # Output: [89, 45, 33, 12]

The sorted() Function
---------------------

The ``sorted(iterable)`` built-in function returns a **brand new** sorted list while leaving the original list completely unchanged. It also accepts ``reverse=True``.

.. code-block:: python

    numbers = [5, 2, 8, 1]

    # Creates a new sorted list without modifying the original
    sorted_numbers = sorted(numbers)
    print(sorted_numbers)  # Output: [1, 2, 5, 8]
    print(numbers)         # Output: [5, 2, 8, 1]

The .reverse() Method
---------------------

The ``.reverse()`` method simply flips the current order of elements in place **without** performing any alphabetical or numerical sorting.

.. code-block:: python

    colors = ["red", "blue", "green"]

    # Reverses the element positions in place
    colors.reverse()
    print(colors)  # Output: ["green", "blue", "red"]


Quiz: Sorting and Reversing
---------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. To arrange items in ascending or alphabetical order, call the @@.sort()@@ method.
    2. To sort a list in descending order, pass @@reverse=True@@ into the ``.sort()`` method.
    3. To flip the order of items without sorting them numerically or alphabetically, use the @@.reverse()@@ method.
    4. By default, calling ``.sort()`` on numbers orders them from @@smallest@@ to largest.
    5. Both ``.sort()`` and ``.reverse()`` modify the original list in @@place@@ rather than returning a new list.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Create a list of unsorted numbers, sort them in ascending order, and print the result.

.. ordering::

    numbers = [42, 11, 88, 23]
    numbers.sort()
    print(numbers)

----

**Example 2:** Create a list of names, sort them in reverse alphabetical order, and print them.

.. ordering::

    names = ["Charlie", "Alice", "Bob"]
    names.sort(reverse=True)
    print(names)

----

**Example 3:** Create a list of steps, reverse their order, and print the reversed steps.

.. ordering::

    steps = ["Step 1", "Step 2", "Step 3"]
    steps.reverse()
    print(steps)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What does calling ``.sort()`` on a list of strings do by default?

        [x] Sorts them in alphabetical order (A to Z) | Correct! Default sorting for strings is alphabetical.
        [ ] Sorts them in reverse alphabetical order (Z to A) | Incorrect. Reverse sorting requires reverse=True.
        [ ] Sorts them by word length | Incorrect. Default sort handles lexicographical order.
        [ ] Flips the list upside down without sorting | Incorrect. Flipping without sorting is done by .reverse().


    .. multichoice::

        What is the result of ``nums = [3, 1, 4]; nums.sort()``?

        [ ] [3, 1, 4] | Incorrect. .sort() modifies the list.
        [x] [1, 3, 4] | Correct! .sort() orders numbers from smallest to largest.
        [ ] [4, 3, 1] | Incorrect. Smallest to largest is default.
        [ ] [1, 4, 3] | Incorrect. Numbers are ordered sequentially.


    .. multichoice::

        How do you sort a list of numbers from highest to lowest?

        [ ] numbers.sort(descending=True) | Incorrect. The parameter name is reverse, not descending.
        [x] numbers.sort(reverse=True) | Correct! Setting reverse=True sorts in descending order.
        [ ] numbers.reverse(sort=True) | Incorrect. .reverse() does not take a sort argument.
        [ ] numbers.sort_desc() | Incorrect. No such method exists in Python.


    .. multichoice::

        Given ``items = ["a", "c", "b"]``, what does ``items.reverse()`` produce?

        [ ] ["a", "b", "c"] | Incorrect. .reverse() does not sort alphabetically.
        [x] ["b", "c", "a"] | Correct! It flips the current list order directly.
        [ ] ["c", "b", "a"] | Incorrect. That would be alphabetical reverse sort.
        [ ] ["c", "a", "b"] | Incorrect. It flips end-to-end.


    .. multichoice::

        What value is returned when you assign ``x = my_list.sort()``?

        [ ] The sorted list | Incorrect. .sort() modifies in place and returns None.
        [x] None | Correct! Methods that modify lists in place return None.
        [ ] True | Incorrect. It returns None.
        [ ] An integer count | Incorrect. It returns None.


    .. multichoice::

        What happens if you try to run ``.sort()`` on a list containing both numbers and strings like ``[1, "apple", 2]``?

        [ ] Numbers come first, then strings | Incorrect. Python 3 cannot compare strings and integers directly.
        [ ] Strings come first, then numbers | Incorrect. Mixed type sorting is not supported automatically.
        [x] Python raises a TypeError | Correct! Comparing str and int raises a TypeError during sorting.
        [ ] The list remains unchanged | Incorrect. An exception is thrown.


    .. multichoice::

        Which method flips a list's elements end-to-end without comparing their values?

        [ ] .sort() | Incorrect. .sort() compares values.
        [ ] .extend() | Incorrect. .extend() adds elements.
        [x] .reverse() | Correct! .reverse() simply reverses index order.
        [ ] .pop() | Incorrect. .pop() deletes elements.


    .. multichoice::

        What will ``vals = [10, 5, 20]; vals.sort(); vals.reverse(); print(vals)`` output?

        [ ] [5, 10, 20] | Incorrect. Sorting then reversing gives descending order.
        [x] [20, 10, 5] | Correct! Sorting gives [5, 10, 20], and reversing gives [20, 10, 5].
        [ ] [10, 5, 20] | Incorrect. The methods alter the list.
        [ ] [5, 20, 10] | Incorrect. Reversing [5, 10, 20] gives [20, 10, 5].


    .. multichoice::

        If ``words = ["banana", "apple", "cherry"]``, what is ``words`` after ``words.sort()``?

        [x] ["apple", "banana", "cherry"] | Correct! Alphabetical order.
        [ ] ["cherry", "banana", "apple"] | Incorrect. Reverse alphabetical.
        [ ] ["banana", "apple", "cherry"] | Incorrect. List is modified.
        [ ] ["apple", "cherry", "banana"] | Incorrect. Incorrect alphabetical order.


    .. multichoice::

        How does built-in function ``sorted(my_list)`` differ from method ``my_list.sort()``?

        [x] sorted() returns a new sorted list, while .sort() modifies the original list | Correct! sorted() leaves the original list untouched.
        [ ] sorted() works only on strings, while .sort() works on numbers | Incorrect. Both work on both types.
        [ ] .sort() returns a new list, while sorted() modifies in place | Incorrect. It is the opposite.
        [ ] There is no difference | Incorrect. Their return values and side effects differ.

----

Iterating Through a List
========================

Iterating means going through items in a list one by one. We use a **for loop** to do this efficiently.

.. code-block:: python

    team = ["Alex", "Sam", "Jordan"]

    # Loop through each item in the list
    for player in team:
        print(f"Welcome to the team, {player}!")


Quiz: Iterating Through Lists
-----------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. To step through each item in a list one by one, use a @@for@@ loop.
    2. The word following ``for`` in a loop serves as a loop @@variable@@ holding the current item.
    3. The header line of a ``for`` loop must end with a @@colon@@.
    4. Code inside the loop block must use four spaces of @@indentation@@ to run properly.
    5. The built-in function @@len()@@ can be used to find the total number of iterations a loop over a list will make.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Create a list of fruits and use a `for` loop to print each fruit.

.. ordering::

    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)

----

**Example 2:** Create a list of numbers, calculate their double in a loop, and print each doubled value.

.. ordering::

    numbers = [1, 2, 3]
    for n in numbers:
        double_val = n * 2
        print(double_val)

----

**Example 3:** Create a list of names, check if each name is `"Alice"`, and print a greeting when matched.

.. ordering::

    names = ["Alice", "Bob"]
    for name in names:
        if name == "Alice":
            print("Hello Alice!")


Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Which keyword starts a loop that iterates over items in a list?

        [x] for | Correct! Python uses for loops to iterate over sequences.
        [ ] loop | Incorrect. loop is not a Python keyword.
        [ ] foreach | Incorrect. foreach is used in languages like PHP or C#.
        [ ] repeat | Incorrect. repeat is not a Python keyword.


    .. multichoice::

        How many times will the print statement execute in ``for x in [10, 20, 30, 40]: print(x)``?

        [ ] 3 times | Incorrect. There are 4 items in the list.
        [x] 4 times | Correct! The loop runs once for each item in the list.
        [ ] 5 times | Incorrect. The loop visits only items in the list.
        [ ] 1 time | Incorrect. The loop iterates over all items.


    .. multichoice::

        What character MUST end the first line of a ``for`` loop statement?

        [ ] Semicolon ; | Incorrect. Python uses colons for block headers.
        [x] Colon : | Correct! Compound statements in Python end header lines with a colon.
        [ ] Period . | Incorrect. Python does not use periods for headers.
        [ ] Comma , | Incorrect. Commas separate items, not header blocks.


    .. multichoice::

        In ``for item in inventory:``, what does ``item`` represent?

        [ ] The entire list ``inventory`` | Incorrect. ``item`` represents one element at a time.
        [x] A variable that holds the current item during each iteration | Correct! It temporarily stores the active element during that loop step.
        [ ] An integer index number starting from 0 | Incorrect. It holds the actual value, not the index.
        [ ] A function name | Incorrect. It is an iteration variable.


    .. multichoice::

        What error occurs if you forget to indent code inside a ``for`` loop body?

        [x] IndentationError | Correct! Python requires indented blocks after colons.
        [ ] SyntaxError | Incorrect. Specifically, Python raises IndentationError.
        [ ] NameError | Incorrect. Missing indentation causes an IndentationError.
        [ ] TypeError | Incorrect. Indentation governs block structures.


    .. multichoice::

        Which function can be combined with ``range()`` to loop using index numbers?

        [ ] count() | Incorrect.
        [x] len() | Correct! range(len(my_list)) generates index positions 0 to len-1.
        [ ] total() | Incorrect.
        [ ] size() | Incorrect.


    .. multichoice::

        What will ``for c in ["a", "b"]: print(c, end="")`` print?

        [ ] a\nb | Incorrect. end="" prevents newlines.
        [x] ab | Correct! It prints "a" and "b" continuously on one line.
        [ ] ["a", "b"] | Incorrect. The loop prints elements individually.
        [ ] a b | Incorrect. No space separator was specified.



