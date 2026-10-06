====================================
Multiple Assignment in Python
====================================

| In Python, **multiple assignment** allows you to assign values to multiple variables in a single line of code.
| This makes your code shorter, cleaner, and easier to read.
| Python supports assigning different values to multiple variables simultaneously, assigning the same value to several variables at once, and extracting elements directly from collections (unpacking).

.. code-block:: python

    # Assigning multiple values in a single line
    name, age, score = "Alex", 14, 95.5

    print(name)   # Output: Alex
    print(age)    # Output: 14
    print(score)  # Output: 95.5

----

Assigning Multiple Values to Multiple Variables
================================================

You can assign multiple values to multiple variables at the same time by separating both variable names and values with commas:

- **Positional Mapping**: Values on the right side of the `=` operator are assigned to variables on the left side in exact positional order.
- **Atomic Evaluation**: Python evaluates all expressions on the right-hand side **first** before making any assignments.
- **Swapping Variables**: This feature makes swapping the values of two variables effortless without needing a temporary variable!

.. code-block:: python

    # Positional assignment
    x, y, z = 10, 20, 30

    # Swapping variables in one line
    a = 5
    b = 90
    a, b = b, a  # Now a is 90 and b is 5!

Quiz: Multiple Values Assignment
--------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. In positional multiple assignment, Python assigns values from left to @@right@@.
    2. Python evaluates all expressions on the @@right@@ side of the `=` sign before assigning values.
    3. You can swap two variables `a` and `b` in one line using the syntax @@a, b = b, a@@.
    4. Multiple variable names on the left side of an assignment must be separated by @@commas@@.
    5. The number of variables on the left must @@match@@ the number of values on the right when assigning multiple values.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Assign three values to three variables in one line and print the second variable.

.. ordering::

    x, y, z = 5, 10, 15
    print(y)

----

**Example 2:** Swap the values of two variables `first` and `second` in a single line.

.. ordering::

    first = "Apple"
    second = "Banana"
    first, second = second, first
    print(first)

----

**Example 3:** Assign two calculated mathematical expressions to two variables simultaneously.

.. ordering::

    width, height = 5 + 5, 10 * 2
    area = width * height
    print(area)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What are the values of ``a`` and ``b`` after running ``a, b = 1, 2``?

        [x] a = 1, b = 2 | Correct! Python assigns values positionally from left to right.
        [ ] a = 2, b = 1 | Incorrect. Values match corresponding variable positions.
        [ ] a = 1, b = 1 | Incorrect. Each variable gets its corresponding positional value.
        [ ] ValueError | Incorrect. Two variables match two values cleanly.


    .. multichoice::

        How do you swap the values of two variables ``x`` and ``y`` in standard Python?

        [x] x, y = y, x | Correct! Python evaluates the right side first and assigns both values simultaneously.
        [ ] x = y; y = x | Incorrect. This sets x to y, losing x's original value before y updates.
        [ ] swap(x, y) | Incorrect. swap() is not a built-in Python function.
        [ ] x == y | Incorrect. == is a comparison check, not an assignment statement.


    .. multichoice::

        What happens if you run ``x, y = 10, 20, 30`` in Python?

        [x] Python raises a ValueError | Correct! Variable count (2) does not match value count (3).
        [ ] x gets 10 and y gets 20, ignoring 30 | Incorrect. Python requires exact count matching.
        [ ] x gets 10 and y gets 30 | Incorrect. Mismatched counts raise an exception.
        [ ] Python automatically creates a third variable z | Incorrect. Variables are not auto-created.


    .. multichoice::

        What output is produced by ``p, q = 3, 4; p, q = q, p + 2; print(p, q)``?

        [x] 4 5 | Correct! Right side evaluates to (4, 3 + 2) which is (4, 5) before assigning to p and q.
        [ ] 4 6 | Incorrect. p was 3 during right-side evaluation.
        [ ] 3 4 | Incorrect. Reassignment updates both variables.
        [ ] 6 4 | Incorrect. p receives q's initial value (4).


    .. multichoice::

        Which character is used to separate variables during multiple assignment?

        [x] Comma (,) | Correct! Commas separate target variables and source expressions.
        [ ] Semicolon (;) | Incorrect. Semicolons separate distinct lines of statements.
        [ ] Colon (:) | Incorrect. Colons mark block header endings.
        [ ] Pipe (|) | Incorrect. Pipes are bitwise or logical union operators.


    .. multichoice::

        Why is atomic evaluation important in ``a, b = b, a + b``?

        [x] Because all right-side expressions are computed using original variable values before any assignment happens | Correct! Atomic evaluation prevents partial state corruption during assignment.
        [ ] Because it runs code twice as fast | Incorrect. Atomic evaluation ensures logic correctness rather than execution speed.
        [ ] Because it converts integers to floats automatically | Incorrect. Values retain their exact data types.
        [ ] Because it prevents syntax errors | Incorrect. It controls order of evaluation during assignment.


    .. multichoice::

        What is the result of ``m, n = 10, 20; m, n = m * 2, n / 2; print(m, n)``?

        [x] 20 10.0 | Correct! m becomes 10 * 2 = 20; n becomes 20 / 2 = 10.0 (float division).
        [ ] 20 10 | Incorrect. Standard division / always returns a float type in Python 3.
        [ ] 10 20 | Incorrect. Reassignment updates both values.
        [ ] ValueError | Incorrect. Counts match correctly.


    .. multichoice::

        Given ``a, b, c = 1, 2, 3``, what does ``print(c)`` output?

        [x] 3 | Correct! c corresponds to the third position on the right-hand side.
        [ ] 1 | Incorrect. 1 is assigned to variable a.
        [ ] 2 | Incorrect. 2 is assigned to variable b.
        [ ] (1, 2, 3) | Incorrect. Positional assignment sets individual scalar values.


    .. multichoice::

        What error is raised by ``a, b, c = 5, 10``?

        [x] ValueError: not enough values to unpack | Correct! 3 variables were provided but only 2 values were given.
        [ ] TypeError | Incorrect. Missing values trigger ValueError during unpacking.
        [ ] IndexationError | Incorrect. No index operations were called.
        [ ] SyntaxError | Incorrect. Syntax structure is valid, but runtime value count mismatches.


    .. multichoice::

        What will ``x, y = 10 + 2, 5 * 2`` leave inside ``x`` and ``y``?

        [x] x = 12, y = 10 | Correct! Right-hand expressions evaluate to 12 and 10 before positional assignment.
        [ ] x = 10, y = 5 | Incorrect. Mathematical expressions are evaluated first.
        [ ] x = 12, y = 2 | Incorrect. 5 * 2 evaluates to 10.
        [ ] SyntaxError | Incorrect. Expressions inside multiple assignments are completely valid.

