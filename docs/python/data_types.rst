===========================
Python Data Types
===========================

| In Python, every value has a **data type** that tells the computer what kind of data it is and what operations can be performed on it.
| Python automatically detects the data type when you assign a value to a variable (known as **dynamic typing**).
| Understanding fundamental data types—such as **integers**, **floats**, **strings**, **Booleans**, **lists**, and **dictionaries**—is essential for building Python programs.

.. code-block:: python

    age = 14          # Integer (int)
    height = 165.5    # Floating-point number (float)
    name = "Alex"     # String (str)
    is_student = True # Boolean (bool)

    # Check the data type of a variable using type()
    print(type(age))  # Output: <class 'int'>

----

Basic Data Types (int, float, str, bool)
========================================

Python's primary built-in primitive data types represent simple values:

- **Integers (int)**: Whole numbers without decimals (e.g., ``10``, ``-5``, ``0``). Used for counting discrete items.
- **Floats (float)**: Numbers with a decimal point (e.g., ``3.14``, ``-0.5``, ``10.0``). Used for precise measurements.
- **Strings (str)**: Sequences of text characters enclosed in quotes (e.g., ``"Hello"``, ``'Python'``).
- **Booleans (bool)**: Conditional truth values that can only be either ``True`` or ``False``.
- **The type() Function**: Call ``type(variable)`` to inspect the data type of any value.

.. code-block:: python

    score = 100         # int
    price = 19.99       # float
    greeting = "Hi!"    # str
    game_over = False   # bool

    print(type(price))     # Output: <class 'float'>
    print(type(game_over)) # Output: <class 'bool'>

Quiz: Basic Data Types
----------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Whole numbers without decimal points belong to the @@int@@ data type.
    2. Numbers containing a decimal point belong to the @@float@@ data type.
    3. Text enclosed in quotation marks belongs to the @@str@@ data type.
    4. A Boolean variable can only hold the value `True` or @@False@@.
    5. You can inspect the data type of a value in Python using the @@type()@@ function.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Assign different basic data types to variables and print their types.

.. ordering::

    player_name = "Sam"
    player_score = 250
    print(type(player_name))
    print(type(player_score))

----

**Example 2:** Declare a float variable for price and print a summary.

.. ordering::

    item_name = "Book"
    price = 12.50
    print(f"The {item_name} costs ${price}")

----

**Example 3:** Check a Boolean flag in a program workflow.

.. ordering::

    is_logged_in = True
    print(type(is_logged_in))
    print(is_logged_in)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Which data type is assigned to the value ``42``?

        [x] int | Correct! Whole numbers without decimal points are integers (int).
        [ ] float | Incorrect. Floats contain decimal points.
        [ ] str | Incorrect. Strings are enclosed in quotation marks.
        [ ] bool | Incorrect. Booleans are True or False.


    .. multichoice::

        What data type does ``"123"`` belong to in Python?

        [x] str | Correct! Any value enclosed in quotation marks is treated as a string (str).
        [ ] int | Incorrect. Quotes convert numeric characters into a text string.
        [ ] float | Incorrect. Quotes make it a string, not a float.
        [ ] bool | Incorrect. It is surrounded by quotes, making it a string.


    .. multichoice::

        What does ``type(3.14)`` return in Python?

        [x] <class 'float'> | Correct! 3.14 contains a decimal point, classifying it as a float.
        [ ] <class 'int'> | Incorrect. 3.14 has a decimal point, so it is not an integer.
        [ ] <class 'str'> | Incorrect. Unquoted numbers are numeric types, not strings.
        [ ] <class 'bool'> | Incorrect. 3.14 is a floating-point number.


    .. multichoice::

        Which of the following values belongs to the ``bool`` data type?

        [x] True | Correct! True and False (capitalized without quotes) are Booleans.
        [ ] "True" | Incorrect. Quoted text forms a string literal (str).
        [ ] 1.0 | Incorrect. 1.0 is a float.
        [ ] "False" | Incorrect. Quoted text is a string.


    .. multichoice::

        How does Python determine the data type of a variable during assignment?

        [x] Automatically based on the assigned value (dynamic typing) | Correct! Python infers types automatically without explicit declaration.
        [ ] Developers must declare the type manually before setting values | Incorrect. Python uses dynamic typing.
        [ ] Python randomly picks a type | Incorrect. Python evaluates value representations deterministically.
        [ ] All variables in Python are stored as text strings | Incorrect. Python supports multiple distinct data types.


    .. multichoice::

        What is the data type of ``0`` in Python?

        [x] int | Correct! Zero without a decimal point is an integer.
        [ ] float | Incorrect. 0.0 would be a float, but 0 is an integer.
        [ ] bool | Incorrect. While 0 evaluates as falsy, its type is int.
        [ ] str | Incorrect. Unquoted 0 is an integer.


    .. multichoice::

        Which function returns the data type of an object in Python?

        [x] type() | Correct! The built-in type() function reports object classifications.
        [ ] typeof() | Incorrect. typeof is JavaScript syntax, not Python.
        [ ] check_type() | Incorrect. No check_type() built-in exists in Python.
        [ ] get_type() | Incorrect. Python uses type().


    .. multichoice::

        What is the data type of the result of ``10 / 2`` in Python 3?

        [x] float | Correct! Division / always returns a float in Python 3 (5.0).
        [ ] int | Incorrect. Standard division yields float output even for exact divisions.
        [ ] str | Incorrect. Arithmetic operations output numeric types.
        [ ] bool | Incorrect. Math division returns numbers.


    .. multichoice::

        Which of the following is a valid floating-point number?

        [x] -0.75 | Correct! Negative numbers with decimal points are valid floats.
        [ ] "5.5" | Incorrect. Surrounded by quotes, making it a string.
        [ ] 12 | Incorrect. Whole numbers without decimals are ints.
        [ ] True | Incorrect. True is a Boolean.


    .. multichoice::

        What happens when you enclose a Boolean value in quotation marks like ``"False"``?

        [x] It becomes a string (str) | Correct! Placing quotes around any value transforms it into a string.
        [ ] It remains a Boolean (bool) | Incorrect. Quotation marks define string literals.
        [ ] Python raises a SyntaxError | Incorrect. "False" is a valid string literal.
        [ ] It converts to an integer (int) | Incorrect. String quotes prevent numeric conversion.

