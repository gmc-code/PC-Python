===========================
Sets
===========================

| A **set** in Python is used to store multiple unique items in a single variable.
| Sets are **unordered**, **unchangeable** (you cannot change existing items, but you can add or remove items), and **unindexed**.
| Sets are created using curly braces ``{}``, but unlike dictionaries, they contain individual items separated by commas rather than key-value pairs.
| Sets automatically remove any duplicate values—every item in a set must be unique!

.. code-block:: python

    # Creating a simple set of numbers (duplicates are automatically ignored)
    numbers = {1, 2, 3, 3, 4}  # Result: {1, 2, 3, 4}

----

Adding Items to a Set
======================

To add new items to an existing set, Python gives us two primary methods:

- ``.add(item)``: Adds a **single item** to the set.
- ``.update(iterable)``: Adds **multiple items** from another set, list, or iterable to the current set.

.. code-block:: python

    inventory = {"sword", "shield"}

    # Adds "potion" to the set
    inventory.add("potion")      # Result: {"sword", "shield", "potion"}

    # Adding a duplicate item does nothing because set items must be unique
    inventory.add("sword")       # Result: {"sword", "shield", "potion"}

    # Adds multiple items from another set
    more_items = {"bow", "arrow"}
    inventory.update(more_items) # Result: {"sword", "shield", "potion", "bow", "arrow"}

Quiz: Adding Items
------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Sets in Python are created using curly @@braces@@.
    2. To add a single item to a set, call the @@.add()@@ method.
    3. To add multiple items from another set or list, call the @@.update()@@ method.
    4. A key property of sets is that they automatically remove @@duplicate@@ values.
    5. Sets do not preserve item order, which means they are @@unordered@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Create a set of primary colors, add a new color, and print the set.

.. ordering::

    colors = {"red", "blue"}
    colors.add("yellow")
    print(colors)

----

**Example 2:** Create a fruit set, attempt to add a duplicate fruit, and print the set.

.. ordering::

    fruits = {"apple", "banana"}
    fruits.add("apple")
    print(fruits)

----

**Example 3:** Create a set of items, update it with another set of items, and print the total set.

.. ordering::

    gear = {"helmet"}
    extra_gear = {"boots", "gloves"}
    gear.update(extra_gear)
    print(gear)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Which method adds a single item to a Python set?

        [x] .add() | Correct! .add() places one single item into a set.
        [ ] .append() | Incorrect. .append() is a list method, not a set method.
        [ ] .insert() | Incorrect. Sets are unordered and do not support index positions.
        [ ] .push() | Incorrect. .push() is not a Python set method.


    .. multichoice::

        What happens when you run ``nums = {1, 2}; nums.add(2)``?

        [ ] 2 is added a second time so the set becomes {1, 2, 2} | Incorrect. Sets cannot contain duplicate values.
        [x] The set remains {1, 2} with no changes | Correct! Adding an existing item has no effect on a set.
        [ ] Python raises a ValueError | Incorrect. Adding a duplicate is ignored safely without errors.
        [ ] The number 2 is removed from the set | Incorrect. .add() does not delete existing values.


    .. multichoice::

        Which character symbol is used to define a set in Python?

        [x] Curly braces {} | Correct! Sets are defined using curly braces {}.
        [ ] Square brackets [] | Incorrect. Square brackets are used for lists.
        [ ] Parentheses () | Incorrect. Parentheses are used for tuples.
        [ ] Angle brackets <> | Incorrect. Angle brackets are comparison operators.


    .. multichoice::

        What is the difference between ``.add()`` and ``.update()`` for sets?

        [x] .add() adds a single item, while .update() adds multiple items from an iterable | Correct! .add() takes one item, whereas .update() unpacks multiple items.
        [ ] .add() works on numbers, while .update() works on strings | Incorrect. Both work with any valid data types.
        [ ] .add() preserves list order, while .update() reverses it | Incorrect. Sets are always unordered.
        [ ] There is no difference between them | Incorrect. They handle single vs multiple items differently.


    .. multichoice::

        What will ``items = {"pen"}; items.update(["ruler", "eraser"]); print(len(items))`` output?

        [ ] 1 | Incorrect. Two new items were added.
        [ ] 2 | Incorrect. The original item "pen" remains in the set.
        [x] 3 | Correct! "pen", "ruler", and "eraser" make 3 unique items.
        [ ] 4 | Incorrect. Exactly 2 items were added to 1 existing item.


    .. multichoice::

        Why do Python sets NOT support index positions like ``my_set[0]``?

        [x] Because sets are unordered, so items do not have fixed positions | Correct! Sets have no deterministic index order.
        [ ] Because sets can only store numbers | Incorrect. Sets can store strings, floats, and booleans.
        [ ] Because set items are read-only | Incorrect. Unordered structure is the reason indexing is unsupported.
        [ ] Python sets do support indexing | Incorrect. Indexing a set raises a TypeError.


    .. multichoice::

        How do you add multiple items from ``new_scores`` into an existing set ``all_scores``?

        [ ] all_scores.add(new_scores) | Incorrect. .add() would treat the whole collection as a single element or fail.
        [ ] all_scores.insert(new_scores) | Incorrect. .insert() is a list method requiring an index.
        [x] all_scores.extend(new_scores) | Incorrect. Sets use .update(), not .extend().
        [x] all_scores.update(new_scores) | Correct! .update() merges elements from new_scores into all_scores.


    .. multichoice::

        What is the result of ``len({"apple", "apple", "banana"})``?

        [ ] 3 | Incorrect. Duplicate "apple" entries are automatically merged.
        [x] 2 | Correct! "apple" and "banana" make 2 unique items.
        [ ] 1 | Incorrect. "banana" is also in the set.
        [ ] Error | Incorrect. Defining duplicates in set literals is valid syntax.


    .. multichoice::

        Given ``nums = {10, 30}``, which command adds 20 to the set?

        [ ] nums.insert(1, 20) | Incorrect. Sets do not support .insert().
        [x] nums.add(20) | Correct! .add(20) places 20 into the set.
        [ ] nums.append(20) | Incorrect. Sets do not have an .append() method.
        [ ] nums.push(20) | Incorrect. .push() is not a set method.


    .. multichoice::

        What happens if you run ``data = {1, 2}; data.update("34")``?

        [x] ``data`` becomes ``{1, 2, '3', '4'}`` | Correct! Strings are iterables, so .update() adds each character separately.
        [ ] ``data`` becomes ``{1, 2, '34'}`` | Incorrect. .update() iterates through string characters.
        [ ] Raises a TypeError | Incorrect. Strings are valid iterables for .update().
        [ ] ``data`` becomes ``{1, 2, 34}`` | Incorrect. Characters added from strings are string types.

