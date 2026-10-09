===========================
Dictionaries
===========================

| A **dictionary** in Python is used to store data in **key-value pairs**.
| Dictionaries are ordered, changeable, and created using curly braces ``{}``.
| Each key is separated from its value by a colon ``:``, and key-value pairs are separated by commas.
| Dictionaries allow you to look up values quickly using unique keys instead of index numbers.
| e.g. student["name"] returns "Alex".

.. code-block:: python

    # Creating a simple dictionary of a student profile
    student = {
        "name": "Alex",
        "age": 13,
        "grade": 8
    }

----

Adding and Modifying Items in a Dictionary
===========================================

To add a new key-value pair or change an existing value, you access the key using square brackets ``[]`` and assign a value to it:

- ``dict[key] = value``: If the key **does not exist**, it adds the new key-value pair to the dictionary.
- ``dict[key] = new_value``: If the key **already exists**, it overwrites and updates the existing value.
- ``.update(other_dict)``: Adds or updates **multiple key-value pairs** at once from another dictionary.


**Setting value**
------------------

.. code-block:: python

    inventory = {"apples": 5, "bananas": 2}

    # Adds a new key "oranges" with a value of 10
    inventory["oranges"] = 10
    # Result: {"apples": 5, "bananas": 2, "oranges": 10}
    print(inventory)

**Replace value**
------------------

.. code-block:: python

    inventory = {"apples": 5, "bananas": 2}

    # Updates the existing key "apples" with a new value
    inventory["apples"] = 8
    # Result: {"apples": 8, "bananas": 2}
    print(inventory)


**Update method**
------------------

.. code-block:: python

    inventory = {"apples": 5, "bananas": 2}

    # Adds multiple items from another dictionary
    more_items = {"grapes": 4, "peaches": 6}
    inventory.update(more_items)
    # Result: {"apples": 58, "bananas": 2, "grapes": 4, "peaches": 6}
    print(inventory)


----

Quiz: Adding and Modifying Items
--------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Dictionaries store information using key-value @@pairs@@.
    2. To assign or access a value using a key, you place the key inside square @@brackets@@.
    3. Assigning a value to an existing key will @@overwrite@@ its previous value.
    4. To add multiple key-value pairs from another dictionary at once, use the @@.update()@@ method.
    5. Dictionaries in Python are defined using curly @@braces@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Create a player dictionary, add a score key, and print the result.

.. ordering::

    player = {"name": "Sam"}
    player["score"] = 100
    print(player)

----

**Example 2:** Create a fruit count dictionary, update the quantity of apples, and print the dictionary.

.. ordering::

    counts = {"apples": 3, "peaches": 5}
    counts["apples"] = 10
    print(counts)

----

**Example 3:** Create a dictionary of primary inventory, update it with bonus inventory, and print the dictionary.

