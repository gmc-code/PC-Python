===========================
Tuples
===========================

| A **tuple** in Python is used to store multiple items in a single variable.
| Tuples are **ordered**, **immutable** (unchangeable), and allow **duplicate values**.
| Tuples are created using parentheses ``()``, with individual items separated by commas.
| Once a tuple is created, you cannot add, remove, or change its items—making tuples perfect for data that should never change!

.. code-block:: python

    # Creating a simple tuple of numbers
    coordinates = (10, 20, 30)

    # Creating a single-item tuple requires a trailing comma
    single_item = ("apple",)  # Without the comma, Python treats this as a regular string!

----

Accessing Tuple Items
=====================

Tuple items are **indexed**, starting at index position ``0`` for the first item.

- **Positive Indexing**: Access items from the front (e.g., ``my_tuple[0]``).
- **Negative Indexing**: Access items from the back (e.g., ``my_tuple[-1]`` for the last item).
- **Slicing**: Extract a portion of a tuple using ``[start:stop]``.

.. code-block:: python

    colors = ("red", "green", "blue", "yellow")

    # Accessing individual items
    first = colors[0]     # Result: "red"
    last = colors[-1]     # Result: "yellow"

    # Slicing a range of items
    middle = colors[1:3]  # Result: ("green", "blue")

Quiz: Accessing Tuple Items
---------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Tuples in Python are defined using @@parentheses@@.
    2. The first item in a tuple is located at index position @@0@@.
    3. To access the last item in a tuple, you can use negative indexing with @@-1@@.
    4. To create a tuple with only one item, you must place a @@comma@@ after the item.
    5. Attempting to access an index that does not exist raises an @@IndexError@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Create a tuple of fruits, access the first item, and print it.

.. ordering::

    fruits = ("apple", "banana", "cherry")
    first_fruit = fruits[0]
    print(first_fruit)

----

**Example 2:** Create a tuple of numbers, access the last item using negative indexing, and print it.

.. ordering::

    numbers = (10, 20, 30, 40)
    last_num = numbers[-1]
    print(last_num)

----

**Example 3:** Slice a tuple to extract the middle two items and print the result.

