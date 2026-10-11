====================================================
Dictionary with functions
====================================================

Dictionaries
-------------------

| A dictionary is a collection of ``key: value`` pairs.
| All keys are unique; duplicate keys are not possible.
| Keys can be an integer, float, string, Boolean (True or False) and even a tuple.
| A key can be used to retrieve a value from a dictionary.
| See: https://v2.scrimba.com/learn-python-c03/~014


Dictionary structure
-------------------------

| The dictionary uses {} brackets.
| Each key value pair is separated by a comma.
| Each key is followed by a colon :

| Below is a dictionary of car details.

.. code-block:: python

    car_dictionary = {"brand": "Ford", "model": "Mustang", "year": 1965}

| The first key value pair is "brand": "Ford".
| There are 3 keys: "brand", "model", "year".
| There are 3 corresponding values: "Ford", "Mustang", 1965.

----

Quiz: Dictionary Structure
--------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. A dictionary is a collection of key-value @@pairs@@.
    2. A dictionary is created using curly @@braces@@.
    3. Each key is separated from its value by a @@colon@@.
    4. Each key-value pair is separated from the next pair by a @@comma@@.
    5. Every key in a dictionary must be @@unique@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Create a car dictionary and print it.

.. ordering::

    car_dictionary = {"brand": "Ford", "model": "Mustang", "year": 1965}
    print(car_dictionary)

----

**Example 2:** Create a dictionary of pet ages, add a new pet, and print the dictionary.

.. ordering::

    pet_ages = {"Rex": 4, "Milo": 2}
    pet_ages["Bella"] = 7
    print(pet_ages)

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        How many keys are in ``car_dictionary = {"brand": "Ford", "model": "Mustang", "year": 1965}``?

        [ ] 1 | Incorrect. Each key-value pair has its own key.
        [ ] 2 | Incorrect. Count each pair separated by commas.
        [x] 3 | Correct! The keys are "brand", "model" and "year".
        [ ] 6 | Incorrect. len() counts pairs, not keys and values separately.


    .. multichoice::

        Which of the following CANNOT be used as a dictionary key?

        [ ] A string such as "brand" | Incorrect. Strings are the most common type of key.
        [ ] An integer such as 7 | Incorrect. Integers can be keys.
        [ ] A tuple such as (1, 2) | Incorrect. Tuples can be keys because they cannot be changed.
        [x] A list such as [1, 2] | Correct! Lists can be changed, so they cannot be used as keys.


    .. multichoice::

        What is the value paired with the key ``"model"`` in ``car_dictionary``?

        [ ] "Ford" | Incorrect. "Ford" is the value for "brand".
        [x] "Mustang" | Correct! "model": "Mustang" is the second key-value pair.
        [ ] 1965 | Incorrect. 1965 is the value for "year".
        [ ] "model" | Incorrect. "model" is the key, not the value.


    .. multichoice::

        What is stored in ``d`` after running ``d = {"a": 1, "a": 2}``?

        [ ] {"a": 1, "a": 2} | Incorrect. Duplicate keys are not possible.
        [ ] {"a": 1} | Incorrect. The later value overwrites the earlier one.
        [x] {"a": 2} | Correct! The second "a" overwrites the first.
        [ ] An error is raised | Incorrect. Python allows this but keeps only the last value.


    .. multichoice::

        Which line is a correctly written dictionary?

        [x] car = {"brand": "Ford", "year": 1965} | Correct! Curly braces, colons between keys and values, commas between pairs.
        [ ] car = {"brand" = "Ford", "year" = 1965} | Incorrect. Keys and values are separated by colons, not equals signs.
        [ ] car = ["brand": "Ford", "year": 1965] | Incorrect. Square brackets create lists.
        [ ] car = {"brand": "Ford" "year": 1965} | Incorrect. A comma is missing between the pairs.

----

Looking up dictionary values by key
--------------------------------------

.. py:function:: value = dictionary[key]

    | Get the value of a specific key in a dictionary.
    | Raises an **error** if the key doesn't exist, so a **try-except** block is needed.

Example:

.. code-block:: python

    car_dictionary = {"brand": "Ford", "model": "Mustang", "year": 1965}

    # key exists
    value = car_dictionary["brand"]
    print(value)

    # key doesn't exist
    try:
        value = car_dictionary["brands"]
        print(value)
    except KeyError:
        print("not a valid key")

----

Looking up dictionary values by the get method
----------------------------------------------------

.. py:method:: dict.get(key, default=None)

    Returns the value for the specified key if the key is in the dictionary, otherwise returns the default value.

Example:

