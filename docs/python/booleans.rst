==================================
Python Booleans
==================================

| In Python, a **Boolean** is a data type that can hold one of only two possible values: **``True``** or **``False``**.
| Booleans are essential for controlling program flow, making decisions in code, and evaluating logical conditions.
| In Python, Boolean keywords are case-sensitive and must always begin with a capital letter.

.. code-block:: python

    # Defining Boolean variables
    is_logged_in = True
    has_permission = False

    print("Logged In:", is_logged_in)
    print("Has Permission:", has_permission)

    # Checking data type
    print(type(is_logged_in))  # Output: <class 'bool'>

----

Boolean Values and Comparison Operators
=======================================

Boolean values are most frequently produced when comparing values using comparison operators:

- **Comparison Operators**: ``==`` (equal to), ``!=`` (not equal to), ``>`` (greater than), ``<`` (less than), ``>=`` (greater than or equal to), and ``<=`` (less than or equal to).
- **Conditionals**: Expressions using comparison operators evaluate directly to either ``True`` or ``False``.
- **Case Sensitivity**: Python requires capitalized ``True`` and ``False``; using lowercase ``true`` or ``false`` results in a ``NameError``.
- **The bool() Function**: Evaluates any value to determine its Boolean equivalent (truthiness or falsiness).

.. code-block:: python

    x = 10
    y = 5

    # Comparison evaluations
    print(x > y)   # Output: True
    print(x == y)  # Output: False
    print(x != y)  # Output: True

    # Using bool() conversion
    print(bool(10))   # Output: True
    print(bool(0))    # Output: False
    print(bool(""))   # Output: False (empty string)

Quiz: Boolean Values and Comparison Operators
---------------------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. The two possible Boolean values in Python are @@True@@ and `False`.
    2. Python Boolean values are @@case-sensitive@@ and must start with a capital letter.
    3. The comparison operator used to check if two values are @@equal@@ is ==.
    4. The comparison operator used to check if two values are @@not equal@@ is !=.
    5. The built-in function used to convert a value to a Boolean is @@bool()@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Compare two variables and store the Boolean result.

.. ordering::

    age = 15
    is_teenager = age >= 13
    print(is_teenager)

----

**Example 2:** Evaluate a string comparison to produce a Boolean.

.. ordering::

    user_input = "python"
    is_correct = user_input == "python"
    print(is_correct)

----

**Example 3:** Check truthiness of a number using the bool() function.