.. ordering::

    items = {"coins": 50}
    bonus = {"gems": 5, "potions": 2}
    items.update(bonus)
    print(items)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 10


    .. multichoice::

        Which symbol is used to create a new dictionary in Python?

        [x] Curly braces {} | Correct! Dictionaries are defined using curly braces.
        [ ] Square brackets [] | Incorrect. Square brackets are used for lists.
        [ ] Parentheses () | Incorrect. Parentheses are used for tuples and functions.
        [ ] Angle brackets <> | Incorrect. Angle brackets are used for comparison operators.


    .. multichoice::

        How do you add a new key ``"score"`` with a value of ``50`` to a dictionary named ``player``?

        [x] player["score"] = 50 | Correct! Using square brackets with a key assigns a new value.
        [ ] player.append("score", 50) | Incorrect. Dictionaries do not have an .append() method.
        [ ] player.add("score" = 50) | Incorrect. .add() is not used for dictionaries.
        [ ] player{"score"} = 50 | Incorrect. Bracket notation [] must be used to access keys.


    .. multichoice::

        What happens if you run ``scores["Alex"] = 95`` on a dictionary that ALREADY has a key ``"Alex"`` with a value of ``80``?

        [ ] A duplicate key is added to the dictionary | Incorrect. Keys in a dictionary must be unique.
        [ ] An error is raised | Incorrect. Updating existing keys is valid Python syntax.
        [x] The value for "Alex" changes from 80 to 95 | Correct! Assigning to an existing key updates its value.
        [ ] Nothing changes | Incorrect. The value is overwritten.


    .. multichoice::

        Which character separates each key from its corresponding value in a dictionary?

        [ ] Comma , | Incorrect. Commas separate individual key-value pairs from each other.
        [x] Colon : | Correct! Colons separate a key from its value (key: value).
        [ ] Equals sign = | Incorrect. Equals signs are used for variable assignment.
        [ ] Dash - | Incorrect. Dashes are not used in dictionary syntax.


    .. multichoice::

        What method allows you to add multiple key-value pairs from another dictionary?

        [x] .update() | Correct! .update() combines key-value pairs from one dictionary into another.
        [ ] .extend() | Incorrect. .extend() is a list method.
        [ ] .append() | Incorrect. .append() is a list method.
        [ ] .concat() | Incorrect. .concat() is not a standard dictionary method in Python.


    .. multichoice::

        Given ``hero = {"hp": 100}``, what is the output of ``hero["hp"] = hero["hp"] + 20; print(hero["hp"])``?

        [ ] 100 | Incorrect. The value was increased by 20.
        [x] 120 | Correct! 100 + 20 updates "hp" to 120.
        [ ] 20 | Incorrect. The original value was added to 20.
        [ ] Error | Incorrect. Reassigning values based on existing keys is valid.


    .. multichoice::

        What happens if you execute ``data = {"a": 1}; data.update({"b": 2, "c": 3})``?

        [ ] Only "b" is added | Incorrect. .update() adds all key-value pairs in the dictionary.
        [x] "b": 2 and "c": 3 are both added to ``data`` | Correct! .update() adds all entries from the passed dictionary.
        [ ] ``data`` is overwritten so it only contains {"b": 2, "c": 3} | Incorrect. .update() merges new entries into the existing dictionary.
        [ ] A TypeError is raised | Incorrect. Passing a dictionary to .update() is correct.


    .. multichoice::

        Which of the following is a valid Python dictionary definition?

        [x] student = {"name": "Maya", "age": 12} | Correct! Uses curly braces with key: value pairs separated by commas.
        [ ] student = ["name": "Maya", "age": 12] | Incorrect. Square brackets are for lists.
        [ ] student = ("name" -> "Maya", "age" -> 12) | Incorrect. Incorrect syntax for dictionaries.
        [ ] student = {"name" = "Maya", "age" = 12} | Incorrect. Keys and values must be separated by colons, not equals signs.


    .. multichoice::

        Why are keys in a dictionary required to be unique?

        [x] So Python knows exactly which value to look up for that key | Correct! Unique keys ensure unambiguous value lookups.
        [ ] Keys do not have to be unique | Incorrect. Duplicate keys are not allowed; later entries overwrite earlier ones.
        [ ] Because Python can only store numbers as keys | Incorrect. Strings, integers, and other immutable types can be keys.
        [ ] To keep the dictionary sorted | Incorrect. Key uniqueness is about lookups, not sorting.


    .. multichoice::

        What will ``item = {}; item["type"] = "sword"; print(len(item))`` output?

        [ ] 0 | Incorrect. A key-value pair was added.
        [x] 1 | Correct! There is 1 key-value pair in the dictionary.
        [ ] 2 | Incorrect. A key-value pair counts as 1 single entry in len().
        [ ] 5 | Incorrect. len() counts pairs, not characters in string values.

----

Deleting Items from a Dictionary
================================

Python provides several ways to remove key-value pairs from a dictionary depending on whether you want to save the removed value, use the key name, or clear everything:

- ``.pop(key)``: Removes the key-value pair and **returns the value**.
- ``del dict[key]``: Deletes a key-value pair using the ``del`` statement.
- ``.popitem()``: Removes and returns the **last inserted** key-value pair as a tuple.
- ``.clear()``: Removes **all items** from the dictionary, leaving it completely empty ``{}``.

.. code-block:: python

    pet = {"type": "dog", "name": "Buddy", "age": 3, "color": "brown"}

    # Removes "age" and stores its value (3) in a variable
    removed_age = pet.pop("age")  # Result: {"type": "dog", "name": "Buddy", "color": "brown"}
    print(removed_age)
    print(pet)

.. code-block:: python

    pet = {"type": "dog", "name": "Buddy", "color": "brown"}

    # Deletes the key "color" and its value
    del pet["color"]              # Result: {"type": "dog", "name": "Buddy"}
    print(pet)