.. code-block:: python

    car_dictionary = {"brand": "Ford", "model": "Mustang", "year": 1965}

    # without default
    value = car_dictionary.get("brand")
    print(value)
    # output is "Ford"

    # without default; returns None
    value = car_dictionary.get("brands")
    print(value)
    # output is None

    # with default
    value = car_dictionary.get("brands", "not a valid key")
    print(value)
    # output is "not a valid key"

----

Check if the key is in the dictionary
---------------------------------------

.. py:function:: key in dictionary

    | Returns **True** if the key is among the keys of the dictionary; **False** if not.

Example:

.. code-block:: python

    car_dictionary = {"brand": "Ford", "model": "Mustang", "year": 1965}

    # key exists
    key_exists = "model" in car_dictionary
    print(key_exists)

    # key doesn't exists
    key_exists = "models" in car_dictionary
    print(key_exists)

----

Quiz: Looking Up Values
-----------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. Looking up a missing key with square brackets raises a @@KeyError@@.
    2. To handle a missing key without the program crashing, wrap the lookup in a @@try@@-except block.
    3. The @@.get()@@ method returns a default value instead of raising an error when a key is missing.
    4. If no default is given, ``.get()`` returns @@None@@ for a missing key.
    5. The @@in@@ keyword returns True if a key is in the dictionary and False if it is not.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Look up a key that might not exist, using a try-except block.

.. ordering::

    car_dictionary = {"brand": "Ford", "model": "Mustang", "year": 1965}
    try:
        value = car_dictionary["colour"]
        print(value)
    except KeyError:
        print("not a valid key")

----

**Example 2:** Look up a key with ``.get()`` and a default value, then print the result.

.. ordering::

    car_dictionary = {"brand": "Ford", "model": "Mustang", "year": 1965}
    value = car_dictionary.get("colour", "not a valid key")
    print(value)

----

**Example 3:** Check whether a key exists before printing its value.

.. ordering::

    car_dictionary = {"brand": "Ford", "model": "Mustang", "year": 1965}
    if "year" in car_dictionary:
        print(car_dictionary["year"])

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        What does ``car_dictionary["year"]`` return?

        [x] 1965 | Correct! The value stored with the key "year" is 1965.
        [ ] "year" | Incorrect. Square brackets return the value, not the key.
        [ ] "Mustang" | Incorrect. "Mustang" is the value for "model".
        [ ] None | Incorrect. The key exists, so its value is returned.


    .. multichoice::

        What happens when you run ``car_dictionary["Brand"]``?

        [ ] It returns "Ford" | Incorrect. Keys are case-sensitive, so "Brand" is not the same as "brand".
        [x] Python raises a KeyError | Correct! "Brand" with a capital B is not a key in the dictionary.
        [ ] It returns None | Incorrect. Square brackets raise an error rather than returning None.
        [ ] It adds "Brand" to the dictionary | Incorrect. Looking up a key never adds it.


    .. multichoice::

        Which exception should the ``except`` line catch when looking up a missing key with square brackets?

        [ ] IndexError | Incorrect. IndexError is for list positions that are out of range.
        [ ] ValueError | Incorrect. ValueError is for values of the wrong kind, such as int("abc").
        [x] KeyError | Correct! A missing dictionary key raises a KeyError.
        [ ] NameError | Incorrect. NameError is for variables that have not been defined.


    .. multichoice::

        What does ``car_dictionary.get("colour")`` return?

        [ ] "colour" | Incorrect. .get() returns a value, not the key.
        [ ] An empty string "" | Incorrect. The default return value is None.
        [x] None | Correct! With no default given, .get() returns None for a missing key.
        [ ] Python raises a KeyError | Incorrect. .get() never raises a KeyError.


    .. multichoice::

        What does ``car_dictionary.get("colour", "unknown")`` return?

        [x] "unknown" | Correct! "colour" is missing, so the default value is returned.
        [ ] None | Incorrect. A default value was given, so it is returned instead of None.
        [ ] "colour" | Incorrect. .get() returns the default, not the key.
        [ ] Python raises a KeyError | Incorrect. .get() never raises a KeyError.


    .. multichoice::

        What does ``car_dictionary.get("brand", "unknown")`` return?

        [x] "Ford" | Correct! The key exists, so its real value is returned and the default is ignored.
        [ ] "unknown" | Incorrect. The default is only used when the key is missing.
        [ ] "brand" | Incorrect. .get() returns the value, not the key.
        [ ] None | Incorrect. The key exists.


    .. multichoice::

        What does ``"Ford" in car_dictionary`` evaluate to?

        [ ] True | Incorrect. The in keyword checks keys, and "Ford" is a value.
        [x] False | Correct! "Ford" is a value, not a key.
        [ ] "brand" | Incorrect. The in keyword returns True or False.
        [ ] Python raises a KeyError | Incorrect. The in keyword never raises a KeyError.


    .. multichoice::

        What does ``"year" in car_dictionary`` evaluate to?

        [x] True | Correct! "year" is one of the keys.
        [ ] False | Incorrect. "year" is a key in the dictionary.
        [ ] 1965 | Incorrect. The in keyword returns True or False, not the value.
        [ ] None | Incorrect. The in keyword returns True or False.


    .. multichoice::

        Why might you choose ``.get()`` instead of square brackets?

        [x] It avoids a KeyError when the key might be missing | Correct! .get() returns None or a default instead of crashing.
        [ ] It is the only way to read a value | Incorrect. Square brackets also read values.
        [ ] It adds the key if it is missing | Incorrect. .get() never changes the dictionary.
        [ ] It returns all the keys | Incorrect. .keys() returns all the keys.


    .. multichoice::

        Which code safely prints "missing" when the key ``"colour"`` is not in ``car_dictionary``?

        [ ] print(car_dictionary["colour", "missing"]) | Incorrect. Square brackets do not take a default value.
        [x] print(car_dictionary.get("colour", "missing")) | Correct! The second argument to .get() is the default.
        [ ] print(car_dictionary.find("colour", "missing")) | Incorrect. Dictionaries do not have a .find() method.
        [ ] print("colour" in car_dictionary, "missing") | Incorrect. This prints False missing.