.. ordering::

    letters = ("a", "b", "c", "d")
    slice_letters = letters[1:3]
    print(slice_letters)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Which character symbol is used to define a tuple in Python?

        [x] Parentheses () | Correct! Tuples are defined using parentheses ().
        [ ] Square brackets [] | Incorrect. Square brackets are used for lists.
        [ ] Curly braces {} | Incorrect. Curly braces are used for sets and dictionaries.
        [ ] Angle brackets <> | Incorrect. Angle brackets are not used to define collections.


    .. multichoice::

        What syntax correctly defines a single-item tuple containing the string ``"cat"``?

        [x] ("cat",) | Correct! A trailing comma is required to define a single-item tuple.
        [ ] ("cat") | Incorrect. Without a trailing comma, Python treats this as a plain string.
        [ ] ("cat";) | Incorrect. Semicolons are not used in Python tuple literals.
        [ ] tuple("cat") | Incorrect. tuple("cat") creates ('c', 'a', 't') by splitting the string.


    .. multichoice::

        What is the result of ``data = (10, 20, 30, 40); print(data[1:3])``?

        [x] (20, 30) | Correct! Slicing includes index 1 up to (but not including) index 3.
        [ ] (10, 20, 30) | Incorrect. Slicing starts at index 1, skipping index 0.
        [ ] (20, 30, 40) | Incorrect. The stop index 3 is non-inclusive.
        [ ] (10, 20) | Incorrect. Slicing starts at index 1 (20) and ends before index 3 (40).


    .. multichoice::

        Given ``items = ("pen", "paper", "ruler")``, how do you access ``"ruler"`` using negative indexing?

        [x] items[-1] | Correct! -1 accesses the final element of a tuple.
        [ ] items[-3] | Incorrect. -3 accesses "pen", the first element.
        [ ] items[-0] | Incorrect. -0 is equivalent to 0, which accesses "pen".
        [ ] items[-2] | Incorrect. -2 accesses "paper".


    .. multichoice::

        What happens if you try to evaluate ``nums = (1, 2, 3); print(nums[5])``?

        [x] Python raises an IndexError | Correct! Accessing an out-of-range index raises an IndexError.
        [ ] Python prints None | Incorrect. Out-of-bounds indexing produces an error.
        [ ] Python prints 3 | Incorrect. Index 5 exceeds the bounds of the tuple.
        [ ] Python returns an empty tuple () | Incorrect. Out-of-bounds indexing raises an exception.


    .. multichoice::

        Which statement accurately describes the ordering property of tuples?

        [x] Tuples are ordered, meaning items maintain their defined sequence | Correct! Tuples preserve item order.
        [ ] Tuples are unordered and automatically sort items alphabetically | Incorrect. Tuples preserve insertion order, not alphabetical sorting.
        [ ] Tuples randomize item order every time they are accessed | Incorrect. Tuple ordering is stable and deterministic.
        [ ] Tuples only support reverse order | Incorrect. Tuples maintain their original sequence.


    .. multichoice::

        What will ``len((5, 10, 15, 20))`` output?

        [x] 4 | Correct! The tuple contains exactly 4 elements.
        [ ] 3 | Incorrect. All 4 elements are counted.
        [ ] 20 | Incorrect. len() counts items, not the value of the last item.
        [ ] 5 | Incorrect. len() returns total item count.


    .. multichoice::

        What type is created by evaluating ``x = (5)`` vs ``y = (5,)``?

        [x] x is an int, y is a tuple | Correct! Without a comma, (5) evaluates as integer 5.
        [ ] Both x and y are tuples | Incorrect. The comma is mandatory for single-item tuples.
        [ ] Both x and y are integers | Incorrect. (5,) is a tuple.
        [ ] x is a tuple, y is an int | Incorrect. The comma signifies the tuple structure.


    .. multichoice::

        What is returned by ``("a", "b", "c")[-2]``?

        [x] "b" | Correct! Index -2 refers to the second-to-last item.
        [ ] "a" | Incorrect. "a" is at index -3.
        [ ] "c" | Incorrect. "c" is at index -1.
        [ ] IndexError | Incorrect. -2 is a valid index for a 3-item tuple.


    .. multichoice::

        Given ``tup = (10, 20, 30, 40, 50)``, what is ``tup[:2]``?

        [x] (10, 20) | Correct! Omitting the start index defaults to 0, slicing up to index 2 (exclusive).
        [ ] (10, 20, 30) | Incorrect. Index 2 is excluded.
        [ ] (30, 40, 50) | Incorrect. tup[:2] extracts items from the start.
        [ ] (20, 30) | Incorrect. Slicing starts at index 0 when unsupplied.

----

Immutability and Updating Tuples
================================

Tuples are **immutable**, which means their elements **cannot be changed, added, or removed** after creation.

-
Attempting to assign a new value to a tuple index (e.g., ``tup[0] = "new"``) raises a **TypeError**.
-
To modify tuple data, you must **convert the tuple into a list**, make your changes, and **convert it back into a tuple**.

.. code-block:: python

    point = (5, 10)

    # ❌ This will raise a TypeError!
    # point[0] = 7

    # ✅ Correct way: Workaround using list conversion
    point_list = list(point)  # Convert tuple to list: [5, 10]
    point_list[0] = 7         # Modify item: [7, 10]
    point = tuple(point_list) # Convert back to tuple: (7, 10)

Quiz: Immutability and Updating
-------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. The property that prevents items in a tuple from being changed is called @@immutability@@.
    2. Modifying a tuple item directly raises a @@TypeError@@.
    3. To change a tuple's content, you can convert it to a list using the @@list()@@ function.
    4. To convert a modified list back into a tuple, use the @@tuple()@@ function.
    5. Unlike lists, tuples do not have an @@.append()@@ method to add new items directly.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Convert a tuple to a list, change an item, and convert it back to a tuple.