.. code-block:: python

    pet = {"type": "dog", "name": "Buddy"}

    # Removes the last inserted item ("name": "Buddy")
    last_removed = pet.popitem()     # Result: {"type": "dog"}
    print(last_removed)
    print(pet)

.. code-block:: python

    pet = {"type": "dog"}

    # Wipes all key-value pairs from the dictionary
    pet.clear()                   # Result: {}
    print(pet)


----

Quiz: Deleting Items
--------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. To delete a key-value pair and get its value returned, use the @@.pop()@@ method.
    2. You can delete a key-value pair without returning its value using the @@del@@ keyword followed by ``dict[key]``.
    3. The @@.popitem()@@ method removes the last inserted key-value pair and and returns its value.
    4. Attempting to delete a key that does not exist in a dictionary raises a @@KeyError@@.
    5. To wipe all key-value pairs from a dictionary, call the @@.clear()@@ method.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Create a profile dictionary, delete the `"city"` key using `del`, and print the dictionary.

.. ordering::

    user = {"name": "Liam", "city": "Sydney"}
    del user["city"]
    print(user)

----

**Example 2:** Create a game stats dictionary, pop the `"lives"` key into a variable, and print the popped value.

.. ordering::

    stats = {"score": 250, "lives": 3}
    lost_lives = stats.pop("lives")
    print(lost_lives)

----

**Example 3:** Create a dictionary, clear all its contents, and print the empty dictionary.

.. ordering::

    data = {"a": 1, "b": 2}
    data.clear()
    print(data)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Which method deletes a key and returns its associated value?

        [x] .pop() | Correct! .pop(key) removes the key and returns its value.
        [ ] del | Incorrect. del deletes the entry but does not return a value.
        [ ] .remove() | Incorrect. Dictionaries do not have a .remove() method.
        [ ] .clear() | Incorrect. .clear() deletes all key-value pairs.


    .. multichoice::

        What happens if you try to delete a key that does NOT exist using ``del student["grade"]``?

        [ ] The command is ignored | Incorrect. Python will raise an exception.
        [x] Python raises a KeyError | Correct! Accessing or deleting a non-existent key raises a KeyError.
        [ ] Python raises an IndexError | Incorrect. IndexErrors occur with sequence position numbers, not dictionary keys.
        [ ] The dictionary is set to None | Incorrect. An exception is raised.


    .. multichoice::

        If ``person = {"name": "Ana", "age": 14}``, what does ``person.pop("age")`` return?

        [ ] "name" | Incorrect. "age" was specified as the key to pop.
        [ ] "age" | Incorrect. .pop() returns the value, not the key name.
        [x] 14 | Correct! .pop("age") returns the value associated with the key "age".
        [ ] {"age": 14} | Incorrect. .pop() returns just the value, not a dictionary.


    .. multichoice::

        How do you delete the key ``"level"`` from a dictionary named ``game`` using the ``del`` statement?

        [x] del game["level"] | Correct! Proper syntax is del dict_name[key].
        [ ] del(game, "level") | Incorrect. del is a statement, not a function.
        [ ] game.del["level"] | Incorrect. del is not a method attached to dictionaries.
        [ ] del game("level") | Incorrect. Keys must be specified inside square brackets [].


    .. multichoice::

        What is the difference between ``.pop("key")`` and ``del dict["key"]``?

        [x] .pop() returns the removed value, whereas del does not | Correct! You can store the output of .pop() in a variable.
        [ ] del removes keys, while .pop() removes values only | Incorrect. Both remove the entire key-value pair.
        [ ] .pop() works on lists only, while del works on dictionaries | Incorrect. Both work on dictionaries.
        [ ] There is no difference | Incorrect. Their return values differ.


    .. multichoice::

        What does calling ``.popitem()`` on a dictionary do?

        [x] Removes and returns the last inserted key-value pair | Correct! .popitem() target the most recently added entry.
        [ ] Removes a random item | Incorrect. In modern Python (3.7+), it consistently removes the last inserted item.
        [ ] Removes the first key-value pair | Incorrect. It targeted the last inserted pair.
        [ ] Clears all items | Incorrect. .clear() clears all items.


    .. multichoice::

        What will be the content of ``inventory`` after running ``inventory = {"wood": 10}; inventory.clear()``?

        [ ] {"wood": 10} | Incorrect. .clear() removes all contents.
        [x] {} | Correct! .clear() leaves an empty dictionary.
        [ ] None | Incorrect. The dictionary variable still exists as an empty dict {}.
        [ ] Error | Incorrect. .clear() is a valid dictionary method.


    .. multichoice::

        Given ``book = {"title": "Python", "pages": 200}``, what happens after ``del book["pages"]``?

        [ ] ``book`` becomes ``{"pages": 200}`` | Incorrect. "pages" key was deleted.
        [x] ``book`` becomes ``{"title": "Python"}`` | Correct! The key "pages" and its value 200 are removed.
        [ ] ``book`` becomes ``{}`` | Incorrect. Only "pages" was deleted.
        [ ] A KeyError is raised | Incorrect. "pages" exists in the dictionary.


    .. multichoice::

        What happens if you run ``.pop()`` on a key with a default fallback value specified, like ``info.pop("phone", "N/A")``, when ``"phone"`` is NOT in ``info``?

        [ ] Raises a KeyError | Incorrect. Providing a default value prevents a KeyError.
        [x] Returns "N/A" without raising an error | Correct! The second argument acts as a safe fallback if the key is missing.
        [ ] Returns None | Incorrect. It returns the specified default "N/A".
        [ ] Creates the key "phone" with value "N/A" | Incorrect. .pop() does not add items.


    .. multichoice::

        How do you remove ALL key-value pairs from a dictionary named ``scores``?

        [ ] scores.remove_all() | Incorrect. No such method exists in Python.
        [ ] del scores | Incorrect. del scores deletes the variable itself, not just its entries.
        [x] scores.clear() | Correct! .clear() removes all key-value pairs inside the dictionary.
        [ ] scores.pop() | Incorrect. .pop() requires a key argument.