----

Collection Data Types (list, tuple, dict, set)
==============================================

When storing multiple pieces of data together, Python provides collection data types:

- **Lists (list)**: Ordered, mutable (changeable) sequences enclosed in square brackets ``[]`` (e.g., ``[1, 2, 3]``).
- **Tuples (tuple)**: Ordered, immutable (unchangeable) sequences enclosed in parentheses ``()`` (e.g., ``(10, 20)``).
- **Dictionaries (dict)**: Unordered mappings of key-value pairs enclosed in curly braces ``{}`` (e.g., ``{"name": "Alex"}``).
- **Sets (set)**: Unordered collections of unique values enclosed in curly braces ``{}`` (e.g., ``{1, 2, 3}``).

.. code-block:: python

    fruits = ["apple", "banana", "cherry"]  # list
    coordinates = (10.0, 20.0)             # tuple
    user = {"name": "Taylor", "age": 14}   # dict
    unique_ids = {101, 102, 103}            # set

    print(type(fruits))  # Output: <class 'list'>
    print(type(user))    # Output: <class 'dict'>

Quiz: Collection Data Types
---------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Lists are defined using @@square@@ brackets `[]`.
    2. Tuples are defined using @@parentheses@@ `()`.
    3. Dictionaries store data as @@key-value@@ pairs inside curly braces `{}`.
    4. Sets contain only @@unique@@ values and ignore duplicates.
    5. Unlike lists, tuples are @@immutable@@ and cannot be modified after creation.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Create and inspect a list of student names.

.. ordering::

    students = ["Alex", "Jordan", "Taylor"]
    print(type(students))
    print(students[0])

----

**Example 2:** Construct a dictionary and look up a value by key.

.. ordering::

    profile = {"username": "gamer1", "score": 900}
    print(type(profile))
    print(profile["username"])

----

**Example 3:** Define a tuple representing GPS coordinates.

