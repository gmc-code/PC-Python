==========================
Match - Case
==========================

| Match-case statements are in python from 3.10. 
| Python refers to this as structural pattern matching.
| Match-case statements can be used for what is known as switch-case statements in general use in other languages.
| See: https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching
| See: https://www.youtube.com/watch?v=-79HGfWmH_w
| See: https://github.com/mCodingLLC/VideosSampleCode/blob/master/videos/039_the_hottest_new_feature_coming_in_python_310_structural_pattern_matching___match_statement/match_statement.py
| See: https://peps.python.org/pep-0636/

| Match-case can be used to match all the simple data types: string, numbers, booleans, lists, tuples, sets, dictionaries.
----

Match-case
--------------------------------

| Match case can be used to replace lengthy if-elif blocks, making the alternatives more readable.
| In the simple pattern below, the subject is checked against each case pattern in order till a match is found.

.. code-block::

    match subject:
        case <pattern_1>:
            <action_1>
        case <pattern_2>:
            <action_2>

| An example of a simple if-elif block is below.

.. code-block:: python

    age_flag = False
    if age_flag == True:
        print("Entry permitted")
    elif age_flag ==  False:
        print("No entry until you reach 13 years of age.")

| The same example written as a match-case block is below..

.. code-block:: python

    age_flag = False
    match age_flag:
        case True:
            print("Entry permitted")
        case False:
            print("No entry until you reach 13 years of age.")


----

.. admonition:: Tasks

    1. Rewrite the selection based code below to use match-case.

        .. code-block:: python

            action = "rest"    
            if action = "rest":
                print("resting")
            elif action = "go":
                print("continuing")


----

Case Alternatives
--------------------------------

| Several alternatives can be used in a single pattern using the pipe symbol for ``or``: ``|``.
| In the code below, 3 different ways of going in each direction are allowed.
| To go north, the user can enter "N" or "north" or "go north".

.. code-block:: python

    def do_action(action):
        match action:
            case "N" | "north" | "go north":
                print("going north")
            case "S" | "south" | "go south":
                print("going south")

    do_action("N")
    do_action("north")
    do_action("go north")
    do_action("go south")

----

.. admonition:: Tasks

    1. Add similar code for going east or west.

        .. code-block:: python

            def do_action(action):
                match action:
                case "N" | "north" | "go north":
                    print("going north")
                case "S" | "south" | "go south":
                    print("going south")


----

Wilcard
--------------------------------

| If an exact match is not found, the last case, if provided, will be used as the matching case.
| The wildcard ``_`` is usually used when it is not referred to again in the code block.

.. code-block:: python

    def do_action(action):
        match action:
            case "N" | "north" | "go north":
                print("going north")
            case "S" | "south" | "go south":
                print("going south")
            case _:
                print("Not a valid direction")

    do_action("NW")

----

Vaiable instead of Wilcard
--------------------------------

| Instead of using the wildcard ``_``, another variable, such as ``other``, can be used so that it may be referred to in the following case block code. 

.. code-block:: python

    def do_action(action):
        match action:
            case "N" | "north" | "go north":
                print("going north")
            case "S" | "south" | "go south":
                print("going south")
            case other:
                print(f"{other} is not a valid direction")

    do_action("NW")

----

Splitting multi-word strings into a list for complex matching
----------------------------------------------------------------

| A text string can be split into a list of words.
| e.g The split string ``"go north".split()`` the list ``["go", "north"]``.

.. code-block:: python

def match_alternatives(command):
    match command.split():
        case ["north"] | ["go", "north"]:
            print("going north")
        case ["get", obj] | ["pick", "up", obj] | ["pick", obj, "up"]:
            print(f"picking up: {obj}")


.. code-block:: python


def match_capture_subpattern(command):
    match command.split():
        case ["go", ("north" | "south" | "east" | "west") as direction]:
            print(f"going {direction}")

----

Matching tuples for coordinates
--------------------------------

| Other objects, apart from strings can be matched. 
| An example with a tuple is below.


.. code-block:: python

    point = (2, 3)
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"{y} on Y axis")
        case (x, 0):
            print(f"{x} on X axis")
        case (x, y):
            print(f"{x} on X axis, {y} on Y axis")
        case _:
            print("Invalid point")


----



.. code-block:: python

def match_guard(command, exits):
    match command.split():
        case ["go", direction] if direction in exits:
            print(f"going {direction}")
        case ["go", _]:
            print(f"can't go that way")