----

Inspecting Keys, Values, and Items
===================================

Python provides special methods to view the keys, the values, or both together without changing the dictionary:

- ``.keys()``: Returns a view of all **keys** in the dictionary.
- ``.values()``: Returns a view of all **values** in the dictionary.
- ``.items()``: Returns a view of all **key-value pairs** as tuples ``(key, value)``.
- ``key in dict``: Checks if a specific key **exists** in the dictionary (returns ``True`` or ``False``).

.. code-block:: python

    prices = {"apple": 1.5, "banana": 0.8, "orange": 1.2}

    # Get all keys
    all_keys = prices.keys()      # Result: dict_keys(['apple', 'banana', 'orange'])

    # Get all values
    all_values = prices.values()  # Result: dict_values([1.5, 0.8, 1.2])

    # Get key-value pairs
    all_items = prices.items()    # Result: dict_items([('apple', 1.5), ('banana', 0.8), ('orange', 1.2)])

    # Check if a key exists
    has_apple = "apple" in prices # Result: True
    has_grape = "grape" in prices # Result: False


Quiz: Inspecting Keys, Values, and Items
----------------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. To get a list-like view of all key names in a dictionary, call the @@.keys()@@ method.
    2. To get a view of all stored values without their keys, call the @@.values()@@ method.
    3. To get both keys and values paired together as tuples, use the @@.items()@@ method.
    4. To test if a key exists in a dictionary, use the @@in@@ keyword.
    5. The expression ``"age" in {"name": "Sam"}`` evaluates to the boolean value @@False@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Create a dictionary, retrieve all keys, and print them.

.. ordering::

    student = {"name": "Ella", "grade": 7}
    keys_list = student.keys()
    print(keys_list)

----

**Example 2:** Create a menu price dictionary, get all values, and print them.

.. ordering::

    menu = {"pizza": 12, "burger": 10}
    price_values = menu.values()
    print(price_values)

----

**Example 3:** Check if `"cat"` is a key in a pets dictionary and print the result.