.. ordering::

    score = 0
    has_score = bool(score)
    print(has_score)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Which of the following is a valid Boolean literal in Python?

        [x] True | Correct! True starts with a capital letter and is a reserved Boolean keyword.
        [ ] true | Incorrect. Python is case-sensitive; lowercase true causes a NameError.
        [ ] "True" | Incorrect. Quotes make this a string, not a Boolean.
        [ ] TRUE | Incorrect. All-caps TRUE is not a valid Python Boolean keyword.


    .. multichoice::

        What output does ``10 < 5`` evaluate to in Python?

        [x] False | Correct! 10 is not less than 5, so the expression yields False.
        [ ] True | Incorrect. 10 is greater than 5.
        [ ] None | Incorrect. Comparison operators always return a Boolean (True or False).
        [ ] Error | Incorrect. Valid numeric comparison.


    .. multichoice::

        Which comparison operator checks if two values are NOT equal?

        [x] != | Correct! != is the not-equal comparison operator.
        [ ] == | Incorrect. == checks if two values are equal.
        [ ] =! | Incorrect. Syntactically invalid operator.
        [ ] <> | Incorrect. <> is deprecated in Python 3.


    .. multichoice::

        What is displayed by executing ``print(type(True))``?

        [x] <class 'bool'> | Correct! The Boolean data type in Python is bool.
        [ ] <class 'Boolean'> | Incorrect. Python uses the shortened name bool.
        [ ] <class 'str'> | Incorrect. True is a Boolean, not a string.
        [ ] <class 'int'> | Incorrect. True belongs to the bool class.


    .. multichoice::

        What does ``bool("Hello")`` evaluate to?

        [x] True | Correct! Any non-empty string evaluates to True.
        [ ] False | Incorrect. Only empty strings evaluate to False.
        [ ] None | Incorrect. bool() always returns True or False.
        [ ] Error | Incorrect. Valid function call.


    .. multichoice::

        Which of the following evaluates to ``False`` when passed into ``bool()``?

        [x] 0 | Correct! The integer 0 is considered falsey.
        [ ] 1 | Incorrect. Non-zero numbers evaluate to True.
        [ ] -5 | Incorrect. Non-zero numbers evaluate to True.
        [ ] "False" | Incorrect. Non-empty strings evaluate to True regardless of text content.


    .. multichoice::

        What is the difference between ``=`` and ``==`` in Python?

        [x] = assigns a value to a variable, while == compares two values | Correct! = is the assignment operator; == is the equality operator.
        [ ] They are identical and can be used interchangeably | Incorrect. They perform entirely different operations.
        [ ] = is used for math, while == is used for text | Incorrect. Both work with any supported data types.
        [ ] == assigns values, while = compares values | Incorrect. Opposite is true.


    .. multichoice::

        What is the result of ``5 >= 5``?

        [x] True | Correct! 5 is equal to 5, satisfying greater than or equal to.
        [ ] False | Incorrect. >= includes equality.
        [ ] None | Incorrect. Returns a Boolean value.
        [ ] Error | Incorrect. Valid operator usage.


    .. multichoice::

        What happens if you write ``is_valid = false`` in Python?

        [x] Python raises a NameError because false is not capitalized | Correct! Python expects True or False with a capital letter.
        [ ] Python converts it to False automatically | Incorrect. Python does not auto-capitalize keywords.
        [ ] It sets is_valid to an empty string | Incorrect. It raises a NameError exception.
        [ ] It sets is_valid to 0 silently | Incorrect. It raises a NameError.


    .. multichoice::

        Which of the following string values evaluates to ``False`` when passed into ``bool()``?

        [x] "" | Correct! An empty string contains zero characters and evaluates to False.
        [ ] " " | Incorrect. A string containing a space character is non-empty and evaluates to True.
        [ ] "0" | Incorrect. A string containing "0" is non-empty and evaluates to True.
        [ ] "false" | Incorrect. Any non-empty string evaluates to True.

----

Logical Operators and Truthiness (and, or, not)
===============================================

Logical operators combine or modify Boolean values to evaluate complex logic:

- **The and Operator**: Returns ``True`` only if **both** conditions on either side are ``True``.
- **The or Operator**: Returns ``True`` if **at least one** of the conditions is ``True``.
- **The not Operator**: Inverts the Boolean value (turns ``True`` to ``False``, and ``False`` to ``True``).
- **Truthiness and Falsiness**: In Python, values like ``0``, ``None``, ``""`` (empty string), ``[]`` (empty list), and ``{}`` (empty dictionary) are considered **falsy**. Almost all other values are **truthy**.

.. code-block:: python

    has_ticket = True
    has_id = False

    # Logical AND
    can_enter = has_ticket and has_id
    print("Can enter:", can_enter)  # Output: False

    # Logical OR
    can_get_discount = has_ticket or has_id
    print("Discount:", can_get_discount)  # Output: True

    # Logical NOT
    print("Needs ID:", not has_id)  # Output: True

Quiz: Logical Operators and Truthiness
--------------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. The @@and@@ operator returns `True` only if both surrounding conditions are true.
    2. The @@or@@ operator returns `True` if at least one condition is true.
    3. The @@not@@ operator reverses or inverts a Boolean value.
    4. In Python, the integer value @@0@@ is evaluated as falsy.
    5. An empty string `""` evaluates to @@False@@ in a Boolean context.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Combine two conditions using the and operator.

.. ordering::

    age = 16
    has_permit = True
    can_drive = age >= 16 and has_permit

----

**Example 2:** Use the not operator to flip a Boolean state.

.. ordering::

    is_active = False
    is_paused = not is_active
    print(is_paused)

----

