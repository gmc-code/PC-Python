===========================
Python Dictionary Methods
===========================

| In Python, **dictionaries** store data in **key-value pairs**, allowing fast lookup, addition, and modification of values.
| Built-in dictionary **methods** are specialized functions that help manage, inspect, and manipulate these key-value pairs efficiently.
| Common dictionary methods include ``.keys()``, ``.values()``, ``.items()``, ``.get()``, and ``.pop()``.

.. code-block:: python

    student = {
        "name": "Alex",
        "age": 13,
        "grade": "Year 8"
    }

    # Accessing values safely using .get()
    print(student.get("name"))  # Output: Alex

----

Accessing Keys, Values, and Items
=================================

Python provides built-in methods to extract different parts of a dictionary as dynamic view objects:

- **The .keys() Method**: Returns a view object containing all the keys present in the dictionary.
- **The .values() Method**: Returns a view object containing all the values stored in the dictionary.
- **The .items() Method**: Returns a view object containing key-value pairs as tuples ``(key, value)``.
- **Iterating and Inspection**: These methods make it easy to loop through keys, values, or both simultaneously.

.. code-block:: python

    scores = {"Alice": 95, "Bob": 88, "Charlie": 92}

    print(scores.keys())    # Output: dict_keys(['Alice', 'Bob', 'Charlie'])
    print(scores.values())  # Output: dict_values([95, 88, 92])
    print(scores.items())   # Output: dict_items([('Alice', 95), ('Bob', 88), ('Charlie', 92)])

Quiz: Accessing Keys, Values, and Items
---------------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. The @@.keys()@@ method returns a view of all keys in a dictionary.
    2. To get all values stored in a dictionary, use the @@.values()@@ method.
    3. The `.items()` method returns key-value pairs grouped as @@tuples@@.
    4. Dictionaries store data in @@key-value@@ pairs.
    5. View objects returned by `.keys()` automatically @@update@@ when the dictionary changes.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Extract and display all keys from a inventory dictionary.

.. ordering::

    inventory = {"apples": 10, "bananas": 5, "oranges": 8}
    all_keys = inventory.keys()
    print(all_keys)

----

**Example 2:** Loop through all values stored in a game score dictionary.

.. ordering::

    scores = {"p1": 100, "p2": 250, "p3": 180}
    for val in scores.values():
        print(val)

----

**Example 3:** Print key and value pairs together using the `.items()` method.

