===========================
Python Unpacking Iterables
===========================

| In Python, **unpacking** allows you to assign elements from an iterable (such as a tuple, list, or string) directly into individual variables in a single line of code.
| Instead of accessing elements individually by their index numbers, unpacking provides a clean and readable way to extract values.
| Unpacking works with any sequence or collection where Python can iterate through elements step-by-step.

.. code-block:: python

    # Traditional indexing
    point = (10, 20)
    x = point[0]
    y = point[1]

    # Unpacking into variables
    x, y = point  # x gets 10, y gets 20

----

Basic Tuple and List Unpacking
==============================

Basic unpacking works by placing variables on the left side of an assignment operator and an iterable on the right:

- **Exact Matching**: The number of variables on the left **must match** the exact number of elements in the iterable on the right.
- **Order Matters**: Elements are assigned sequentially from left to right based on their position in the collection.
- **Supported Iterables**: Unpacking works on tuples, lists, sets, ranges, and strings.
- **ValueError on Mismatch**: Providing too few or too many variables compared to the iterable elements will raise a ``ValueError``.

.. code-block:: python

    # Unpacking a tuple
    coordinates = (4, 9, 2)
    x, y, z = coordinates

    # Unpacking a list
    colors = ["red", "green", "blue"]
    primary, secondary, tertiary = colors

    # Unpacking a string
    a, b, c = "CAT"  # a="C", b="A", c="T"

Quiz: Basic Tuple and List Unpacking
------------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Unpacking assigns elements from an iterable into multiple @@variables@@ in a single line.
    2. The number of variables on the left must @@match@@ the number of items in the iterable.
    3. If variable count does not match the element count, Python raises a @@ValueError@@.
    4. Unpacking assigns values based on their sequential @@order@@ in the iterable.
    5. Unpacking the string `"PY"` into `a, b` assigns `"P"` to @@a@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Unpack a 2D coordinate tuple into x and y variables and print them.

.. ordering::

    point = (5, 12)
    x, y = point
    print("X:", x)
    print("Y:", y)

----

**Example 2:** Unpack a list of three fruit names into individual variables.

.. ordering::

    fruits = ["apple", "banana", "cherry"]
    f1, f2, f3 = fruits
    print(f1, f2, f3)

----

**Example 3:** Swap two variable values in a single line using unpacking logic.