----

Deleting Items from a Set
=========================

Python provides several ways to remove items from a set:

- ``.remove(item)``: Deletes the item. Raises a **KeyError** if the item is not found.
- ``.discard(item)``: Deletes the item, but does **NOT** raise an error if the item is missing.
- ``.pop()``: Removes and returns an **arbitrary (random) item** because sets are unordered.
- ``.clear()``: Removes **all items** from the set, leaving it completely empty.

.. code-block:: python

    pets = {"dog", "cat", "fish"}

    # Removes "cat" by value
    pets.remove("cat")    # Result: {"dog", "fish"}

    # Safely removes "bird" without error even though it isn't in the set
    pets.discard("bird")  # Result: {"dog", "fish"}

    # Removes and returns a random item
    removed_pet = pets.pop()

    # Wipes all remaining items from the set
    pets.clear()          # Result: set()


Quiz: Deleting Items
--------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. To delete an item from a set and throw an error if it isn't present, use the @@.remove()@@ method.
    2. To safely remove an item without throwing an error if it is missing, use the @@.discard()@@ method.
    3. The @@.pop()@@ method removes and returns a random item from a set.
    4. Attempting to ``.remove()`` an item that does not exist in a set raises a @@KeyError@@.
    5. An empty set is displayed by Python as @@set()@@ rather than ``{}`` (which creates an empty dictionary).

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Create a set of animals, remove `"dog"`, and print the remaining set.

.. ordering::

    animals = {"cat", "dog", "bird"}
    animals.remove("dog")
    print(animals)

----

**Example 2:** Create a scores set, safely discard a non-existent score, and print the set.

.. ordering::

    scores = {100, 85, 90}
    scores.discard(50)
    print(scores)

----

**Example 3:** Create a set of colors, pop a random color, and print the popped item.