.. ordering::

    lat_long = (-37.81, 144.96)
    print(type(lat_long))
    print(lat_long[0])

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Which pair of brackets is used to create a Python ``list``?

        [x] Square brackets [] | Correct! Lists use square brackets [].
        [ ] Parentheses () | Incorrect. Parentheses create tuples.
        [ ] Curly braces {} | Incorrect. Curly braces create dictionaries or sets.
        [ ] Angle brackets <> | Incorrect. Angle brackets are comparison operators.


    .. multichoice::

        What key characteristic distinguishes a ``tuple`` from a ``list``?

        [x] Tuples are immutable (cannot be changed after creation), while lists are mutable | Correct! Tuples cannot be modified after instantiation.
        [ ] Lists can only store numbers, while tuples store text | Incorrect. Both can hold any data type.
        [ ] Tuples use square brackets [] | Incorrect. Tuples use parentheses ().
        [ ] Lists cannot contain duplicate elements | Incorrect. Lists permit duplicate elements.


    .. multichoice::

        What data type is represented by ``{"a": 1, "b": 2}``?

        [x] dict | Correct! Key-value pairs inside curly braces form a dictionary (dict).
        [ ] set | Incorrect. Sets contain individual elements without key values.
        [ ] list | Incorrect. Lists use square brackets and single values.
        [ ] tuple | Incorrect. Tuples use parentheses and sequence items.


    .. multichoice::

        What happens when you add a duplicate item to a Python ``set`` (e.g., ``{1, 2, 2, 3}``)?

        [x] The duplicate is automatically removed | Correct! Sets only preserve unique elements.
        [ ] Python throws a ValueError | Incorrect. Adding duplicates is handled silently by ignoring them.
        [ ] The program crashes | Incorrect. Duplicate elements are ignored without errors.
        [ ] The set converts into a list | Incorrect. Object type remains a set.


    .. multichoice::

        Which of the following is a valid tuple definition?

        [x] colors = ("red", "green", "blue") | Correct! Uses parentheses enclosing comma-separated values.
        [ ] colors = ["red", "green", "blue"] | Incorrect. Square brackets define a list.
        [ ] colors = {"red", "green", "blue"} | Incorrect. Curly braces without key-value colons define a set.
        [ ] colors = "red", "green", "blue" | Incorrect. Explicit parentheses are preferred for standard tuple definition.


    .. multichoice::

        Given ``nums = [1, 2, 3]``, what does ``type(nums)`` print?

        [x] <class 'list'> | Correct! nums is a list defined with square brackets.
        [ ] <class 'tuple'> | Incorrect. Defined with [], not ().
        [ ] <class 'set'> | Incorrect. Defined with [], not {}.
        [ ] <class 'dict'> | Incorrect. Defined with [], not key-value {}.


    .. multichoice::

        Which collection type stores key-value pairs?

        [x] Dictionary (dict) | Correct! Dictionaries map key identifiers to stored values.
        [ ] List (list) | Incorrect. Lists store ordered sequence values by numerical index.
        [ ] Tuple (tuple) | Incorrect. Tuples store ordered sequence values.
        [ ] Set (set) | Incorrect. Sets store unique individual elements.


    .. multichoice::

        Which collection type is created using ``my_data = {10, 20, 30}``?

        [x] set | Correct! Curly braces containing single values create a set.
        [ ] dict | Incorrect. Dictionaries require key-value pairs separated by colons (e.g., {"k": "v"}).
        [ ] list | Incorrect. Lists use square brackets [].
        [ ] tuple | Incorrect. Tuples use parentheses ().


    .. multichoice::

        Can a single Python list contain items of different data types (e.g., integers, strings, and Booleans)?

        [x] Yes, Python lists can store mixed data types simultaneously | Correct! Python collections accept heterogeneous data types.
        [ ] No, lists must strictly contain items of a single data type | Incorrect. Python lists are heterogeneous containers.
        [ ] Yes, but only if numbers are converted to floats first | Incorrect. Any data type can be mixed directly.
        [ ] No, mixing types raises a TypeError | Incorrect. Mixed types inside lists are fully supported.


    .. multichoice::

        Given ``person = {"name": "Eva"}``, how do you access the value ``"Eva"``?

        [x] person["name"] | Correct! Dictionary values are accessed using key names inside square brackets.
        [ ] person[0] | Incorrect. Dictionaries are indexed by keys, not positional indices.
        [ ] person.Eva | Incorrect. Key indexing uses bracket notation person["name"].
        [ ] person("name") | Incorrect. Accessing keys uses square brackets, not parentheses.

----

Type Conversion (Casting)
=========================

Python allows you to convert values from one data type to another using built-in conversion functions:

- **int()**: Converts compatible values (like floats or string numbers) to integers (truncates decimals).
- **float()**: Converts integers or valid numeric strings into floating-point numbers.
- **str()**: Converts any data type into its string representation.
- **bool()**: Converts values to Booleans. Non-zero numbers and non-empty strings convert to ``True``; ``0``, ``""``, and ``None`` convert to ``False``.

.. code-block:: python

    num_str = "100"
    num_int = int(num_str)    # Converts string "100" to integer 100
    print(num_int + 50)       # Output: 150

    pi_float = 3.99
    pi_int = int(pi_float)    # Truncates decimal part -> 3
    print(pi_int)             # Output: 3

    text_score = str(95)      # Converts integer 95 to string "95"
    print("Score: " + text_score) # Output: Score: 95