.. ordering::

    original = ("a", "b", "c")
    temp_list = list(original)
    temp_list[0] = "z"
    original = tuple(temp_list)

----

**Example 2:** Convert a tuple to a list, add a new item using `.append()`, and convert back to a tuple.

.. ordering::

    data = (1, 2)
    temp = list(data)
    temp.append(3)
    data = tuple(temp)

----

**Example 3:** Convert a tuple to a list, remove an item using `.remove()`, and convert back to a tuple.

.. ordering::

    items = ("shield", "sword", "potion")
    items_list = list(items)
    items_list.remove("sword")
    items = tuple(items_list)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What happens when you try to run ``tup = (1, 2, 3); tup[0] = 99``?

        [x] Python raises a TypeError | Correct! Tuples are immutable and do not support item assignment.
        [ ] The first item changes to 99 so tup becomes (99, 2, 3) | Incorrect. Tuples cannot be modified in place.
        [ ] Python converts the tuple into a list automatically | Incorrect. Explicit conversion is required.
        [ ] Python raises an IndexError | Incorrect. The error type is a TypeError due to immutability.


    .. multichoice::

        Why would a programmer choose a tuple over a list in Python?

        [x] To ensure data cannot be accidentally modified or deleted | Correct! Immutability provides data protection.
        [ ] Because tuples can store more items than lists | Incorrect. Both can store arbitrary numbers of elements.
        [ ] Because tuples allow duplicate items while lists do not | Incorrect. Both support duplicates.
        [ ] Because tuples are mutable | Incorrect. Tuples are immutable, while lists are mutable.


    .. multichoice::

        Which sequence of built-in functions converts tuple ``t`` to a list, then back to a tuple?

        [x] list(t) then tuple(...) | Correct! list() creates a list, and tuple() converts it back.
        [ ] set(t) then dict(...) | Incorrect. Converts to a set and dictionary, altering structure.
        [ ] str(t) then int(...) | Incorrect. Converts to string and integer representation.
        [ ] tuple(t) then list(...) | Incorrect. This executes the conversion steps in reverse order.


    .. multichoice::

        Which method exists on tuples in Python?

        [x] .count() | Correct! .count() is a valid tuple method to count item occurrences.
        [ ] .append() | Incorrect. .append() exists on lists, not tuples.
        [ ] .pop() | Incorrect. .pop() exists on lists and sets, not tuples.
        [ ] .sort() | Incorrect. .sort() modifies lists in place and does not exist on tuples.


    .. multichoice::

        What is the result of ``tuple(["red", "blue"])``?

        [x] ("red", "blue") | Correct! tuple() converts a list into a tuple.
        [ ] ["red", "blue"] | Incorrect. The result is converted into a tuple.
        [ ] ("r", "e", "d", "b", "l", "u", "e") | Incorrect. The list elements become tuple items directly.
        [ ] TypeError | Incorrect. Passing a list to tuple() is valid syntax.


    .. multichoice::

        What error occurs if you try to delete an item using ``del tup[0]`` on a tuple?

        [x] TypeError | Correct! Deleting items from a tuple raises a TypeError because tuples are immutable.
        [ ] KeyError | Incorrect. KeyError applies to sets and dictionaries.
        [ ] ValueError | Incorrect. Item deletion raises TypeError on immutable objects.
        [ ] AttributeError | Incorrect. Syntax is valid but operation is unsupported.


    .. multichoice::

        Can you concatenate two tuples using the ``+`` operator (e.g., ``(1, 2) + (3, 4)``)?

        [x] Yes, it produces a new combined tuple ``(1, 2, 3, 4)`` | Correct! The + operator creates a new tuple combining elements.
        [ ] No, Python raises a TypeError | Incorrect. + concatenation creates a new object without mutating inputs.
        [ ] Yes, but it modifies the first tuple in place | Incorrect. Tuples cannot be modified in place.
        [ ] No, it adds the values numerically to yield (4, 6) | Incorrect. + concatenates collections.


    .. multichoice::

        What happens to the original tuple when you write ``a = (1, 2); a = a + (3,)``?

        [x] A new tuple is created and reassigned to variable ``a`` | Correct! The original tuple isn't changed; a new tuple is bound to the variable name.
        [ ] The original tuple is modified in place | Incorrect. Tuples are immutable and cannot be modified in place.
        [ ] Python raises a TypeError | Incorrect. Reassigning a variable with a new tuple object is completely valid.
        [ ] 3 is added at index 0 | Incorrect. Concatenation appends items to the end.


    .. multichoice::

        Which function returns a sorted **list** from the items of a tuple without altering the tuple?

        [x] sorted(my_tuple) | Correct! sorted() takes an iterable and returns a new sorted list.
        [ ] my_tuple.sort() | Incorrect. .sort() is a list method and does not exist on tuples.
        [ ] my_tuple.order() | Incorrect. No such method exists in Python.
        [ ] sort(my_tuple) | Incorrect. The function name is sorted(), not sort().


    .. multichoice::

        If ``p = (10, 20)``, what is the value of ``p`` after evaluating ``list(p).append(30)``?

        [x] (10, 20) | Correct! list(p) creates a temporary list; modifying it leaves the original tuple ``p`` unchanged.
        [ ] (10, 20, 30) | Incorrect. The modification was made to an unassigned temporary list object.
        [ ] [10, 20, 30] | Incorrect. Variable p still points to the original tuple.
        [ ] TypeError | Incorrect. No error occurs, but p is untouched.

