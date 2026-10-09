==================================
Python Strings
==================================

| In Python, a **string** is a sequence of characters used to store and manipulate text.
| Text values are enclosed inside single quotes (``'...'``) or double quotes (``"..."``).
| Strings are fundamental in Python programs for handling user input, displaying output messages, and processing text data.

.. code-block:: python

    # Defining string variables
    greeting = "Hello, World!"
    name = 'Alex'

    print(greeting)
    print("Welcome,", name)

    # Checking data type
    print(type(greeting))  # Output: <class 'str'>

----

Basic String Operations and Indexing (concatenation, len, indexing, slicing)
=============================================================================

Python provides built-in tools and syntax for measuring, combining, and extracting parts of strings:

- **String Length (len)**: The ``len()`` function returns the total count of characters in a string, including spaces and punctuation.
- **Concatenation (+)**: The ``+`` operator joins two or more strings together into a single string.
- **String Indexing ([ ])**: Individual characters are accessed using zero-based index numbers in square brackets (e.g., ``text[0]`` gets the first character).
- **String Slicing ([start:stop])**: Extracts a substring from the ``start`` index up to, but **not including**, the ``stop`` index.
- **Negative Indexing**: Using negative numbers accesses characters counting from the right end of the string (e.g., ``text[-1]`` gets the last character).

.. code-block:: python

    message = "Python"

    # Measuring length
    print(len(message))  # Output: 6

    # Indexing
    print(message[0])   # Output: 'P' (first character)
    print(message[-1])  # Output: 'n' (last character)

    # Slicing
    print(message[0:2]) # Output: 'Py'
    print(message[2:])  # Output: 'thon'

    # Concatenation
    full_text = message + " Programming"
    print(full_text)    # Output: 'Python Programming'

Quiz: Basic String Operations and Indexing
------------------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Python string indices start at @@0@@ for the first character.
    2. To get the total number of characters in a string, use the @@len()@@ function.
    3. Combining two strings together using the `+` operator is called @@concatenation@@.
    4. To access the last character of a string using negative indexing, use index @@-1@@.
    5. In string slicing `text[1:4]`, character at index position @@4@@ is excluded.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Concatenate a first name and last name with a space in between.

.. ordering::

    first_name = "Sarah"
    last_name = "Connor"
    full_name = first_name + " " + last_name
    print(full_name)

----

**Example 2:** Extract the first three characters of a string using slicing.

.. ordering::

    word = "Computer"
    prefix = word[0:3]
    print(prefix)

----

**Example 3:** Find and print the last character of a user-entered word.