.. ordering::

    user = {"username": "coder123", "role": "admin"}
    for k, v in user.items():
        print(f"{k}: {v}")

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Which method returns all the keys present in a Python dictionary?

        [x] .keys() | Correct! The .keys() method extracts a view of all dictionary keys.
        [ ] .all_keys() | Incorrect. There is no .all_keys() method in Python.
        [ ] .get_keys() | Incorrect. Python uses .keys() directly.
        [ ] .indexes() | Incorrect. Dictionaries are indexed by keys, not numerical indices.


    .. multichoice::

        What does the ``.values()`` method return?

        [x] A view object containing all values in the dictionary | Correct! .values() extracts every value in the dictionary.
        [ ] A list of dictionary key names | Incorrect. .keys() retrieves key names.
        [ ] The number of keys stored | Incorrect. len() determines key count.
        [ ] A single randomly selected value | Incorrect. .values() returns all stored values.


    .. multichoice::

        Given ``d = {"a": 1, "b": 2}``, what is returned by ``d.items()``?

        [x] dict_items([('a', 1), ('b', 2)]) | Correct! .items() returns key-value pairs formatted as tuples.
        [ ] ['a', 'b'] | Incorrect. That is returned by .keys().
        [ ] [1, 2] | Incorrect. That is returned by .values().
        [ ] {'a': 1, 'b': 2} | Incorrect. .items() returns a view object of tuples.


    .. multichoice::

        How do you loop through both keys and values simultaneously in a dictionary ``data``?

        [x] for key, value in data.items(): | Correct! .items() provides key and value in each iteration loop.
        [ ] for key, value in data.keys(): | Incorrect. .keys() only yields key names.
        [ ] for key, value in data.values(): | Incorrect. .values() only yields dictionary values.
        [ ] for key, value in data: | Incorrect. Iterating directly over a dictionary yields keys only.


    .. multichoice::

        What type of data structure are individual key-value pairs wrapped in inside ``.items()``?

        [x] Tuples | Correct! Key-value pairs are returned as immutable (key, value) tuples.
        [ ] Lists | Incorrect. Items view uses tuples (key, value).
        [ ] Strings | Incorrect. Original data types are preserved inside tuples.
        [ ] Sets | Incorrect. Items view uses paired tuples.


    .. multichoice::

        Given ``fruit = {"apple": "red", "banana": "yellow"}``, what does ``"apple" in fruit.keys()`` evaluate to?

        [x] True | Correct! "apple" is a key present in the dictionary.
        [ ] False | Incorrect. "apple" is actively present as a key.
        [ ] "red" | Incorrect. Membership test returns Boolean True or False.
        [ ] TypeError | Incorrect. Membership testing on key views is valid syntax.


    .. multichoice::

        If you modify a dictionary after calling ``k = dict.keys()``, what happens to ``k``?

        [x] k automatically updates because it is a dynamic view object | Correct! Dictionary views reflect dictionary modifications dynamically.
        [ ] k stays static and loses track of new keys | Incorrect. Dictionary views are dynamic.
        [ ] Python throws a RuntimeError | Incorrect. Dynamic view tracking is intentional behavior.
        [ ] k gets converted into an integer | Incorrect. Object type remains a dictionary view.


    .. multichoice::

        Which method would you use to get a collection of ONLY player scores from ``{"p1": 50, "p2": 90}``?

        [x] .values() | Correct! .values() returns all score numbers without player key names.
        [ ] .keys() | Incorrect. .keys() returns player names ("p1", "p2").
        [ ] .pop() | Incorrect. .pop() removes and returns a specific item.
        [ ] .get() | Incorrect. .get() retrieves a single specified key's value.


    .. multichoice::

        Given ``info = {"age": 14}``, what is printed by ``print(type(info.keys()))``?

        [x] <class 'dict_keys'> | Correct! .keys() returns a specialized dict_keys object.
        [ ] <class 'list'> | Incorrect. Views can be converted to lists using list(), but are dict_keys types by default.
        [ ] <class 'tuple'> | Incorrect. dict_keys is its own view type.
        [ ] <class 'str'> | Incorrect. Key views are specialized iterable objects.


    .. multichoice::

        How can you convert ``dict.values()`` into a standard Python list?

        [x] list(dict.values()) | Correct! The built-in list() function converts view objects into standard lists.
        [ ] dict.values().to_list() | Incorrect. Method .to_list() does not exist in standard Python.
        [ ] str(dict.values()) | Incorrect. str() converts the object to a string representation.
        [ ] tuple(dict.keys()) | Incorrect. This converts keys to a tuple instead of values to a list.

----

Safe Retrieval using .get()
===========================

Accessing a non-existent key using bracket notation (``dict[key]``) raises a ``KeyError``. The **``.get()`` method** provides a safe alternative:

- **Key Lookup**: Returns the value associated with a specified key if it exists.
- **Default Fallback**: Returns ``None`` (or a custom specified default) if the key is missing instead of crashing the program.
- **Custom Default Syntax**: Pass a second argument to specify custom output when missing: ``dict.get(key, default_value)``.
- **Error Prevention**: Prevents unexpected crashes when handling unpredictable data inputs.

.. code-block:: python

    profile = {"username": "Alex", "level": 5}

    # Safe lookup for an existing key
    print(profile.get("username"))  # Output: Alex

    # Safe lookup for a missing key with default fallback
    print(profile.get("coins", 0))  # Output: 0 (since "coins" is not in profile)

