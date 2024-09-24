===============================
Data Structures: Dictionaries
===============================

Dictionaries
-------------------

Dictionary is an unordered set of ``key : value`` pairs. It's a rule that all keys are unique and have no duplicates. Unlike lists or tuples, which are indexed by numbers, 
you can retrieve a value from a dictionary by using the key as an index.

For example, you can store the highscores of all the players:

.. code-block:: python

    game_register = {
                    'googolplex': 100,
                    'terminat0r': 27,
                    'r00t': 150,
                    'dent': 42,
                    'teapot418' : 0
                    } 

    # Access elements
    game_register['dent']

    # Add or update and existing entry
    game_register['pepper'] = 50

    # Delete an entry
    del game_register['pepper']    

    # Delete all entries
    game_register.clear()

    # Delete the dictionary
    del game_register

    # Retrieve a value for the key or default if not in dicionary
    game_register.get('dent')        

