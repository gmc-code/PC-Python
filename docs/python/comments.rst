===========================
Comments
===========================

| In Python, **comments** are notes written in the source code to explain what the code does.
| They are completely ignored by the Python interpreter when the program runs.
| Comments make code easier to understand for yourself, your teammates, and anyone else reading your scripts.

.. code-block:: python

    # This is a single-line comment explaining the next line
    player_score = 100  # Comments can also go at the end of a line

    print(player_score)

----

Single-Line Comments
====================

Single-line comments are the most common type of comment in Python:

- **The Hash Symbol (#)**: Python recognizes any text following a `#` symbol on a line as a comment.
- **Line Placement**: Comments can occupy an entire line by themselves or be placed at the end of a line of code (inline comments).
- **Execution Skip**: Python ignores everything from the `#` character to the end of that specific line.
- **Code Explanation**: Use single-line comments to describe the intent, purpose, or logic of a specific instruction.

.. code-block:: python

    # Calculate total cost including shipping
    item_price = 25
    shipping = 5
    total = item_price + shipping  # Adding price and shipping together

    print(total)

Quiz: Single-Line Comments
--------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Single-line comments in Python start with the @@#@@ symbol.
    2. Python @@ignores@@ comments when executing code.
    3. Comments placed at the end of a line of code are called @@inline@@ comments.
    4. Code comments help developers improve code @@readability@@.
    5. Everything after the hash symbol on a line is treated as a @@comment@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Write a program with a single-line comment explaining a greeting.

.. ordering::

    # Set the user's name
    user_name = "Alex"
    # Print welcome greeting
    print("Welcome, " + user_name)

----

**Example 2:** Place an inline comment next to a calculation variable.

.. ordering::

    radius = 7
    # Calculate area of circle
    area = 3.14 * (radius ** 2)  # Formula: pi * r^2
    print(area)

----

**Example 3:** Use comments to explain a simple conditional setup.

.. ordering::

    age = 15
    # Check if user meets minimum age requirement
    can_enter = age >= 13
    print(can_enter)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Which character is used to start a single-line comment in Python?

        [x] # | Correct! The hash symbol (#) marks the start of a single-line comment in Python.
        [ ] // | Incorrect. Double slashes are used for comments in languages like C++ or JavaScript.
        [ ] <!-- | Incorrect. That syntax is used for HTML comments.
        [ ] % | Incorrect. Percent signs are not used for comments in Python.


    .. multichoice::

        What does the Python interpreter do when it encounters a comment?

        [x] It skips the comment completely and moves to the next instruction | Correct! Comments are ignored during program execution.
        [ ] It prints the comment text to the console | Incorrect. Comments are not displayed during normal execution unless printed explicitly.
        [ ] It raises a SyntaxError | Incorrect. Comments are valid syntax in Python.
        [ ] It saves the comment to a database | Incorrect. Comments do not interact with storage or databases.


    .. multichoice::

        Where can single-line comments be placed in a Python file?

        [x] On their own line or at the end of a line of code | Correct! Comments can occupy a standalone line or follow code inline.
        [ ] Only at the very top of the script | Incorrect. Comments can appear anywhere in Python code.
        [ ] Only inside function definitions | Incorrect. Comments can be written anywhere.
        [ ] Only after a print statement | Incorrect. Comments can follow any valid Python statement.


    .. multichoice::

        Given the line ``x = 10  # Initialize x``, what gets executed by Python?

        [x] Only x = 10 | Correct! Everything after # is treated as a comment and ignored.
        [ ] Only # Initialize x | Incorrect. The statement prior to # is executed normally.
        [ ] Both x = 10 and the comment text | Incorrect. The comment is omitted from execution.
        [ ] Neither line executes | Incorrect. Code prior to # executes as standard Python.


    .. multichoice::

        Which of the following is a valid single-line comment in Python?

        [x] # This is a comment | Correct! Prefixing text with # creates a valid comment.
        [ ] // This is a comment | Incorrect. // is integer division in Python.
        [ ] -- This is a comment | Incorrect. Double dashes are used in SQL, not Python.
        [ ] /* This is a comment */ | Incorrect. C-style comment syntax is invalid in Python.


    .. multichoice::

        Why are comments added to source code?

        [x] To explain the code's purpose and logic to human readers | Correct! Comments enhance readability and maintainability.
        [ ] To speed up program execution time | Incorrect. Comments do not improve execution performance.
        [ ] To make the script output text automatically | Incorrect. Output requires print statements.
        [ ] To prevent bugs from occurring | Incorrect. Comments do not affect logic or execution.


    .. multichoice::

        What happens if you put code *after* a `#` symbol on the same line?

        [x] The code is treated as text inside the comment and ignored | Correct! All text following # to the end of the line is ignored.
        [ ] Python executes the code normally | Incorrect. The hash symbol comments out everything after it on that line.
        [ ] Python throws an error | Incorrect. Text after # is considered comment content.
        [ ] The code runs at double speed | Incorrect. Comments have no performance effect.


    .. multichoice::

        Which statement about Python comments is TRUE?

        [x] Comments are intended for human readers, not the computer | Correct! Comments serve as notes for programmers.
        [ ] Python requires every line to have a comment | Incorrect. Comments are completely optional.
        [ ] Comments must always end with a semicolon | Incorrect. Python comments do not require punctuation.
        [ ] Comments cannot contain numbers | Incorrect. Any text character can appear inside a comment.


    .. multichoice::

        Given ``print("Hello")  # print("World")``, what is printed?

        [x] Hello | Correct! The second print statement is commented out and ignored.
        [ ] Hello World | Incorrect. The second print statement is treated as a comment.
        [ ] World | Incorrect. Only the active code before # executes.
        [ ] SyntaxError | Incorrect. Commenting out code is valid syntax.


    .. multichoice::

        What is an "inline comment"?

        [x] A comment placed on the same line as a statement of code | Correct! Inline comments appear after standard code on the same line.
        [ ] A comment written inside quotation marks | Incorrect. Text inside quotes forms a string literal.
        [ ] A comment that spans across multiple lines | Incorrect. Inline comments exist on a single line.
        [ ] A comment written in HTML | Incorrect. Python comments use Python syntax.

----

Multi-Line Comments and Docstrings
==================================

When you need to write explanations that span across multiple lines, Python offers two primary methods:

- **Multiple Hash Marks**: Use a `#` symbol at the start of each line to create multi-line comment blocks.
- **Triple-Quoted Strings (""" or ''')**: Multi-line strings not assigned to a variable are ignored by Python and serve as multi-line comments.
- **Docstrings**: Triple-quoted strings placed immediately below module, function, or class headers are reserved as documentation strings (docstrings).
- **Clean Formatting**: Block comments help summarize complex algorithms, program headers, or multi-step logic.

.. code-block:: python

    # Line 1: Program Author
    # Line 2: Date Created
    # Line 3: Description of code logic

    """
    This is a multi-line string comment.
    It can span as many lines as needed
    without typing # on every line.
    """

    def add(a, b):
        """Return the sum of two numbers."""  # Docstring describing function behavior
        return a + b

Quiz: Multi-Line Comments and Docstrings
----------------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. To write a multi-line comment using `#`, place a hash symbol at the start of @@each@@ line.
    2. Multi-line string comments use triple @@quotes@@ (`"""` or `'''`).
    3. A documentation string placed inside a function is called a @@docstring@@.
    4. Unassigned triple-quoted strings are @@ignored@@ by Python during execution.
    5. Docstrings help describe what a function or @@module@@ does.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Create a multi-line comment block using hash symbols.

.. ordering::

    # Project: Grade Calculator
    # Author: Student
    # Purpose: Compute final percentage
    score = 85

----

**Example 2:** Use a triple-quoted multi-line string comment to document a script setup.

.. ordering::

    """
    Script Setup:
    - Set default parameters
    - Initialize screen display
    """
    width = 800
    height = 600

----

**Example 3:** Write a function accompanied by a descriptive docstring.

.. ordering::

    def multiply(x, y):
        """Multiply two numbers and return result."""
        return x * y

    print(multiply(3, 4))

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Which quotation set is used to construct triple-quoted multi-line comments?

        [x] """ or ''' | Correct! Either three double quotes or three single quotes create multi-line string blocks.
        [ ] " or ' | Incorrect. Single quotes only span a single line.
        [ ] // or /* | Incorrect. C-style comment characters are invalid in Python.
        [ ] # or ## | Incorrect. Multi-line blocks with # require # on every individual line.


    .. multichoice::

        What is a "docstring" in Python?

        [x] A triple-quoted string used to document functions, classes, or modules | Correct! Docstrings store official documentation for code structures.
        [ ] A comment that disables syntax checking | Incorrect. Docstrings do not affect language syntax rules.
        [ ] A string that automatically converts to numbers | Incorrect. Docstrings are text blocks.
        [ ] A list of error messages | Incorrect. Docstrings document code intent.


    .. multichoice::

        What happens if a triple-quoted string is NOT assigned to a variable or function?

        [x] Python evaluates it, does nothing with it, and continues execution | Correct! Unassigned multi-line strings act as effective block comments.
        [ ] Python throws a NameError | Incorrect. Unassigned string literals are valid syntax.
        [ ] Python converts it to an integer | Incorrect. String content remains unassigned string data.
        [ ] Python deletes the script file | Incorrect. Unassigned strings do not affect file contents.


    .. multichoice::

        Where should a function docstring be placed?

        [x] On the first lines directly under the function header (def line) | Correct! Docstrings must immediately follow the header line.
        [ ] At the bottom of the entire script file | Incorrect. Must be inside the target function body.
        [ ] Outside the function file | Incorrect. Docstrings belong inside the source module.
        [ ] Before the def statement | Incorrect. Docstrings follow the def header line.


    .. multichoice::

        How do you create a multi-line comment block using standard `#` symbols?

        [x] Place a # character at the beginning of every individual line | Correct! Each comment line must explicitly begin with #.
        [ ] Place # only on the first line and # on the last line | Incorrect. Python requires # on every line.
        [ ] Use #* and *# to enclose the block | Incorrect. That syntax is invalid in Python.
        [ ] Wrap the lines inside braces {# ... #} | Incorrect. Brace comments are not supported in Python.


    .. multichoice::

        Which of the following is a valid multi-line comment or docstring representation?

        [x] """ This is a note """ | Correct! Triple quotes define multi-line string blocks.
        [ ] # This is line 1 \n line 2 | Incorrect. # comments terminate at line breaks.
        [ ] // Line 1 \n // Line 2 | Incorrect. // is invalid comment syntax in Python.
        [ ] <!-- Multi line comment --> | Incorrect. HTML comment format is invalid in Python.


    .. multichoice::

        Can triple-quoted string comments span across multiple lines without syntax errors?

        [x] Yes, triple-quoted strings natively allow line breaks across lines | Correct! Triple quotes allow string text to span multiline blocks.
        [ ] No, every line break requires a backslash character | Incorrect. Triple quotes handle newlines automatically.
        [ ] Yes, but only inside while loops | Incorrect. Triple quotes work anywhere in Python scripts.
        [ ] No, Python prohibits multi-line strings | Incorrect. Multi-line strings are fully supported.


    .. multichoice::

        What is the main difference between `#` comments and docstrings?

        [x] Docstrings can be accessed at runtime via the __doc__ attribute, whereas # comments are stripped out | Correct! Docstrings are stored object attributes in memory.
        [ ] # comments execute code, while docstrings do not | Incorrect. Neither comments nor docstrings execute logic.
        [ ] # comments only work on numbers | Incorrect. # comments work with any text.
        [ ] Docstrings require compilation | Incorrect. Python interprets docstrings standardly.


    .. multichoice::

        Is it valid to mix single-line `#` comments and triple-quoted docstrings in the same script?

        [x] Yes, programmers regularly use both depending on the context | Correct! Both comment styles coexist in standard Python scripts.
        [ ] No, scripts can only use one style throughout | Incorrect. Both styles are valid simultaneously.
        [ ] Yes, but only in Python 2 | Incorrect. Supported in all Python 3 versions.
        [ ] No, mixing them causes a IndentationError | Incorrect. Syntax remains valid regardless of mixing.


    .. multichoice::

        Which syntax is best practice for documenting what a custom module or function does?

        [x] Docstring using triple quotes (""") | Correct! PEP 8 style guide recommends docstrings for function/module documentation.
        [ ] Inline # comments on every line | Incorrect. Docstrings provide structured header documentation.
        [ ] Output printing using print() | Incorrect. Documentation should not output to users during normal execution.
        [ ] Variable assignments | Incorrect. Comments/docstrings document logic without taking variable state.

----

Best Practices and "Commenting Out" Code
========================================

Comments are powerful, but writing effective comments requires following good coding practices:

- **Explain WHY, Not WHAT**: Avoid stating obvious code actions (e.g., `# Add 1 to x`). Explain *why* the operation is happening.
- **Keep Comments Updated**: Outdated comments that contradict code logic cause confusion and bugs.
- **Commenting Out Code**: Temporarily disable lines of code during debugging by adding `#` in front of them without deleting them.
- **Avoid Over-Commenting**: Write clear, self-explanatory variable names so you don't need comments for trivial operations.

.. code-block:: python

    # BAD PRACTICE: Explaining the obvious
    x = x + 1  # Add 1 to x

    # GOOD PRACTICE: Explaining the logic/reason
    x = x + 1  # Increment round count for current player

    # COMMENTING OUT CODE FOR DEBUGGING:
    # print("Debugging value:", x)
    print("Game Over")

Quiz: Best Practices and "Commenting Out" Code
----------------------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Good comments explain @@why@@ code is written, rather than just what it does.
    2. Temporarily disabling code by adding `#` in front of lines is called @@commenting out@@ code.
    3. Comments that contradict updated code logic are called @@outdated@@ comments.
    4. Using clear variable names reduces the need for @@excessive@@ comments.
    5. Commenting out code helps developers test and @@debug@@ programs.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Comment out a print statement used for temporary testing.

.. ordering::

    score = 50
    # print("DEBUG: score is", score)
    total = score + 10
    print(total)

----

**Example 2:** Replace an obvious comment with a clear, meaningful logic explanation.

.. ordering::

    health = 100
    # Apply shield bonus when entering defense mode
    health = health + 20
    print(health)

----

**Example 3:** Re-enable disabled code by removing the hash symbol.

.. ordering::

    # Step 1: Initialize player speed
    speed = 5
    # Step 2: Apply booster
    speed = speed * 2
    print(speed)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What does "commenting out" code mean?

        [x] Adding # in front of code lines to temporarily stop them from executing | Correct! Allows developers to disable code without deleting it.
        [ ] Deleting code permanently from a script file | Incorrect. Commented code remains in the file.
        [ ] Converting Python code into HTML | Incorrect. Has nothing to do with file format conversion.
        [ ] Encrypting code for security | Incorrect. Commenting out merely disables execution.


    .. multichoice::

        What is considered a best practice when writing comments?

        [x] Explain why the logic exists rather than stating obvious code actions | Correct! Focus comments on reasoning and intent.
        [ ] Comment on every single line of code regardless of simplicity | Incorrect. Over-commenting clutter code unnecessarily.
        [ ] Leave outdated comments when you update code logic | Incorrect. Outdated comments mislead readers.
        [ ] Write comments in all capital letters | Incorrect. Standard text casing is preferred.


    .. multichoice::

        Why might a developer "comment out" a line of code during testing?

        [x] To test how the script runs without executing that specific line | Correct! Helps isolate bugs without losing code.
        [ ] To make that line run faster | Incorrect. Commented code does not execute at all.
        [ ] To make the output print in green | Incorrect. Comments do not affect terminal output styling.
        [ ] To share the code on social media | Incorrect. Commenting out is an isolation debugging technique.


    .. multichoice::

        Which comment example follows BEST practice guidelines?

        [x] # Apply 10% discount for gold membership status | Correct! Explains business rule logic behind calculation.
        [ ] # Multiply price by 0.90 | Incorrect. Merely repeats what math operator does.
        [ ] # This is a line of Python code | Incorrect. Provides zero context or value.
        [ ] # print statement below | Incorrect. States the obvious code component.


    .. multichoice::

        What problem occurs when code is updated but associated comments are NOT updated?

        [x] The comments become misleading and create confusion for developers | Correct! Inaccurate comments hinder debugging and code maintenance.
        [ ] Python throws a SyntaxError during execution | Incorrect. Python ignores comment text regardless of accuracy.
        [ ] The program automatically deletes the file | Incorrect. Python performs no automated file deletion.
        [ ] The output becomes corrupted | Incorrect. Comments are ignored at runtime.


    .. multichoice::

        How can you reduce the need for excessive comments in your code?

        [x] Use descriptive, self-explanatory variable and function names | Correct! Clear naming makes code self-documenting.
        [ ] Use single-letter variable names everywhere | Incorrect. Cryptic variable names increase comment requirements.
        [ ] Remove all whitespace from your script | Incorrect. Eliminating whitespace harms readability.
        [ ] Put all code on a single line | Incorrect. Single-line clutter makes code unreadable.


    .. multichoice::

        Given the following code block, which line is currently disabled?

        | ``x = 5``
        | ``# x = x + 10``
        | ``print(x)``

        [x] x = x + 10 | Correct! The hash prefix disables execution of x = x + 10.
        [ ] x = 5 | Incorrect. Standard active assignment line.
        [ ] print(x) | Incorrect. Active print statement line.
        [ ] None of the lines | Incorrect. Line 2 is commented out.


    .. multichoice::

        When should you delete commented-out code rather than keeping it?

        [x] When the feature is fully completed and code is ready for final release | Correct! Clean up leftover temporary debug code before production.
        [ ] Before saving the file for the first time | Incorrect. Useful during active development.
        [ ] Never; keep all commented code forever | Incorrect. Dead code clutters repository files.
        [ ] Deleting code is prohibited in Python | Incorrect. Developers routinely delete dead code.


    .. multichoice::

        What is the effect of having too many obvious comments in a program?

        [x] It clutters the file and makes code harder to read | Correct! Excessive clutter reduces readability.
        [ ] It makes the program run significantly slower | Incorrect. Comments are ignored and do not slow runtime speed.
        [ ] It increases file sizes by gigabytes | Incorrect. Comments add negligible text bytes.
        [ ] It causes function names to change | Incorrect. Comments do not alter variable or function names.


    .. multichoice::

        Which technique allows developers to quickly enable or disable lines of code in modern code editors?

        [x] Using keyboard shortcuts to toggle comment tags (#) | Correct! Editors provide quick shortcuts (e.g., Ctrl+/ or Cmd+/) to toggle comments.
        [ ] Changing file extensions | Incorrect. File extensions do not toggle code lines.
        [ ] Re-installing Python | Incorrect. Comment toggles are standard editor actions.
        [ ] Compiling code to binary | Incorrect. Commenting is handled within source editors.