.. ordering::

    colors = {"red", "green", "blue"}
    popped_color = colors.pop()
    print(popped_color)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What error occurs if you use ``.remove()`` on an item that does NOT exist in a set?

        [x] KeyError | Correct! .remove() raises a KeyError when the item is missing.
        [ ] ValueError | Incorrect. Lists raise ValueError, but sets raise KeyError.
        [ ] IndexError | Incorrect. Sets do not use index positions.
        [ ] TypeError | Incorrect. The syntax is valid, but the key was not found.


    .. multichoice::

        Which method safely deletes an item from a set WITHOUT raising an error if it is missing?

        [ ] .remove() | Incorrect. .remove() throws a KeyError if missing.
        [x] .discard() | Correct! .discard() ignores missing items silently.
        [ ] .pop() | Incorrect. .pop() removes a random item and errors on empty sets.
        [ ] .delete() | Incorrect. No such method exists on sets.


    .. multichoice::

        Why does ``.pop()`` on a set remove an arbitrary (random) item instead of the last item?

        [x] Because sets are unordered, so there is no concept of a "last" item | Correct! Unordered sets have no defined start or end position.
        [ ] Because Python flips set elements dynamically | Incorrect. Unordered nature is the core reason.
        [ ] Because .pop() requires an index argument | Incorrect. .pop() takes no index argument on sets.
        [ ] It does remove the last item | Incorrect. Set elements are unordered.


    .. multichoice::

        What is the result of ``items = {"apple"}; items.discard("banana")``?

        [x] ``items`` remains ``{"apple"}`` with no error | Correct! .discard() safely ignores missing items.
        [ ] Raises a KeyError | Incorrect. .discard() does not raise KeyErrors.
        [ ] Raises a ValueError | Incorrect. .discard() is safe from missing item errors.
        [ ] ``items`` becomes empty | Incorrect. "apple" is not removed.


    .. multichoice::

        How do you remove ALL items from a set named ``data`` so it becomes empty ``set()``?

        [ ] data.remove() | Incorrect. .remove() requires an item parameter.
        [ ] data.pop(all) | Incorrect. .pop() takes no arguments for sets.
        [x] data.clear() | Correct! .clear() empties all elements from a set.
        [ ] del data | Incorrect. del data deletes the variable entirely.


    .. multichoice::

        Why is an empty set represented as ``set()`` instead of ``{}`` in Python?

        [x] Because ``{}`` is already reserved for creating empty dictionaries | Correct! Python treats {} as an empty dictionary by default.
        [ ] Because sets cannot be empty | Incorrect. Sets can be empty.
        [ ] Because set syntax requires square brackets | Incorrect. Sets use curly braces when non-empty.
        [ ] It is a bug in Python | Incorrect. It is intentional design to prevent syntax ambiguity.


    .. multichoice::

        Given ``letters = {"a", "b", "c"}``, what does ``letters.clear(); print(letters)`` output?

        [ ] {} | Incorrect. {} represents an empty dictionary.
        [x] set() | Correct! Python prints set() to represent an empty set.
        [ ] None | Incorrect. The variable still holds an empty set object.
        [ ] Error | Incorrect. .clear() is valid syntax.


    .. multichoice::

        What happens if you execute ``.pop()`` on an EMPTY set?

        [ ] It returns None | Incorrect. Python raises an exception.
        [x] Python raises a KeyError | Correct! Calling .pop() on an empty set raises a KeyError.
        [ ] It returns set() | Incorrect. An exception is raised.
        [ ] It creates a new element | Incorrect. .pop() cannot create elements.


    .. multichoice::

        Which statement about ``.remove()`` vs ``.discard()`` is true?

        [x] .remove() raises a KeyError on missing items, while .discard() does not | Correct! That is the primary functional difference.
        [ ] .discard() returns the removed value, while .remove() does not | Incorrect. Neither method returns a value.
        [ ] .remove() works on strings only, while .discard() works on numbers | Incorrect. Both work with any valid data types.
        [ ] They are exact synonyms | Incorrect. Their behavior with missing items differs.


    .. multichoice::

        Given ``numbers = {1, 2, 3}``, what will ``numbers.remove(2); print(2 in numbers)`` output?

        [ ] True | Incorrect. 2 was removed.
        [x] False | Correct! 2 is no longer present in the set.
        [ ] 2 | Incorrect. in operator yields booleans.
        [ ] KeyError | Incorrect. Checking with in evaluates cleanly to False.

----

Set Operations (Union, Intersection, Difference)
================================================

Sets let us perform powerful mathematical operations to compare two sets:

- ``setA.union(setB)`` or ``setA | setB``: Combines **all unique items** from both sets.
- ``setA.intersection(setB)`` or ``setA & setB``: Finds items that exist in **both sets**.
- ``setA.difference(setB)`` or ``setA - setB``: Finds items in setA that are **NOT in setB**.

.. code-block:: python

    group_a = {"Alex", "Sam", "Jordan"}
    group_b = {"Sam", "Taylor", "Morgan"}

    # All unique people across both groups
    all_people = group_a.union(group_b)
    # Result: {"Alex", "Sam", "Jordan", "Taylor", "Morgan"}

    # People who are in BOTH groups
    both = group_a.intersection(group_b)
    # Result: {"Sam"}

    # People only in group A, but not in group B
    only_a = group_a.difference(group_b)
    # Result: {"Alex", "Jordan"}


