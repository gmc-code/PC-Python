===========================
Selection (If Statements)
===========================

| In programming, **selection** allows a computer program to make decisions and execute different blocks of code based on conditions.
| A **condition** is an expression that evaluates to either ``True`` or ``False`` (a **Boolean** value).
| In Python, selection is implemented using the ``if`` statement, alongside comparison operators to test conditions.
| Python uses **indentation** (usually 4 spaces) to define which lines of code belong inside the ``if`` block.

.. code-block:: python

    # Basic selection in Python
    age = 15

    if age >= 12:
        print("You are eligible for a student ticket!")

----

Comparison and Logical Operators
================================

To create conditional expressions for selection, Python relies on comparison and logical operators:

- **Comparison Operators**: Used to compare two values: ``==`` (equals), ``!=`` (not equals), ``>`` (greater than), ``<`` (less than), ``>=`` (greater than or equal to), ``<=`` (less than or equal to).
- **Logical Operators**: Used to combine multiple conditions: ``and`` (both True), ``or`` (at least one True), ``not`` (reverses True/False).

.. code-block:: python

    # Using comparison and logical operators
    score = 85
    has_pass = True

    if score >= 80 and has_pass:
        print("You passed with distinction!")

Quiz: Comparison Operators and Basic If
---------------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Making decisions in a program based on conditions is called @@selection@@.
    2. An expression that evaluates to either True or False is called a @@Boolean@@ expression.
    3. The comparison operator used to test if two values are equal is @@==@@.
    4. Python uses @@indentation@@ (4 spaces) to specify the block of code inside an if statement.
    5. The logical operator @@and@@ requires both conditions to be True for the overall statement to evaluate to True.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Check if a temperature is greater than 30 degrees and print a warning message.

.. ordering::

    temperature = 32
    if temperature > 30:
        print("Warning: High temperature detected!")

----

**Example 2:** Combine two conditions using the `and` operator to verify login status.

.. ordering::

    user = "admin"
    logged_in = True
    if user == "admin" and logged_in:
        print("Access granted to administrative portal.")

----

**Example 3:** Use the `!=` operator to test for unequal values.

