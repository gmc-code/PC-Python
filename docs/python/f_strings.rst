===========================
f-strings
===========================

| In Python, **f-strings** (formatted string literals) provide a clean, fast, and readable way to embed variables and expressions inside string literals.
| Introduced in Python 3.6, f-strings are created by placing the letter ``f`` or ``F`` directly before the opening quotation mark of a string.
| Inside an f-string, Python evaluates any expression wrapped inside **curly braces** ``{}`` and automatically converts the result to a string.

.. code-block:: python

    name = "Alex"
    age = 13

    # Using an f-string to combine text and variables
    greeting = f"Hello, my name is {name} and I am {age} years old."
    print(greeting)  # Output: Hello, my name is Alex and I am 13 years old.

----

Basic f-string Formatting
=========================

Basic f-strings allow you to insert variable values directly into text without using string concatenation:

- **The Prefix**: Place ``f`` or ``F`` before the opening single, double, or triple quotes.
- **Curly Braces ({})**: Enclose variable names inside ``{}`` to insert their stored values.
- **Automatic Conversion**: Python automatically converts non-string data types (like integers, floats, and Booleans) into strings inside ``{}``.
- **Readability**: f-strings eliminate the need for cluttering code with multiple plus operators (``+``) and manual ``str()`` conversions.

.. code-block:: python

    score = 95
    player = "Jordan"

    # Old concatenation method
    text1 = "Player " + player + " scored " + str(score) + " points."

    # Modern f-string method
    text2 = f"Player {player} scored {score} points."

Quiz: Basic f-string Formatting
-------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. To create an f-string in Python, prefix the string with the letter @@f@@.
    2. Place variable names inside @@curly braces@@ to embed them in an f-string.
    3. f-strings automatically @@convert@@ integers and floats to string format.
    4. Compared to using the `+` operator, f-strings improve code @@readability@@.
    5. In `f"Value: {x}"`, Python evaluates `{x}` and replaces it with the value of @@x@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Create an f-string to display a person's name and favorite color.

.. ordering::

    name = "Taylor"
    color = "blue"
    msg = f"{name}'s favorite color is {color}."
    print(msg)

----

**Example 2:** Display a game inventory item and its quantity.

.. ordering::

    item = "Potions"
    count = 5
    status = f"Inventory: {count} {item}"
    print(status)

----

**Example 3:** Construct a welcome banner for a school house team.