Quiz: Set Operations
--------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. To combine all unique items from two sets together, use the @@.union()@@ method.
    2. To find items that are shared in both sets, use the @@.intersection()@@ method.
    3. To find items present in the first set but absent from the second set, use the @@.difference()@@ method.
    4. The shorthand symbol operator for set union is the @@pipe@@ symbol |.
    5. The shorthand symbol operator for set intersection is the @@ampersand@@ symbol &.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Create two sets, find their union, and print the result.

.. ordering::

    set1 = {1, 2}
    set2 = {2, 3}
    combined = set1.union(set2)
    print(combined)

----

**Example 2:** Create two sets, find their common elements using intersection, and print them.

.. ordering::

    a = {"cat", "dog"}
    b = {"dog", "fish"}
    common = a.intersection(b)
    print(common)

----

**Example 3:** Create two sets, find the difference (items in A not in B), and print them.

.. ordering::

    a = {10, 20, 30}
    b = {20, 40}
    diff = a.difference(b)
    print(diff)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Which set operation returns all items that appear in BOTH sets?

        [x] .intersection() | Correct! .intersection() identifies shared items.
        [ ] .union() | Incorrect. .union() combines all unique items.
        [ ] .difference() | Incorrect. .difference() finds items unique to one set.
        [ ] .update() | Incorrect. .update() modifies a set in place.


    .. multichoice::

        What is the result of ``{1, 2}.union({2, 3})``?

        [ ] {1, 2, 2, 3} | Incorrect. Sets eliminate duplicate values.
        [x] {1, 2, 3} | Correct! Union combines unique elements across sets.
        [ ] {2} | Incorrect. {2} is the intersection, not the union.
        [ ] {1, 3} | Incorrect. {1, 3} is the symmetric difference.


    .. multichoice::

        What symbol operator is equivalent to calling ``.intersection()`` between two sets?

        [ ] | | Incorrect. | is the union operator.
        [x] & | Correct! The ampersand symbol & computes set intersection.
        [ ] - | Incorrect. - is the difference operator.
        [ ] + | Incorrect. Sets do not support the + operator.


    .. multichoice::

        Given ``a = {1, 2, 3}`` and ``b = {2, 3, 4}``, what does ``a.difference(b)`` return?

        [x] {1} | Correct! 1 is the only item in set a that is absent from set b.
        [ ] {4} | Incorrect. 4 is in b, but difference calculates items in a NOT in b.
        [ ] {2, 3} | Incorrect. {2, 3} is the intersection.
        [ ] {1, 4} | Incorrect. That would be symmetric difference.


    .. multichoice::

        What happens if you try to concatenate two sets using the ``+`` operator, like ``{1} + {2}``?

        [ ] Returns {1, 2} | Incorrect. Sets do not support + for joining.
        [x] Python raises a TypeError | Correct! Combining sets requires .union() or the | operator.
        [ ] Returns {3} | Incorrect. Sets do not add values numerically with +.
        [ ] Returns [{1}, {2}] | Incorrect. TypeError is raised.


    .. multichoice::

        Which operator symbol performs set union?

        [x] | | Correct! The pipe symbol | computes the union of two sets.
        [ ] & | Incorrect. & computes intersection.
        [ ] ^ | Incorrect. ^ computes symmetric difference.
        [ ] % | Incorrect. % is the modulus operator.


    .. multichoice::

        Given ``x = {"a", "b"}`` and ``y = {"c"}``, what is ``x & y``?

        [ ] {"a", "b", "c"} | Incorrect. & computes intersection.
        [x] set() | Correct! No elements are shared between x and y, leaving an empty set.
        [ ] {"a"} | Incorrect. "a" is not in y.
        [ ] Error | Incorrect. Valid set operation.


    .. multichoice::

        What is the outcome of ``{10, 20} - {20, 30}``?

        [x] {10} | Correct! The difference operator - keeps elements from the left set not in the right set.
        [ ] {30} | Incorrect. Difference evaluates items in the left operand only.
        [ ] {10, 30} | Incorrect. 20 is subtracted out.
        [ ] {20} | Incorrect. 20 is removed because it is present in the right set.


    .. multichoice::

        If ``setA = {1, 2}`` and ``setB = {1, 2}``, what is ``setA.intersection(setB)``?

        [ ] set() | Incorrect. Both sets share all elements.
        [x] {1, 2} | Correct! All elements are present in both sets.
        [ ] {1} | Incorrect. 2 is also in both sets.
        [ ] {2} | Incorrect. 1 is also in both sets.


    .. multichoice::

        Which method creates a NEW set containing elements in set A or set B, but NOT both?

        [ ] .union() | Incorrect. Union includes all elements.
        [ ] .intersection() | Incorrect. Intersection includes only common elements.
        [x] .symmetric_difference() | Correct! Symmetric difference selects items unique to each set.
        [ ] .difference() | Incorrect. Difference checks items in one direction only.