**Example 3:** Check multiple conditions using an or statement.

.. ordering::

    is_weekend = True
    is_holiday = False
    can_relax = is_weekend or is_holiday

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What does ``True and False`` evaluate to?

        [x] False | Correct! Both operands must be True for an 'and' operation to evaluate to True.
        [ ] True | Incorrect. Both sides must be True.
        [ ] None | Incorrect. Returns a Boolean value.
        [ ] Error | Incorrect. Valid logical expression.


    .. multichoice::

        What does ``True or False`` evaluate to?

        [x] True | Correct! Only one condition needs to be True for 'or' to evaluate to True.
        [ ] False | Incorrect. Since one side is True, 'or' returns True.
        [ ] None | Incorrect. Returns a Boolean value.
        [ ] Error | Incorrect. Valid logical expression.


    .. multichoice::

        What output is produced by ``not (5 > 2)``?

        [x] False | Correct! 5 > 2 is True, and 'not True' inverts to False.
        [ ] True | Incorrect. 5 > 2 is True, but 'not' flips it to False.
        [ ] 5 | Incorrect. Logical 'not' returns a Boolean value.
        [ ] Error | Incorrect. Valid logical expression.


    .. multichoice::

        Which of the following values is considered **falsy** in Python?

        [x] [] (an empty list) | Correct! Empty containers like [] evaluate to False.
        [ ] [0] | Incorrect. A list containing 0 is non-empty, so it is truthy.
        [ ] "False" | Incorrect. Non-empty strings are truthy.
        [ ] -1 | Incorrect. Non-zero numbers are truthy.


    .. multichoice::

        Given ``a = True`` and ``b = False``, what is the value of ``not a or b``?

        [x] False | Correct! 'not True' becomes False; 'False or False' evaluates to False.
        [ ] True | Incorrect. 'not a' becomes False, and 'False or False' is False.
        [ ] None | Incorrect. Returns a Boolean value.
        [ ] Error | Incorrect. Valid expression.


    .. multichoice::

        Which logical operator returns ``True`` if **either** operand is ``True``?

        [x] or | Correct! 'or' requires only one condition to be True.
        [ ] and | Incorrect. 'and' requires both conditions to be True.
        [ ] not | Incorrect. 'not' takes a single operand and flips its value.
        [ ] equal | Incorrect. 'equal' is a comparison operator, not a logical operator.


    .. multichoice::

        What does ``not Not True`` evaluate to?

        [x] True | Correct! Double negation ('not not') cancels out and returns True.
        [ ] False | Incorrect. First 'not True' becomes False, second 'not False' becomes True.
        [ ] None | Incorrect. Returns a Boolean value.
        [ ] SyntaxError | Incorrect. Note that keywords are case-sensitive, but 'not not True' is valid logic.


    .. multichoice::

        What is short-circuit evaluation in Python logical operators?

        [x] Python stops evaluating an expression as soon as the outcome is guaranteed | Correct! e.g., in 'False and ...', the second part is skipped because result is already False.
        [ ] Python speeds up code by turning Booleans into integers | Incorrect. Short-circuiting relates to skipping unnecessary condition checks.
        [ ] Python raises an error when mixing and/or operators | Incorrect. Short-circuiting is a standard feature.
        [ ] Python automatically converts all strings to Booleans | Incorrect. Unrelated to short-circuiting.


    .. multichoice::

        What does ``bool(None)`` return?

        [x] False | Correct! None represents the absence of a value and is falsy in Python.
        [ ] True | Incorrect. None evaluates to False.
        [ ] None | Incorrect. bool() always returns True or False.
        [ ] Error | Incorrect. Valid function call.


    .. multichoice::

        What is the result of ``(10 > 5) and (3 == 3)``?

        [x] True | Correct! Both (10 > 5) and (3 == 3) are True, so 'True and True' gives True.
        [ ] False | Incorrect. Both conditions evaluate to True.
        [ ] None | Incorrect. Returns a Boolean value.
        [ ] 10 | Incorrect. Comparison and logical operators evaluate to a Boolean.