.. ordering::

    house = "Red Dragon"
    points = 120
    banner = f"Welcome {house}! Current Points: {points}"
    print(banner)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        How do you mark a string literal as an f-string in Python?

        [x] Place f or F immediately before the opening quotation mark | Correct! Prefixing the string with f tells Python to process curly braces as formatting expressions.
        [ ] Place f at the end of the string | Incorrect. The f prefix must go before the opening quote.
        [ ] Enclose the entire string in f-quotes f"..."f | Incorrect. The f is only written as a prefix before the opening quote.
        [ ] Use the format() keyword inside the string | Incorrect. .format() is an older method; f-strings use the f prefix.


    .. multichoice::

        Given ``x = 10``, what does ``f"x is {x}"`` evaluate to?

        [x] "x is 10" | Correct! {x} is evaluated and replaced by the value 10.
        [ ] "x is {10}" | Incorrect. The curly braces are evaluated and removed from output.
        [ ] "x is x" | Incorrect. Variable x is evaluated inside curly braces.
        [ ] "x is {x}" | Incorrect. Without forgetting the f prefix, braces trigger expression evaluation.


    .. multichoice::

        What happens if you omit the ``f`` prefix, writing ``"Hello {name}"`` when ``name = "Sam"``?

        [x] Python prints the literal text "Hello {name}" without replacing {name} | Correct! Without the f prefix, Python treats curly braces as literal text characters.
        [ ] Python raises a SyntaxError | Incorrect. Standard string literals can contain literal braces.
        [ ] Python automatically converts it to an f-string | Incorrect. Explicit prefix f is required for string interpolation.
        [ ] Python raises a NameError | Incorrect. {name} is not evaluated as a variable without the f prefix.


    .. multichoice::

        Which pair of characters is used to enclose embedded variables inside an f-string?

        [x] Curly braces {} | Correct! Curly braces enclose expressions to evaluate within f-strings.
        [ ] Square brackets [] | Incorrect. Square brackets are used for indexing and list literals.
        [ ] Parentheses () | Incorrect. Parentheses are used for function calls and tuple literals.
        [ ] Angle brackets <> | Incorrect. Angle brackets are comparison operators.


    .. multichoice::

        Given ``a = 5`` and ``b = "apples"``, which f-string is written correctly?

        [x] f"I have {a} {b}." | Correct! Places f prefix before quotes and wraps variables in curly braces.
        [ ] "I have {a} {b}."f | Incorrect. Prefix f must precede opening quotation mark.
        [ ] f"I have a b." | Incorrect. Variables must be enclosed inside {} to evaluate.
        [ ] {f}"I have a b." | Incorrect. Syntax is invalid.


    .. multichoice::

        What is the primary advantage of f-strings over string concatenation with ``+``?

        [x] f-strings are clearer to read and avoid manual str() conversion | Correct! f-strings clean up string construction syntax.
        [ ] f-strings automatically save output to a file | Incorrect. Printing or file saving requires separate operations.
        [ ] f-strings only work inside while loops | Incorrect. f-strings work anywhere in Python scripts.
        [ ] f-strings encrypt string data | Incorrect. f-strings perform standard string formatting.


    .. multichoice::

        Given ``city = "Melbourne"``, what is output by ``print(f"Welcome to {city}!")``?

        [x] Welcome to Melbourne! | Correct! {city} is replaced by "Melbourne".
        [ ] Welcome to city! | Incorrect. Braces trigger variable evaluation.
        [ ] Welcome to {Melbourne}! | Incorrect. Braces are replaced during evaluation.
        [ ] SyntaxError | Incorrect. Valid f-string statement.


    .. multichoice::

        Can you embed integer variables directly inside f-strings without using ``str()``?

        [x] Yes, f-strings automatically convert non-string variables into string representations | Correct! Implicit conversion happens inside {}.
        [ ] No, integers must be wrapped as str(num) inside curly braces | Incorrect. Manual type conversion is unnecessary inside f-strings.
        [ ] Yes, but only for positive integers | Incorrect. Works for all numbers and data types.
        [ ] No, f-strings only accept string variables | Incorrect. f-strings accept any printable Python object.


    .. multichoice::

        What will ``f"{'A'}{'B'}"`` evaluate to?

        [x] "AB" | Correct! Evaluates 'A' and 'B' sequentially and combines them into "AB".
        [ ] "{A}{B}" | Incorrect. Expressions inside braces are evaluated.
        [ ] "A B" | Incorrect. No space character was specified between braces.
        [ ] TypeError | Incorrect. String literals inside f-string braces evaluate correctly.


    .. multichoice::

        What is output by ``val = True; print(f"Status: {val}")``?

        [x] Status: True | Correct! Boolean True is converted to string "True".
        [ ] Status: val | Incorrect. {val} evaluates variable contents.
        [ ] Status: {True} | Incorrect. Braces are evaluated and replaced.
        [ ] TypeError | Incorrect. Booleans format cleanly in f-strings.

----

Expressions inside f-strings
============================

f-strings do not just hold variable names; you can put full **Python expressions** directly inside the curly braces ``{}``:

- **Arithmetic Calculations**: Perform calculations directly inside ``{}`` (e.g., ``f"{2 + 2}"``).
- **String Methods**: Call built-in string methods on variables inside ``{}`` (e.g., ``f"{name.upper()}"``).
- **Function Calls**: Call custom or built-in functions inside ``{}`` to insert returned values.
- **Inline Logic**: Evaluate Boolean expressions or conditional ternary operators inside curly braces.

.. code-block:: python

    price = 10
    quantity = 3
    name = "alice"

    # Math expression inside f-string
    print(f"Total: ${price * quantity}")  # Output: Total: $30

    # Calling a string method
    print(f"Hello, {name.capitalize()}!")  # Output: Hello, Alice!

Quiz: Expressions inside f-strings
----------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Python evaluates any valid Python @@expression@@ placed inside f-string curly braces.
    2. The f-string `f"{5 * 2}"` evaluates to the string @@"10"@@.
    3. To convert a variable `text` to @@uppercase@@ inside an f-string, write `{text.upper()}`.
    4. You can call custom @@functions@@ directly inside f-string curly braces.
    5. Evaluating `f"{len('cat')}"` outputs @@3@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Evaluate a math multiplication expression inside an f-string.