----

Iterating Through a Set
======================

Iterating means stepping through items in a set one by one using a **for loop**. Because sets are **unordered**, items may appear in any random order during iteration!

.. code-block:: python

    players = {"Alex", "Sam", "Jordan"}

    # Loop through each item in the set
    for player in players:
        print(f"Player: {player}")


Quiz: Iterating Through Sets
----------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. To step through each item in a set one by one, use a @@for@@ loop.
    2. Because sets are unordered, the order of items printed during iteration is @@unpredictable@@.
    3. The header line of a set ``for`` loop must end with a @@colon@@.
    4. Code inside the loop body must use four spaces of @@indentation@@.
    5. The built-in function @@len()@@ can be used to find how many iterations a loop over a set will make.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Create a set of fruits and use a `for` loop to print each fruit.

.. ordering::

    fruits = {"apple", "banana", "cherry"}
    for fruit in fruits:
        print(fruit)

----

**Example 2:** Create a set of numbers, calculate their double in a loop, and print each doubled value.

.. ordering::

    numbers = {1, 2, 3}
    for n in numbers:
        double_val = n * 2
        print(double_val)

----

**Example 3:** Check membership while looping through a set of names and print matched items.

.. ordering::

    names = {"Alice", "Bob"}
    for name in names:
        if name == "Alice":
            print("Found Alice!")


Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What should you expect about the output order when looping through a set with ``for item in my_set:``?

        [x] The order is not guaranteed and can vary | Correct! Sets are unordered collections.
        [ ] Items always print in alphabetical or numerical order | Incorrect. Sets do not sort automatically.
        [ ] Items always print in the exact order they were inserted | Incorrect. Sets do not keep insertion order.
        [ ] Items print in reverse order | Incorrect. Set iteration order is non-deterministic.


    .. multichoice::

        How many times will a ``for`` loop execute over ``s = {10, 20, 20, 30}``?

        [ ] 4 times | Incorrect. The duplicate 20 is eliminated when the set is created.
        [x] 3 times | Correct! The set contains 3 unique items ({10, 20, 30}).
        [ ] 2 times | Incorrect. There are 3 unique values.
        [ ] 1 time | Incorrect. It loops through all unique items.


    .. multichoice::

        What operator checks if an item exists inside a set during or before iteration?

        [ ] has | Incorrect. Python uses in.
        [x] in | Correct! The in keyword checks set membership very fast.
        [ ] contains | Incorrect. contains is not a keyword.
        [ ] exists | Incorrect. exists is not a keyword.


    .. multichoice::

        Why is checking ``item in my_set`` faster than ``item in my_list`` for large datasets?

        [x] Sets use hash tables for instant O(1) lookups | Correct! Set membership lookup speed does not depend on dataset size.
        [ ] Sets store items alphabetically | Incorrect. Sets are unordered.
        [ ] Lists are stored on disk while sets are in memory | Incorrect. Both reside in memory.
        [ ] There is no performance difference | Incorrect. Set membership checks are significantly faster.


    .. multichoice::

        What error occurs if you forget to indent code inside a set ``for`` loop body?

        [x] IndentationError | Correct! Python requires indented blocks after colons.
        [ ] KeyError | Incorrect. KeyErrors occur with missing set/dict items.
        [ ] SyntaxError | Incorrect. Python raises a specific IndentationError.
        [ ] TypeError | Incorrect. Indentation governs structural blocks.


    .. multichoice::

        Which function tells you how many elements a loop over a set will visit?

        [ ] count() | Incorrect. Sets do not have a count method.
        [x] len() | Correct! len(my_set) returns the total number of unique elements.
        [ ] size() | Incorrect. size() is not built into Python.
        [ ] total() | Incorrect. total() is not built into Python.


    .. multichoice::

        What will ``for x in {"a", "b"}: print(x, end="")`` print?

        [ ] "ab" only | Incorrect. Because sets are unordered, output could be "ab" or "ba".
        [x] Either "ab" or "ba" | Correct! Unordered iteration means character order is unpredictable.
        [ ] {"a", "b"} | Incorrect. The loop prints items individually.
        [ ] Error | Incorrect. Valid loop syntax.


