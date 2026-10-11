====================================================
User additions to dictionary
====================================================

| The code below maintains a dictionary of the top Australian Football League (AFL) teams and their premiership counts.
| It repeatedly prompts the user to input a team's short name and checks if the team is in the dictionary.
| If the team is found, it displays the number of premierships won.
| If not, it asks the user to input the number of premierships for the new team and updates the dictionary.
| The loop continues until the user decides to stop, after which the final dictionary is printed.


.. code-block:: python

    premiers = {"ESS": 16, "COLL": 16, "CARL": 16, "MELB": 13, "RICH": 13, "HAW": 13, "GEE": 10}

    while True:
        user_team = input("What team (short name)? ").upper().strip()

        # Check if the input is valid (not empty and only letters)
        if not user_team.isalpha():
            print("Invalid input. Please enter a valid team short name consisting of letters only.")
            continue

        team_premierships = premiers.get(user_team)
        if team_premierships is None:
            print(f"{user_team} is not in the dictionary")
            while True:
                try:
                    new_team_premierships = int(input("How many premierships have they won? "))
                    break
                except ValueError:
                    print("Please enter a valid number.")
            premiers[user_team] = new_team_premierships
            print(f"{user_team} has won {new_team_premierships} premierships.")
        else:
            print(f"{user_team} has won {team_premierships} premierships.")

        get_more_premiers = input("Press Enter to continue or any other key to exit: ").strip()
        if get_more_premiers != "":
            print("Exiting the program.\n")
            break

    print(premiers)

----

**Initialize Dictionary**:
-----------------------------------------------------------------------

| The `premiers` dictionary is initialized with team abbreviations as keys and their respective premiership counts as values.

.. code-block:: python

    premiers = {"ESS": 16, "COLL": 16, "CARL": 16, "MELB": 13, "RICH": 13, "HAW": 13, "GEE": 10}


**Start Infinite Loop**:
-----------------------------------------------------------------------

| The `while True:` loop begins, allowing the program to repeatedly prompt the user for input.

.. code-block:: python

    while True:


**Get User Input**:
-----------------------------------------------------------------------

| The user is prompted to enter a team's short name, which is then converted to uppercase and stripped of any leading or trailing whitespace.

.. code-block:: python

    user_team = input("What team (short name)? ").upper().strip()


**Validate User Input**:
-----------------------------------------------------------------------

| The code checks if the input is valid (i.e., not empty and consists only of letters). If the input is invalid, it prints an error message and continues to the next iteration of the loop.

.. code-block:: python

    if not user_team.isalpha():
        print("Invalid input. Please enter a valid team short name consisting of letters only.")
        continue


**Check Team in Dictionary**:
-----------------------------------------------------------------------

| The code attempts to retrieve the number of premierships for the entered team from the `premiers` dictionary.

.. code-block:: python

    team_premierships = premiers.get(user_team)


**Handle Team Not Found**:
-----------------------------------------------------------------------

| If the team is not found in the dictionary (`team_premierships` is `None`), the code informs the user and prompts for the number of premierships the team has won. It then adds this new entry to the dictionary.

.. code-block:: python

    if team_premierships is None:
        print(f"{user_team} is not in the dictionary")
        while True:
            try:
                new_team_premierships = int(input("How many premierships have they won? "))
                break
            except ValueError:
                print("Please enter a valid number.")
        premiers[user_team] = new_team_premierships
        print(f"{user_team} has won {new_team_premierships} premierships.")


**Handle Team Found**:
-----------------------------------------------------------------------

| If the team is found in the dictionary, the code prints the number of premierships the team has won.

.. code-block:: python

    else:
        print(f"{user_team} has won {team_premierships} premierships.")


**Prompt to Continue or Exit**:
-----------------------------------------------------------------------

| The user is prompted to press Enter to continue or any other key to exit. If the user chooses to exit, the loop breaks.

.. code-block:: python

    get_more_premiers = input("Press Enter to continue or any other key to exit: ").strip()
    if get_more_premiers != "":
        print("Exiting the program.\n")
        break


**Print Final Dictionary**:
-----------------------------------------------------------------------

| After the loop ends, the final state of the `premiers` dictionary is printed.

.. code-block:: python

    print(premiers)

----

Quiz: User Additions to a Dictionary
------------------------------------