.. ordering::

    width = 5
    height = 4
    info = f"Area: {width * height} sq units"
    print(info)

----

**Example 2:** Format a user name using the `.upper()` method inside an f-string.

.. ordering::

    user = "charlie"
    greeting = f"WELCOME {user.upper()}!"
    print(greeting)

----

**Example 3:** Call a custom function inside an f-string expression.

.. ordering::

    def double(n):
        return n * 2

    val = 6
    msg = f"Double of {val} is {double(val)}"
    print(msg)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What is the output of ``f"Result: {10 + 20}"``?

        [x] "Result: 30" | Correct! $10 + 20 = 30$ is calculated inside the braces.
        [ ] "Result: 10 + 20" | Incorrect. Expressions inside {} evaluate mathematically.
        [ ] "Result: {30}" | Incorrect. Braces are stripped during expression evaluation.
        [ ] SyntaxError | Incorrect. Math expressions are valid inside f-string braces.


    .. multichoice::

        Given ``word = "python"``, what does ``f"{word.upper()}"`` evaluate to?

        [x] "PYTHON" | Correct! The .upper() method runs on word inside the braces.
        [ ] "python" | Incorrect. Method execution transforms string casing.
        [ ] "word.upper()" | Incorrect. Python executes the method call.
        [ ] SyntaxError | Incorrect. String methods execute cleanly inside f-strings.


    .. multichoice::

        What is the result of ``f"Length: {len('hello')}"``?

        [x] "Length: 5" | Correct! len('hello') returns 5, which is embedded into the string.
        [ ] "Length: len('hello')" | Incorrect. Function calls inside {} are evaluated.
        [ ] "Length: 6" | Incorrect. 'hello' contains 5 letters.
        [ ] TypeError | Incorrect. Built-in function calls are allowed inside f-strings.


    .. multichoice::

        Given ``x = 7``, what is printed by ``print(f"Is even: {x % 2 == 0}")``?

        [x] Is even: False | Correct! 7 % 2 == 0 evaluates to Boolean False.
        [ ] Is even: True | Incorrect. 7 is an odd number.
        [ ] Is even: 7 % 2 == 0 | Incorrect. Comparison expression is evaluated.
        [ ] SyntaxError | Incorrect. Comparison logic evaluates inside braces.


    .. multichoice::

        Can you call user-defined functions inside f-string curly braces?

        [x] Yes, any valid function call can be evaluated inside curly braces | Correct! Python executes functions and inserts returned values.
        [ ] No, only built-in functions can be called | Incorrect. User-defined functions work identically.
        [ ] Yes, but only if the function returns an integer | Incorrect. Functions returning any printable data type work.
        [ ] No, functions must be called outside f-strings | Incorrect. Embedding function calls directly is fully supported.


    .. multichoice::

        What is the value of ``f"{3 ** 2}"``?

        [x] "9" | Correct! $3^2 = 9$.
        [ ] "6" | Incorrect. ** is exponentiation, not $3 \times 2$.
        [ ] "3 ** 2" | Incorrect. Math operator evaluates inside braces.
        [ ] "{9}" | Incorrect. Braces are consumed during evaluation.


    .. multichoice::

        Given ``items = ["apple", "banana"]``, what does ``f"First: {items[0]}"`` output?

        [x] "First: apple" | Correct! List indexing items[0] evaluates to "apple".
        [ ] "First: ['apple', 'banana']" | Incorrect. Index [0] selects the first element.
        [ ] "First: banana" | Incorrect. "banana" is at index [1].
        [ ] SyntaxError | Incorrect. Container indexing works inside f-string braces.


    .. multichoice::

        What will ``f"{'hello'.capitalize()}"`` output?

        [x] "Hello" | Correct! .capitalize() turns the first letter to uppercase.
        [ ] "HELLO" | Incorrect. That would be produced by .upper().
        [ ] "hello" | Incorrect. Method alters string casing.
        [ ] TypeError | Incorrect. String method call is valid.


    .. multichoice::

        What is the result of ``f"{10 > 5}"``?

        [x] "True" | Correct! Relational expression 10 > 5 evaluates to Boolean True.
        [ ] "False" | Incorrect. 10 is strictly greater than 5.
        [ ] "10 > 5" | Incorrect. Relational operator evaluates inside braces.
        [ ] SyntaxError | Incorrect. Logical comparisons are valid expressions.


    .. multichoice::

        Given ``score = 80``, what does ``f"Status: {'Pass' if score >= 50 else 'Fail'}"`` produce?

        [x] "Status: Pass" | Correct! Ternary conditional expression evaluates to 'Pass' because 80 >= 50.
        [ ] "Status: Fail" | Incorrect. score is 80, satisfying >= 50.
        [ ] "Status: Pass if score >= 50 else Fail" | Incorrect. Conditional expression is evaluated.
        [ ] SyntaxError | Incorrect. Ternary expressions are valid inside f-strings.