----

Assigning One Value to Multiple Variables
==========================================

When you want several variables to store the exact same initial value, you can chain assignment operators (`=`):

- **Chained Assignment**: Uses multiple `=` signs in a single statement (e.g., `a = b = c = 0`).
- **Shared Value**: All variables are assigned the exact same value or object reference.
- **Common Uses**: Ideal for initializing multiple counter variables, scores, or flags to zero or default states.

.. code-block:: python

    # Chained assignment
    score1 = score2 = score3 = 0

    print(score1)  # Output: 0
    print(score2)  # Output: 0
    print(score3)  # Output: 0

Quiz: Chained Assignment
------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Setting multiple variables to the same value in one line using multiple `=` signs is called @@chained@@ assignment.
    2. In `a = b = c = 5`, variable `b` receives the value @@5@@.
    3. Chained assignment statements are evaluated from @@right@@ to left.
    4. Chained assignment is commonly used to @@initialize@@ counter or score variables at the start of a program.
    5. Modifying a primitive integer variable `a` after `a = b = 10` does @@not@@ change variable `b`.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Initialize three score variables to zero in a single chained assignment line.

.. ordering::

    player1 = player2 = player3 = 0
    print(player1)

----

**Example 2:** Assign the string `"Active"` to two status variables and print one.

.. ordering::

    status1 = status2 = "Active"
    print(status2)

----

**Example 3:** Initialize two variables to 100, update one, and display both.