Fill-in-the-Blanks (Cloze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. cloze::
    :instructions: Complete the following sentences by filling in the blanks.

    1. A ``while True:`` loop keeps running until a @@break@@ statement is reached.
    2. The ``.upper()`` method converts the team name to @@uppercase@@ letters.
    3. The ``.strip()`` method removes leading and trailing @@whitespace@@.
    4. The ``.isalpha()`` method returns True only if every character is a @@letter@@.
    5. The @@continue@@ statement skips the rest of the loop and asks for a team again.
    6. If the team is not a key, ``premiers.get(user_team)`` returns @@None@@.
    7. If the user types text that ``int()`` cannot convert, Python raises a @@ValueError@@.

Code Ordering Examples
~~~~~~~~~~~~~~~~~~~~~~

**Example 1:** Start the loop, get the team name, and reject input that is not made of letters.

.. ordering::

    while True:
        user_team = input("What team (short name)? ").upper().strip()
        if not user_team.isalpha():
            print("Invalid input. Letters only.")
            continue

----

**Example 2:** Look up the team and print a message for both a missing team and a found team.

.. ordering::

    team_premierships = premiers.get(user_team)
    if team_premierships is None:
        print(f"{user_team} is not in the dictionary")
    else:
        print(f"{user_team} has won {team_premierships} premierships.")

----

**Example 3:** Keep asking for a number until the user enters a valid one, then add the team to the dictionary.

.. ordering::

    while True:
        try:
            new_team_premierships = int(input("How many premierships have they won? "))
            break
        except ValueError:
            print("Please enter a valid number.")
    premiers[user_team] = new_team_premierships

Multiple Choice Questions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. mcqgroup::
    :nav_position: both
    :show-instant-feedback:
    :enable-instant-feedback:
    :shuffle_questions:
    :num_questions: 5


    .. multichoice::

        The user types ``  ess `` (with spaces). What is stored in ``user_team``?

        [ ] "  ess " | Incorrect. .upper() and .strip() change the input.
        [ ] "  ESS " | Incorrect. .strip() also removes the spaces.
        [x] "ESS" | Correct! .upper() makes it uppercase and .strip() removes the spaces.
        [ ] "ess" | Incorrect. .upper() converts the letters to uppercase.


    .. multichoice::

        What does ``"ESS1".isalpha()`` return?

        [ ] True | Incorrect. "1" is not a letter.
        [x] False | Correct! Every character must be a letter for .isalpha() to return True.
        [ ] "ESS" | Incorrect. .isalpha() returns True or False.
        [ ] Python raises a ValueError | Incorrect. .isalpha() never raises an error.


    .. multichoice::

        The user just presses Enter at the team prompt. What happens?

        [x] The invalid input message prints and the loop asks again | Correct! "".isalpha() is False, so the code prints the message and continues.
        [ ] An empty key is added to the dictionary | Incorrect. The input is rejected before the lookup.
        [ ] The program exits | Incorrect. continue restarts the loop rather than ending it.
        [ ] Python raises a KeyError | Incorrect. The lookup is never reached.


    .. multichoice::

        What does ``premiers.get("SYD")`` return before Sydney has been added?

        [ ] 0 | Incorrect. No default value is given to .get().
        [x] None | Correct! "SYD" is not a key and no default is given.
        [ ] "SYD" | Incorrect. .get() returns a value, not the key.
        [ ] Python raises a KeyError | Incorrect. .get() never raises a KeyError.


    .. multichoice::

        Why does the code test ``team_premierships is None`` instead of ``if not team_premierships:``?

        [x] A team with 0 premierships would wrongly be treated as missing | Correct! 0 counts as False, but it is still a real value.
        [ ] ``if not`` cannot be used with dictionaries | Incorrect. ``if not`` works with any value.
        [ ] ``is None`` is required by ``.get()`` | Incorrect. It is a choice to handle 0 correctly.
        [ ] There is no difference | Incorrect. They behave differently when the value is 0.


    .. multichoice::

        The user types ``three`` when asked how many premierships. What happens?

        [ ] The team is added with the value "three" | Incorrect. int() cannot convert "three".
        [ ] The program crashes | Incorrect. The ValueError is caught by the except block.
        [x] "Please enter a valid number." prints and the question is asked again | Correct! The except block catches the ValueError and the inner loop repeats.
        [ ] The team is added with the value 0 | Incorrect. Nothing is added until a valid number is entered.


    .. multichoice::

        Which loop does the ``break`` inside the ``try`` block exit?

        [x] Only the inner loop that asks for a number | Correct! break exits the closest loop only.
        [ ] Both loops, ending the program | Incorrect. break only exits the loop it is directly inside.
        [ ] Only the outer loop | Incorrect. The inner loop is the closest one.
        [ ] Neither loop | Incorrect. break always exits the closest loop.


    .. multichoice::

        What does ``premiers["SYD"] = 5`` do?

        [x] Adds a new key "SYD" with the value 5 | Correct! Assigning to a new key adds it to the dictionary.
        [ ] Raises a KeyError because "SYD" is missing | Incorrect. Assigning to a missing key adds it; only reading a missing key raises KeyError.
        [ ] Changes every value to 5 | Incorrect. Only the "SYD" key is affected.
        [ ] Looks up "SYD" and returns 5 | Incorrect. The = sign assigns a value.


    .. multichoice::

        At the prompt "Press Enter to continue or any other key to exit", the user presses Enter. What happens?

        [x] The loop repeats and asks for another team | Correct! An empty string equals "", so break is not reached.
        [ ] The program exits | Incorrect. The program exits only if something other than Enter is typed.
        [ ] The dictionary is printed and the loop repeats | Incorrect. The dictionary prints only after the loop ends.
        [ ] Python raises a ValueError | Incorrect. Comparing strings never raises an error.


    .. multichoice::

        The user adds "SYD" with 5 premierships, then exits. How many key-value pairs does the printed dictionary contain?

        [ ] 7 | Incorrect. A new team was added to the original 7.
        [x] 8 | Correct! The original 7 teams plus "SYD".
        [ ] 9 | Incorrect. Only one team was added.
        [ ] 1 | Incorrect. The original teams are still in the dictionary.