----

Definition to get a dictionary value
-----------------------------------------

Create a dictionary
~~~~~~~~~~~~~~~~~~~~~~

| Below are hex values for colours in the rainbow:

| red is #FF0000
| orange is #FFA500
| yellow is #FFFF00
| green is #008000
| blue is #0000FF
| indigo is #4B0082
| violet is #EE82EE

.. admonition:: Tasks

    #. Create a dictionary, rainbow_colors, with the colour name as the key and the hex value as the value.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a dictionary, rainbow_colors, with the colour name as the key and the hex value as the value.

                .. code-block:: python

                    # Dictionary for rainbow colors
                    rainbow_colors = {
                        "red": "#FF0000",
                        "orange": "#FFA500",
                        "yellow": "#FFFF00",
                        "green": "#008000",
                        "blue": "#0000FF",
                        "indigo": "#4B0082",
                        "violet": "#EE82EE"
                    }

User input
~~~~~~~~~~~~~~~~

| For user input see: https://www.w3schools.com/python/ref_func_input.asp
| The input() function allows user input.

.. py:function:: input(prompt)

    | prompt is a string, representing a default message for the input.
    | Returns a string.

Example:

.. code-block:: python

    colour = input("Enter a colour: ")
    print(colour)

.. admonition:: Tasks

    #. Create a user input that refers to all the possible colors and stores it in the variable, user_color.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a user input that refers to all the possible colors and stores it in the variable, user_color

                .. code-block:: python

                    user_color = input("Enter a color from the rainbow (red, orange, yellow, green, blue, indigo, violet): ")


Hex colour function
~~~~~~~~~~~~~~~~~~~~~~

A scaffold of a simple function to return the hex value of a colour is below.

.. code-block:: python

     def hex_color(user_color, ________________):
        # Convert the input to lowercase for case-insensitivity
        user_color = ______________.lower()
        return ________________.get(_________________, "not listed in the dictionary")

.. cloze::
    :instructions: Fill in the four blanks in the scaffold above, in order.

    1. The second parameter of the function is @@rainbow_colors@@.
    2. The ``.lower()`` method is called on @@user_color@@.
    3. The ``.get()`` method is called on @@rainbow_colors@@.
    4. The first argument passed to ``.get()`` is @@user_color@@.

**Check:** Put the lines of the completed function in the correct order.

.. ordering::

    def hex_color(user_color, rainbow_colors):
        user_color = user_color.lower()
        return rainbow_colors.get(user_color, "not listed in the dictionary")


Final code
~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Exercise

    Create a python script that gets user input and prints the hex colour for the color name the user inputs.
    Example output: ``The hexadecimal value for green is #008000.``

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a python script that gets user input and prints the hex colour for the color name the user inputs.
                Example output: ``The hexadecimal value for green is #008000.``

                .. code-block:: python

                    # Dictionary with rainbow colors
                    rainbow_colors = {
                        "red": "#FF0000",
                        "orange": "#FFA500",
                        "yellow": "#FFFF00",
                        "green": "#008000",
                        "blue": "#0000FF",
                        "indigo": "#4B0082",
                        "violet": "#EE82EE"
                    }

                    user_color = input('Enter a rainbow color (red, orange, yellow, green, blue, indigo, violet): ')

                    def hex_color(user_color, rainbow_colors):
                        # Convert the input to lowercase for case-insensitivity
                        user_color = user_color.lower()
                        return rainbow_colors.get(user_color, "not listed in the dictionary")

                    hex_val = hex_color(user_color, rainbow_colors)
                    print(f"The hexadecimal value for {user_color} is {hex_val}")