Quiz: Safe Retrieval using .get()
---------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. The `.get()` method prevents a program from raising a @@KeyError@@ when a key is missing.
    2. If a key is not found and no default is set, `.get()` returns @@None@@.
    3. To provide a custom fallback value, pass it as the @@second@@ argument to `.get()`.
    4. Accessing `d["missing"]` directly causes Python to @@crash@@ if the key doesn't exist.
    5. In `dict.get("score", 0)`, the number `0` acts as the @@default@@ value.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Safely fetch a user rank using `.get()` with a default value.

.. ordering::

    stats = {"score": 450}
    rank = stats.get("rank", "Unranked")
    print(rank)

----

**Example 2:** Compare standard bracket notation with safe `.get()` retrieval.

.. ordering::

    data = {"id": 101}
    # Safe retrieval without crashing
    role = data.get("role", "Guest")
    print(role)

----

**Example 3:** Check inventory count for an item not in stock.

.. ordering::

    stock = {"pens": 12, "notebooks": 5}
    erasers = stock.get("erasers", 0)
    print(f"Erasers available: {erasers}")

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What happens when you request a missing key using standard square brackets (e.g., ``d["missing"]``)?

        [x] Python raises a KeyError and stops program execution | Correct! Missing keys in bracket notation crash with a KeyError.
        [ ] Python returns None | Incorrect. .get() returns None, square brackets raise KeyError.
        [ ] Python creates the key automatically with value 0 | Incorrect. Standard lookups do not mutate dictionaries.
        [ ] Python returns an empty string | Incorrect. An exception is raised.


    .. multichoice::

        What is returned by ``{"a": 1}.get("b")``?

        [x] None | Correct! When a key is missing and no default is given, .get() returns None.
        [ ] KeyError | Incorrect. .get() avoids raising KeyErrors.
        [ ] 0 | Incorrect. 0 is only returned if explicitly passed as default.
        [ ] False | Incorrect. Default fallback is None.


    .. multichoice::

        What is the output of ``{"hero": "Knight"}.get("shield", "No Shield")``?

        [x] "No Shield" | Correct! "shield" key is missing, so custom default "No Shield" is returned.
        [ ] "Knight" | Incorrect. "Knight" is the value for "hero", not "shield".
        [ ] None | Incorrect. Custom default overrides None.
        [ ] KeyError | Incorrect. .get() handles missing keys safely.


    .. multichoice::

        Given ``colors = {"red": "#FF0000"}``, what does ``colors.get("red", "#000000")`` return?

        [x] "#FF0000" | Correct! Key "red" exists, so stored value "#FF0000" is returned instead of default.
        [ ] "#000000" | Incorrect. Fallback value is ignored when key is found.
        [ ] None | Incorrect. Stored value is returned.
        [ ] KeyError | Incorrect. Valid existing key lookup.


    .. multichoice::

        Which statement about ``.get()`` is TRUE?

        [x] It retrieves values safely without risking KeyError crashes | Correct! .get() handles missing keys gracefully.
        [ ] It permanently adds missing keys to the dictionary | Incorrect. .get() does not modify dictionary content.
        [ ] It deletes existing keys after reading them | Incorrect. .get() reads values without removing keys.
        [ ] It only works with integer keys | Incorrect. Works with string, tuple, or integer keys.


    .. multichoice::

        What is the default return value of ``dict.get(key)`` if ``key`` is missing and no second parameter is provided?

        [x] None | Correct! None is Python's built-in default for absent values in .get().
        [ ] 0 | Incorrect. Must pass 0 explicitly as second parameter.
        [ ] False | Incorrect. None is returned.
        [ ] Empty string "" | Incorrect. None is returned.


    .. multichoice::

        Given ``settings = {"volume": 80}``, what is printed by ``print(settings.get("brightness", 50))``?

        [x] 50 | Correct! Key "brightness" is absent, so fallback integer 50 prints.
        [ ] 80 | Incorrect. 80 belongs to "volume".
        [ ] None | Incorrect. Custom fallback 50 overrides None.
        [ ] KeyError | Incorrect. Method handles missing key.


    .. multichoice::

        Why is ``.get()`` preferred over bracket lookup when reading user input keys?

        [x] User input keys may not exist in dictionary, so .get() prevents program crashes | Correct! Protects scripts from bad/unexpected key inputs.
        [ ] .get() executes 100 times faster | Incorrect. Lookup speeds are virtually identical.
        [ ] Square brackets cannot read string keys | Incorrect. Square brackets read string keys fine.
        [ ] .get() automatically converts keys to uppercase | Incorrect. Key casing is unchanged.


    .. multichoice::

        What is output by ``d = {}; print(d.get("x") is None)``?

        [x] True | Correct! d.get("x") returns None, and None is None evaluates to True.
        [ ] False | Incorrect. Lookup returns None.
        [ ] KeyError | Incorrect. No error raised.
        [ ] SyntaxError | Incorrect. Expression is valid syntax.


    .. multichoice::

        Does ``dict.get("key", "default")`` modify ``dict`` if ``"key"`` is not in ``dict``?

        [x] No, .get() never modifies or adds items to the dictionary | Correct! .get() is strictly a non-mutating read operation.
        [ ] Yes, it adds "key": "default" to the dictionary | Incorrect. Use .setdefault() if key addition is desired.
        [ ] Yes, but only if default is an integer | Incorrect. .get() never alters dictionary contents.
        [ ] Yes, it deletes all existing keys | Incorrect. Non-mutating operation.