----

Tuple Unpacking and Operations
=============================

Python allows you to extract tuple values directly into variables using **tuple unpacking**. You can also perform operations like checking membership or multiplying tuples.

- **Unpacking**: Assign each item in a tuple to an individual variable.
- **Membership**: Check if an item exists using the ``in`` operator.
- **Repetition**: Multiply a tuple using ``*`` to repeat its contents.

.. code-block:: python

    # Tuple Unpacking
    person = ("Alex", 14, "Year 8")
    name, age, grade = person  # name = "Alex", age = 14, grade = "Year 8"

    # Membership Checking
    is_present = 14 in person   # Result: True

    # Repetition Operator
    pattern = (1, 2) * 3        # Result: (1, 2, 1, 2, 1, 2)


Quiz: Tuple Unpacking and Operations
------------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Extracting tuple elements directly into separate variables is called tuple @@unpacking@@.
    2. When unpacking a tuple, the number of variables must @@match@@ the number of tuple items.
    3. To check if an item exists within a tuple, use the @@in@@ keyword operator.
    4. To repeat the elements of a tuple multiple times, use the multiplication symbol @@*@@.
    5. The tuple method that returns how many times a value appears is @@.count()@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Define a 2-element tuple and unpack its values into `x` and `y` variables.

.. ordering::

    point = (5, 10)
    x, y = point
    print(x)

----

**Example 2:** Multiply a tuple by `2` to repeat its pattern and print the result.

.. ordering::

    base = ("a", "b")
    repeated = base * 2
    print(repeated)

----

**Example 3:** Count how many times the number `1` appears in a tuple and print the count.

