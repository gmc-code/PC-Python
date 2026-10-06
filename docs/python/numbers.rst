==================================
Python Numbers
==================================

| In Python, numbers are used to store numerical data and perform mathematical operations.
| The three primary built-in numeric types in Python are **integers** (whole numbers), **floats** (decimal numbers), and **complex numbers**.
| Understanding how Python handles numbers is essential for calculations, tracking scores, processing measurements, and scientific computing.

.. code-block:: python

    # Defining number variables
    age = 14          # Integer
    price = 19.99     # Float
    z = 3 + 4j        # Complex number

    print("Age:", age, type(age))
    print("Price:", price, type(price))
    print("Complex:", z, type(z))

----

Numeric Types and Arithmetic Operators (+, -, *, /, //, %, **)
=============================================================

Python supports various numeric data types and arithmetic operators for mathematical calculations:

-
**Integers (int)**: Positive or negative whole numbers without decimals (e.g., ``42``, ``-7``).
-
**Floats (float)**: Real numbers containing decimal points or scientific notation (e.g., ``3.14``, ``-0.001``).
-
**Standard Operators**: Basic arithmetic includes addition (``+``), subtraction (``-``), multiplication (``*``), and division (``/``). Standard division always returns a float.
-
**Specialized Operators**: Floor division (``//``) rounds down to the nearest integer, modulus (``%``) returns the division remainder, and exponentiation (``**``) raises a power.

.. code-block:: python

    # Basic arithmetic
    print(10 + 5)   # Addition -> 15
    print(10 - 5)   # Subtraction -> 5
    print(10 * 5)   # Multiplication -> 50
    print(10 / 4)   # Division -> 2.5 (Float)

    # Floor Division, Modulus, and Exponents
    print(10 // 4)  # Floor Division -> 2
    print(10 % 4)   # Modulus (Remainder) -> 2
    print(2 ** 3)   # Exponent (2 to power 3) -> 8

Quiz: Numeric Types and Arithmetic Operators
--------------------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Whole numbers without decimals belong to the @@int@@ data type in Python.
    2. Numbers containing a decimal point belong to the @@float@@ data type.
    3. Standard division using `/` always returns a @@float@@ result in Python 3.
    4. To calculate the remainder of a division, use the @@%@@ operator.
    5. To calculate powers in Python (e.g., 2 to the power of 3), use the @@**@@ operator.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Calculate floor division and remainder for 17 divided by 5.

.. ordering::

    num = 17
    quotient = num // 5
    remainder = num % 5
    print(quotient, remainder)

----

**Example 2:** Calculate total cost by multiplying item count by price.

.. ordering::

    quantity = 4
    unit_price = 2.50
    total = quantity * unit_price
    print(total)

----

**Example 3:** Raise a base number to an exponent power.

.. ordering::

    base = 3
    exponent = 4
    result = base ** exponent
    print(result)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Which data type represents whole numbers without decimal points in Python?

        [x] int | Correct! Integer (int) represents positive or negative whole numbers.
        [ ] float | Incorrect. Float represents decimal numbers.
        [ ] double | Incorrect. Python uses float for decimal numbers.
        [ ] num | Incorrect. Correct type name is int.


    .. multichoice::

        What output is produced by ``7 / 2`` in Python 3?

        [x] 3.5 | Correct! Standard division using / always yields a float result.
        [ ] 3 | Incorrect. Use floor division // to get 3.
        [ ] 3.0 | Incorrect. 7 divided by 2 gives exact float value 3.5.
        [ ] 4 | Incorrect. / returns exact division 3.5.


    .. multichoice::

        What does the modulus operator (``%``) calculate?

        [x] The remainder after division | Correct! Modulus returns leftover remainder from integer division.
        [ ] The percentage of two numbers | Incorrect. % returns division remainder.
        [ ] The result rounded down | Incorrect. Floor division // rounds down.
        [ ] Power exponentiation | Incorrect. ** performs exponentiation.


    .. multichoice::

        What is the result of ``15 // 4``?

        [x] 3 | Correct! Floor division discards fractional remainder, returning 3.
        [ ] 3.75 | Incorrect. Standard division / returns 3.75; // returns 3.
        [ ] 4 | Incorrect. Discards fractional part and rounds down to 3.
        [ ] 3.0 | Incorrect. Integer floor division returns integer 3.


    .. multichoice::

        Which expression calculates $5^3$ (5 raised to the power of 3) in Python?

        [x] 5 ** 3 | Correct! ** is the exponentiation operator in Python.
        [ ] 5 ^ 3 | Incorrect. ^ is a bitwise XOR operator in Python.
        [ ] 5 * 3 | Incorrect. * performs multiplication.
        [ ] power(5, 3) | Incorrect. Correct exponent operator is ** or pow(5, 3).


    .. multichoice::

        What type of value does ``type(4.0)`` return?

        [x] <class 'float'> | Correct! Presence of decimal point classifies 4.0 as a float.
        [ ] <class 'int'> | Incorrect. 4.0 contains a decimal point and is a float.
        [ ] <class 'double'> | Incorrect. Python decimal numbers belong to float class.
        [ ] <class 'number'> | Incorrect. Returns class 'float'.


    .. multichoice::

        What output is displayed by ``print(10 % 3)``?

        [x] 1 | Correct! 10 divided by 3 is 3 with a remainder of 1.
        [ ] 3 | Incorrect. 3 is the quotient, 1 is the remainder.
        [ ] 0 | Incorrect. 10 is not evenly divisible by 3.
        [ ] 3.33 | Incorrect. Modulus returns integer remainder 1.


    .. multichoice::

        What happens when an integer and a float are combined in an operation (e.g., ``5 + 2.0``)?

        [x] Python automatically converts the integer to a float and returns a float | Correct! Mixed numeric operations evaluate to float.
        [ ] Python raises a TypeError | Incorrect. Implicit type conversion automatically takes place.
        [ ] Returns an integer by dropping decimals | Incorrect. Evaluates to float 7.0.
        [ ] Program crashes | Incorrect. Valid arithmetic expression.


    .. multichoice::

        What is the result of ``2 + 3 * 4`` according to operator precedence?

        [x] 14 | Correct! Multiplication takes precedence over addition (3 * 4 = 12; 2 + 12 = 14).
        [ ] 20 | Incorrect. Precedence executes multiplication before addition.
        [ ] 24 | Incorrect. Follows standard operator precedence rules.
        [ ] 10 | Incorrect. Evaluates to 14.


    .. multichoice::

        Which built-in function returns the absolute value of a number (distance from zero)?

        [x] abs() | Correct! abs(-5) returns positive distance 5.
        [ ] absolute() | Incorrect. Built-in function name is abs().
        [ ] pos() | Incorrect. Function name is abs().
        [ ] convert() | Incorrect. Function name is abs().

----

Type Conversion and Rounding (int, float, round, math)
======================================================

Converting between numeric types and formatting numeric output is essential when working with calculations:

-
**Converting to Integer (int)**: ``int()`` converts numeric strings or floats to integers by truncating decimal places towards zero.
-
**Converting to Float (float)**: ``float()`` converts integers or valid numeric strings into floating-point numbers.
-
**Rounding Numbers (round)**: ``round(number, ndigits)`` rounds a number to a specified number of decimal places.
-
**The math Module**: Importing ``math`` provides access to functions like ``math.ceil()`` (round up), ``math.floor()`` (round down), and ``math.sqrt()`` (square root).

.. code-block:: python

    import math

    # Type Conversion
    val_str = "45"
    num_int = int(val_str)      # 45
    num_float = float(num_int)  # 45.0
    print(num_int, num_float)

    # Rounding
    pi_val = 3.14159
    print(round(pi_val, 2))     # Output: 3.14

    # Math Module Functions
    print(math.sqrt(16))        # Square root -> 4.0
    print(math.ceil(4.1))       # Round up -> 5
    print(math.floor(4.9))      # Round down -> 4

Quiz: Type Conversion and Rounding
----------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. To convert a numeric string like `"12"` into an integer, use the @@int()@@ function.
    2. To round a floating-point number to two decimal places, use `round(val, @@2@@)`.
    3. The function used to calculate square roots in Python's math module is `math.@@sqrt()@@`.
    4. To round a decimal number UP to the nearest whole integer, use `math.@@ceil()@@`.
    5. To convert an integer like `5` into `5.0`, pass it into the @@float()@@ function.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Convert user input string into an integer and double it.

.. ordering::

    user_input = "25"
    number = int(user_input)
    result = number * 2
    print(result)

----

**Example 2:** Calculate and round square root of a number to 2 decimal places.

.. ordering::

    import math
    val = 20
    root = math.sqrt(val)
    rounded_root = round(root, 2)

----

**Example 3:** Use math.floor to round a decimal value down.

.. ordering::

    import math
    price = 12.89
    discounted_whole = math.floor(price)
    print(discounted_whole)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What does ``int(9.99)`` evaluate to in Python?

        [x] 9 | Correct! int() truncates decimal digits without rounding.
        [ ] 10 | Incorrect. int() truncates decimals rather than rounding up.
        [ ] 9.0 | Incorrect. int() returns an integer, not a float.
        [ ] Error | Incorrect. Valid conversion syntax.


    .. multichoice::

        What is displayed by ``print(round(3.567, 1))``?

        [x] 3.6 | Correct! Rounds 3.567 to 1 decimal place.
        [ ] 3.5 | Incorrect. 6 rounds second digit up to 3.6.
        [ ] 3.57 | Incorrect. 1 specifies 1 decimal place limit.
        [ ] 4.0 | Incorrect. Specifying 1 decimal place yields 3.6.


    .. multichoice::

        Which function from the ``math`` module always rounds a decimal number UP to the next integer?

        [x] math.ceil() | Correct! ceil() (ceiling) rounds numbers up to nearest whole integer.
        [ ] math.floor() | Incorrect. floor() rounds numbers down.
        [ ] math.up() | Incorrect. Method name is math.ceil().
        [ ] round() | Incorrect. round() follows standard nearest rounding rules.


    .. multichoice::

        What happens if you attempt ``int("12.5")`` directly?

        [x] Python raises a ValueError | Correct! int() cannot directly parse float-formatted strings; float("12.5") must be called first.
        [ ] Converts to integer 12 | Incorrect. Raises a ValueError exception.
        [ ] Converts to float 12.5 | Incorrect. int() expects integer text or floats.
        [ ] Returns 0 | Incorrect. Raises ValueError.


    .. multichoice::

        What does ``math.sqrt(25)`` return?

        [x] 5.0 | Correct! math.sqrt() returns a floating-point number 5.0.
        [ ] 5 | Incorrect. sqrt() returns float outputs.
        [ ] 25 | Incorrect. Calculates square root value.
        [ ] 625 | Incorrect. 625 is 25 squared, not square root.


    .. multichoice::

        What result is produced by ``float(7)``?

        [x] 7.0 | Correct! float() converts integer 7 into floating-point representation 7.0.
        [ ] 7 | Incorrect. Converts value to float format.
        [ ] "7.0" | Incorrect. Returns float numeric value, not string.
        [ ] 7.00 | Incorrect. Displayed as 7.0.


    .. multichoice::

        What statement imports Python's built-in mathematical library?

        [x] import math | Correct! Standard import statement for math library functions.
        [ ] include math | Incorrect. 'include' is C++ syntax.
        [ ] using math | Incorrect. 'using' is C# syntax.
        [ ] load math | Incorrect. Python uses import keyword.


    .. multichoice::

        What output is produced by ``math.floor(8.9)``?

        [x] 8 | Correct! math.floor() rounds numbers down to nearest lower integer.
        [ ] 9 | Incorrect. math.ceil() rounds up to 9.
        [ ] 8.0 | Incorrect. math.floor() returns integer 8.
        [ ] 8.9 | Incorrect. Rounds value down.


    .. multichoice::

        How does Python handle very large integers (e.g., ``10 ** 100``)?

        [x] Python handles arbitrarily large integers automatically without overflow errors | Correct! Python automatically manages memory for arbitrarily large integers.
        [ ] Causes a MemoryOverflowError | Incorrect. Python handles large integers seamlessly.
        [ ] Automatically caps values at 2,147,483,647 | Incorrect. No fixed 32-bit ceiling limit.
        [ ] Converts value to string | Incorrect. Remains integer object.


    .. multichoice::

        What does ``round(2.5)`` evaluate to in Python 3 rounding rules?

        [x] 2 | Correct! Python 3 uses 'round half to even' (banker's rounding), rounding 2.5 to nearest even integer 2.
        [ ] 3 | Incorrect. Banker's rounding rounds half values to nearest even integer (2).
        [ ] 2.5 | Incorrect. Rounds to whole integer when ndigits is omitted.
        [ ] Error | Incorrect. Valid rounding operation.

