==========================
Variables
==========================

| A variable is a name used to refer to a memory location where a value is stored.
| It can be thought of as a box that stores data.
| In Python, the same variable can be reused to store values of any type.
| e.g In ``rectangle_length = 2.3``, the variable names is ``rectangle_length``, the type is ``float`` (decimal) and the value is ``2.3``.
| e.g In ``user_name = Annie``, the variable names is ``user_name``, the type is ``str`` (string) and the value is ``Annie``.

Rules for Python variable names:
    • A variable name must start with a letter or the underscore character
    • A variable name cannot start with a number
    • A variable name can only contain alpha-numeric characters (A-z, 0-9) and underscores ( _ )
    • Variable names are case-sensitive (``age``, ``Age`` and ``AGE`` are three different variables)

----

Python Reserved Words
--------------------------

Reserved Words are keywords that have a set meaning and can't be used for other purposes such as for variable names. Reserved words are case-sensitive and must be used exactly as shown. They are all entirely lowercase, except for False, None, and True.

| The list of reserved words is:

| False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

| A list of keywords can be shown by using ``print(help("keywords"))``.
| A second method for listing keywords uses the keyword library. (see: https://docs.python.org/3/library/keyword.html)

.. code-block:: python

    import keyword

    print(keyword.kwlist)

----

Python conventions
--------------------------

| It is helpful to use meaningful variable names that indicate what the variable is. e.g. ``height`` instead of ``x`` for the height of an object.

Snake case
---------------

| Snake case is used for variables and functions.
| Snake case uses underscores between words. e.g. player_count, player_1_score, player_2_score

ALL_CAPS
---------------

| ALL_CAPS are used for constants, such as ``PI = 3.14``, ``GRAVITY = 9.8``, ``MILES_TO_METRES = 1609``.

CapWords
---------------

| CapWords, such as ``AnimalFeatures``, are used for Class names in python.

camelCase
---------------

| camelCase variables, such as ``playerScore``, are not recommended in python.

KebabCase
---------------

| KebabCase variables, such as ``player-score``, are not recommended in python.

----

Sample code
--------------------------

| The print statement below can be generalised using a variable for the team name and a variable for the number of premierships.
| This is good practice since it separates the data from the output.

.. code-block:: python

    print('Federer has won 20 Grand Slams.')

Generalised to:

.. code-block:: python

    player_name = 'Federer'
    wins = '20'
    print(player_name + ' has won ' + wins + ' Grand Slams.')

----

Tasks
--------------------------

.. admonition:: Questions

    #. Write ``AGE`` in snake case.
    #. Write ``MyName`` in snake case.
    #. Write ``MyFirstNameLastName`` in snake case.
    #. Write ``rectangleArea`` in snake case.
    #. Write ``cm_in_an_inch = 2.14`` as ALL_CAPS.
    #. Write ``lbs_in_a_kg = 2.2`` as ALL_CAPS.
    #. A program asks for a person's age and stores it. What would be a good variable to use: ``x``, ``variable1``, ``AGE``, ``age``, ``Years_Old``?
    #. A program uses a person's first name and last name. What would be a good variable to use for their last name: ``x``, ``variable1``, ``SURNAME``, ``last_name``, ``Name``?
    #. A program calculates the area of a rectangle. What would be two good variables to use for the length and width of the rectangle: ``x``, ``y``, ``LENGTH``, ``length``, ``Width``, ``width``?

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write ``AGE`` in snake case.

                .. code-block:: python

                    age

            .. tab-item:: Q2

                Write ``MyName`` in snake case.

                .. code-block:: python

                    my_name

            .. tab-item:: Q3

                Write ``MyFirstNameLastName`` in snake case.

                .. code-block:: python

                    my_first_name_last_name

            .. tab-item:: Q4

                Write ``rectangleArea`` in snake case.

                .. code-block:: python

                    rectangle_area

            .. tab-item:: Q5

                Write ``cm_in_an_inch = 2.14`` as ALL_CAPS.

                .. code-block:: python

                    CM_IN_AN_INCH = 2.14

            .. tab-item:: Q6

                Write ``lbs_in_a_kg = 2.2`` as ALL_CAPS.

                .. code-block:: python

                    LBS_IN_A_KG = 2.2

            .. tab-item:: Q7

                A program asks for a person's age and stores it. What would be a good variable to use: ``x``, ``variable1``, ``AGE``, ``age``, ``Years_Old``?

                .. code-block:: python

                    age

            .. tab-item:: Q8

                A program uses a person's first name and last name. What would be a good variable to use for their last name: ``x``, ``variable1``, ``SURNAME``, ``last_name``, ``Name``?

                .. code-block:: python

                    last_name

            .. tab-item:: Q9

                A program calculates the area of a rectangle. What would be two good variables to use for the length and width of the rectangle: ``x``, ``y``, ``LENGTH``, ``length``, ``Width``, ``width``?

                .. code-block:: python

                    length, width
===========================
Variables
===========================

| A **variable** in Python is used to store data in computer memory so it can be used and modified later in a program.
| Think of a variable as a labeled container or box holding a piece of information.
| In Python, variables are created automatically the moment you assign a value to them using the assignment operator ``=``.
| Variables can store different types of data, such as text (strings), whole numbers (integers), and decimal numbers (floats).

.. code-block:: python

    # Creating variables with different data types
    player_name = "Alex"  # String (text)
    score = 100           # Integer (whole number)
    speed = 4.5           # Float (decimal number)

----

Variable Naming Rules
=====================

When naming variables in Python, you must follow specific rules and conventions:

- **Must start with a letter or an underscore (`_`)**: A variable name cannot start with a number.
- **Can only contain alphanumeric characters and underscores**: Only letters (`a-z`, `A-Z`), numbers (`0-9`), and `_` are allowed.
- **Case-sensitive**: `score`, `Score`, and `SCORE` are three completely different variables!
- **Use snake_case**: Use lowercase letters separated by underscores for multi-word names (e.g., `player_score`).

.. code-block:: python

    # ✅ Valid variable names
    user_age = 14
    _total = 50
    player2_score = 95

    # ❌ Invalid variable names (will cause SyntaxError)
    # 2nd_place = "Bob"   # Starts with a number
    # user-name = "Sam"   # Contains a hyphen (-)
    # total score = 100   # Contains spaces

Quiz: Variable Naming Rules
---------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. In Python, variables are created using the @@=@@ assignment operator.
    2. A variable name cannot start with a @@number@@.
    3. Multi-word variable names in Python typically use @@snake_case@@ naming style with underscores.
    4. Variable names in Python are @@case-sensitive@@, meaning `age` and `Age` are distinct.
    5. Attempting to use a variable with spaces in its name raises a @@SyntaxError@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Define a valid player name variable, assign a string, and print it.

.. ordering::

    player_name = "Jordan"
    print(player_name)

----

**Example 2:** Create two distinct variables demonstrating case sensitivity, then print their sum.

.. ordering::

    score = 10
    Score = 20
    total = score + Score
    print(total)

----

**Example 3:** Assign a score using snake_case, update it, and print the updated value.

.. ordering::

    current_score = 50
    current_score = current_score + 10
    print(current_score)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Which of the following is a valid Python variable name?

        [x] my_total_score | Correct! Uses letters, underscores, and lowercase snake_case syntax.
        [ ] 1st_player | Incorrect. Variable names cannot start with a number.
        [ ] player-score | Incorrect. Variable names cannot contain hyphens (-).
        [ ] user score | Incorrect. Variable names cannot contain spaces.


    .. multichoice::

        What operator symbol is used to assign a value to a variable in Python?

        [x] = | Correct! The single equals sign = is the assignment operator.
        [ ] == | Incorrect. == is used to compare equality, not for variable assignment.
        [ ] := | Incorrect. = is the standard assignment operator.
        [ ] -> | Incorrect. -> is used in function type annotations.


    .. multichoice::

        What happens if you define ``x = 5`` and then try to run ``print(X)``?

        [x] Python raises a NameError | Correct! Variables are case-sensitive, so capital X is not defined.
        [ ] Python prints 5 | Incorrect. x and X are distinct due to case sensitivity.
        [ ] Python prints None | Incorrect. Python raises an unhandled NameError exception.
        [ ] Python creates X automatically and assigns 0 | Incorrect. Python will not auto-define X.


    .. multichoice::

        Which variable naming convention is recommended by Python style guidelines (PEP 8)?

        [x] snake_case (e.g., user_age) | Correct! Snake case with lowercase letters and underscores is the standard.
        [ ] camelCase (e.g., userAge) | Incorrect. camelCase is common in JavaScript, but not Python's default style.
        [ ] PascalCase (e.g., UserAge) | Incorrect. PascalCase is reserved primarily for class names in Python.
        [ ] UPPERCASE (e.g., USERAGE) | Incorrect. UPPERCASE is reserved for constants.


    .. multichoice::

        Why is ``class = 10`` an invalid variable name in Python?

        [x] Because ``class`` is a reserved Python keyword | Correct! Reserved keywords cannot be used as variable names.
        [ ] Because variable names cannot hold numbers | Incorrect. Variables can store numbers.
        [ ] Because it starts with a lowercase letter | Incorrect. Starting with lowercase is standard practice.
        [ ] Because 10 is an integer | Incorrect. Integers are valid variable values.


    .. multichoice::

        What is the primary function of a variable in computer programming?

        [x] To store data values in memory for later use and manipulation | Correct! Variables act as named containers for data.
        [ ] To display text on the screen | Incorrect. print() displays text on the screen.
        [ ] To prevent bugs from occurring | Incorrect. Variables store data rather than handle errors.
        [ ] To create loops automatically | Incorrect. For and while structures create loops.


    .. multichoice::

        Which statement about Python variable creation is TRUE?

        [x] Variables are created automatically when you assign a value to them | Correct! Python requires no explicit declaration keyword.
        [ ] You must declare the variable type (like int or string) before using it | Incorrect. Python uses dynamic typing.
        [ ] You must use the keyword ``var`` or ``let`` to create a variable | Incorrect. Python uses simple assignment syntax.
        [ ] Variables can only be created at the top of a file | Incorrect. Variables can be created anywhere.


    .. multichoice::

        What will ``_count = 100; print(_count)`` output?

        [x] 100 | Correct! Variable names starting with an underscore are completely valid in Python.
        [ ] SyntaxError | Incorrect. Underscores are valid initial characters.
        [ ] NameError | Incorrect. _count is properly assigned before printing.
        [ ] None | Incorrect. _count evaluates to 100.


    .. multichoice::

        Which character cannot be used anywhere inside a Python variable name?

        [x] $ | Correct! Special symbols like $, @, !, and % are not permitted in variable names.
        [ ] _ | Incorrect. Underscores are valid and widely used in variable names.
        [ ] 5 | Incorrect. Numbers can be used anywhere except as the first character.
        [ ] a | Incorrect. Letters are valid variable characters.


    .. multichoice::

        Given ``a = 5`` and ``A = 10``, what does ``print(a + A)`` yield?

        [x] 15 | Correct! Since variables are case-sensitive, a and A store separate values (5 and 10).
        [ ] 10 | Incorrect. Both variables contribute to the sum.
        [ ] 20 | Incorrect. a is 5, not 10.
        [ ] NameError | Incorrect. Both variables are validly defined.

----

Updating Variables and Dynamic Typing
======================================

In Python, variables are **dynamic**, meaning:

- **Values can be overwritten**: Assigning a new value replaces the old value stored in the variable.
- **Data types can change**: A variable holding a number can later be assigned a string.
- **Re-assignment using existing values**: You can update a variable based on its current value (e.g., incrementing a counter).

.. code-block:: python

    # Overwriting a variable value
    health = 100
    health = 80          # Replaced 100 with 80

    # Updating a variable relative to its current value
    health = health - 15  # Result: 65

    # Changing the data type dynamically
    data = 42            # Currently an integer
    data = "Forty-two"   # Now a string!

Quiz: Updating Variables
------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Replacing an existing variable's value with a new one is called @@reassigning@@.
    2. Python allows a variable to hold different data types over time because it uses @@dynamic@@ typing.
    3. To increase a number variable ``x`` by 1, you can write ``x = x + 1`` or use the shorthand @@x += 1@@.
    4. Attempting to reference a variable before assigning a value to it causes a @@NameError@@.
    5. The built-in function @@type()@@ can be used to check the current data type of a variable.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Initialize a variable, update its value by adding `5`, and print it.

.. ordering::

    coins = 10
    coins = coins + 5
    print(coins)

----

**Example 2:** Reassign a variable from an integer to a string, then print the variable's type.

.. ordering::

    val = 100
    val = "One Hundred"
    print(type(val))

----

**Example 3:** Swap the values of two variables `a` and `b` using Python's tuple assignment.

.. ordering::

    a = 1
    b = 2
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

        What is the final value of ``score`` after evaluating ``score = 10; score = score + 5; score = 20``?

        [x] 20 | Correct! The final assignment ``score = 20`` completely overwrites previous values.
        [ ] 15 | Incorrect. 15 was overwritten by the final assignment of 20.
        [ ] 35 | Incorrect. Assignments overwrite rather than accumulate unless explicitly added.
        [ ] 10 | Incorrect. Initial value 10 was modified and then overwritten.


    .. multichoice::

        What does the statement ``count += 1`` do in Python?

        [x] Adds 1 to the current value of ``count`` and updates the variable | Correct! += is shorthand for count = count + 1.
        [ ] Checks if count is equal to 1 | Incorrect. == checks equality.
        [ ] Creates a new variable named count1 | Incorrect. += modifies the variable in place.
        [ ] Multiplies count by 1 | Incorrect. *= performs multiplication assignment.


    .. multichoice::

        What happens when you run ``x = 5; x = "hello"`` in Python?

        [x] ``x`` cleanly changes from an integer to storing the string "hello" | Correct! Python features dynamic typing.
        [ ] Python raises a TypeError because types cannot change | Incorrect. Python allows dynamic reassignment across types.
        [ ] ``x`` stores both 5 and "hello" in a list | Incorrect. Reassignment replaces the old value.
        [ ] Python raises a SyntaxError | Incorrect. Type reassignment is standard syntax.


    .. multichoice::

        Which built-in function tells you the current data type stored in variable ``item``?

        [x] type(item) | Correct! type() returns the class type of the object.
        [ ] typeof(item) | Incorrect. typeof is used in JavaScript, not Python.
        [ ] class(item) | Incorrect. class is a reserved keyword for object definitions.
        [ ] datatype(item) | Incorrect. No such built-in function exists in Python.


    .. multichoice::

        What error occurs if you run ``print(points)`` before defining ``points = 0``?

        [x] NameError | Correct! Referencing an unassigned variable raises a NameError.
        [ ] TypeError | Incorrect. TypeErrors occur during invalid operation combinations.
        [ ] ValueError | Incorrect. ValueErrors occur with incompatible arguments.
        [ ] AttributeError | Incorrect. AttributeErrors occur with missing object methods.


    .. multichoice::

        Given ``a = 3; b = a; a = 5``, what is the value stored in ``b``?

        [x] 3 | Correct! b was assigned the value of a when a was 3; changing a later does not update b.
        [ ] 5 | Incorrect. Primitive variable assignment copies the value at execution time.
        [ ] 8 | Incorrect. Values are separate, not combined.
        [ ] None | Incorrect. b holds value 3.


    .. multichoice::

        What does evaluating ``x = 10; x *= 2`` leave inside ``x``?

        [x] 20 | Correct! *= multiplies the current value (10) by 2 and reassigns it.
        [ ] 12 | Incorrect. += adds, whereas *= multiplies.
        [ ] 100 | Incorrect. 10 * 2 equals 20.
        [ ] 5 | Incorrect. /= divides, whereas *= multiplies.


    .. multichoice::

        What type is returned by ``type(3.14)``?

        [x] <class 'float'> | Correct! Decimal numbers in Python are classified as float objects.
        [ ] <class 'int'> | Incorrect. Whole numbers are integers, whereas 3.14 is a decimal.
        [ ] <class 'str'> | Incorrect. Unquoted decimal numbers are float types.
        [ ] <class 'decimal'> | Incorrect. The standard built-in type name is float.


    .. multichoice::

        What does shorthand ``a -= 3`` do?

        [x] Subtracts 3 from variable ``a`` and updates its value | Correct! -= is shorthand for a = a - 3.
        [ ] Checks if a is less than -3 | Incorrect. Comparison operators do not use -=.
        [ ] Sets variable a equal to -3 | Incorrect. Direct assignment uses = -3.
        [ ] Creates a negative variable | Incorrect. -= subtracts and reassigns.


    .. multichoice::

        What is the result of running ``x = 10; x = x / 2; print(type(x))``?

        [x] <class 'float'> | Correct! Division / always returns a float in Python 3.
        [ ] <class 'int'> | Incorrect. Standard division converts results to float (5.0).
        [ ] <class 'str'> | Incorrect. Numbers remain numeric types.
        [ ] <class 'double'> | Incorrect. Python represents floating-point numbers as float.

----

Multiple Variable Assignment and Unpacking
=========================================

Python provides concise syntax shortcuts for creating and assigning multiple variables simultaneously:

- **Assigning multiple values to multiple variables**: Assign distinct items in one line using commas.
- **Assigning one value to multiple variables**: Assign the exact same value across several variables.
- **Unpacking collections**: Extract values from lists or tuples directly into variables.

.. code-block:: python

    # Assigning multiple values in one line
    x, y, z = 1, 2, 3              # x=1, y=2, z=3

    # Assigning the same value to multiple variables
    a = b = c = 0                  # a=0, b=0, c=0

    # Unpacking a list into variables
    fruits = ["apple", "banana"]
    first, second = fruits         # first="apple", second="banana"

Quiz: Multiple Assignment and Unpacking
---------------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Setting multiple variables to the exact same value in one line uses multiple @@=@@ signs.
    2. Extracting elements from a list into individual variables is called list @@unpacking@@.
    3. In multiple assignment ``x, y = 10, 20``, variable ``y`` receives the value @@20@@.
    4. Unpacking a list into variables requires the number of variables to @@match@@ the number of list elements.
    5. If unpacking variable count does not match collection length, Python raises a @@ValueError@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Assign three values to three variables in a single line and print their sum.

.. ordering::

    x, y, z = 10, 20, 30
    total = x + y + z
    print(total)

----

**Example 2:** Assign zero to three variables simultaneously and print one of them.

.. ordering::

    score1 = score2 = score3 = 0
    print(score1)

----

**Example 3:** Unpack a list of coordinates into `x_pos` and `y_pos` variables and print `x_pos`.

.. ordering::

    coords = [150, 300]
    x_pos, y_pos = coords
    print(x_pos)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What are the values of ``a`` and ``b`` after executing ``a, b = 5, 10``?

        [x] a = 5, b = 10 | Correct! Values map positionally from left to right.
        [ ] a = 10, b = 5 | Incorrect. Values match variables in corresponding order.
        [ ] a = 15, b = 15 | Incorrect. Values are assigned individually.
        [ ] ValueError | Incorrect. Two variables match two values cleanly.


    .. multichoice::

        What does ``x = y = z = 100`` achieve?

        [x] Assigns integer 100 to all three variables x, y, and z | Correct! Chained assignment sets all targets to the rightmost value.
        [ ] Compares whether x, y, and z equal 100 | Incorrect. Equality checking uses == operators.
        [ ] Raises a SyntaxError | Incorrect. Chained assignment is valid syntax.
        [ ] Assigns 100 to x, 0 to y, and 0 to z | Incorrect. All targets receive 100.


    .. multichoice::

        What error occurs if you try ``a, b = [1, 2, 3]``?

        [x] ValueError | Correct! ValueError occurs when unpacking mismatched counts (2 variables vs 3 items).
        [ ] TypeError | Incorrect. Syntax is valid, but item counts mismatch.
        [ ] IndexError | Incorrect. Direct list indexing was not performed.
        [ ] NameError | Incorrect. Variables are assigned during execution.


    .. multichoice::

        How do you swap the values of two variables ``p`` and ``q`` without using a third temporary variable?

        [x] p, q = q, p | Correct! Tuple packing/unpacking swaps variables atomically in one line.
        [ ] p = q; q = p | Incorrect. Overwrites p with q first, losing p's original value.
        [ ] swap(p, q) | Incorrect. swap() is not a built-in Python function.
        [ ] p == q | Incorrect. == tests equality without updating variables.


    .. multichoice::

        Given ``colors = ["red", "green"]; c1, c2 = colors``, what does ``print(c2)`` output?

        [x] "green" | Correct! c2 gets the second item from the list colors.
        [ ] "red" | Incorrect. c1 receives "red".
        [ ] ["red", "green"] | Incorrect. Unpacking extracts scalar string values.
        [ ] TypeError | Incorrect. Valid list unpacking syntax.


    .. multichoice::

        What will ``x, y, z = "ABC"`` assign to variable ``y``?

        [x] "B" | Correct! Strings are iterables, so unpacking extracts each character into variables.
        [ ] "ABC" | Incorrect. Individual characters are unpacked positionally.
        [ ] "A" | Incorrect. "A" is assigned to x.
        [ ] "C" | Incorrect. "C" is assigned to z.


    .. multichoice::

        What is the outcome of ``a = 1, 2, 3; print(type(a))``?

        [x] <class 'tuple'> | Correct! Assigning comma-separated values without parentheses creates a tuple object.
        [ ] <class 'int'> | Incorrect. Comma separation packs elements into a tuple.
        [ ] <class 'list'> | Incorrect. Square brackets [] are required for explicit list literals.
        [ ] SyntaxError | Incorrect. Automatic tuple packing is valid Python syntax.


    .. multichoice::

        Given ``m, n = 10 * 2, 30 + 5``, what value does ``n`` hold?

        [x] 35 | Correct! Expressions are evaluated first before positionally assigning to n.
        [ ] 20 | Incorrect. 20 is assigned to m.
        [ ] 55 | Incorrect. Values evaluate separately before assignment.
        [ ] 10 | Incorrect. Expressions are fully evaluated first.


    .. multichoice::

        If ``data = [100]``, what happens when you run ``x, y = data``?

        [x] Python raises a ValueError | Correct! Cannot unpack 1 item into 2 variables.
        [ ] x becomes 100 and y becomes None | Incorrect. Mismatched unpacking counts raise an exception.
        [ ] x becomes 100 and y becomes 0 | Incorrect. Python does not provide default values during unpacking.
        [ ] Both x and y become 100 | Incorrect. Python requires explicit variable-to-value matches.


    .. multichoice::

        What is output by ``x = 5; y = 10; x, y = y, x + 2; print(x, y)``?

        [x] 10 7 | Correct! Right side evaluates to (10, 7) before assigning to x and y simultaneously.
        [ ] 10 12 | Incorrect. x was 5 when evaluating x + 2.
        [ ] 5 10 | Incorrect. Variables swap and reassign values.
        [ ] 12 7 | Incorrect. Expression uses right-hand initial state.

----

Variable Scope and Constants
============================

Understanding where variables can be accessed (**scope**) and how to represent unchanging values (**constants**) is essential:

- **Global Scope**: Variables defined outside functions, accessible throughout the script.
- **Local Scope**: Variables defined inside a function, accessible **only** within that function.
- **Constants**: Values that should not change throughout a program. Python does not have enforced constants, but programmers use **ALL_CAPS** names as a convention!

.. code-block:: python

    # Constant convention (ALL_CAPS)     MAX_SPEED = 120
    PI = 3.14159

    # Global variable
    player_status = "Active"

    def update_game():
        # Local variable (only exists inside this function)
        local_score = 50
        print(player_status)  # Can access global variable

    update_game()
    # print(local_score)  # ❌ Error! local_score does not exist outside the function.

Quiz: Variable Scope and Constants
----------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. A variable declared inside a function has @@local@@ scope.
    2. A variable declared outside all functions has @@global@@ scope.
    3. In Python, constants are indicated by writing variable names in @@ALL_CAPS@@.
    4. Trying to access a local variable from outside its function causes a @@NameError@@.
    5. To modify a global variable inside a function, use the @@global@@ keyword keyword.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Define a global constant and display it inside a function call.

.. ordering::

    MAX_LEVEL = 10
    def show_max():
        print(MAX_LEVEL)
    show_max()

----

**Example 2:** Define a global variable, modify it inside a function using `global`, and print it.

.. ordering::

    score = 0
    def add_points():
        global score
        score += 10
    add_points()

----

**Example 3:** Demonstrate local scope by defining a local variable inside a function.

.. ordering::

    def calculate():
        result = 42
        print(result)
    calculate()

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        How do Python programmers indicate that a variable should be treated as a CONSTANT (unchanging value)?

        [x] By writing the variable name in ALL_CAPS (e.g., MAX_USERS = 100) | Correct! Uppercase naming is the standard convention for constants.
        [ ] By using the keyword ``const`` before the variable name | Incorrect. Python does not have a const keyword.
        [ ] By putting dollar signs around the variable name | Incorrect. Dollar signs are not valid in variable names.
        [ ] Python automatically locks variables that contain numbers | Incorrect. Python variables remain reassignable.


    .. multichoice::

        What happens if you try to access a local variable outside the function where it was created?

        [x] Python raises a NameError | Correct! Local variables cease to exist outside their function scope.
        [ ] Python returns None | Incorrect. Out-of-scope variable access raises an error.
        [ ] Python automatically converts it to a global variable | Incorrect. Scope boundaries are strictly maintained.
        [ ] Python prints 0 | Incorrect. Python raises an exception.


    .. multichoice::

        Which keyword allows you to modify a global variable from INSIDE a function?

        [x] global | Correct! Declaring global variable_name inside a function allows modification of the global instance.
        [ ] nonlocal | Incorrect. nonlocal is used for nested functions, not top-level global variables.
        [ ] public | Incorrect. public is not a Python scope keyword.
        [ ] import | Incorrect. import loads modules into the script.


    .. multichoice::

        Given ``x = 10`` outside functions and ``x = 5`` inside a function without ``global``, what happens?

        [x] A new local variable ``x`` is created inside the function, leaving global ``x`` unchanged at 10 | Correct! Assigning creates a local variable shadowing the global one.
        [ ] Global x is updated to 5 | Incorrect. Explicit global keyword is required to modify global scope.
        [ ] Python raises a UnboundLocalError | Incorrect. Assigning creates a local binding.
        [ ] Both x variables combine to make 15 | Incorrect. Local and global scopes remain distinct.


    .. multichoice::

        Does Python enforce constant immutability (meaning Python prevents you from changing ALL_CAPS variables)?

        [x] No, ALL_CAPS is just a visual convention for programmers; Python will still allow re-assignment | Correct! Python relies on convention rather than strict enforcement.
        [ ] Yes, Python raises a TypeError if you reassign an uppercase variable | Incorrect. Python permits reassignment of uppercase names.
        [ ] Yes, UPPERCASE names are read-only | Incorrect. Uppercase names remain reassignable variables.
        [ ] Only if declared inside a class | Incorrect. Python does not enforce const immutability anywhere natively.


    .. multichoice::

        Where are global variables stored and accessible?

        [x] Throughout the entire script file, including inside functions for reading | Correct! Global variables have module-level scope.
        [ ] Only inside function definitions | Incorrect. Local variables belong to function blocks.
        [ ] Only within conditional if statements | Incorrect. Global variables span the entire file.
        [ ] In external text files | Incorrect. Variables reside in memory during script execution.


    .. multichoice::

        What will the following code output? ``val = 5; def test(): val = 2; test(); print(val)``

        [x] 5 | Correct! The function created a local variable val = 2, leaving the global val equal to 5.
        [ ] 2 | Incorrect. Global val was untouched without global keyword.
        [ ] 7 | Incorrect. Scope variables do not add together automatically.
        [ ] NameError | Incorrect. val exists cleanly in global scope.


