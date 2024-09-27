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
| See: https://datagy.io/python-switch-case/

----

| Match-case can be used to match all the simple data types: string, numbers, booleans, lists, tuples, sets, dictionaries.

----

Match-case
--------------------------------

| Match case can be used to replace lengthy if-elif blocks, making the alternatives more readable.
| An example of a simple if-elif block is below.

.. code-block:: python

    age_flag = False
    if age_flag == True:
        print("Entry permitted")
    elif age_flag ==  False:
        print("No entry until you reach 13 years of age.")


| In the simple pattern below, the subject is checked against each case pattern, in order, till a match is found.

.. code-block:: python

    match subject:
        case <pattern_1>:
            <action_1>
        case <pattern_2>:
            <action_2>

| The example, above, of an if-elif block rewritten as a match-case block is below..

.. code-block:: python

    age_flag = False
    match age_flag:
        case True:
            print("Entry permitted")
        case False:
            print("No entry until you reach 13 years of age.")


----

.. admonition:: Tasks

    1. Rewrite the selection-based code below to use match-case.

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
| In the code below, 3 different forms of each direction are allowed.
| To go north, the user can enter "N" or "north" or "go north".

.. code-block:: python

    def do_action(action):
        match action:
            case "N" | "north" | "go north":
                print("going north")

    do_action("N")
    do_action("north")
    do_action("go north")


----

.. admonition:: Tasks

    1. Add similar code, with 3 options each, for going south, east or west.

        .. code-block:: python

            def do_action(action):
                match action:
                case "N" | "north" | "go north":
                    print("going north")

----

Wildcard
--------------------------------

| If an exact match is not found, the last case, if provided, will be used as the matching case.
| The wildcard ``_`` is usually used when it is not referred to again in the code block.
| The unmatched "NW" triggers the ``case _:`` statement.

.. code-block:: python

    def do_action(action):
        match action:
            case "N" | "north" | "go north":
                print("going north")
            case "W" | "west" | "go west":
                print("going west")
            case _:
                print("Not a valid direction")

    do_action("NW")

----

.. admonition:: Tasks

    1. Add a wildcard code, to respond to an unmatched action, with a ``print("Not a valid action")`` statement.

        .. code-block:: python

            def do_action(action):
                match action:
                case "get" | "pick up":
                    print("pick up item")

----

Variable instead of Wildcard
--------------------------------

| Instead of using the wildcard ``_``, another variable, such as ``other``, can be used so that it may be referred to in the following case block code. 

.. code-block:: python

    def do_action(action):
        match action:
            case "N" | "north" | "go north":
                print("going north")
            case "W" | "west" | "go west":
                print("going west")
            case other:
                print(f"{other} is not a valid direction")

    do_action("NW")

----

.. admonition:: Tasks

    1. Add a final case using ``other``, to respond to an unmatched action, with a message indicating the invalid action.

        .. code-block:: python

            def do_action(action):
                match action:
                case "north" | "go north":
                    print("pick up item")
                case "get" | "pick up":
                    print("pick up item")

             do_action("NW")

----

Splitting multi-word strings into a list for complex matching
----------------------------------------------------------------

| A text string can be split into a list of words.
| e.g The string, ``"go north"``, can be split using ``"go north".split()``. It results in the list ``["go", "north"]``.
| This not only allows flexibility in the forms that can be matched, but allows part of the string to be bound to a variable.
| The action "get sword" can be matched with ``["get", obj]``, allowing ``obj`` to be used in the print statement, which will be ``"picking up sword"``.

.. code-block:: python

    def do_action(action):
        match action.split():
            case ["get", obj] | ["pick", "up", obj] | ["pick", obj, "up"]:
                print(f"picking up {obj}")

    do_action("get sword")

----

.. admonition:: Tasks

    1. Add a case to match these patterns: ``"go north"``, ``"to the south"``, ``"east is the way"``; and print out ``"going "`` and the direction.

        .. code-block:: python

            def do_action(action):
                match action.split():
                    case ["get", obj] | ["pick", "up", obj] | ["pick", obj, "up"]:
                        print(f"picking up {obj}")


            do_action("to the west")

----

Splitting with the use of as to capture the alternative used
----------------------------------------------------------------

| Part of the split string may have several alternatives that can be captured using ``as``.
| In the example below, an action like ``"go north"`` is split into the list ``["go", "north"]``.
| ``"go south"`` is split into the list ``["go", "south"]``.
| ``"go east"`` is split into the list ``["go", "east"]``.
| ``"go west"`` is split into the list ``["go", "west"]``.
| Each list has the same pattern: ``"go direction"``.
| ``("north" | "south" | "east" | "west") as direction`` captures the direction used.