.. ordering::

    status = "pending"
    if status != "complete":
        print("Task is still in progress.")

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Which operator is used to check if two values are equal in an if condition?

        [x] == | Correct! The double equals sign == checks for equality.
        [ ] = | Incorrect. The single equals sign = is used for variable assignment.
        [ ] != | Incorrect. != checks if two values are NOT equal.
        [ ] := | Incorrect. := is the walrus operator, not the equality comparison operator.


    .. multichoice::

        What happens in Python if you forget to indent the line directly following an ``if`` statement?

        [x] Python raises an IndentationError | Correct! Python strictly requires indented blocks after conditional statements.
        [ ] The code runs normally without checking the condition | Incorrect. Python cannot parse unindented code blocks following an if statement.
        [ ] Python automatically fixes the spacing | Incorrect. Syntax and indentation rules are strictly enforced by the interpreter.
        [ ] The statement evaluates to False automatically | Incorrect. Indentation errors prevent code execution.


    .. multichoice::

        Given ``x = 10``, what does ``x > 5 and x < 15`` evaluate to?

        [x] True | Correct! Both 10 > 5 (True) and 10 < 15 (True) are True, so the combined statement is True.
        [ ] False | Incorrect. Since both conditions are satisfied, the and expression evaluates to True.
        [ ] None | Incorrect. Logical comparisons always yield Boolean True or False.
        [ ] IndentationError | Incorrect. The expression is valid Python syntax.


    .. multichoice::

        Which symbol is placed at the end of an ``if`` line in Python?

        [x] : | Correct! A colon : must follow the condition in an if statement.
        [ ] ; | Incorrect. Colons : are used in Python conditional headers rather than semicolons.
        [ ] . | Incorrect. Colons indicate the start of an indented block.
        [ ] { | Incorrect. Python uses colons and indentation rather than curly braces.


    .. multichoice::

        What will ``print(5 != 5)`` output?

        [x] False | Correct! 5 is equal to 5, so the 'not equal to' check yields False.
        [ ] True | Incorrect. 5 is equal to 5, so 5 != 5 is False.
        [ ] SyntaxError | Incorrect. != is valid syntax.
        [ ] None | Incorrect. Logical checks return a Boolean value.


    .. multichoice::

        Which logical operator reverses a Boolean value (turning True to False, and False to True)?

        [x] not | Correct! The not operator negates any Boolean expression.
        [ ] and | Incorrect. and joins two expressions together.
        [ ] or | Incorrect. or evaluates if at least one condition is True.
        [ ] flip | Incorrect. flip is not a valid Python operator keyword.


    .. multichoice::

        What is the outcome of ``True or False`` in Python?

        [x] True | Correct! An or statement evaluates to True if at least one side is True.
        [ ] False | Incorrect. At least one side is True, so or yields True.
        [ ] None | Incorrect. Logical operators evaluate to Boolean results.
        [ ] SyntaxError | Incorrect. Valid logical expression.


    .. multichoice::

        What does the operator ``<=`` test?

        [x] Less than or equal to | Correct! <= tests whether the left value is smaller than or equal to the right value.
        [ ] Greater than or equal to | Incorrect. Greater than or equal to is represented as >=.
        [ ] Strictly less than | Incorrect. Strictly less than uses <.
        [ ] Not equal to | Incorrect. Not equal to uses !=.


    .. multichoice::

        Given ``a = 3`` and ``b = 7``, which condition evaluates to True?

        [x] a < b | Correct! 3 is strictly less than 7.
        [ ] a > b | Incorrect. 3 is not greater than 7.
        [ ] a == b | Incorrect. 3 is not equal to 7.
        [ ] a >= b | Incorrect. 3 is not greater than or equal to 7.


    .. multichoice::

        What value type does a conditional check evaluate to?

        [x] Boolean | Correct! Conditions evaluate to True or False, which are Boolean values.
        [ ] String | Incorrect. Strings store text values.
        [ ] Integer | Incorrect. Integers represent whole numbers.
        [ ] Float | Incorrect. Floats represent decimal numbers.

----

The Else Statement
==================

An ``else`` statement provides an alternative path in code execution:

- **Fallback Execution**: The code inside an ``else`` block runs **only** when the preceding ``if`` condition evaluates to ``False``.
- **Syntax**: The ``else:`` keyword must align vertically with its corresponding ``if`` statement and be followed by a colon.
- **Binary Decision Making**: ``if-else`` creates a two-way choice (either the condition is met, or the alternative happens).

.. code-block:: python

    # Using if-else for two-way selection
    password = "secret"
    user_input = "12345"

    if user_input == password:
        print("Access Granted")
    else:
        print("Access Denied: Incorrect Password")

Quiz: The Else Statement
------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. An @@else@@ block executes when the preceding condition evaluates to False.
    2. An else statement does not accept a condition; it simply uses the @@else:@@ syntax.
    3. Selection structures with both if and else handle @@binary@@ or two-way choices.
    4. The else statement must match the @@indentation@@ level of its corresponding if statement.
    5. Code inside an else block must be @@indented@@ to show membership in that block.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Check if a number is positive or non-positive using `if-else`.

.. ordering::

    num = -5
    if num > 0:
        print("Positive number")
    else:
        print("Zero or negative number")

----

**Example 2:** Determine passing status based on score threshold.

.. ordering::

    score = 45
    if score >= 50:
        print("Passed")
    else:
        print("Failed")

----

**Example 3:** Check item stock availability.

.. ordering::

    stock = 0
    if stock > 0:
        print("Item is in stock")
    else:
        print("Out of stock")

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        When does code inside an ``else`` block execute?

        [x] When the initial ``if`` condition evaluates to False | Correct! The else block acts as a fallback when conditions fail.
        [ ] When the initial ``if`` condition evaluates to True | Incorrect. True conditions run the if block, bypassing else.
        [ ] Every time the program runs regardless of conditions | Incorrect. Else blocks execution depends on condition failure.
        [ ] Only when a SyntaxError occurs | Incorrect. Else handles runtime logic branches.


    .. multichoice::

        Which of the following syntax structures for an ``else`` statement is correct?

        [x] else: | Correct! else is followed by a colon and an indented code block below.
        [ ] else (x > 5): | Incorrect. else statements do not take explicit condition arguments.
        [ ] else then: | Incorrect. then is not a keyword in Python syntax.
        [ ] else; | Incorrect. Statements end with colons rather than semicolons.


    .. multichoice::

        Given ``age = 10``, what will execute in ``if age >= 18: print("Adult") else: print("Child")``?

        [x] Prints "Child" | Correct! 10 >= 18 is False, triggering the else block.
        [ ] Prints "Adult" | Incorrect. The condition fails, so "Adult" is skipped.
        [ ] Prints both "Adult" and "Child" | Incorrect. Only one path executes in if-else.
        [ ] Prints nothing | Incorrect. The else branch executes and prints "Child".


    .. multichoice::

        Can an ``else`` block exist in Python without a preceding ``if`` statement?

        [x] No, an ``else`` block must always be attached to an ``if`` (or loop structure) | Correct! Unattached else statements raise SyntaxError.
        [ ] Yes, an ``else`` statement can run independently anywhere | Incorrect. Else requires a preceding control structure.
        [ ] Yes, if initialized at the beginning of a script | Incorrect. Else requires context.
        [ ] Only if placed inside a function | Incorrect. Else requires an accompanying conditional.


    .. multichoice::

        What is output by ``is_logged = False; if is_logged: print("In") else: print("Out")``?

        [x] Out | Correct! is_logged is False, directing execution to the else block.
        [ ] In | Incorrect. Condition evaluates to False.
        [ ] None | Incorrect. Output is produced by the print in the else block.
        [ ] IndentationError | Incorrect. The structure is valid.


    .. multichoice::

        How many paths in an ``if-else`` block can be executed during a single run?

        [x] Exactly 1 | Correct! Either the if block executes OR the else block executes.
        [ ] 2 | Incorrect. If and else are mutually exclusive.
        [ ] 0 | Incorrect. Exactly one path will be taken.
        [ ] Up to 3 | Incorrect. Standard if-else offers two branches.


    .. multichoice::

        What error occurs if ``else:`` is indented further right than its matching ``if:`` statement?

        [x] IndentationError or SyntaxError | Correct! Else must align with its paired if statement.
        [ ] NameError | Incorrect. NameErrors relate to unassigned identifiers.
        [ ] TypeError | Incorrect. TypeErrors involve incompatible types.
        [ ] ValueError | Incorrect. ValueErrors stem from invalid argument values.


    .. multichoice::

        What will happen in ``x = 5; if x == 5: print("A") else: print("B")``?

        [x] "A" is printed | Correct! Condition 5 == 5 is True, so the if block runs and else is skipped.
        [ ] "B" is printed | Incorrect. The condition is True, so else does not run.
        [ ] Both "A" and "B" are printed | Incorrect. Only one branch executes.
        [ ] Nothing is printed | Incorrect. "A" is output.


    .. multichoice::

        Why does ``else x > 10:`` raise a SyntaxError in Python?

        [x] Because ``else`` statements cannot take explicit conditions | Correct! Use elif when testing additional conditions.
        [ ] Because 10 is an integer | Incorrect. Integers are valid in condition expressions.
        [ ] Because > is an invalid operator | Incorrect. > is a valid comparison operator.
        [ ] Because else must be capitalized | Incorrect. Keywords must be lowercase in Python.


    .. multichoice::

        What is the primary role of an ``else`` branch?

        [x] To specify default code execution when preceding conditions are False | Correct! Else acts as the catch-all branch.
        [ ] To loop a set of instructions multiple times | Incorrect. Loops handle repetition.
        [ ] To define new variables | Incorrect. Variables can be assigned in any branch.
        [ ] To stop the entire script | Incorrect. Else manages conditional branching.

----

Multi-Branch Selection with Elif
================================

When you need to test multiple conditions in sequence, use ``elif`` (short for **else if**):

- **Sequential Evaluation**: Python checks conditions from top to bottom. The **first** condition that evaluates to ``True`` runs its block, and all remaining ``elif`` and ``else`` branches are skipped!
- **Multiple Conditions**: You can chain as many ``elif`` blocks as necessary.
- **Optional Else**: An ``else`` block can be placed at the end as a final catch-all branch.

.. code-block:: python

    # Multi-branch selection with if-elif-else
    score = 75

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print("Grade:", grade)

Quiz: Multi-Branch Selection with Elif
--------------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. The keyword @@elif@@ is short for "else if" in Python syntax.
    2. In an if-elif-else chain, Python stops testing conditions as soon as it finds the @@first@@ True expression.
    3. An optional @@else@@ statement can be placed at the end of an if-elif chain to handle all unmatched cases.
    4. You can include @@multiple@@ elif statements within a single selection structure.
    5. Order matters in elif chains because expressions are evaluated @@sequentially@@ from top to bottom.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Assign a descriptive label based on speed evaluation.

.. ordering::

    speed = 45
    if speed > 60:
        print("Fast")
    elif speed > 30:
        print("Moderate")
    else:
        print("Slow")

----

**Example 2:** Determine ticket pricing based on age category.

.. ordering::

    age = 8
    if age < 5:
        price = 0
    elif age < 18:
        price = 10
    else:
        price = 20

----

**Example 3:** Categorize temperature into hot, warm, or cold.

.. ordering::

    temp = 18
    if temp >= 25:
        category = "Hot"
    elif temp >= 15:
        category = "Warm"
    else:
        category = "Cold"

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What does ``elif`` stand for in Python?

        [x] else if | Correct! elif is a contraction of else if.
        [ ] element if | Incorrect. elif stands for else if.
        [ ] else loop if | Incorrect. elif is used exclusively for conditional branching.
        [ ] evaluate if | Incorrect. elif stands for else if.


    .. multichoice::

        What will be output by the following code? ``x = 15; if x > 20: print("A") elif x > 10: print("B") elif x > 5: print("C") else: print("D")``

        [x] B | Correct! x > 20 is False, but x > 10 is True. Output is "B", and remaining branches are skipped.
        [ ] B and C | Incorrect. Only the first matching branch executes.
        [ ] A | Incorrect. 15 is not greater than 20.
        [ ] D | Incorrect. 15 > 10 evaluated to True, so else does not run.


    .. multichoice::

        How many ``elif`` blocks can be included inside a single selection structure?

        [x] As many as needed | Correct! You can add unlimited elif statements between if and else.
        [ ] Exactly 1 | Incorrect. Multiple elif blocks are permitted.
        [ ] Maximum of 3 | Incorrect. There is no artificial cap on elif count.
        [ ] None, elif is optional | Incorrect. While optional, when used, count is unlimited.


    .. multichoice::

        Why is the order of conditions important in an ``if-elif-else`` chain?

        [x] Because Python executes only the first branch whose condition evaluates to True | Correct! Subsequent conditions are skipped once a match is found.
        [ ] Because Python evaluates conditions from bottom to top | Incorrect. Python evaluates top to bottom.
        [ ] Because misplaced conditions cause a SyntaxError | Incorrect. Order affects logic, not syntax validity.
        [ ] Because Python averages all conditions | Incorrect. Conditions are tested sequentially.


    .. multichoice::

        Given ``score = 95``, why would ``if score >= 60: print("Pass") elif score >= 90: print("Excellent")`` be considered logically flawed?

        [x] Because ``score >= 60`` is True first, so "Pass" prints and "Excellent" is never reached | Correct! Specific conditions should precede broader conditions.
        [ ] Because 95 is too large for Python conditions | Incorrect. Python handles numeric comparisons cleanly.
        [ ] Because print statements cannot accept strings | Incorrect. Strings are standard arguments for print().
        [ ] Because elif cannot come after if | Incorrect. Elif correctly follows if.


    .. multichoice::

        In an ``if-elif-else`` structure, is the final ``else`` block required?

        [x] No, the ``else`` block is optional | Correct! You can write if-elif chains without a trailing else.
        [ ] Yes, an ``if-elif`` chain fails without an ``else`` | Incorrect. Else is completely optional.
        [ ] Only if there are more than 2 elif blocks | Incorrect. Optional regardless of elif count.
        [ ] Yes, Python requires else for clean exit | Incorrect. Execution continues past the chain normally.


    .. multichoice::

        What is output by ``val = 0; if val > 0: print("Pos") elif val < 0: print("Neg") else: print("Zero")``?

        [x] Zero | Correct! 0 > 0 is False, 0 < 0 is False, so execution lands in else.
        [ ] Pos | Incorrect. 0 is not strictly greater than 0.
        [ ] Neg | Incorrect. 0 is not strictly less than 0.
        [ ] SyntaxError | Incorrect. The structure is valid.


    .. multichoice::

        What happens if none of the conditions in an ``if-elif`` structure (without an ``else``) evaluate to True?

        [x] Nothing inside the selection block executes, and the program moves to the next statement | Correct! The entire selection block is bypassed cleanly.
        [ ] Python raises a ValueError | Incorrect. No error occurs when conditions evaluate to False.
        [ ] The first elif executes automatically | Incorrect. Conditions must evaluate to True to execute.
        [ ] Python halts script execution | Incorrect. Execution proceeds past the block.


    .. multichoice::

        Which statement about conditional evaluation is TRUE?

        [x] If an ``if`` condition is True, Python skips checking all following ``elif`` and ``else`` blocks | Correct! Evaluation short-circuits on first match.
        [ ] Python checks all ``elif`` blocks even if the main ``if`` condition was True | Incorrect. Execution skips remaining branches.
        [ ] Python checks conditions in random order | Incorrect. Conditions are tested top to bottom.
        [ ] ``elif`` conditions run before ``if`` conditions | Incorrect. Execution begins at the initial if.


    .. multichoice::

        Given ``x = 10``, what does ``if x == 5: print("Five") elif x == 10: print("Ten") else: print("Other")`` output?

        [x] Ten | Correct! First condition is False, second condition evaluates to True.
        [ ] Five | Incorrect. 10 == 5 is False.
        [ ] Other | Incorrect. The elif branch matches, so else is bypassed.
        [ ] Ten and Other | Incorrect. Only one branch executes.

----

Nested Selection Structures
===========================

You can place an ``if`` statement **inside** another ``if`` statement. This is called **nested selection**:

- **Hierarchical Logic**: Used when a second condition only needs to be checked if a primary condition passes.
- **Indentation Levels**: Each nested level requires an additional 4 spaces of indentation.

.. code-block:: python

    # Nested selection example
    age = 16
    has_permission = True

    if age < 18:
        if has_permission:
            print("Allowed with parental consent.")
        else:
            print("Not allowed without consent.")
    else:
        print("Allowed independently.")

Quiz: Nested Selection Structures
---------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Placing an if statement inside another if statement is called @@nested@@ selection.
    2. Each inner level of nested selection requires additional @@indentation@@.
    3. In a nested structure, inner conditions are evaluated only if the outer condition is @@True@@.
    4. Complex nested selection can often be simplified using @@logical@@ operators like `and`.
    5. An inner else block attaches to the closest preceding @@if@@ statement at the same indentation level.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Check membership status and apply discount if active.

.. ordering::

    is_member = True
    points = 120
    if is_member:
        if points > 100:
            print("Eligible for reward discount!")

----

**Example 2:** Check user age and driving test status.

.. ordering::

    age = 17
    passed_test = True
    if age >= 17:
        if passed_test:
            print("Licence granted.")
        else:
            print("Must pass test first.")

----

**Example 3:** Check weather conditions for outdoor activity.

.. ordering::

    is_sunny = True
    temp = 22
    if is_sunny:
        if temp > 20:
            print("Perfect outdoor picnic weather!")

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What is nested selection in Python?

        [x] An ``if`` statement placed inside another ``if`` statement | Correct! Nesting involves placing control structures inside existing blocks.
        [ ] An ``if`` statement placed inside a variable | Incorrect. Statements cannot be assigned inside variables.
        [ ] Using multiple logical operators on one line | Incorrect. Logical operators combine conditions in single statements.
        [ ] An ``if`` statement without an ``else`` block | Incorrect. Nesting specifically refers to hierarchical block structures.


    .. multichoice::

        Given ``a = True`` and ``b = False``, what prints in ``if a: if b: print("1") else: print("2")``?

        [x] 2 | Correct! Outer condition a is True, so execution enters the inner block. Inner condition b is False, executing inner else.
        [ ] 1 | Incorrect. Inner condition b is False.
        [ ] Nothing | Incorrect. Inner else executes and outputs "2".
        [ ] 1 and 2 | Incorrect. Only one inner branch executes.


    .. multichoice::

        How is indentation handled for a nested ``if`` block?

        [x] Indented 8 spaces (or two levels of indentation) relative to the script edge | Correct! Each nested layer adds 4 indentation spaces.
        [ ] Unindented | Incorrect. All nested statements require indentation.
        [ ] Indented with tabs and spaces mixed randomly | Incorrect. Python prohibits mixing tabs and spaces.
        [ ] Indented 2 spaces only | Incorrect. Standard Python style uses 4 spaces per nesting level.


    .. multichoice::

        What happens if the outer condition of a nested ``if`` statement evaluates to False?

        [x] The entire inner block is skipped completely | Correct! Execution proceeds past the outer block.
        [ ] The inner block runs anyway | Incorrect. Outer condition failure bypasses nested contents.
        [ ] Python raises an exception | Incorrect. Bypassing conditions is standard control flow behavior.
        [ ] The inner else branch executes | Incorrect. Inner branches are unreachable if outer condition fails.


    .. multichoice::

        Which single ``if`` statement is equivalent to: ``if x > 0: if y > 0: print("Both positive")``?

        [x] if x > 0 and y > 0: print("Both positive") | Correct! Nested if checks without alternative branches match logical and conditions.
        [ ] if x > 0 or y > 0: print("Both positive") | Incorrect. or allows execution when only one condition passes.
        [ ] if not(x > 0): print("Both positive") | Incorrect. not negates the condition.
        [ ] if x == y: print("Both positive") | Incorrect. Equality check differs from positive check.


    .. multichoice::

        Given ``x = 5`` and ``y = -2``, what outputs in ``if x > 0: if y > 0: print("A") else: print("B") else: print("C")``?

        [x] B | Correct! Outer condition x > 0 is True. Inner condition y > 0 is False, triggering inner else ("B").
        [ ] A | Incorrect. y > 0 is False.
        [ ] C | Incorrect. Outer condition was True, so outer else is skipped.
        [ ] Nothing | Incorrect. "B" prints.


    .. multichoice::

        Why might a programmer choose logical operators over deep nesting?

        [x] To make code cleaner, flatter, and easier to read | Correct! Deep nesting creates hard-to-read "pyramid" code structures.
        [ ] Because Python limits nesting to 1 level | Incorrect. Python allows multiple nesting levels.
        [ ] Because logical operators run faster | Incorrect. Primary benefit is readability and maintenance.
        [ ] Because nested statements cause memory leaks | Incorrect. Nesting is valid syntax without memory issues.


    .. multichoice::

        To which ``if`` statement does an ``else`` block attach in nested selection?

        [x] To the closest preceding ``if`` statement at the same indentation level | Correct! Indentation defines statement binding.
        [ ] To the outermost ``if`` statement always | Incorrect. Indentation matches else to its specific level.
        [ ] To the very first line of code in the file | Incorrect. Binding is scoped strictly by indentation level.
        [ ] To all ``if`` statements simultaneously | Incorrect. Else attaches to a single corresponding statement.


    .. multichoice::

        What output is produced by ``p = False; q = True; if p: if q: print("X") else: print("Y")``?

        [x] Nothing is printed | Correct! p is False, so outer condition fails and inner statements are bypassed.
        [ ] X | Incorrect. Outer condition p is False.
        [ ] Y | Incorrect. Outer block is completely skipped.
        [ ] IndentationError | Incorrect. Syntax is valid.


    .. multichoice::

        What does excessive levels of nesting (deep nesting) make difficult?

        [x] Code readability and maintenance | Correct! Deep nesting reduces legibility and increases logic bug risk.
        [ ] Variable assignment | Incorrect. Variables function identically regardless of depth.
        [ ] Mathematical operations | Incorrect. Math operations are unaffected by nesting depth.
        [ ] Python installation | Incorrect. Nesting affects code structure rather than installation.

