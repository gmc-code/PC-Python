==========================
Operators
==========================

| **Arithmetic Operators**: Perform standard mathematical calculations.
| **Assignment** operators are used to assign values to variables.
| The **compound assignment** operators consist of two operators as a shorthand.
| **Comparison** operators are used to compare two values.
| **Booleans** represent one of two values: True or False.
| **Logical** operators are used to combine conditional statements.
| **Membership** operators are used to test if a sequence is presented in an object.
| **Identity** operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.

| The **None** keyword is used to define a null value, or no value at all. None is not the same as 0, False, or an empty string. None is a data type of its own and only None can be None.


.. code-block:: python

    # Arithmetic calculation
    result = 10 + 5 * 2  # Result is 20

    # Comparison check
    is_valid = result > 15  # Result is True

----

Arithmetic Operators
====================

Arithmetic operators are used to carry out mathematical calculations:

- **Addition (+)** and **Subtraction (-)**: Standard arithmetic sum and difference.
- **Multiplication (*)** and **Division (/)**: Multiplication and true division (always returns a ``float``).
- **Floor Division (//)**: Divides and rounds down to the nearest whole integer.
- **Modulus (%)**: Returns the **remainder** left over after division.
- **Exponentiation (**)**: Raises a base number to a power.

.. code-block:: python

    print(10 / 3)   # True Division -> 3.3333333333333335
    print(10 // 3)  # Floor Division -> 3
    print(10 % 3)   # Modulus (Remainder) -> 1
    print(2 ** 3)   # Exponentiation (2^3) -> 8

Quiz: Arithmetic Operators
--------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. The / operator performs @@division@@ and always returns a floating-point number.
    2. The % operator (@@modulus@@) returns the remainder of a division.
    3. The // operator performs @@floor division@@, rounding down to the nearest integer.
    4. The symbol for exponentiation (raising a number to a @@power@@) in Python is **.
    5. Python follows the @@order@@ of operations, meaning multiplication occurs before addition.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Compute the total price of 3 items costing 5 dollars each with a 2-dollar discount.

.. ordering::

    price = 5
    quantity = 3
    discount = 2
    total = price * quantity - discount
    print(total)

----

**Example 2:** Calculate both the quotient and remainder of 17 divided by 5.

.. ordering::

    quotient = 17 // 5
    remainder = 17 % 5
    print(quotient, remainder)

----

**Example 3:** Calculate the area of a square with a side length of 4 using the exponentiation operator.

.. ordering::

    side = 4
    area = side ** 2
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

        What is the result of ``15 % 4`` in Python?

        [x] 3 | Correct! 15 divided by 4 is 3 with a remainder of 3.
        [ ] 3.75 | Incorrect. % returns the remainder as an integer, not floating-point division.
        [ ] 3 | Incorrect. While 15 // 4 is 3, the remainder itself is also 3.
        [ ] 0 | Incorrect. 15 is not evenly divisible by 4.


    .. multichoice::

        Which operator always outputs a value of type ``float``?

        [x] / | Correct! Standard division / always returns a float in Python 3.
        [ ] // | Incorrect. Floor division yields an integer when given integer inputs.
        [ ] * | Incorrect. Integer multiplication yields an integer.
        [ ] + | Incorrect. Integer addition yields an integer.


    .. multichoice::

        What does ``2 ** 4`` evaluate to in Python?

        [x] 16 | Correct! 2 raised to the power of 4 ($2 \times 2 \times 2 \times 2$) is 16.
        [ ] 8 | Incorrect. 2 * 4 is 8, but ** is the exponentiation operator.
        [ ] 6 | Incorrect. Exponentiation multiplies base by itself power times.
        [ ] 64 | Incorrect. $2^4 = 16$.


    .. multichoice::

        What is the value of ``7 // 2``?

        [x] 3 | Correct! Floor division discards the fractional part, rounding 3.5 down to 3.
        [ ] 3.5 | Incorrect. True division / returns 3.5; // floors it to 3.
        [ ] 4 | Incorrect. Floor division rounds down toward negative infinity.
        [ ] 1 | Incorrect. 1 is the remainder returned by 7 % 2.


    .. multichoice::

        According to Python operator precedence, what is the result of ``2 + 3 * 4``?

        [x] 14 | Correct! Multiplication takes precedence over addition: $3 \times 4 = 12$, then $2 + 12 = 14$.
        [ ] 20 | Incorrect. Python evaluates multiplication before addition, not left-to-right blindly.
        [ ] 24 | Incorrect. Expression evaluates as $2 + (3 \times 4)$.
        [ ] 10 | Incorrect. Multiplication precedes addition.


    .. multichoice::

        What does ``10 % 2`` return?

        [x] 0 | Correct! 10 is an even number, so dividing by 2 leaves a remainder of 0.
        [ ] 5 | Incorrect. 10 / 2 is 5, but % checks the remainder.
        [ ] 1 | Incorrect. Even numbers have 0 remainder when divided by 2.
        [ ] 2 | Incorrect. Remainder cannot equal or exceed the divisor 2.


    .. multichoice::

        What is the result of ``(2 + 3) * 4``?

        [x] 20 | Correct! Parentheses override default precedence: $(2 + 3) = 5$, then $5 \times 4 = 20$.
        [ ] 14 | Incorrect. Parentheses force addition to evaluate before multiplication.
        [ ] 24 | Incorrect. $5 \times 4 = 20$.
        [ ] 9 | Incorrect. Parentheses group 2 + 3 together first.


    .. multichoice::

        What will ``19 // 5`` evaluate to?

        [x] 3 | Correct! 19 divided by 5 is 3.8, which rounds down to 3.
        [ ] 4 | Incorrect. Floor division rounds down, not up.
        [ ] 3.8 | Incorrect. // discards decimal values for integer inputs.
        [ ] 4 | Incorrect. Remainder is 4 (19 % 5), but // calculates integer quotient.


    .. multichoice::

        Which operator should you use to check if an integer is even or odd?

        [x] % | Correct! Checking if `number % 2 == 0` determines whether a number is even.
        [ ] // | Incorrect. Quotient does not directly indicate parity.
        [ ] / | Incorrect. True division returns float results.
        [ ] ** | Incorrect. Exponentiation raises numbers to powers.


    .. multichoice::

        What is the result of ``3 ** 3``?

        [x] 27 | Correct! $3^3 = 3 \times 3 \times 3 = 27$.
        [ ] 9 | Incorrect. 3 * 3 is 9, but $3^3 = 27$.
        [ ] 12 | Incorrect. Exponentiation is repeated multiplication.
        [ ] 81 | Incorrect. $3^4 = 81$, whereas $3^3 = 27$.

----

Comparison Operators
====================

Comparison operators evaluate expressions and return a Boolean value (``True`` or ``False``):

- **Equal to (==)**: Returns ``True`` if both operands are equal.
- **Not equal to (!=)**: Returns ``True`` if operands are not equal.
- **Greater than (>)** and **Less than (<)**: Standard inequality checks.
- **Greater than or equal to (>=)** and **Less than or equal to (<=)**: Inclusive boundary checks.

.. code-block:: python

    x = 10
    y = 20

    print(x == y)  # False
    print(x != y)  # True
    print(x < y)   # True
    print(x >= 10) # True

Quiz: Comparison Operators
--------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. To check if two values are @@equal@@ in Python, use the == operator.
    2. A single `=` sign is used for @@assignment@@, while `==` is used for comparison.
    3. The != operator checks whether two values are @@not equal@@.
    4. A @@comparison@@ operators always return a Boolean result (`True` or `False`).
    5. The expression `10 >= 10` evaluates to @@True@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Check if a user's age qualifies for a adult ticket (18 or older).

.. ordering::

    age = 20
    is_adult = age >= 18
    print(is_adult)

----

**Example 2:** Compare two test scores to see if they are different.

.. ordering::

    score1 = 85
    score2 = 90
    are_different = score1 != score2
    print(are_different)

----

**Example 3:** Check if a given number falls below a ceiling limit.

.. ordering::

    limit = 100
    current = 85
    is_under = current < limit
    print(is_under)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What is the difference between ``=`` and ``==`` in Python?

        [x] = assigns a value to a variable, while == compares two values for equality | Correct! Single = sets values; double == compares values.
        [ ] = compares values, while == assigns variables | Incorrect. Roles are reversed.
        [ ] They perform identical tasks | Incorrect. = is assignment; == is comparison.
        [ ] == is used only for string operations | Incorrect. == compares any compatible data types.


    .. multichoice::

        What does ``15 != 15`` evaluate to?

        [x] False | Correct! 15 is equal to 15, so "not equal to" evaluates to False.
        [ ] True | Incorrect. Expression checks if values are different.
        [ ] None | Incorrect. Comparison operators output Booleans.
        [ ] ValueError | Incorrect. Valid syntax comparison.


    .. multichoice::

        Which expression evaluates to ``True``?

        [x] 7 <= 7 | Correct! 7 is equal to 7, satisfying less than or equal to.
        [ ] 5 > 10 | Incorrect. 5 is smaller than 10.
        [ ] 8 != 8 | Incorrect. 8 equals 8, so != is False.
        [ ] 12 < 10 | Incorrect. 12 is greater than 10.


    .. multichoice::

        What is returned by ``"apple" == "Apple"`` in Python?

        [x] False | Correct! Python string comparison is case-sensitive ('a' != 'A').
        [ ] True | Incorrect. Capitalization causes string mismatch.
        [ ] SyntaxError | Incorrect. String comparison is valid.
        [ ] TypeError | Incorrect. Both operands are string types.


    .. multichoice::

        What is the result of ``100 >= 50``?

        [x] True | Correct! 100 is greater than 50.
        [ ] False | Incorrect. 100 exceeds 50.
        [ ] 100 | Incorrect. Relational comparisons output Booleans.
        [ ] 50 | Incorrect. Relational operations do not return numeric operands.


    .. multichoice::

        What is the evaluation of ``5 < 5``?

        [x] False | Correct! 5 is equal to 5, not strictly less than 5.
        [ ] True | Incorrect. Strict less-than requires a smaller value.
        [ ] None | Incorrect. Comparison yields Boolean False.
        [ ] SyntaxError | Incorrect. Valid comparison syntax.


    .. multichoice::

        Which operator checks if a value is less than or equal to another?

        [x] <= | Correct! Less than or equal operator is written as <=.
        [ ] =< | Incorrect. Operator syntax requires < followed by =.
        [ ] <== | Incorrect. Comparison operators consist of maximum two characters.
        [ ] != | Incorrect. != checks for inequality.


    .. multichoice::

        What will ``3.0 == 3`` return in Python?

        [x] True | Correct! Python converts numeric types during comparison; float 3.0 equals integer 3.
        [ ] False | Incorrect. Numeric comparison checks equal mathematical value.
        [ ] TypeError | Incorrect. Python permits float and int numeric comparisons.
        [ ] SyntaxError | Incorrect. Valid comparison syntax.


    .. multichoice::

        Given ``a = 5`` and ``b = 10``, what does ``a > b`` evaluate to?

        [x] False | Correct! 5 is not greater than 10.
        [ ] True | Incorrect. 5 is smaller than 10.
        [ ] 5 | Incorrect. Relational checks return Booleans.
        [ ] 10 | Incorrect. Operands are not returned.


    .. multichoice::

        What does ``"cat" != "dog"`` evaluate to?

        [x] True | Correct! The string "cat" is not equal to "dog".
        [ ] False | Incorrect. The strings are distinct.
        [ ] None | Incorrect. Relational comparisons return Booleans.
        [ ] SyntaxError | Incorrect. Valid string comparison.

----

Logical Operators
=================

Logical operators combine or modify Boolean expressions:

- **and**: Returns ``True`` **only if both** conditions evaluate to ``True``.
- **or**: Returns ``True`` if **at least one** condition evaluates to ``True``.
- **not**: Inverts a Boolean value (turns ``True`` to ``False`` and vice versa).

.. code-block:: python

    age = 15
    has_permission = True

    # Both conditions must be True
    can_enter = (age >= 13) and has_permission  # True

    # At least one condition must be True
    is_weekend = False
    is_holiday = True
    no_school = is_weekend or is_holiday       # True

    # Invert result
    print(not is_weekend)                       # True

Quiz: Logical Operators
-----------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. The @@and@@ operator returns `True` only if all connected conditions are true.
    2. The @@or@@ operator returns `True` if at least one connected condition is true.
    3. The @@not@@ operator reverses or inverts a Boolean truth value.
    4. The expression `True and False` evaluates to @@False@@.
    5. The expression `not False` evaluates to @@True@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Check if a number is within a valid range between 10 and 20 inclusive.

.. ordering::

    num = 15
    is_valid = (num >= 10) and (num <= 20)
    print(is_valid)

----

**Example 2:** Determine if a person gets free entry (child under 5 or senior over 65).

.. ordering::

    age = 70
    free_entry = (age < 5) or (age > 65)
    print(free_entry)

----

**Example 3:** Check if game over condition is NOT met.

.. ordering::

    lives = 3
    game_over = lives == 0
    keep_playing = not game_over
    print(keep_playing)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What does ``(5 > 2) and (10 < 5)`` evaluate to?

        [x] False | Correct! True and False evaluates to False because 'and' requires both conditions to be True.
        [ ] True | Incorrect. Second condition (10 < 5) is False.
        [ ] None | Incorrect. Logical operators evaluate to Booleans.
        [ ] ValueError | Incorrect. Valid logical check.


    .. multichoice::

        What is the result of ``(5 > 2) or (10 < 5)``?

        [x] True | Correct! First condition (5 > 2) is True, so 'or' evaluates to True.
        [ ] False | Incorrect. 'or' requires only one condition to be True.
        [ ] None | Incorrect. Logical checks yield Booleans.
        [ ] SyntaxError | Incorrect. Valid syntax.


    .. multichoice::

        What does ``not (10 == 10)`` evaluate to?

        [x] False | Correct! 10 == 10 is True; 'not' inverts True to False.
        [ ] True | Incorrect. 'not' negates the truth value of True.
        [ ] 10 | Incorrect. 'not' returns a Boolean value.
        [ ] SyntaxError | Incorrect. Valid expression structure.


    .. multichoice::

        Which logical operator requires ONLY ONE condition to be true for the overall expression to be true?

        [x] or | Correct! 'or' returns True if any operand is True.
        [ ] and | Incorrect. 'and' requires all operands to be True.
        [ ] not | Incorrect. 'not' is a unary operator that inverts truth value.
        [ ] == | Incorrect. == is a comparison operator, not a logical operator.


    .. multichoice::

        What is the output of ``not (5 > 10)``?

        [x] True | Correct! 5 > 10 is False; 'not False' evaluates to True.
        [ ] False | Incorrect. Inner expression is False, so 'not' turns it True.
        [ ] None | Incorrect. Operator evaluates to Boolean True.
        [ ] SyntaxError | Incorrect. Valid structure.


    .. multichoice::

        What evaluates to ``True`` when combining conditions with ``and``?

        [x] Every individual condition is True | Correct! 'and' requires 100% true conditions.
        [ ] At least one condition is True | Incorrect. That describes 'or' behavior.
        [ ] All conditions are False | Incorrect. False and False evaluates to False.
        [ ] The first condition is False | Incorrect. First condition being False forces 'and' to return False.


    .. multichoice::

        Given ``a = True`` and ``b = False``, what is ``a and (not b)``?

        [x] True | Correct! b is False, so 'not b' is True; True and True evaluates to True.
        [ ] False | Incorrect. 'not b' turns False into True.
        [ ] None | Incorrect. Evaluates to Boolean True.
        [ ] SyntaxError | Incorrect. Expression is syntactically valid.


    .. multichoice::

        What is short-circuit evaluation in Python logical operators?

        [x] Stopping evaluation as soon as the overall result is determined | Correct! Python skips evaluating remaining sub-expressions once outcome is fixed.
        [ ] Automatically correcting syntax errors in boolean logic | Incorrect. Short-circuiting affects execution order, not syntax parsing.
        [ ] Running logical checks in parallel threads | Incorrect. Execution remains sequential.
        [ ] Converting integers into boolean values | Incorrect. Type casting performs boolean conversion.


    .. multichoice::

        What is the result of ``False or False or True``?

        [x] True | Correct! A single True condition causes an 'or' chain to evaluate to True.
        [ ] False | Incorrect. One condition is True.
        [ ] None | Incorrect. Evaluates to Boolean True.
        [ ] SyntaxError | Incorrect. Valid chained logical statement.


    .. multichoice::

        What does ``not (True and False)`` evaluate to?

        [x] True | Correct! Inside parens evaluates to False; 'not False' evaluates to True.
        [ ] False | Incorrect. Inner expression yields False, negated to True.
        [ ] None | Incorrect. Evaluates to Boolean True.
        [ ] SyntaxError | Incorrect. Valid logical expression.

----

Assignment Operators
====================

Assignment operators are used to assign or update variable values:

- **Basic Assignment (=)**: Assigns right-side value to left-side variable.
- **Add and Assign (+=)**: Adds value and reassigns result (`x += 5` is `x = x + 5`).
- **Subtract and Assign (-=)**: Subtracts value and reassigns result (`x -= 2` is `x = x - 2`).
- **Multiply and Assign (*=)**: Multiplies value and reassigns result (`x *= 3` is `x = x * 3`).
- **Divide and Assign (/=)**: Divides value and reassigns result (`x /= 2` is `x = x / 2`).

.. code-block:: python

    score = 100

    score += 10  # score is now 110
    score -= 25  # score is now 85
    score *= 2   # score is now 170

Quiz: Assignment Operators
--------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. The statement `x += 5` is a @@shorthand@@ equivalent of `x = x + 5`.
    2. The -= operator @@subtracts@@ a value from a variable and reassigns the new value.
    3. Running `score *= 2` @@doubles@@ the current value stored inside score.
    4. Compound assignment operators update variables in-place without repeating the @@variable@@ name twice.
    5. Performing `x /= 2` updates `x` to a @@float@@ data type regardless of initial integer value.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Increase a player's score by 50 points using compound assignment.

.. ordering::

    score = 100
    score += 50
    print(score)

----

**Example 2:** Apply a 10% discount to a price using the `/=` or `*=` operator.

.. ordering::

    price = 100
    price *= 0.9
    print(price)

----

**Example 3:** Count down remaining lives in a video game by 1.

.. ordering::

    lives = 3
    lives -= 1
    print(lives)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        If ``count = 10``, what is the value of ``count`` after ``count += 5``?

        [x] 15 | Correct! count += 5 adds 5 to 10, updating count to 15.
        [ ] 10 | Incorrect. Variable was updated by += operator.
        [ ] 5 | Incorrect. += adds to existing value rather than replacing it with 5.
        [ ] 50 | Incorrect. Addition occurred, not multiplication.


    .. multichoice::

        Which statement is equivalent to ``x = x * 3``?

        [x] x *= 3 | Correct! *= is the compound multiplication assignment operator.
        [ ] x =* 3 | Incorrect. Invalid operator syntax sequence.
        [ ] x **= 3 | Incorrect. **= is compound exponentiation assignment.
        [ ] x3 = * | Incorrect. Invalid syntax.


    .. multichoice::

        Given ``val = 20``, what is ``val`` after executing ``val /= 4``?

        [x] 5.0 | Correct! Division /= always produces a float result (20 / 4 = 5.0).
        [ ] 5 | Incorrect. /= operator outputs float types in Python 3.
        [ ] 80 | Incorrect. Division was performed, not multiplication.
        [ ] 16 | Incorrect. 20 / 4 evaluates to 5.0.


    .. multichoice::

        What is the final value of ``num`` after: ``num = 8; num -= 3; num *= 2``?

        [x] 10 | Correct! $8 - 3 = 5$, then $5 \times 2 = 10$.
        [ ] 13 | Incorrect. Operations occur sequentially: subtraction then multiplication.
        [ ] 16 | Incorrect. num -= 3 updates num to 5 first.
        [ ] 10.0 | Incorrect. Operations involve integers without standard division.


    .. multichoice::

        Why do programmers use compound assignment operators (like ``+=``, ``-=``)?

        [x] They make code concise and easier to read by avoiding redundant variable names | Correct! Compound operators simplify variable update statements.
        [ ] They allow variables to store multiple values at once | Incorrect. Variables store single values unless holding collections.
        [ ] They prevent variables from changing values | Incorrect. They explicitly update variable values.
        [ ] They convert text strings into integer numbers | Incorrect. Type casting functions perform type conversions.


    .. multichoice::

        If ``n = 4``, what does ``n **= 2`` set ``n`` to?

        [x] 16 | Correct! $4^2 = 16$.
        [ ] 8 | Incorrect. **= is exponentiation ($4^2$), not multiplication ($4 \times 2$).
        [ ] 6 | Incorrect. Exponentiation multiplies 4 by itself.
        [ ] 2 | Incorrect. Exponent is 2.


    .. multichoice::

        Given ``items = 12``, what is the value of ``items`` after ``items %= 5``?

        [x] 2 | Correct! $12 \% 5 = 2$ (remainder of 12 divided by 5).
        [ ] 2.4 | Incorrect. %= performs modulus (remainder), not division.
        [ ] 10 | Incorrect. Remainder is 2.
        [ ] 0 | Incorrect. 12 is not evenly divisible by 5.


    .. multichoice::

        What happens if you run ``x += 1`` before defining ``x``?

        [x] Python raises a NameError | Correct! Variable x must be defined before its value can be updated.
        [ ] x is automatically created with value 1 | Incorrect. Variables must exist prior to compound updates.
        [ ] x is set to 0 | Incorrect. Python does not auto-initialize unassigned variables.
        [ ] Python runs an infinite loop | Incorrect. NameError occurs immediately.


    .. multichoice::

        Given ``text = "Hello"``, what is ``text`` after ``text += " World"``?

        [x] "Hello World" | Correct! The += operator concatenates strings when applied to string variables.
        [ ] "World" | Incorrect. += appends string to existing string.
        [ ] TypeError | Incorrect. String concatenation with += is fully valid.
        [ ] SyntaxError | Incorrect. Valid string compound assignment.


    .. multichoice::

        What is the result of ``a = 10; a //= 3``?

        [x] 3 | Correct! Floor division integer result ($10 // 3 = 3$) is assigned back to a.
        [ ] 3.333 | Incorrect. //= performs floor division (rounds down to integer).
        [ ] 1 | Incorrect. 1 is remainder (%=); //= computes integer quotient.
        [ ] 30 | Incorrect. Floor division was executed.