.. ordering::

    user_word = "Python"
    last_char = user_word[-1]
    print(last_char)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What index position represents the first character in a Python string?

        [x] 0 | Correct! Python uses zero-based indexing, so the first character is at index 0.
        [ ] 1 | Incorrect. Indexing begins at 0, not 1.
        [ ] -1 | Incorrect. -1 represents the last character from the right.
        [ ] First | Incorrect. Integer indices are used.


    .. multichoice::

        What is the result of ``len("Hello World")``?

        [x] 11 | Correct! len counts all 10 letters plus the 1 space character (total 11).
        [ ] 10 | Incorrect. The space character between words is included in length.
        [ ] 12 | Incorrect. Count total letters plus space.
        [ ] 2 | Incorrect. Returns total character count, not word count.


    .. multichoice::

        Given ``text = "Coding"``, what does ``text[1:4]`` evaluate to?

        [x] "odi" | Correct! Includes index 1 ('o'), 2 ('d'), and 3 ('i'), excluding index 4.
        [ ] "Codi" | Incorrect. Index 0 ('C') is excluded because slicing starts at index 1.
        [ ] "odin" | Incorrect. Index 4 ('n') is excluded from the slice result.
        [ ] "od" | Incorrect. Includes indices 1, 2, and 3.


    .. multichoice::

        What operator is used to concatenate strings in Python?

        [x] "+" | Correct! The + operator joins strings end-to-end.
        [ ] "*" | Incorrect. The * operator repeats strings.
        [ ] "&"| Incorrect. & is a bitwise operator.
        [ ] "." | Incorrect. Dot operator is used for methods/attributes.


    .. multichoice::

        What character is returned by ``"Python"[-1]``?

        [x] "n" | Correct! Negative index -1 references the last character.
        [ ] "P" | Incorrect. "P" is at index 0.
        [ ] "o" | Incorrect. "o" is at index -2.
        [ ] Error | Incorrect. Negative indices are valid.


    .. multichoice::

        What happens when you execute ``"Py" * 3``?

        [x] "PyPyPy" | Correct! Multiplying a string by an integer repeats it that many times.
        [ ] "Py3" | Incorrect. * repeats the text sequence.
        [ ] TypeError | Incorrect. String repetition with integers is valid.
        [ ] "Py Py Py" | Incorrect. No extra spaces are inserted automatically.


    .. multichoice::

        Which expression gets characters from index 3 up to the very end of ``word = "Elephant"``?

        [x] word[3:] | Correct! Omitting the stop index slices through to the end of the string.
        [ ] word[:3] | Incorrect. Slices from start up to index 3.
        [ ] word[3] | Incorrect. Retrieves single character at index 3.
        [ ] word[3:-1] | Incorrect. Excludes the final character.


    .. multichoice::

        Are Python strings mutable (can you change a character directly like ``text[0] = 'A'``)?

        [x] No, strings are immutable and cannot be modified in-place | Correct! Attempting to reassign individual characters raises a TypeError.
        [ ] Yes, characters can be changed directly | Incorrect. Strings are immutable data structures.
        [ ] Yes, but only if using double quotes | Incorrect. Quote style does not alter immutability.
        [ ] No, unless wrapped in a list | Incorrect. Strings themselves remain immutable.


    .. multichoice::

        What output is produced by ``"Cat" + "Dog"``?

        [x] "CatDog" | Correct! Concatenates both strings without adding spaces.
        [ ] "Cat Dog" | Incorrect. No space is added unless explicitly included in string literals.
        [ ] "Cat+Dog" | Incorrect. Combines string contents directly.
        [ ] TypeError | Incorrect. Joining two strings with + is valid.


    .. multichoice::

        What does ``"Code"[:]`` return?

        [x] "Code" | Correct! Omitting both start and stop slices creates a full copy of the string.
        [ ] "" | Incorrect. Returns entire original text content.
        [ ] "C" | Incorrect. Full text slice is returned.
        [ ] Error | Incorrect. Valid slice syntax.

----

String Methods and Formatting (upper, lower, strip, replace, f-strings)
========================================================================

Python includes powerful built-in methods to transform text and format dynamic variables:

- **Case Conversion**: Methods ``.upper()`` and ``.lower()`` convert text entirely to uppercase or lowercase.
- **Trimming Whitespace**: The ``.strip()`` method removes leading and trailing spaces from a string.
- **Replacing Substrings**: The ``.replace(old, new)`` method substitutes occurrences of a substring with new text.
- **Formatted String Literals (f-strings)**: Prefixing a string with ``f"..."`` allows inserting variables directly inside curly braces ``{variable}``.

.. code-block:: python

    raw_text = "   python programming   "

    # Cleaning and case transformation
    clean_text = raw_text.strip().upper()
    print(clean_text)  # Output: 'PYTHON PROGRAMMING'

    # Replacing text
    sentence = "I like apples"
    new_sentence = sentence.replace("apples", "oranges")
    print(new_sentence)  # Output: 'I like oranges'

    # f-string formatting
    name = "Jordan"
    score = 95
    print(f"Student {name} scored {score} points.")

Quiz: String Methods and Formatting
-----------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. To convert all characters in a string to lowercase, use the @@.lower()@@ method.
    2. To remove extra spaces from both ends of a string, use the @@.strip()@@ method.
    3. To substitute parts of a string with new text, use the @@.replace()@@ method.
    4. Formatted string literals begin with the letter @@f@@ placed before the opening quote.
    5. Inside an f-string, variable names are placed inside @@curly braces@@ `{}`.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Clean user input by removing spaces and converting to lowercase.

.. ordering::

    user_input = "  YES  "
    cleaned = user_input.strip()
    result = cleaned.lower()

----

**Example 2:** Construct an f-string combining text and numeric variables.