.. code-block:: python

    def do_action(action):
        match action.split():
            case ["go", ("north" | "south" | "east" | "west") as direction]:
                print(f"going {direction}")

    do_action("go west")

---

.. admonition:: Tasks

    1. Write similar code to capture the weapon from these alternatives: "use dagger", "use sword", "use spear". Print out a statement indicating which weapon was used.

----

Guard pattern: Combing a condition in a case
----------------------------------------------------------------

| In the first case statement below, a condition is added using ``if weapon in weapons``.
| The case only applies if the condition is met.
| The list of weapons is: ``weapons = ["dagger", "sword", "spear"]``.
| In executing ``do_action("use sword", weapons)``, the first case statement will check to see if the weapon, sword, is in the weapons list.

| The second action with the crossbow will result in the print statement indicating that the weapon can't be used.

.. code-block:: python

    def do_action(action, weapons):
    match action.split():
        case ["use", weapon] if weapon in weapons:
            print(f"using {weapon}")
        case ["use", _]:
            print(f"Can't use that weapon.")

    weapons = ["dagger", "sword", "spear"]
    do_action("use sword", weapons)
    do_action("use crossbow", weapons)

----

.. admonition:: Tasks

    1. Modify the code below in 3 places to include a guard pattern that checks to see if the direction is allowed.

        .. code-block:: python

            def do_action(action):
                match action.split():
                    case ["go", ("north" | "south" | "east" | "west") as direction]:
                        print(f"going {direction}")

            allowed_directions = ["north", "south", "east"]
            do_action("go west")

----

Using the unpacking operator on a list
--------------------------------------

| Put the asterisk (*) in front of a variable name to pack the leftover elements into a list and assign it to a variable.
| In the example below, ``a`` is assigned the value ``1`` and ``b`` the rest of the list.

.. code-block:: python

    nums = [1, 2, 3, 4, 5, 6, 7]
    a, *b = nums
    print(a)   # 1
    print(b)   # [2, 3, 4, 5, 6, 7]

| THis allows multiple weapons to be used in the example below.
| From the string, ``"use dagger sword spear"``, a list of multiple weapons can be collected using ``*weapons``.
| This list, ``["dagger", "sword", "spear"]``, can then then be iterated over to do something with each weapon.


.. code-block:: python

    def do_action(action):
        match action.split():
            case ["use", *weapons]:
                for w in weapons:
                    print(f"using {w}")
            case ["use", weapon]:
                print(f"using {weapon}")
            case ["use", _]:
                print(f"Can't use that weapon.")

    do_action("use dagger sword spear")
    do_action("use crossbow")

----

.. admonition:: Tasks

    1. The code below has a case statement for ``"look north"``. Add a case statement for ``"look north south east"``.

        .. code-block:: python

            def do_action(action):
                match action.split():
                    case ["look", direction]:
                        print(f"looking {direction}")

            do_action("look north")
            do_action("look north south east")

----

Structure Matching lists or tuples
---------------------------------------

| The length of a list or tuple can be used in the structure matching below. 

.. code-block:: python

    def list_match(values):
        match values:
            case [a]:
                print(f'Only one item: {a}')
            case [a, b]:
                print(f'Two items: {a}, {b}')
            case [a, b, c]:
                print(f'Three items: {a}, {b}, and {c}')
            case [a, b, c, *rest]:
                print(f'More than three items: {a}, {b}, {c}, as well as: {rest}')

    list_match([1])
    list_match((2, 3))
    list_match((4, 5, 6))
    list_match((9, 8, 7, 6, 5, 4))

----

.. admonition:: Tasks

    1. A silly maths function does different things with a list of values depending in the number of elements in the list. 
    Complete the code below by filling in the square brackets and the curly brackets. Some parts are done already. 
    Here are the silly rules: for 1 element in the list, square it. 
    For 2 elements raise a to the power of b using the inbuilt pow function. 
    For 3 elements, multiply the first two then use floor division with the third. 
    For more than 3 elements, add the first 3 then subtract the sum of the rest.

        .. code-block:: python

            def list_maths(values):
                match values:
                    case []:
                        print(f'Only one item: {}')
                    case []:
                        print(f'Two items: {pow(a, b)}')
                    case []:
                        print(f'Three items: {}')
                    case [a, b, c, *rest]:
                        print(f'More than three items: { - sum(rest)}')

            list_maths([3])
            list_maths((2, 3))
            list_maths((4, 5, 6))
            list_maths((9, 8, 7, 6, 5, 4))

----

Matching tuples for coordinates
--------------------------------

| Other objects, apart from strings can be matched. 
| An example with a tuple is below.