.. ordering::

    pets = {"dog": 2, "fish": 5}
    is_present = "cat" in pets
    print(is_present)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What does calling ``.keys()`` on a dictionary return?

        [x] A view of all key names in the dictionary | Correct! .keys() retrieves all dictionary keys.
        [ ] A view of all values in the dictionary | Incorrect. Values are retrieved using .values().
        [ ] A count of how many items exist | Incorrect. Counting items is done using len().
        [ ] A new sorted list of keys and values | Incorrect. It returns a dict_keys view object.


    .. multichoice::

        Given ``scores = {"Alice": 90, "Bob": 85}``, what is the output of ``"Alice" in scores``?

        [x] True | Correct! "Alice" is a key present in the dictionary.
        [ ] False | Incorrect. "Alice" exists as a key.
        [ ] 90 | Incorrect. The in operator returns a boolean (True/False), not the value.
        [ ] KeyError | Incorrect. Checking existence with in does not raise errors for missing items.


    .. multichoice::

        How do you check if a VALUE (e.g. ``90``) exists in a dictionary named ``scores``?

        [ ] 90 in scores | Incorrect. The in operator checks keys by default, not values.
        [x] 90 in scores.values() | Correct! Checking against .values() tests for values instead of keys.
        [ ] 90 in scores.keys() | Incorrect. .keys() only checks key names.
        [ ] scores.has_value(90) | Incorrect. .has_value() is not a Python method.


    .. multichoice::

        What type of data structures are returned inside ``.items()``?

        [ ] Lists | Incorrect. Individual key-value pairs are stored as tuples.
        [ ] Integers | Incorrect. Pairs contain keys and values of any data type.
        [x] Tuples containing (key, value) pairs | Correct! .items() returns pairs in (key, value) format.
        [ ] Dictionaries | Incorrect. They are returned as key-value tuples inside a dict_items view.


    .. multichoice::

        What will ``info = {"a": 1, "b": 2}; print(len(info.keys()))`` output?

        [ ] 1 | Incorrect. There are 2 keys ("a" and "b").
        [x] 2 | Correct! len() counts the 2 keys returned by .keys().
        [ ] 4 | Incorrect. len() counts the keys, not keys + values combined.
        [ ] Error | Incorrect. len() works on dict_keys view objects.


    .. multichoice::

        Which expression tests whether ``"gold"`` is NOT a key in ``inventory``?

        [ ] "gold" not inventory | Incorrect. Incorrect keyword syntax.
        [x] "gold" not in inventory | Correct! not in tests if a key is absent from the dictionary.
        [ ] "gold" != inventory.keys() | Incorrect. Comparing a string to a view object does not test membership properly.
        [ ] inventory.missing("gold") | Incorrect. No such method exists.


    .. multichoice::

        Given ``hero = {"hp": 100, "mp": 50}``, what is the result of ``list(hero.values())``?

        [ ] ["hp", "mp"] | Incorrect. Those are the keys.
        [x] [100, 50] | Correct! .values() returns 100 and 50, converted to a list.
        [ ] [("hp", 100), ("mp", 50)] | Incorrect. That is the output of .items().
        [ ] [150] | Incorrect. It returns individual values, not their sum.


    .. multichoice::

        What does ``"100" in {"score": 100}`` evaluate to?

        [ ] True | Incorrect. "100" is a string value, whereas the key is "score". The in operator checks keys by default.
        [x] False | Correct! "100" is not a KEY in the dictionary.
        [ ] KeyError | Incorrect. The in operator returns False, not an error.
        [ ] None | Incorrect. The in operator returns a boolean.


    .. multichoice::

        If ``data = {"x": 10, "y": 20}``, what does ``for entry in data.items():`` yield in ``entry`` on each step?

        [ ] Just the key string ("x", then "y") | Incorrect. That would happen with for entry in data:.
        [ ] Just the integer value (10, then 20) | Incorrect. That would happen with for entry in data.values():.
        [x] A tuple containing key and value like ("x", 10) | Correct! .items() yields (key, value) tuples.
        [ ] A sub-dictionary | Incorrect. .items() yields tuples.


    .. multichoice::

        Which statement about dictionary keys is TRUE?

        [x] Keys must be unique, but values can be duplicated | Correct! Multiple keys can share the same value (e.g., {"a": 1, "b": 1}).
        [ ] Keys can be duplicated, but values must be unique | Incorrect. Keys must be unique.
        [ ] Both keys and values must always be unique | Incorrect. Values can repeat.
        [ ] Neither keys nor values need to be unique | Incorrect. Keys must be unique.

----

Iterating Through a Dictionary
==============================

Iterating means stepping through entries in a dictionary one by one using a **for loop**. You can iterate over keys, values, or both together.