.. ordering::

    item = "Book"
    price = 12
    msg = f"The {item} costs ${price}."

----

**Example 3:** Replace spaces in a phrase with hyphens.

.. ordering::

    title = "python lesson plan"
    slug = title.replace(" ", "-")
    print(slug)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        Which string method converts every letter in a string to uppercase?

        [x] .upper() | Correct! .upper() returns a copy of the string in all capital letters.
        [ ] .to_upper() | Incorrect. Method name is .upper().
        [ ] .capitalize() | Incorrect. .capitalize() only capitalizes the first character.
        [ ] .uppercase() | Incorrect. Method name is .upper().


    .. multichoice::

        What is the effect of ``"  hello  ".strip()``?

        [x] "hello" | Correct! Removes spaces from both leading and trailing edges.
        [ ] "hello  " | Incorrect. Removes whitespace from both ends.
        [ ] "  hello" | Incorrect. Removes whitespace from both ends.
        [ ] "h e l l o" | Incorrect. Only affects leading and trailing spaces.


    .. multichoice::

        Which string method is used to swap specific characters or words with new ones?

        [x] .replace() | Correct! .replace(old, new) substitutes matching substrings.
        [ ] .swap() | Incorrect. Correct method name is .replace().
        [ ] .change() | Incorrect. Correct method name is .replace().
        [ ] .substitute() | Incorrect. Correct method name is .replace().


    .. multichoice::

        What prefix letter identifies a formatted string literal in Python?

        [x] f | Correct! Placing 'f' before opening quotes turns a string into an f-string.
        [ ] s | Incorrect. Prefix 'f' is required.
        [ ] v | Incorrect. Prefix 'f' is required.
        [ ] str | Incorrect. Use lowercase 'f' prefix.


    .. multichoice::

        Given ``age = 14``, which syntax correctly formats the string using an f-string?

        [x] f"I am {age} years old" | Correct! Uses f prefix and curly braces around variables.
        [ ] "I am {age} years old" | Incorrect. Missing leading 'f' prefix.
        [ ] f"I am $age years old" | Incorrect. Variables must be enclosed in curly braces {}.
        [ ] str("I am" + age + "years old") | Incorrect. Raises TypeError combining string and int.


    .. multichoice::

        What does ``"python".capitalize()`` do?

        [x] Capitalizes the first letter, returning "Python" | Correct! .capitalize() capitalizes initial letter only.
        [ ] Capitalizes all letters, returning "PYTHON" | Incorrect. All caps requires .upper().
        [ ] Returns True if capitalized | Incorrect. Returns transformed string copy.
        [ ] Reverses character order | Incorrect. Capitalizes first character.


    .. multichoice::

        What is displayed by ``print("abc".upper())``?

        [x] "ABC" | Correct! Converts all lowercase characters to uppercase.
        [ ] "abc" | Incorrect. Transformed string is printed.
        [ ] "Abc" | Incorrect. .upper() converts all characters to uppercase.
        [ ] None | Incorrect. Method returns transformed string value.


    .. multichoice::

        Which method checks if a string contains only numeric digits?

        [x] .isdigit() | Correct! Returns True if all characters in string are digits.
        [ ] .isnumber() | Incorrect. Method name is .isdigit() or .isnumeric().
        [ ] .check_int() | Incorrect. Method name is .isdigit().
        [ ] .has_digits() | Incorrect. Method name is .isdigit().


    .. multichoice::

        How do string methods like ``.lower()`` affect the original variable content?

        [x] They return a new modified string without changing the original variable | Correct! Strings are immutable, so methods return new string objects.
        [ ] They permanently overwrite original variable data | Incorrect. Original variable remains unchanged unless reassigned.
        [ ] They cause a SyntaxError | Incorrect. Method execution is valid.
        [ ] They delete original variable | Incorrect. Returns new modified value.


    .. multichoice::

        What string method splits a single string into a list of words using space separators?

        [x] .split() | Correct! .split() divides strings by delimiters into list items.
        [ ] .divide() | Incorrect. Method name is .split().
        [ ] .cut() | Incorrect. Method name is .split().
        [ ] .separate() | Incorrect. Method name is .split().