.. ordering::

    x = y = 100
    x = x + 50
    print(x, y)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What is the value of variable ``x`` after running ``x = y = z = 50``?

        [x] 50 | Correct! All three variables receive the rightmost value 50.
        [ ] 0 | Incorrect. The rightmost value 50 is assigned.
        [ ] 150 | Incorrect. Chained assignment does not add values together.
        [ ] None | Incorrect. All variables cleanly hold integer 50.


    .. multichoice::

        Which statement correctly initializes ``a``, ``b``, and ``c`` to the number ``10``?

        [x] a = b = c = 10 | Correct! Chained assignment syntax assigns 10 to all targets.
        [ ] a, b, c = 10 | Incorrect. Raises ValueError because 3 variables require 3 values or an iterable.
        [ ] a == b == c == 10 | Incorrect. == tests equality rather than performing variable assignment.
        [ ] a = 10, b = 10, c = 10 | Incorrect. Comma assignment requires proper tuple/value structures.


    .. multichoice::

        Given ``p = q = 5; p = 10``, what are the values of ``p`` and ``q``?

        [x] p = 10, q = 5 | Correct! Reassigning primitive variable p does not alter q.
        [ ] p = 10, q = 10 | Incorrect. Primitive reassignments do not affect other variables.
        [ ] p = 5, q = 5 | Incorrect. p was explicitly reassigned to 10.
        [ ] p = 5, q = 10 | Incorrect. p received 10, q remained 5.


    .. multichoice::

        In which direction does Python process chained assignment statements (like ``a = b = 5``)?

        [x] Right to left | Correct! 5 is evaluated first, then assigned to b, and then assigned to a.
        [ ] Left to right | Incorrect. Rightmost expressions evaluate first in chained assignments.
        [ ] Top to bottom | Incorrect. Evaluation occurs within a single line right-to-left.
        [ ] Randomly | Incorrect. Python evaluation order is strictly defined.


    .. multichoice::

        Why do programmers use chained assignment?

        [x] To cleanly set multiple variables to the same initial starting value | Correct! It removes repetitive assignment lines.
        [ ] To create loops automatically | Incorrect. Loops require for or while statements.
        [ ] To force variables to be read-only constants | Incorrect. Variables remain fully reassignable.
        [ ] To import external modules | Incorrect. Module importing uses import keywords.


    .. multichoice::

        What does ``a = b = c = "Hello"`` output when running ``print(b)``?

        [x] Hello | Correct! Variable b received string "Hello".
        [ ] a | Incorrect. "Hello" is assigned as data content.
        [ ] None | Incorrect. b holds "Hello".
        [ ] SyntaxError | Incorrect. Valid string chained assignment.


    .. multichoice::

        Given ``x = y = 20; y = y + 5``, what does ``print(x)`` yield?

        [x] 20 | Correct! x remains 20 because updating y does not alter x.
        [ ] 25 | Incorrect. Modifying y leaves x untouched.
        [ ] 0 | Incorrect. x was initialized to 20.
        [ ] NameError | Incorrect. Both variables were defined cleanly.


    .. multichoice::

        What is output by ``a = b = c = 2 * 4; print(a)``?

        [x] 8 | Correct! Expression 2 * 4 evaluates to 8 first, assigning 8 to c, b, and a.
        [ ] 2 | Incorrect. Mathematical expression evaluates fully first.
        [ ] 4 | Incorrect. Expression result is 8.
        [ ] 24 | Incorrect. Multiplication yields 8.


    .. multichoice::

        Which of the following is TRUE regarding primitive variables assigned via ``x = y = 100``?

        [x] They act as independent variables holding the value 100 | Correct! Modifying one primitive variable later will not change the other.
        [ ] Changing x will always change y | Incorrect. Integers are immutable primitives.
        [ ] y becomes a constant | Incorrect. Both remain standard reassignable variables.
        [ ] x and y cannot be printed | Incorrect. Both can be printed normally.


    .. multichoice::

        What will ``v1 = v2 = v3 = True; print(v1 and v2)`` evaluate to?

        [x] True | Correct! Both v1 and v2 hold Boolean True, so True and True evaluates to True.
        [ ] False | Incorrect. Both variables hold True.
        [ ] None | Incorrect. Boolean logical check yields True.
        [ ] SyntaxError | Incorrect. Valid Boolean chained assignment.

----

Sequence and Collection Unpacking
=================================

Extracting individual elements from a collection (like a list, tuple, or string) directly into variables is called **unpacking**:

- **List & Tuple Unpacking**: Elements inside a list or tuple are automatically extracted into variables from left to right.
- **String Unpacking**: Individual characters of a string can be unpacked into separate variables.
- **Exact Match Requirement**: The number of variables on the left **must strictly equal** the number of items in the collection.

.. code-block:: python

    # Unpacking a list
    point = [100, 200]
    x_coord, y_coord = point

    # Unpacking a string
    char1, char2, char3 = "CAT"

    print(x_coord)  # Output: 100
    print(char2)    # Output: A

Quiz: Sequence Unpacking
------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Extracting values from a list or tuple into individual variables is called @@unpacking@@.
    2. Unpacking a string like `"PYTHON"` into individual variables yields one @@character@@ per variable.
    3. Unpacking a 3-element list requires exactly @@3@@ receiving variables.
    4. If the variable count does not match the collection length, Python raises a @@ValueError@@.
    5. Elements in list unpacking are assigned in @@positional@@ order from index 0 upwards.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Unpack a list containing RGB color values into three variables.

.. ordering::

    rgb_colors = [255, 128, 0]
    red, green, blue = rgb_colors
    print(red)

----

**Example 2:** Unpack a 3-letter string into three separate character variables.