.. code-block:: python

    def do_point(point):
        match point:
            case (0, 0):
                print("Origin")
            case (0, y):
                print(f"{y} on the Y axis")
            case (x, 0):
                print(f"{x} on the X axis")
            case (x, y):
                print(f"{x} on the X axis, {y} on the Y axis")
            case _:
                print("Invalid point")

    point_1 = (2, 3)
    do_point(point_1)

----

.. admonition:: Tasks

    1. Modify the curly brackets below to give feedback using the variables from the case statements used in playing a game of cards.

        .. code-block:: python

            def play_card(card):
                match card:
                    case (face_value, "Hearts"):
                        print(f"{} of Hearts wins")
                    case ("A", suit):
                        print(f"Ace of {} wins")
                    case (face_value, suit):
                        print(f"{} of {} looses")
                    case _:
                        print("Dodgy card. Get a new deck.")

            card_1 = ("A", "Hearts")
            play_card(card_1)
            card_1 = ("A", "Clubs")
            play_card(card_1)
            card_1 = ("K", "Spades")
            play_card(card_1)

----

Matching sets
--------------------------------

| The code below matches the length of the set.


.. code-block:: python

    def do_setlength(values):
    match len(values):
        case 1:
            print(f'Only one item: {values}')
        case 2:
            print(f'Two items: {values}')
        case 3:
            print(f'Three items: {values}')
        case 4:
            print(f'More than three items: {values}')
        case _:
            print("error")

    new_set = {2, 3}     
    do_setlength(new_set)


----

Matching dictionaries
--------------------------------

| Dictionaries can be matched.
| The two cases below only differ in the first key: whether it is a pizza or a main meal.



.. code-block:: python

    def order_cost(order):
        match order:
            case {"pizza": type , "amount": amount, "per_item_cost": per_item_cost}:
                print(f"{amount} {type} pizza ${amount * per_item_cost}")
            case {"mains": type , "amount": amount, "per_item_cost": per_item_cost}:
                print(f"{amount} {type} ${amount * per_item_cost}")


    order_cost({"pizza": "Hawaiian", "amount": 2, "per_item_cost": 15})
    order_cost({"mains": "Chicken Parma", "amount": 1, "per_item_cost": 26})
    order_cost({"mains": "Chicken Saltimbocca", "amount": 1, "per_item_cost": 30})


----

.. admonition:: Tasks

    1. The above example has been redesigned to have a separate prices list, ``prices``, which is passed into the order_cost function.
    This makes it easier to alter the prices list and helps make it independent from the rest of the code.
    Extend the cases to include entrees. Add two entrees to the prices list. Make an order with an entree. 
    Sample entrees might be.g Focaccia $16, Aranchini $17.

        .. code-block:: python

            def order_cost(order, prices):
                match order:
                    case {"pizza": type , "amount": amount}:
                        print(f"{amount} {type} pizza ${amount * costs[type]}")
                    case {"mains": type , "amount": amount}:
                        print(f"{amount} {type} ${amount * costs[type]}")

            prices = {"Hawaiian": 15, "Chicken Parma": 26, "Chicken Saltimbocca": 30 }

            order_cost({"pizza": "Hawaiian", "amount": 2}, prices)
            order_cost({"mains": "Chicken Parma", "amount": 1}, prices)
            order_cost({"mains": "Chicken Saltimbocca", "amount": 1}, prices)

----

Checking Types in Python Match-Case Statements
---------------------------------------------------

| Python match-case statements can be used to check the **types** of something being passed in.
| In the code below, lists ``[ ]``, tuples ``( )`` and sets ``{ }`` are distinguished.


.. code-block:: python

    def list_or_tuple_or_set(var):
        match var:
            case list(a):
                return f"List, {a}"
            case tuple(a):
                return f"Tuple, {a}"
            case set(a):
                return f"Set, {a}"
            case _:
                return "Something else"

    print(list_or_tuple_or_set([1, 2]))
    print(list_or_tuple_or_set((3, 4)))
    print(list_or_tuple_or_set({5, 6}))

----

| In the example below, lists and tuples are nested within each other and their pattern distinguished. 


.. code-block:: python

    def nested_lists_tuples(var):
        match var:
            case list((list(), list())) as x:
                return f"List of 2 lists, {x}"
            case list((tuple(), tuple())) as x:
                return f"List of 2 tuples, {x}"
            case tuple((list(), list())) as x:
                return f"tuple of 2 lists, {x}"
            case _:
                return "Something else"

    print(nested_lists_tuples([[1, 2], [3, 4]]))
    print(nested_lists_tuples([(5, 6), (7, 8)]))
    print(nested_lists_tuples(([1, 4], [5, 2])))

----

.. admonition:: Tasks

    1. Run the 2 codes above and check the output.
    2. Create a nested_lists function with cases for a list, a list of 2 lists, a list of 3 lists and a list of 4 lists.