.. ordering::

    a = 10
    b = 20
    a, b = b, a
    print(a, b)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What happens if you run ``a, b = [10, 20, 30]`` in Python?

        [x] Python raises a ValueError because there are too many values to unpack | Correct! The list has 3 items, but only 2 variables are provided.
        [ ] Python assigns 10 to a and 20 to b, ignoring 30 | Incorrect. Python requires exact matching unless star unpacking is used.
        [ ] Python assigns 10 to a and [20, 30] to b | Incorrect. Standard unpacking does not collect remaining elements without *.
        [ ] Python creates a new variable c automatically | Incorrect. Variable names must be explicitly declared.


    .. multichoice::

        What is stored in variable ``y`` after executing ``x, y, z = (1, 2, 3)``?

        [x] 2 | Correct! Positional unpacking assigns the second element (2) to the second variable (y).
        [ ] 1 | Incorrect. 1 is assigned to x.
        [ ] 3 | Incorrect. 3 is assigned to z.
        [ ] (1, 2, 3) | Incorrect. Unpacking assigns individual elements, not the entire tuple.


    .. multichoice::

        Given ``char1, char2 = "GO"``, what value does ``char2`` hold?

        [x] "O" | Correct! Strings are iterables; unpacking assigns character "G" to char1 and "O" to char2.
        [ ] "G" | Incorrect. "G" is assigned to char1.
        [ ] "GO" | Incorrect. Characters are unpacked individually.
        [ ] ValueError | Incorrect. 2 characters match 2 variables perfectly.


    .. multichoice::

        How does Python perform variable swapping using ``a, b = b, a``?

        [x] It creates a temporary tuple on the right and unpacks it back into the variables on the left | Correct! The right side evaluates to a tuple (b, a) before unpacking into a, b.
        [ ] It modifies computer memory registers directly | Incorrect. Python constructs a tuple under the hood to perform the swap safely.
        [ ] It requires a third temporary variable declared by the user | Incorrect. Unpacking eliminates the need for manual temp variables.
        [ ] It only works for numerical data types | Incorrect. Tuple unpacking swaps any data type.


    .. multichoice::

        What error occurs when running ``x, y, z = (1, 2)``?

        [x] ValueError: not enough values to unpack | Correct! 3 variables need 3 elements, but only 2 are provided.
        [ ] TypeError | Incorrect. Missing elements trigger ValueError.
        [ ] IndexError | Incorrect. IndexErrors occur during manual indexing, not tuple unpacking.
        [ ] NameError | Incorrect. All variable positions are syntactically valid.


    .. multichoice::

        Which statement correctly unpacks a 3-element list ``data = [100, 200, 300]``?

        [x] low, mid, high = data | Correct! Matches 3 variables to 3 list elements.
        [ ] low, high = data | Incorrect. Mismatched count causes ValueError.
        [ ] [low, mid, high] == data | Incorrect. == tests equality rather than assigning unpacking targets.
        [ ] data = low, mid, high | Incorrect. This assigns undefined variables to data.


    .. multichoice::

        Given ``first, second = range(2)``, what is the value of ``second``?

        [x] 1 | Correct! range(2) generates values 0 and 1; first gets 0, second gets 1.
        [ ] 0 | Incorrect. 0 is assigned to first.
        [ ] 2 | Incorrect. range(2) excludes 2 (generates 0, 1).
        [ ] [0, 1] | Incorrect. Values are unpacked individually.


    .. multichoice::

        Why is unpacking preferred over indexing (e.g., ``x = item[0]``)?

        [x] It makes code cleaner, shorter, and less prone to off-by-one indexing errors | Correct! Unpacking improves readability and reduces boilerplate code.
        [ ] It speeds up Python code execution by 500% | Incorrect. It enhances code quality without drastic performance differences.
        [ ] Indexing is deprecated in modern Python | Incorrect. Indexing remains standard for accessing specific elements.
        [ ] Unpacking prevents variables from changing later | Incorrect. Unpacked variables remain mutable.


    .. multichoice::

        Given ``a, b, c = [1, 1, 1]``, what is the value of ``a + b + c``?

        [x] 3 | Correct! Each variable gets 1; $1 + 1 + 1 = 3$.
        [ ] 1 | Incorrect. Three distinct variables each hold value 1.
        [ ] [1, 1, 1] | Incorrect. Unpacked values are numbers, not a list.
        [ ] TypeError | Incorrect. Adding integers is valid.


    .. multichoice::

        What happens when you unpack a set like ``a, b = {10, 20}``?

        [x] Values unpack into a and b, but ordering is not guaranteed across different set instances | Correct! Sets are unordered, so variable assignment order may vary.
        [ ] It always raises a TypeError | Incorrect. Sets are iterables and support unpacking.
        [ ] Python automatically sorts the set before unpacking | Incorrect. Sets do not auto-sort during unpacking.
        [ ] Python converts the set into a string | Incorrect. Data types of elements remain unchanged.

----

Extended Unpacking (The Asterisk * Operator)
=============================================

When the number of elements in an iterable does not match the number of variables, Python provides the **asterisk (``*``) operator** for extended unpacking:

- **Catch-All Variable**: Placing ``*`` before a variable name gathers remaining elements into a **list**.
- **Flexible Position**: The starred variable can be at the beginning, middle, or end of the variable sequence.
- **Single Asterisk Limit**: You can only use **one** starred variable per unpacking expression.
- **Empty List Output**: If there are no extra elements left to capture, the starred variable receives an empty list ``[]``.

.. code-block:: python

    numbers = [1, 2, 3, 4, 5]

    # Star at the end
    first, *rest = numbers  # first = 1, rest = [2, 3, 4, 5]

    # Star in the middle
    first, *middle, last = numbers  # first = 1, middle = [2, 3, 4], last = 5

    # Star at the start
    *head, last = numbers  # head = [1, 2, 3, 4], last = 5

Quiz: Extended Unpacking
------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. The @@*@@ operator is used in extended unpacking to collect multiple remaining elements.
    2. A starred variable always stores collected elements inside a @@list@@.
    3. You can use a maximum of @@1@@ starred variable in a single unpacking assignment.
    4. If there are no spare elements left for a starred variable, it receives an @@empty@@ list.
    5. In `first, *others = [10]`, the variable `others` evaluates to @@[]@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Separate the first item of a list from the remaining items using extended unpacking.