----

Format Specifiers (Numbers and Alignment)
=========================================

f-strings allow you to control how values are displayed using a **colon ``:``** followed by a format specifier:

- **Rounding Decimals (``.2f``)**: Round floating-point numbers to a specific number of decimal places (e.g., ``{pi:.2f}``).
- **Padding and Alignment**: Align text left (``<``), right (``>``), or center (``^``) within a fixed width (e.g., ``{text:>10}``).
- **Thousands Separators**: Insert commas into large numbers automatically using ``,`` (e.g., ``{1000000:,}``).
- **Percentage Formatting**: Format decimals as percentages using ``%`` (e.g., ``{0.75:.0%}`` displays ``75%``).

.. code-block:: python

    pi = 3.14159265
    money = 1250000

    # Decimal rounding
    print(f"Pi: {pi:.2f}")  # Output: Pi: 3.14

    # Thousands comma separator
    print(f"Total: ${money:,}")  # Output: Total: $1,250,000

    # Column alignment (width 10, right aligned)
    print(f"{'Score':>10}")  # Output: '     Score'

Quiz: Format Specifiers
-----------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. In f-strings, format @@specifiers@@ are separated from the expression using a colon.
    2. The format specifier :.2f @@rounds@@ a floating-point number to 2 decimal places.
    3. To add @@commas@@ as thousands separators in large numbers, use the , specifier.
    4. The alignment character > @@aligns@@ text to the right within a specified field width.
    5. Formatting 0.5 with {0.5:.0%} @@outputs@@ 50%.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Format a float number to 2 decimal places as currency.

.. ordering::

    price = 19.9934
    formatted_price = f"Price: ${price:.2f}"
    print(formatted_price)

----

**Example 2:** Format a large population figure with comma thousands separators.

.. ordering::

    pop = 8400000
    display_pop = f"Population: {pop:,}"
    print(display_pop)

----

**Example 3:** Center-align a title header within a 20-character padded field.

