==========================
Selection
==========================

Selection is one of the three basic control structures:

#. Sequence (steps in order)
#. Selection (branching using ``if`` ... ``elif`` ... ``else``)
#. Iteration (repetition or looping using ``while`` or ``for``)

Selection provides choice or branches in the code.

----

If, elif, else
----------------------------

| ``if`` is used with a condition that results in ``True`` or ``False``.
| When the condition is True, the code indented below the ``if`` statement is executed.
| Alternatives can be provided using ``elif`` with a condition.
| If all conditions are ``False``, ``else:`` can be used to execute other code.
| Note that there must be a colon, ``:``, at the end of each ``if``, ``elif`` and ``else`` statement.

| In the code below, scoreA is compared to scoreB.

.. code-block:: python

    scoreA = 88
    scoreB = 85
    if scoreA > scoreB:
        print("A won")
    elif scoreB > scoreA:
        print("B won")
    else:
        print("A drew with B")

----

.. admonition:: Tasks

    #. Add the variables ``teamA`` and ``teamB`` and set team names for them. Modify the code to print the team name instead of 'A' or 'B'. Hint: To join text use a plus symbol. e.g (myteam + " my text")

----

Nested if 
----------------------------

| Nesting includes other ``if`` statements have within ``if`` statements.
| Both the ``if`` and the ``elif`` have a nested ``if`` and ``else`` that are used when their condition is True. 

.. code-block:: python

    scoreA = 120
    scoreB = 55
    if scoreA > scoreB:
        if scoreA - scoreB > 60:
            print("A won easily")
        else:
            print("A won")
    elif scoreB > scoreA:
        if scoreB - scoreA > 60:
            print("B won easily")
        else:
            print("B won")
    else:
        print("A drew with B")


----

.. admonition:: Tasks

    #. Add the variables ``teamA`` and ``teamB`` and set team names for them. Modify the code to print the team name instead of 'A' or 'B'. Hint: To join text use a plus symbol. e.g (myteam + " my text")
    #. Modify the code to print the winning margins. Use ``str(number)`` to convert numbers to text for joining with other text. Add the variables ``teamA_win_by`` and ``teamB_win_by``. Calculate those variables using scoreA and scoreB. e.g ``teamA_win_by = scoreA - scoreB``. Replace "A won easily" with code to output "A won easily by 65". Do similar replacements for the other printed text.