.. code-block:: python

    scores = {"Alex": 88, "Sam": 92, "Jordan": 79}

    # Loop through keys (default behavior)
    for name in scores:
        print(name)

    # Loop through key and value together using .items()
    for name, score in scores.items():
        print(f"{name} scored {score} points!")


Quiz: Iterating Through Dictionaries
------------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. By default, iterating directly over a dictionary with a ``for`` loop steps through its @@keys@@.
    2. To loop through both keys and values at the same time, call the @@.items()@@ method.
    3. To loop through only the values of a dictionary, use the @@.values()@@ method.
    4. When looping with ``for k, v in dict.items():``, the variable ``k`` holds the @@key@@.
    5. The header line of a dictionary ``for`` loop must end with a @@colon@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Create a dictionary and loop through its keys to print each key name.

.. ordering::

    fruit_colors = {"apple": "red", "banana": "yellow"}
    for fruit in fruit_colors:
        print(fruit)

----

**Example 2:** Loop through values of a price dictionary and print each price.

.. ordering::

    prices = {"bread": 2.5, "milk": 1.5}
    for price in prices.values():
        print(price)

----

**Example 3:** Loop through keys and values together using `.items()` and print formatted sentences.

.. ordering::

    inventory = {"swords": 1, "potions": 5}
    for item, qty in inventory.items():
        print(f"You have {qty} {item}")


Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        When you write ``for x in my_dict:``, what does ``x`` represent during each iteration?

        [x] The current key name | Correct! Direct iteration over a dictionary yields its keys.
        [ ] The current value | Incorrect. To loop over values, use my_dict.values().
        [ ] A tuple of (key, value) | Incorrect. To loop over tuples, use my_dict.items().
        [ ] The entire dictionary | Incorrect. It loops through individual keys one by one.


    .. multichoice::

        Which loop head allows you to unpack both key and value into separate variables ``k`` and ``v``?

        [ ] for k, v in my_dict: | Incorrect. Direct iteration yields keys only, which cannot be unpacked into two variables.
        [ ] for k, v in my_dict.keys(): | Incorrect. .keys() yields single key names only.
        [x] for k, v in my_dict.items(): | Correct! .items() yields (key, value) pairs that unpack cleanly into k and v.
        [ ] for k, v in my_dict.values(): | Incorrect. .values() yields single values only.


    .. multichoice::

        How many times will a ``for`` loop execute when iterating over a dictionary with 4 key-value pairs?

        [ ] 2 times | Incorrect. The loop visits every entry.
        [x] 4 times | Correct! The loop runs once for each key-value pair in the dictionary.
        [ ] 8 times | Incorrect. Key and value pairs count as 1 iteration per entry.
        [ ] 1 time | Incorrect. It iterates through all entries.


    .. multichoice::

        What happens if you try to unpack two variables in a loop without using ``.items()``, like ``for k, v in {"a": 1}:``?

        [ ] It automatically uses values for v | Incorrect. Python will attempt to unpack the key string "a".
        [x] Python raises a ValueError | Correct! A single key string cannot be unpacked into two variables (k and v).
        [ ] It skips the loop | Incorrect. An exception is raised.
        [ ] It prints None for v | Incorrect. An exception is raised.


    .. multichoice::

        Which function can be used to count how many key-value pairs a loop will iterate over?

        [ ] count() | Incorrect. count() is a string/list method.
        [x] len() | Correct! len(my_dict) returns the total number of entries in the dictionary.
        [ ] size() | Incorrect. size() is not a built-in Python function.
        [ ] sum() | Incorrect. sum() calculates numeric totals.


    .. multichoice::

        What will ``for v in {"x": 10, "y": 20}.values(): print(v, end=" ")`` output?

        [ ] x y | Incorrect. .values() iterates over values, not keys.
        [x] 10 20 | Correct! .values() yields 10 and 20.
        [ ] ("x", 10) ("y", 20) | Incorrect. That would require .items().
        [ ] 30 | Incorrect. The loop prints each value separately.


    .. multichoice::

        What error occurs if you forget to indent the body of a ``for`` loop over a dictionary?

        [x] IndentationError | Correct! Python requires indented blocks after compound headers.
        [ ] KeyError | Incorrect. KeyError happens when accessing missing keys.
        [ ] TypeError | Incorrect. Missing block formatting raises IndentationError.
        [ ] NameError | Incorrect. NameError occurs when referencing undefined variables.

----