.. ordering::

    scores = [95, 88, 72, 60]
    top, *others = scores
    print("Top score:", top)
    print("Others:", others)

----

**Example 2:** Extract the head, middle, and tail of a sequence.

.. ordering::

    items = ["A", "B", "C", "D", "E"]
    first, *middle, last = items
    print(first, middle, last)

----

**Example 3:** Capture all leading items into a list and isolate the final item.

.. ordering::

    data = [1, 2, 3, 4]
    *previous, current = data
    print("History:", previous)
    print("Current:", current)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Given ``a, *b, c = [1, 2, 3, 4, 5]``, what is the value of ``b``?

        [x] [2, 3, 4] | Correct! a gets 1, c gets 5, and starred variable b collects the middle elements into a list.
        [ ] (2, 3, 4) | Incorrect. Extended unpacking always produces a list, not a tuple.
        [ ] 2 | Incorrect. Starred variables gather all unassigned middle elements.
        [ ] [2, 3, 4, 5] | Incorrect. c absorbs the final element 5.


    .. multichoice::

        What data type does a starred variable (e.g. ``*rest``) produce?

        [x] list | Correct! Extended unpacking always packs remaining elements into a list.
        [ ] tuple | Incorrect. Extended unpacking explicitly produces lists.
        [ ] set | Incorrect. Results are stored in ordered lists.
        [ ] generator | Incorrect. Extended unpacking evaluates and gathers items into concrete lists.


    .. multichoice::

        What is the value of ``extra`` in ``a, b, *extra = [10, 20]``?

        [x] [] | Correct! All elements are absorbed by a and b, leaving an empty list for extra.
        [ ] None | Incorrect. Starred variables receive empty lists [] rather than None.
        [ ] ValueError | Incorrect. Extended unpacking handles zero surplus elements gracefully.
        [ ] 0 | Incorrect. Output is an empty list container [].


    .. multichoice::

        What happens if you attempt to run ``*a, *b = [1, 2, 3, 4]``?

        [x] Python raises a SyntaxError | Correct! Multiple starred target variables in one assignment are forbidden due to ambiguity.
        [ ] a gets [1, 2] and b gets [3, 4] | Incorrect. Python cannot determine where to split items between two starred variables.
        [ ] a gets [1, 2, 3, 4] and b gets [] | Incorrect. Syntax prevents multiple starred variables.
        [ ] Both a and b become [1, 2, 3, 4] | Incorrect. SyntaxError occurs during parsing.


    .. multichoice::

        Given ``*start, end = "PYTHON"``, what does ``end`` hold?

        [x] "N" | Correct! end absorbs the final character "N", while start collects ['P', 'Y', 'T', 'H', 'O'].
        [ ] "PYTHON" | Incorrect. end absorbs only the last element.
        [ ] ['P', 'Y', 'T', 'H', 'O'] | Incorrect. That list is stored in start.
        [ ] "P" | Incorrect. start absorbs leading elements.


    .. multichoice::

        What does ``first, *rest = (5, 10, 15)`` assign to ``rest``?

        [x] [10, 15] | Correct! Unpacking converts tuple remnants into a list [10, 15].
        [ ] (10, 15) | Incorrect. Starred unpacking always outputs a list type regardless of source iterable.
        [ ] 10 | Incorrect. rest captures all remaining elements.
        [ ] 15 | Incorrect. rest captures a list containing both 10 and 15.


    .. multichoice::

        Given ``a, *b, c, d = [1, 2, 3]``, what is the value of ``b``?

        [x] [] | Correct! a=1, c=2, d=3; leaving 0 surplus elements for starred variable b, resulting in [].
        [ ] [2] | Incorrect. c and d absorb 2 and 3 sequentially.
        [ ] ValueError | Incorrect. 3 items fit into 3 positional requirements, giving b an empty list.
        [ ] None | Incorrect. b receives an empty list [].


    .. multichoice::

        What is output by ``x, *y = range(4); print(y)``?

        [x] [1, 2, 3] | Correct! range(4) provides 0, 1, 2, 3. x gets 0, y receives remaining list [1, 2, 3].
        [ ] [0, 1, 2, 3] | Incorrect. x absorbs 0.
        [ ] (1, 2, 3) | Incorrect. Starred variables output lists.
        [ ] 1 | Incorrect. y captures all remaining items into a list.


    .. multichoice::

        Why does Python disallow ``*a, b, *c = [1, 2, 3]``?

        [x] Two starred variables create ambiguous assignment boundaries | Correct! Python cannot determine how many elements belong to each starred list.
        [ ] Variable b must come first | Incorrect. Starred variables can exist at the beginning or end.
        [ ] Lists cannot be unpacked into middle variables | Incorrect. Single starred middle variables are valid.
        [ ] Python only allows star operators in function definitions | Incorrect. Extended unpacking is valid in assignments.


    .. multichoice::

        Given ``head, *tail = "A"``, what is the value of ``tail``?

        [x] [] | Correct! head gets "A", leaving no remaining characters, so tail gets [].
        [ ] ["A"] | Incorrect. "A" is assigned to head.
        [ ] "" | Incorrect. Extended unpacking creates a list [], not an empty string.
        [ ] ValueError | Incorrect. Valid extended unpacking assignment.