----

Quiz: Rainbow Hex Colours
-------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. The ``input()`` function always returns a @@string@@.
    2. Calling ``.lower()`` on the input makes the lookup case-@@insensitive@@.
    3. The ``hex_color`` function takes the colour name and the @@dictionary@@ as its parameters.
    4. When the colour is not a key, ``.get()`` returns its @@default@@ value.
    5. A function sends its result back to the code that called it using the @@return@@ keyword.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Ask for a colour, call the function, and print the result.

.. ordering::

    user_color = input("Enter a rainbow colour: ")
    hex_val = hex_color(user_color, rainbow_colors)
    print(f"The hexadecimal value for {user_color} is {hex_val}")

----

**Example 2:** Create a small colour dictionary, look up "blue" with the function, and print the result.

.. ordering::

    colours = {"red": "#FF0000", "blue": "#0000FF"}
    result = hex_color("blue", colours)
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

        What data type does ``input()`` return?

        [x] A string | Correct! input() always returns a string, even if the user types a number.
        [ ] An integer | Incorrect. You would need int() to convert the input to an integer.
        [ ] A dictionary | Incorrect. input() returns the text the user typed.
        [ ] A Boolean | Incorrect. input() returns the text the user typed.


    .. multichoice::

        Why does ``hex_color`` call ``.lower()`` on ``user_color``?

        [x] So that "Green", "GREEN" and "green" all match the lowercase key | Correct! The dictionary keys are lowercase, and keys are case-sensitive.
        [ ] To remove spaces from the input | Incorrect. .strip() removes spaces.
        [ ] To convert the input to a number | Incorrect. .lower() changes letters to lowercase.
        [ ] Because .get() only works with lowercase strings | Incorrect. .get() works with any key; the keys here happen to be lowercase.


    .. multichoice::

        What does ``hex_color("GREEN", rainbow_colors)`` return?

        [x] "#008000" | Correct! "GREEN" is converted to "green", which is a key.
        [ ] "not listed in the dictionary" | Incorrect. .lower() converts "GREEN" to "green" before the lookup.
        [ ] None | Incorrect. The key is found after converting to lowercase.
        [ ] Python raises a KeyError | Incorrect. .get() never raises a KeyError.


    .. multichoice::

        What does ``hex_color("purple", rainbow_colors)`` return?

        [ ] "#800080" | Incorrect. Purple is not in the rainbow_colors dictionary.
        [ ] None | Incorrect. A default value was passed to .get().
        [x] "not listed in the dictionary" | Correct! "purple" is missing, so the default value is returned.
        [ ] Python raises a KeyError | Incorrect. .get() never raises a KeyError.


    .. multichoice::

        Why does the function use ``.get()`` instead of ``rainbow_colors[user_color]``?

        [x] So the program does not crash when the user types a colour that is not a key | Correct! Square brackets would raise a KeyError.
        [ ] Because square brackets cannot be used inside a function | Incorrect. Square brackets work anywhere.
        [ ] Because .get() is faster | Incorrect. The reason is handling missing keys safely.
        [ ] Because .get() adds the colour to the dictionary | Incorrect. .get() never changes the dictionary.


    .. multichoice::

        What does ``"#FF0000" in rainbow_colors`` evaluate to?

        [ ] True | Incorrect. The in keyword checks keys, and "#FF0000" is a value.
        [x] False | Correct! "#FF0000" is a value, not a key.
        [ ] "red" | Incorrect. The in keyword returns True or False.
        [ ] Python raises a KeyError | Incorrect. The in keyword never raises a KeyError.


    .. multichoice::

        In ``hex_val = hex_color(user_color, rainbow_colors)``, what is stored in ``hex_val``?

        [x] The value returned by the function | Correct! The returned hex value (or default message) is stored in hex_val.
        [ ] The colour name the user typed | Incorrect. That is stored in user_color.
        [ ] The whole rainbow_colors dictionary | Incorrect. The dictionary is passed in, not returned.
        [ ] None | Incorrect. The function always returns a string.


    .. multichoice::

        What would happen if the ``return`` line were removed from ``hex_color``?

        [ ] The function would print the hex value | Incorrect. Nothing in the function prints.
        [x] The function would return None | Correct! A function with no return statement returns None.
        [ ] Python would raise a KeyError | Incorrect. No lookup would raise an error.
        [ ] The function would return the dictionary | Incorrect. Without return, the result is None.