.. ordering::

    scores = (1, 2, 1, 3, 1)
    ones_count = scores.count(1)
    print(ones_count)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What error occurs if you try to run ``a, b = (1, 2, 3)``?

        [x] ValueError | Correct! Unpacking raises a ValueError when variable count does not match tuple length.
        [ ] TypeError | Incorrect. Syntax is valid, but item count mismatch produces ValueError.
        [ ] IndexError | Incorrect. Indexing isn't used directly here.
        [ ] KeyError | Incorrect. KeyErrors apply to dictionaries and sets.


    .. multichoice::

        Given ``vals = (10, 20, 10, 30, 10)``, what does ``vals.count(10)`` return?

        [x] 3 | Correct! The number 10 appears 3 times in the tuple.
        [ ] 5 | Incorrect. 5 is the total length of the tuple.
        [ ] 0 | Incorrect. Index 0 contains 10, but count() returns total occurrences.
        [ ] 1 | Incorrect. 10 occurs more than once.


    .. multichoice::

        What does ``vals.index(20)`` return for ``vals = (10, 20, 30)``?

        [x] 1 | Correct! The value 20 is located at index position 1.
        [ ] 20 | Incorrect. .index() returns the index position, not the element value.
        [ ] 0 | Incorrect. Index 0 holds value 10.
        [ ] True | Incorrect. .index() yields integer positions.


    .. multichoice::

        What is the result of ``("hi",) * 3``?

        [x] ("hi", "hi", "hi") | Correct! The * operator repeats tuple elements.
        [ ] ("hihihi",) | Incorrect. * repeats tuple elements, not string content inside an existing element.
        [ ] ("hi", 3) | Incorrect. Repetition multiplies elements.
        [ ] TypeError | Incorrect. Tuple repetition using integers is valid syntax.


    .. multichoice::

        How do you check if the item ``"apple"`` is stored inside tuple ``basket``?

        [x] "apple" in basket | Correct! The in operator returns True if the value is present.
        [ ] basket.has("apple") | Incorrect. .has() is not a tuple method in Python.
        [ ] basket.contains("apple") | Incorrect. .contains() is not a tuple method.
        [ ] "apple" == basket | Incorrect. This compares a string directly to a tuple object.


    .. multichoice::

        What is the result of ``a, b, c = (10, 20, 30); print(b)``?

        [x] 20 | Correct! Variable b receives the second item of the tuple (index 1).
        [ ] 10 | Incorrect. Variable a receives 10.
        [ ] 30 | Incorrect. Variable c receives 30.
        [ ] (10, 20, 30) | Incorrect. Unpacking distributes elements into individual scalar variables.


    .. multichoice::

        Given ``data = (5, 10, 15)``, what does ``20 in data`` evaluate to?

        [x] False | Correct! 20 is not present in the tuple data.
        [ ] True | Incorrect. 20 is absent from the tuple.
        [ ] None | Incorrect. Membership tests evaluate to boolean values.
        [ ] ValueError | Incorrect. Membership testing on missing elements returns False safely.


    .. multichoice::

        What method finds the index position of the FIRST occurrence of a value in a tuple?

        [x] .index() | Correct! .index(value) returns the index of the first match.
        [ ] .find() | Incorrect. .find() is a string method, not a tuple method.
        [ ] .search() | Incorrect. No such method exists on tuples.
        [ ] .locate() | Incorrect. No such method exists on tuples.


    .. multichoice::

        What will ``(1, 2) + (3, 4)`` produce?

        [x] (1, 2, 3, 4) | Correct! + concatenates two tuples into a single new tuple.
        [ ] (4, 6) | Incorrect. + concatenates collections rather than adding values numerically.
        [ ] ((1, 2), (3, 4)) | Incorrect. The tuples are joined at the top level.
        [ ] TypeError | Incorrect. Tuple addition is valid concatenation.


    .. multichoice::

        Given ``info = ("Tom", "Smith")``, what does ``first, last = info`` assign to ``last``?

        [x] "Smith" | Correct! Unpacking maps the second variable "last" to index 1 ("Smith").
        [ ] "Tom" | Incorrect. "Tom" is assigned to "first".
        [ ] ("Tom", "Smith") | Incorrect. Unpacking extracts individual elements.
        [ ] None | Incorrect. Matching variables receive their corresponding elements.

----

Iterating Through a Tuple
=========================

Iterating through a tuple means stepping through each element one by one using a **for loop**. Because tuples are **ordered**, elements are always visited in their exact index order (from index ``0`` to the end).

.. code-block:: python

    cities = ("London", "Paris", "Tokyo")

    # Loop through each item in the tuple
    for city in cities:
        print(f"City: {city}")