----

Unpacking in Loops and Functions
================================

Unpacking is frequently used inside ``for`` loops and function calls to streamline data handling:

- **Loop Unpacking**: Automatically unpack nested structures (like tuples inside a list) directly in the loop header.
- **Dictionary Iteration**: Use ``.items()`` with unpacking to access keys and values simultaneously.
- **Argument Unpacking (*args)**: Use ``*`` in function calls to expand list or tuple elements into positional arguments.
- **Keyword Unpacking (**kwargs)**: Use ``**`` in function calls to unpack dictionary key-value pairs into keyword arguments.

.. code-block:: python

    # Unpacking in a for loop
    pairs = [(1, "one"), (2, "two"), (3, "three")]
    for num, word in pairs:
        print(num, "->", word)

    # Function argument unpacking (* operator)
    def calculate_sum(a, b, c):
        return a + b + c

    nums = [5, 10, 15]
    result = calculate_sum(*nums)  # Equivalent to calculate_sum(5, 10, 15)

Quiz: Unpacking in Loops and Functions
--------------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. When looping over dictionary items with `.items()`, unpacking extracts @@key@@ and value pairs.
    2. The @@*@@ operator unpacks list or tuple elements as individual positional function arguments.
    3. The @@**@@ operator unpacks dictionary key-value pairs as keyword function arguments.
    4. Unpacking inside a `for` loop header automatically extracts elements for each @@iteration@@.
    5. In `for x, y in [(1, 2)]`, the variable `y` receives @@2@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Iterate over a list of coordinate tuples using loop unpacking.

.. ordering::

    points = [(0, 0), (3, 4), (5, 12)]
    for x, y in points:
        print("X:", x, "Y:", y)

----

**Example 2:** Unpack dictionary keys and values simultaneously in a loop.

.. ordering::

    student_grades = {"Alice": "A", "Bob": "B"}
    for name, grade in student_grades.items():
        print(name, "received grade", grade)

----

**Example 3:** Unpack a list of numbers into a function requiring three parameters.