Getting Values from a Python Dictionary
=========================================

Direct Key Access (Square Brackets)
--------------------------------------

Accessing a dictionary value using square brackets ``dict[key]``.

.. code-block:: python

   person = {"name": "Alice", "age": 30}

   # Accessing an existing key
   name = person["name"]
   print(name)  # Output: Alice

   # Accessing a non-existent key raises a KeyError
   # city = person["city"]  # KeyError: 'city'


Safe Retrieval with ``get()``
--------------------------------

The ``get()`` method avoids raising errors when a key is missing. It returns ``None`` or a custom default value instead.

.. code-block:: python

   person = {"name": "Alice", "age": 30}

   # Returns value if key exists
   age = person.get("age")
   print(age)  # Output: 30

   # Returns None if key does not exist
   city = person.get("city")
   print(city)  # Output: None

   # Returns custom default value if key does not exist
   country = person.get("country", "Unknown")
   print(country)  # Output: Unknown


Retrieve and Remove with ``pop()``
------------------------------------

The ``pop()`` method removes the key from the dictionary and returns its value.

.. code-block:: python

   inventory = {"apples": 5, "bananas": 12}

   # Removes "apples" and returns 5
   apple_count = inventory.pop("apples")
   print(apple_count)  # Output: 5

   # Returns default value if key is missing
   orange_count = inventory.pop("oranges", 0)
   print(orange_count)  # Output: 0


Retrieve and Set Default with ``setdefault()``
------------------------------------------------
Returns the value if the key is in the dictionary. If not, inserts the key with a specified default value and returns it.

.. code-block:: python

   user_settings = {"theme": "dark"}

   # Key exists: returns existing value
   theme = user_settings.setdefault("theme", "light")
   print(theme)  # Output: dark

   # Key missing: sets "language": "en" and returns "en"
   language = user_settings.setdefault("language", "en")
   print(language)  # Output: en

----

Quiz: Getting Values from Dictionaries
--------------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Accessing a missing key directly using square brackets raises a @@KeyError@@.
    2. To safely retrieve a value without raising an exception when the key is missing, use the @@.get()@@ method.
    3. The default value returned by ``dict.get("missing_key")`` when no default parameter is specified is @@None@@.
    4. To retrieve a value and simultaneously delete its key-value pair from the dictionary, use the @@.pop()@@ method.
    5. The @@.setdefault()@@ method retrieves the value if the key exists, or inserts the key with a specified default value if it does not.


Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Retrieve a person's age safely using ``.get()`` with a fallback default value.

.. ordering::

    person = {"name": "Alice", "role": "Developer"}
    user_age = person.get("age", 25)
    print(f"Age: {user_age}")

----

**Example 2:** Remove and retrieve a setting using ``.pop()``, printing both the popped value and updated dictionary.

.. ordering::

    config = {"theme": "dark", "notifications": True}
    active_theme = config.pop("theme", "light")
    print(f"Removed theme: {active_theme}")
    print(config)

----

**Example 3:** Ensure a missing preference key exists with a default value using ``.setdefault()``.