Quiz: Iterating Through Tuples
------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. To visit every element in a tuple sequentially, use a @@for@@ loop.
    2. Because tuples are ordered, iteration visits items in their exact @@index@@ order.
    3. The loop statement header must always end with a @@colon@@.
    4. The code block executed inside a loop must be indented by @@4@@ spaces.
    5. You can iterate over tuple indices using ``for i in range(len(my_tuple)):`` with the @@range()@@ function.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Create a tuple of primary colors and print each color in order using a `for` loop.

.. ordering::

    colors = ("red", "green", "blue")
    for color in colors:
        print(color)

----

**Example 2:** Loop through a tuple of numbers and print each number multiplied by `10`.

.. ordering::

    numbers = (1, 2, 3)
    for num in numbers:
        print(num * 10)

----

**Example 3:** Loop through a tuple with `enumerate()` to print both index positions and items.

.. ordering::

    items = ("a", "b", "c")
    for index, item in enumerate(items):
        print(index, item)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        In what order will a ``for`` loop iterate through a tuple ``t = ("first", "second", "third")``?

        [x] Strictly in index order: "first", then "second", then "third" | Correct! Tuples maintain ordered sequence.
        [ ] In random order because tuples are unindexed | Incorrect. Sets are unordered, but tuples are ordered.
        [ ] In reverse order: "third", then "second", then "first" | Incorrect. Iteration processes index 0 through the end.
        [ ] In alphabetical order | Incorrect. Tuples preserve insertion order, not sorted order.


    .. multichoice::

        Which function paired with ``for`` allows you to track both index positions and tuple values simultaneously?

        [x] enumerate() | Correct! enumerate() yields (index, item) pairs during iteration.
        [ ] range() | Incorrect. range() yields numbers, requiring explicit indexing.
        [ ] zip() | Incorrect. zip() combines multiple iterables.
        [ ] count() | Incorrect. count() is a tuple method, not an iteration helper function.


    .. multichoice::

        How many iterations will ``for x in (10, 20, 20, 30):`` perform?

        [x] 4 iterations | Correct! Tuples allow duplicates, so all 4 elements are visited.
        [ ] 3 iterations | Incorrect. Unlike sets, tuples retain duplicate values.
        [ ] 1 iteration | Incorrect. Every element in the tuple is visited once.
        [ ] 0 iterations | Incorrect. Non-empty tuples execute once per item.


    .. multichoice::

        What is output by ``for i in range(len(("a", "b"))): print(i)``?

        [x] 0 then 1 | Correct! len() is 2, so range(2) produces index numbers 0 and 1.
        [ ] "a" then "b" | Incorrect. The loop iterates over range() index numbers, not items.
        [ ] 1 then 2 | Incorrect. Python uses zero-based indexing.
        [ ] ("a", "b") | Incorrect. The loop prints scalar index integers.


    .. multichoice::

        What will happen if you try to modify the tuple item during iteration with ``for x in my_tup: x = 0``?

        [x] The variable ``x`` is changed locally, but the tuple itself remains unchanged | Correct! Reassigning loop variable x does not mutate the tuple.
        [ ] The tuple items are updated to 0 | Incorrect. Tuples are immutable and loop variables are separate bindings.
        [ ] Python raises a TypeError | Incorrect. Reassigning local variable x is valid.
        [ ] Python raises an AttributeError | Incorrect. Valid execution without errors.


    .. multichoice::

        Which keyword breaks out of a tuple ``for`` loop prematurely when a condition is met?

        [x] break | Correct! break terminates the loop immediately.
        [ ] stop | Incorrect. stop is not a Python keyword.
        [ ] exit | Incorrect. exit() is a function, not a loop control statement.
        [ ] skip | Incorrect. continue skips iterations; skip is not a keyword.


    .. multichoice::

        What will ``for item in (): print(item)`` output?

        [x] Nothing (0 iterations) | Correct! An empty tuple has length 0, so the loop body never runs.
        [ ] None | Incorrect. The body is skipped entirely.
        [ ] Error | Incorrect. Iterating over an empty tuple is valid.
        [ ] () | Incorrect. No print statements execute.