.. ordering::

    title = "MENU"
    header = f"{title:^20}"
    print(header)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Which format specifier rounds a floating-point number to exactly two decimal places?

        [x] :.2f | Correct! .2 specifies two decimal digits and f indicates fixed-point notation.
        [ ] :2d | Incorrect. d formats integers, not fixed-point floats.
        [ ] :2p | Incorrect. p is not standard fixed-point decimal notation.
        [ ] :round2 | Incorrect. Use :.2f for decimal precision rounding.


    .. multichoice::

        What does ``f"{1000000:,}"`` evaluate to?

        [x] "1,000,000" | Correct! The comma specifier adds thousands separators.
        [ ] "1000000" | Incorrect. Comma specifier formats output with commas.
        [ ] "1.000.000" | Incorrect. Comma specifier uses commas, not periods.
        [ ] SyntaxError | Incorrect. Comma thousands specifier is valid syntax.


    .. multichoice::

        What character separates the variable/expression from its format specifier inside curly braces?

        [x] Colon (:) | Correct! Colon separates expression from format specification instructions.
        [ ] Semicolon (;) | Incorrect. Semicolons are not formatting separators.
        [ ] Pipe (|) | Incorrect. Pipe is not used for f-string formatting.
        [ ] Equals (=) | Incorrect. Equals sign triggers self-documenting print mode.


    .. multichoice::

        Given ``val = 0.85``, what does ``f"{val:.0%}"`` produce?

        [x] "85%" | Correct! % multiplies by 100 and adds %, while .0 sets zero decimal places.
        [ ] "0.85%" | Incorrect. % specifier multiplies values by 100.
        [ ] "85.0%" | Incorrect. .0 suppresses decimal digits.
        [ ] "85" | Incorrect. % specifier appends percent sign.


    .. multichoice::

        What is output by ``f"{'Hi':>5}"``?

        [x] "   Hi" | Correct! Right-aligns "Hi" in a field of width 5 (adds 3 leading spaces).
        [ ] "Hi   " | Incorrect. < left-aligns text.
        [ ] " Hi " | Incorrect. ^ center-aligns text.
        [ ] "Hi" | Incorrect. Width 5 reserves 5 total character spaces.


    .. multichoice::

        Given ``num = 3.14159``, what is the output of ``f"{num:.1f}"``?

        [x] "3.1" | Correct! Rounds fixed-point float to 1 decimal place.
        [ ] "3.14" | Incorrect. .1f restricts precision to one decimal place.
        [ ] "3" | Incorrect. .1f retains one decimal digit.
        [ ] "3.14159" | Incorrect. Format specifier restricts decimal places.


    .. multichoice::

        Which specifier center-aligns text within a field width of 10?

        [x] :^10 | Correct! ^ symbol requests center alignment.
        [ ] :<10 | Incorrect. < symbol requests left alignment.
        [ ] :>10 | Incorrect. > symbol requests right alignment.
        [ ] :=10 | Incorrect. = symbol is used for sign padding.


    .. multichoice::

        What is output by ``f"{25:05d}"``?

        [x] "00025" | Correct! Specifies integer field width of 5 padded with leading zeros.
        [ ] "25000" | Incorrect. Zero padding occurs on the left side.
        [ ] "25" | Incorrect. Field width 5 fills leading spaces with zeros.
        [ ] "00025.0" | Incorrect. d specifier formats integers without decimals.


    .. multichoice::

        What does ``f"{0.1234:.2%}"`` evaluate to?

        [x] "12.34%" | Correct! Multiplies by 100 and retains 2 decimal places with % sign.
        [ ] "12%" | Incorrect. .2% retains two decimal places.
        [ ] "0.12%" | Incorrect. % multiplies base value by 100.
        [ ] "12.34" | Incorrect. % specifier includes percent symbol.


    .. multichoice::

        What does the specifier ``:<10`` do to string text?

        [x] Left-aligns text within a 10-character wide field | Correct! < specifies left alignment.
        [ ] Right-aligns text within a 10-character wide field | Incorrect. > specifies right alignment.
        [ ] Truncates text to under 10 characters | Incorrect. Alignment pads extra space rather than truncating.
        [ ] Centers text within 10 characters | Incorrect. ^ specifies center alignment.

----

Self-Documenting f-strings (The = Operator)
===========================================

Introduced in Python 3.8, adding an **equals sign ``=``** after an expression inside curly braces creates a self-documenting expression:

- **Debugging Convenience**: Prints both the literal expression text and its evaluated result.
- **Syntax**: Write ``{expression=}`` inside curly braces.
- **Whitespace Preservation**: Preserves spaces around the ``=`` sign for custom formatting.
- **Combining Specifiers**: Can be combined with format specifiers (e.g., ``{x=:.2f}``).

.. code-block:: python

    x = 10
    y = 25

    # Without = operator
    print(f"x = {x}, y = {y}")  # Output: x = 10, y = 25

    # With self-documenting = operator
    print(f"{x=}, {y=}")         # Output: x=10, y=25

    # Complex expression debugging
    print(f"{x + y=}")          # Output: x + y=35

Quiz: Self-Documenting f-strings
--------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Adding an = sign after an expression creates a self-documenting @@f-string@@.
    2. Self-documenting f-strings print both the expression text and its @@result@@.
    3. The self-documenting `=` feature was introduced in Python @@3.8@@.
    4. The f-string `f"{a=}"` when `a = 5` evaluates to the string `"@@a=5@@"`.
    5. Self-documenting f-strings are useful for code @@debugging@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Print a variable name and value using the self-documenting equals operator.

.. ordering::

    score = 100
    debug_msg = f"{score=}"
    print(debug_msg)

----

**Example 2:** Print a mathematical calculation expression and its result automatically.

.. ordering::

    length = 8
    width = 3
    print(f"{length * width=}")

----

**Example 3:** Combine self-documenting debugging with decimal format specifiers.