.. ordering::

    def add_three(a, b, c):
        return a + b + c

    values = [10, 20, 30]
    total = add_three(*values)
    print(total)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What does ``for k, v in my_dict.items():`` do in Python?

        [x] It unpacks each dictionary key into k and its corresponding value into v during iteration | Correct! .items() yields (key, value) tuples that unpack cleanly in loop headers.
        [ ] It compares keys and values for equality | Incorrect. k, v performs variable assignment unpacking.
        [ ] It converts the dictionary into a list of keys | Incorrect. Both keys and values are processed.
        [ ] It creates duplicate dictionary keys | Incorrect. Unpacking iterates through existing items.


    .. multichoice::

        Given ``def add(a, b): return a + b`` and ``nums = [3, 7]``, how do you pass ``nums`` into ``add`` using unpacking?

        [x] add(*nums) | Correct! * unpacks list elements into positional parameters a and b.
        [ ] add(nums) | Incorrect. Passing nums directly sends 1 list argument instead of 2 positional numbers.
        [ ] add(**nums) | Incorrect. ** unpacks dictionary mappings, not lists.
        [ ] add(nums*) | Incorrect. Asterisk precedes variable name.


    .. multichoice::

        What is output by ``data = [(1, 2), (3, 4)]; print([x + y for x, y in data])``?

        [x] [3, 7] | Correct! First iteration $1 + 2 = 3$; second iteration $3 + 4 = 7$.
        [ ] [1, 2, 3, 4] | Incorrect. Loop unpacks pairs and evaluates x + y sums.
        [ ] [(1, 2), (3, 4)] | Incorrect. List comprehension outputs calculated results.
        [ ] 10 | Incorrect. List comprehension returns a list of individual tuple sums.


    .. multichoice::

        Which operator unpacks a dictionary into keyword arguments inside a function call?

        [x] ** | Correct! Double asterisk ** unpacks dictionary key-value pairs into keyword arguments.
        [ ] * | Incorrect. Single asterisk * unpacks positional iterables like lists/tuples.
        [ ] & | Incorrect. & is bitwise AND operator.
        [ ] % | Incorrect. % is modulus operator.


    .. multichoice::

        Given ``def greet(name, age): print(f"{name} is {age}")`` and ``info = {"name": "Sam", "age": 14}``, which call is correct?

        [x] greet(**info) | Correct! ** unpacks key-value dictionary pairs into name="Sam", age=14 keyword arguments.
        [ ] greet(*info) | Incorrect. Single * unpacks only dictionary keys ("name", "age") positionally.
        [ ] greet(info) | Incorrect. Passes 1 dictionary argument to function expecting 2 parameters.
        [ ] greet(info**) | Incorrect. Invalid operator syntax.


    .. multichoice::

        What occurs when calling ``add(*[1, 2, 3])`` on a function ``def add(x, y):``?

        [x] TypeError: add() takes 2 positional arguments but 3 were given | Correct! Unpacking 3 elements supplies 3 arguments to a 2-parameter function.
        [ ] Python adds 1 and 2, ignoring 3 | Incorrect. Mismatched argument counts raise TypeError.
        [ ] Python automatically combines 2 and 3 | Incorrect. Exact parameter counts are enforced.
        [ ] It executes normally returning 6 | Incorrect. Argument count exceeds parameter definition.


    .. multichoice::

        In ``for i, (a, b) in enumerate([(10, 20), (30, 40)]):``, what is assigned to ``a`` on the second iteration?

        [x] 30 | Correct! Second tuple is (30, 40); (a, b) unpacks a=30 and b=40.
        [ ] 1 | Incorrect. 1 is the enumerate index i on second iteration.
        [ ] 10 | Incorrect. 10 belongs to first tuple on first iteration.
        [ ] 40 | Incorrect. 40 is assigned to b.


    .. multichoice::

        What is the primary benefit of unpacking inside loop headers?

        [x] It removes the need for indexing syntax like tuple[0] inside loop bodies | Correct! Directly names tuple elements in the loop signature.
        [ ] It causes loops to terminate faster | Incorrect. Improves syntax readability rather than loop execution speed.
        [ ] It automatically sorts elements before processing | Incorrect. Iteration order matches original collection sequence.
        [ ] It allows loops to run backwards | Incorrect. Loop direction remains unchanged.


    .. multichoice::

        What happens when unpacking dictionary keys in ``a, b = {"x": 1, "y": 2}``?

        [x] a gets "x" and b gets "y" | Correct! Iterating over a dictionary directly yields its keys.
        [ ] a gets 1 and b gets 2 | Incorrect. Accessing values requires .values() or dictionary lookup.
        [ ] a gets ("x", 1) and b gets ("y", 2) | Incorrect. Key-value tuples require .items().
        [ ] TypeError | Incorrect. Unpacking dictionaries directly unpacks key sequences.


    .. multichoice::

        Given ``nums = [1, 2, 3]``, what does ``print(*nums)`` execute as?

        [x] print(1, 2, 3) | Correct! Unpacking expands list elements into separate positional arguments passed to print.
        [ ] print([1, 2, 3]) | Incorrect. Unpacking strips list enclosing brackets.
        [ ] print(6) | Incorrect. print displays space-separated arguments rather than summing them.
        [ ] print("123") | Incorrect. Elements are printed as separate positional arguments.