----

Modifying Dictionaries (.update, .pop, .clear)
==============================================

To modify, remove, or update dictionary content, Python provides several key methods:

- **The .update() Method**: Merges key-value pairs from another dictionary or iterable. Existing keys are overwritten, and new keys are added.
- **The .pop() Method**: Removes a specified key and returns its value. Accepts a default parameter to prevent errors if key is missing.
- **The .popitem() Method**: Removes and returns the last inserted key-value pair as a tuple ``(key, value)``.
- **The .clear() Method**: Removes all key-value pairs from the dictionary, leaving it empty (``{}``).

.. code-block:: python

    player = {"name": "Sam", "health": 100}

    # Updating existing key and adding a new key simultaneously
    player.update({"health": 90, "shield": 50})
    print(player)  # Output: {'name': 'Sam', 'health': 90, 'shield': 50}

    # Removing a key and capturing its value using .pop()
    removed_health = player.pop("health")
    print(removed_health)  # Output: 90

    # Clearing all keys
    player.clear()
    print(player)  # Output: {}

Quiz: Modifying Dictionaries
----------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. The @@.update()@@ method merges another dictionary into an existing one.
    2. To remove a key and return its value, use the @@.pop()@@ method.
    3. The `.popitem()` method removes the @@last@@ inserted key-value pair.
    4. To remove all items from a dictionary at once, call the @@.clear()@@ method.
    5. Calling `.clear()` leaves a dictionary in an @@empty@@ state `{}`.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Update player score and add a new item using `.update()`.

.. ordering::

    game = {"score": 10}
    game.update({"score": 20, "level": 2})
    print(game)

----

**Example 2:** Safely pop a key from a dictionary with a fallback value.

.. ordering::

    inv = {"coins": 50, "gems": 5}
    removed_gems = inv.pop("gems", 0)
    print(f"Removed gems: {removed_gems}")

----

**Example 3:** Empty a configuration dictionary using `.clear()`.