.. ordering::

    val = 12.3456
    print(f"{val=:.2f}")

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What output is produced by ``num = 42; print(f"{num=}")``?

        [x] num=42 | Correct! The = operator prints the expression text followed by = and its evaluated value.
        [ ] 42 | Incorrect. Without =, only the value 42 prints.
        [ ] num | Incorrect. Evaluates both expression name and value.
        [ ] "num=42" | Incorrect. Output displays without literal outer quotes.


    .. multichoice::

        Why do developers use the ``=`` specifier inside f-strings?

        [x] It simplifies debugging by automatically printing variable names alongside their values | Correct! Reduces boilerplate typing during debug logging.
        [ ] It converts variables into constant values | Incorrect. Does not affect variable mutability.
        [ ] It forces values to equal zero | Incorrect. Performs string formatting, not variable reassignment.
        [ ] It compares two variables for equality | Incorrect. == is the equality comparison operator.


    .. multichoice::

        Given ``a = 3`` and ``b = 4``, what does ``f"{a + b=}"`` evaluate to?

        [x] a + b=7 | Correct! Prints expression "a + b=" followed by result 7.
        [ ] 7 | Incorrect. Equals sign includes the expression string.
        [ ] a + b = 7 | Incorrect. Preserves exact spacing typed inside braces.
        [ ] "a + b=7" | Incorrect. Evaluated string content is a + b=7.


    .. multichoice::

        In which Python version was the self-documenting f-string ``{var=}`` feature introduced?

        [x] Python 3.8 | Correct! Feature added in Python 3.8.
        [ ] Python 2.7 | Incorrect. f-strings did not exist in Python 2.7.
        [ ] Python 3.6 | Incorrect. Python 3.6 introduced basic f-strings without = support.
        [ ] Python 3.12 | Incorrect. Feature predates 3.12.


    .. multichoice::

        What is output by ``x = 5; print(f"{x = }")``?

        [x] x = 5 | Correct! Spaces around = inside braces are preserved in output.
        [ ] x=5 | Incorrect. Spaces included before or after = are preserved.
        [ ] 5 | Incorrect. Includes expression label text.
        [ ] SyntaxError | Incorrect. Spaces around = operator are valid.


    .. multichoice::

        What is output by ``name = "Ada"; print(f"{name=}")``?

        [x] name='Ada' | Correct! String values inside self-documenting f-strings include representation quotes.
        [ ] name=Ada | Incorrect. String representations include quotes.
        [ ] Ada | Incorrect. = operator includes variable name.
        [ ] "name=Ada" | Incorrect. Outer quotes are not printed.


    .. multichoice::

        Given ``price = 19.99``, what does ``f"{price=:.1f}"`` output?

        [x] price=20.0 | Correct! Combines self-documenting text "price=" with rounded format specifier 20.0.
        [ ] price=19.99 | Incorrect. .1f rounds float to one decimal place.
        [ ] 20.0 | Incorrect. = operator includes variable name label.
        [ ] SyntaxError | Incorrect. Combining = and format specifiers is fully supported.


    .. multichoice::

        Given ``lst = [1, 2]``, what will ``f"{len(lst)=}"`` print?

        [x] len(lst)=2 | Correct! Prints expression len(lst)= followed by evaluated result 2.
        [ ] len(lst)=len(lst) | Incorrect. Result is evaluated to 2.
        [ ] 2 | Incorrect. Includes expression label text.
        [ ] [1, 2]=2 | Incorrect. Uses literal expression text len(lst).


    .. multichoice::

        What happens if you use ``==`` instead of ``=`` inside an f-string brace like ``f"{x==5}"``?

        [x] Python evaluates the equality test and prints True or False | Correct! == is comparison logic, returning a Boolean rather than self-documenting text.
        [ ] Python prints "x==5" | Incorrect. == acts as comparison operator inside brace expression.
        [ ] Python raises a SyntaxError | Incorrect. Equality tests are valid expressions.
        [ ] Python reassigns x to 5 | Incorrect. == tests equality; = assigns or formats.


    .. multichoice::

        What is the result of ``a = 10; b = 2; print(f"{a / b=}")``?

        [x] a / b=5.0 | Correct! Division / produces float 5.0 attached to label "a / b=".
        [ ] a / b=5 | Incorrect. Standard division returns float 5.0.
        [ ] 5.0 | Incorrect. = operator includes expression label text.
        [ ] SyntaxError | Incorrect. Valid self-documenting expression.