Quiz: Type Conversion (Casting)
-------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Converting a value from one data type to another is called @@type casting@@.
    2. The function `int(5.8)` truncates the decimal part and returns @@5@@.
    3. To convert an integer to a float, use the @@float()@@ function.
    4. Converting an empty string `""` using `bool("")` yields @@False@@.
    5. The function @@str()@@ converts any data type into string format.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Convert user string input into an integer for math calculations.

.. ordering::

    age_input = "15"
    age = int(age_input)
    next_year = age + 1
    print(f"Next year you will be {next_year}")

----

**Example 2:** Convert an integer score to a string for concatenation.

.. ordering::

    score = 85
    msg = "Your final score is " + str(score)
    print(msg)

----

**Example 3:** Convert a float price to an integer representation.

.. ordering::

    total_price = 19.95
    dollars_only = int(total_price)
    print(dollars_only)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What is the output of ``int(7.9)`` in Python?

        [x] 7 | Correct! int() truncates the decimal portion completely without rounding up.
        [ ] 8 | Incorrect. int() drops decimals without rounding up.
        [ ] 7.9 | Incorrect. int() removes the decimal component.
        [ ] ValueError | Incorrect. Floating numbers convert cleanly to int.


    .. multichoice::

        What happens when you run ``int("hello")``?

        [x] Python raises a ValueError | Correct! Non-numeric text strings cannot be parsed into integers.
        [ ] It converts to 0 | Incorrect. Python throws a ValueError rather than defaulting to 0.
        [ ] It converts to None | Incorrect. An exception is raised.
        [ ] It calculates string length | Incorrect. Use len() to check string length.


    .. multichoice::

        What does ``float(5)`` evaluate to?

        [x] 5.0 | Correct! Converting integer 5 to float appends decimal precision .0.
        [ ] 5 | Incorrect. Floats always print with a decimal point.
        [ ] "5.0" | Incorrect. Converts to numeric float, not string.
        [ ] ValueError | Incorrect. Integer to float conversion is valid.


    .. multichoice::

        What does ``bool("")`` (converting an empty string) evaluate to?

        [x] False | Correct! Empty collections and empty strings convert to Boolean False.
        [ ] True | Incorrect. Only non-empty strings evaluate as True.
        [ ] None | Incorrect. bool() strictly returns True or False.
        [ ] ValueError | Incorrect. Empty string conversion is valid.


    .. multichoice::

        Which statement about ``str(100)`` is TRUE?

        [x] It returns the string "100" | Correct! str() wraps numeric values into string representation.
        [ ] It calculates 100 * 100 | Incorrect. Performing string conversion does not execute math.
        [ ] It raises a TypeError | Incorrect. Standard type casting operation.
        [ ] It returns integer 100 | Incorrect. Result data type is str.


    .. multichoice::

        What is output by ``bool(42)``?

        [x] True | Correct! Any non-zero number converts to Boolean True.
        [ ] False | Incorrect. Only 0 converts to False among numbers.
        [ ] 42 | Incorrect. bool() converts output to Boolean type.
        [ ] ValueError | Incorrect. Non-zero integers convert cleanly.


    .. multichoice::

        Given ``x = "10"`` and ``y = "20"``, what does ``x + y`` produce?

        [x] "1020" | Correct! Adding two strings concatenates them together rather than performing math.
        [ ] 30 | Incorrect. Values are strings, so concatenation occurs instead of addition.
        [ ] "30" | Incorrect. String addition concatenates characters.
        [ ] TypeError | Incorrect. String concatenation is valid syntax.


    .. multichoice::

        How can you perform mathematical addition on ``x = "10"`` and ``y = "20"``?

        [x] int(x) + int(y) | Correct! Cast both strings to integers prior to adding them.
        [ ] str(x + y) | Incorrect. Concatenates strings "1020" first.
        [ ] float(x + y) | Incorrect. Concatenates first then casts to float 1020.0.
        [ ] x.add(y) | Incorrect. Strings do not possess an .add() method.


    .. multichoice::

        What is the result of ``str(True)``?

        [x] "True" | Correct! Converts Boolean value True into string literal "True".
        [ ] True | Incorrect. Type transforms to string str.
        [ ] 1 | Incorrect. Int casting int(True) gives 1, but str(True) gives "True".
        [ ] TypeError | Incorrect. Valid type conversion.


    .. multichoice::

        What is output by ``int(True)`` and ``int(False)`` in Python?

        [x] 1 and 0 | Correct! In Python, Booleans inherit from integers where True converts to 1 and False to 0.
        [ ] True and False | Incorrect. int() casts values to integer representation.
        [ ] 0 and 1 | Incorrect. True maps to 1, False maps to 0.
        [ ] ValueError | Incorrect. Boolean to integer conversion is supported natively.