.. ordering::

    config = {"theme": "dark", "volume": 80}
    config.clear()
    print(len(config))

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What does the ``.update()`` method do when passed a key that ALREADY exists in the target dictionary?

        [x] It overwrites the existing key's value with the new value | Correct! .update() replaces existing key values with incoming data.
        [ ] It raises a KeyError | Incorrect. Overwriting existing keys is expected behavior.
        [ ] It ignores the new value and keeps original | Incorrect. Existing values are overwritten.
        [ ] It creates a duplicate key | Incorrect. Python dictionaries cannot contain duplicate keys.


    .. multichoice::

        Given ``d = {"a": 10, "b": 20}``, what does ``d.pop("a")`` return?

        [x] 10 | Correct! .pop() removes key "a" and returns its associated value 10.
        [ ] "a" | Incorrect. .pop() returns the value, not the key name.
        [ ] {"b": 20} | Incorrect. .pop() returns the removed value, not the modified dictionary.
        [ ] None | Incorrect. Returns 10.


    .. multichoice::

        What happens if you run ``dict.pop("missing")`` on a dictionary that does NOT contain "missing"?

        [x] Python raises a KeyError (unless a default parameter was provided) | Correct! Like bracket lookup, .pop() without a default raises KeyError if key is absent.
        [ ] Python silently does nothing | Incorrect. .pop() requires a default value parameter to avoid KeyError on missing keys.
        [ ] Python clears the entire dictionary | Incorrect. Dict content remains unless KeyError interrupts execution.
        [ ] Returns None automatically | Incorrect. Must provide default parameter (e.g. .pop("missing", None)).


    .. multichoice::

        Which method removes ALL items from a dictionary, leaving it with length 0?

        [x] .clear() | Correct! .clear() removes all key-value entries.
        [ ] .delete() | Incorrect. Python uses del statement or .clear() method.
        [ ] .remove() | Incorrect. .remove() is a list method, not a dictionary method.
        [ ] .reset() | Incorrect. No .reset() method exists for dictionaries.


    .. multichoice::

        What does ``.popitem()`` remove and return in Python 3.7+?

        [x] The last inserted key-value pair as a tuple | Correct! In Python 3.7+, dictionaries preserve insertion order, so .popitem() removes LIFO (last-in, first-out) item.
        [ ] A random key-value pair | Incorrect. Dictionaries preserve insertion order in modern Python.
        [ ] The first inserted key-value pair | Incorrect. Removes the last pair added.
        [ ] All keys at once | Incorrect. Removes a single pair.


    .. multichoice::

        Given ``data = {"x": 1}``, what is the value of ``data`` after executing ``data.update({"y": 2})``?

        [x] {"x": 1, "y": 2} | Correct! "y": 2 is added as a new key-value pair.
        [ ] {"y": 2} | Incorrect. .update() merges data without erasing existing keys.
        [ ] {"x": 1} | Incorrect. New pair is inserted.
        [ ] TypeError | Incorrect. Valid dictionary update.


    .. multichoice::

        How can you prevent a ``KeyError`` when popping a potentially missing key "status" from ``info``?

        [x] Use info.pop("status", "default_value") | Correct! Providing a second default argument avoids KeyErrors if key is missing.
        [ ] Use info.pop("status") | Incorrect. Raises KeyError if missing.
        [ ] Use info.clear("status") | Incorrect. .clear() takes no arguments and empties dictionary.
        [ ] Use info.update("status") | Incorrect. .update() expects dictionary/iterable arguments.


    .. multichoice::

        Given ``items = {"a": 1, "b": 2}``, what is ``len(items)`` after ``items.clear()``?

        [x] 0 | Correct! .clear() empties dictionary, reducing length to 0.
        [ ] 2 | Incorrect. All items are removed.
        [ ] 1 | Incorrect. All items are removed.
        [ ] None | Incorrect. len() returns integer 0.


    .. multichoice::

        Given ``d = {"a": 5}``, what does ``d.pop("a")`` leave inside ``d``?

        [x] {} | Correct! Key "a" is removed, leaving an empty dictionary.
        [ ] {"a": 5} | Incorrect. Key is removed by .pop().
        [ ] {"a": None} | Incorrect. Key and value are deleted.
        [ ] None | Incorrect. d remains an empty dictionary object.


    .. multichoice::

        Which dictionary method accepts another dictionary as an argument to combine entries?

        [x] .update() | Correct! .update() takes another dictionary or key-value iterable as argument.
        [ ] .get() | Incorrect. Takes key name and optional default.
        [ ] .pop() | Incorrect. Takes key name and optional default.
        [ ] .items() | Incorrect. Takes no arguments.