.. ordering::

    word = "DOG"
    letter1, letter2, letter3 = word
    print(letter2)

----

**Example 3:** Unpack a nested tuple of dimensions and compute volume.

.. ordering::

    dimensions = (2, 5, 10)
    length, width, height = dimensions
    volume = length * width * height
    print(volume)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Given ``data = [10, 20, 30]; x, y, z = data``, what value is assigned to ``y``?

        [x] 20 | Correct! y receives the second item from list data (index 1).
        [ ] 10 | Incorrect. 10 is assigned to x.
        [ ] 30 | Incorrect. 30 is assigned to z.
        [ ] [10, 20, 30] | Incorrect. Unpacking extracts individual values.


    .. multichoice::

        What happens if you run ``a, b = [1, 2, 3]`` in Python?

        [x] Python raises a ValueError: too many values to unpack | Correct! Cannot unpack a 3-item list into only 2 variables.
        [ ] a gets 1 and b gets 2, ignoring 3 | Incorrect. Strict count matching is required.
        [ ] a gets [1, 2] and b gets 3 | Incorrect. Requires explicit extended unpacking syntax.
        [ ] TypeError is raised | Incorrect. Mismatched unpacking length raises ValueError.


    .. multichoice::

        What is assigned to ``b`` when unpacking string ``a, b, c = "SKY"``?

        [x] "K" | Correct! Strings are iterables; the second character "K" maps to b.
        [ ] "S" | Incorrect. "S" is assigned to variable a.
        [ ] "Y" | Incorrect. "Y" is assigned to variable c.
        [ ] "SKY" | Incorrect. Unpacking distributes single characters.


    .. multichoice::

        Which Python data structure can be unpacked into variables?

        [x] Any iterable collection (lists, tuples, strings, sets) | Correct! Python supports unpacking on all iterable objects.
        [ ] Only integers | Incorrect. Integers are non-iterable scalar values.
        [ ] Only booleans | Incorrect. Booleans cannot be iterated or unpacked.
        [ ] Only float numbers | Incorrect. Floats are scalar objects.


    .. multichoice::

        Given ``pairs = (4, 8); num1, num2 = pairs``, what does ``print(num1 + num2)`` output?

        [x] 12 | Correct! num1 receives 4 and num2 receives 8; 4 + 8 = 12.
        [ ] 48 | Incorrect. Unpacked items are numeric integers, so addition occurs.
        [ ] (4, 8) | Incorrect. Values are extracted from tuple pairs.
        [ ] TypeError | Incorrect. Addition of integers is valid.


    .. multichoice::

        What error occurs if you try to unpack a non-iterable object like ``x, y = 100``?

        [x] TypeError: cannot unpack non-iterable int object | Correct! Integers are not iterables and cannot be unpacked.
        [ ] ValueError | Incorrect. Non-iterables fail type checks first.
        [ ] NameError | Incorrect. Identifier syntax is valid.
        [ ] IndexError | Incorrect. No list indexing took place.


    .. multichoice::

        If ``coords = [5, 10]``, which statement successfully extracts both values?

        [x] x, y = coords | Correct! Unpacks both items into variables x and y.
        [ ] x, y = coords[] | Incorrect. Invalid syntax bracket usage.
        [ ] x = y = coords | Incorrect. Assigns the whole list reference to both variables.
        [ ] coords = x, y | Incorrect. Tries to assign unassigned variables x and y into coords.


    .. multichoice::

        What is output by ``items = ["book", "pen"]; item1, item2 = items; print(item1)``?

        [x] book | Correct! item1 gets the first list element "book".
        [ ] pen | Incorrect. "pen" is assigned to item2.
        [ ] ["book", "pen"] | Incorrect. Unpacking extracts individual scalar elements.
        [ ] SyntaxError | Incorrect. Valid list unpacking syntax.


    .. multichoice::

        Given ``a, b, c = [7, 7, 7]``, what is ``print(a == b == c)``?

        [x] True | Correct! All three variables hold value 7, making equality test True.
        [ ] False | Incorrect. All values equal 7.
        [ ] 7 | Incorrect. Equality check yields Boolean True.
        [ ] ValueError | Incorrect. Counts match perfectly.


    .. multichoice::

        Why is unpacking considered a Pythonic practice?

        [x] It allows clean, readable variable extraction without writing multiple indexing lines (e.g. ``x = point[0]``) | Correct! Unpacking eliminates verbose indexing syntax.
        [ ] It bypasses variable scope rules | Incorrect. Scope rules apply equally.
        [ ] It speeds up internet downloading | Incorrect. Unpacking affects code syntax in memory.
        [ ] It automatically prints variables to the console | Incorrect. Console output requires print().