.. ordering::

    user_prefs = {"language": "English"}
    autosave = user_prefs.setdefault("autosave", True)
    print(f"Autosave status: {autosave}")
    print(user_prefs)


Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What happens when you execute ``data["city"]`` if ``"city"`` is not a key in ``data``?

        [ ] It returns ``None``. | Incorrect. Direct access via brackets does not return None on missing keys.
        [ ] It automatically adds ``"city": None`` to the dictionary. | Incorrect. Square bracket lookup does not mutate the dictionary.
        [x] Python raises a ``KeyError``. | Correct! Direct key lookup with square brackets raises a KeyError if the key is missing.
        [ ] Python raises an ``IndexError``. | Incorrect. IndexError is raised for out-of-range list or tuple indices.


    .. multichoice::

        Which of the following lines safely returns ``"Unknown"`` when ``"status"`` is missing from ``user_info``?

        [ ] ``user_info["status", "Unknown"]`` | Incorrect. SyntaxError or invalid dictionary indexing syntax.
        [x] ``user_info.get("status", "Unknown")`` | Correct! The second argument to .get() is the default value returned if the key isn't found.
        [ ] ``user_info.pop("status")`` | Incorrect. Without a second argument, .pop() will raise a KeyError if the key is missing.
        [ ] ``user_info.find("status", "Unknown")`` | Incorrect. Dictionaries do not have a .find() method.


    .. multichoice::

        Given ``d = {"a": 10, "b": 20}``, what is returned by ``d.get("a", 100)``?

        [x] ``10`` | Correct! Because the key "a" exists, .get() returns its actual value (10) and ignores the default argument.
        [ ] ``100`` | Incorrect. The default value is only returned when the key is missing.
        [ ] ``None`` | Incorrect. The key exists in the dictionary.
        [ ] ``[10, 100]`` | Incorrect. .get() returns a single value.


    .. multichoice::

        What does the ``.pop(key)`` method do when called on a dictionary?

        [ ] Removes the key and returns ``True``. | Incorrect. It returns the value associated with the key, not a boolean.
        [x] Removes the key and returns its value. | Correct! .pop() extracts the value and deletes the key-value pair.
        [ ] Removes the last added key-value pair. | Incorrect. That is the behavior of .popitem().
        [ ] Returns the value without modifying the dictionary. | Incorrect. .pop() mutates the dictionary by removing the entry.


    .. multichoice::

        What happens if you execute ``d.pop("missing_key")`` without providing a default value?

        [ ] It returns ``None``. | Incorrect. .pop() requires a default argument to prevent an error on missing keys.
        [ ] It returns ``False``. | Incorrect. It raises an exception.
        [x] Python raises a ``KeyError``. | Correct! Calling .pop() on a non-existent key without a second default parameter raises a KeyError.
        [ ] The dictionary is cleared. | Incorrect. Nothing is cleared; an exception is raised immediately.


    .. multichoice::

        What is the primary difference between ``.get("key", default)`` and ``.setdefault("key", default)``?

        [ ] ``.get()`` modifies the dictionary, while ``.setdefault()`` does not. | Incorrect. The reverse is true.
        [x] ``.setdefault()`` adds the key with the default value to the dictionary if missing, while ``.get()`` does not. | Correct! .setdefault() mutates the dictionary when keys are missing, whereas .get() leaves it untouched.
        [ ] ``.get()`` raises a KeyError if the key is missing. | Incorrect. Neither method raises a KeyError when provided with default parameters.
        [ ] There is no difference; they are aliases for each other. | Incorrect. They behave differently when keys are missing.


    .. multichoice::

        Given ``scores = {"math": 90}``, what will ``scores.setdefault("math", 0)`` evaluate to?

        [ ] ``0`` | Incorrect. Since "math" already exists, its existing value is returned.
        [x] ``90`` | Correct! Since "math" is already present, .setdefault() returns 90 without changing its value.
        [ ] ``None`` | Incorrect. The key exists and has the value 90.
        [ ] ``{"math": 90}`` | Incorrect. It returns the value, not the entire dictionary.


    .. multichoice::

        Which expression can be used to check if a key exists in a dictionary ``my_dict`` before retrieving it?

        [ ] ``if my_dict.has_key("target"):`` | Incorrect. has_key() was removed in Python 3.
        [x] ``if "target" in my_dict:`` | Correct! The 'in' keyword checks for key membership in a dictionary efficiently.
        [ ] ``if "target" exists my_dict:`` | Incorrect. 'exists' is not valid Python syntax.
        [ ] ``if my_dict.contains("target"):`` | Incorrect. Use the 'in' operator instead.


    .. multichoice::

        Suppose ``inventory = {"apple": 5}``. What is the value of ``inventory`` after running ``val = inventory.get("banana", 0)``?

        [ ] ``{"apple": 5, "banana": 0}`` | Incorrect. .get() never mutates the dictionary.
        [x] ``{"apple": 5}`` | Correct! .get() is a read-only operation and leaves the dictionary unchanged.
        [ ] ``{}`` | Incorrect. The dictionary is not modified.
        [ ] ``{"banana": 0}`` | Incorrect. Existing keys are not removed.


    .. multichoice::

        What value does ``person.get("email")`` return if ``person = {"name": "Bob"}``?

        [ ] ``""`` (empty string) | Incorrect. The default return value is None, not an empty string.
        [ ] ``0`` | Incorrect. The default return value is None.
        [x] ``None`` | Correct! Calling .get() with a missing key and no explicit default returns None.
        [ ] Raises a ``KeyError`` | Incorrect. .get() handles missing keys gracefully by returning None.

