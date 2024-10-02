===============================
Dictionaries
===============================

| Suggested refs:
| https://www.programiz.com/python-programming/dictionary
| https://realpython.com/python-dicts/

----

Dictionary structure
----------------------------

| A Python dictionary is a collection of items.
| Each item  is a ``key: value`` pair.
| Dictionary items are **ordered**, **changeable**, and do not allow duplicates.
| All keys must be **immutable** (not able to be changed) such as integers, strings and tuples of integers or strings.
| Values can be any data types such as string, int, float, boolean, tuple, list, dictionary.

.. py:method:: dict_var = {key1 : value1, key2 : value2, …..}

    Returns a dictionary with the specified key: value pairs.

| An example of a dictionary of states and capitals is below.

.. code-block:: python

    eastern_state_capitals = {
                    'Victoria': 'Melbourne',
                    'New South Wales': 'Sydney',
                    'Queensland': 'Brisbane'
                    }
    print(eastern_state_capitals)

----

Getting a value from a dictionary
-----------------------------------

| Values in a dictionary are retrieved by using the key as an index.

.. py:method:: value_1 = dict_var[key1]

    Returns a value in a dictionary with the specified key, key1.

| In the dictionary below, the capital of Victoria can be found by indexing the dictionary: ``eastern_state_capitals['Victoria']``.
| THe key is 'Victoria'. The value is 'Melbourne'.

.. code-block:: python

    eastern_state_capitals = {
                    'Victoria': 'Melbourne',
                    'New South Wales': 'Sydney',
                    'Queensland': 'Brisbane'
                    }
    capital = eastern_state_capitals['Victoria']
    print(capital)
    # Output is 'Melbourne'

----

Case sensitive keys
-----------------------------------

| Keys in a dictionary are case sensitive.
| The keys 'Vic'and 'VIC' are different keys.

.. code-block:: python

    eastern_state_capitals = {
                    'Vic': 'Melbourne',
                    'VIC': 'MELB',
                    }
    print(eastern_state_capitals['Vic'])
    # Output is 'Melbourne'
    print(eastern_state_capitals['VIC'])
    # Output is 'MELB'

----

Empty dictionary
-------------------

| An empty dictionary is needed as a starting point when a dictionary is built as the program runs.

| An empty dictionary can be made using **curly brackets**:

.. code-block:: python

    empty_dict = {}

| An empty dictionary can be made using the **dict function**:

.. code-block:: python

    empty_dict = dict()

----

Making a dictionary
----------------------

Making a dictionary: curly brackets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Make a dictionary by enclosing a comma-separated sequence of key-value pairs in curly braces ``{}``.
| The dictionary below has 3 items, each separated by a comma.
| Each item is a key: value pair separated by a colon.

.. code-block:: python

    state_capitals = {
                    'Victoria': "Melbourne",
                    'Tasmania': "Hobart",
                    'Queensland': "Brisbane"
                    }
    print(state_capitals)

.. admonition:: Tasks

    #. Create a dictionary using curly brackets such that it maps the names of three countries, Japan, France and England, to their capitals: Tokyo, Paris and London. Print the dictionary.
    #. Create a dictionary using curly brackets such that it maps the names of three fruits, Apple, Banana, and Grapes, to their colors: Red, Yellow, and Purple. Print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a dictionary using curly brackets such that it maps the names of three countries, Japan, France and England, to their capitals: Tokyo, Paris and London. Print the dictionary.

                .. code-block:: python

                    country_capitals = {
                        'Japan': 'Tokyo',
                        'France': 'Paris',
                        'England': 'London'
                    }
                    print(country_capitals)

            .. tab-item:: Q2

                Create a dictionary using curly brackets such that it maps the names of three fruits, Apple, Banana, and Grapes, to their colors: Red, Yellow, and Purple. Print the dictionary.

                .. code-block:: python

                    fruit_colors = {
                        'Apple': 'Red',
                        'Banana': 'Yellow',
                        'Grapes': 'Purple'
                    }
                    print(fruit_colors)


----

Making a dictionary from a list of lists
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Make a dictionary using the dict function.
| Pass in a list of lists, with each list made up 2 elements, e.g ``["New South Wales", "Sydney"]``
| The first element becomes the key and the second element becomes the value. e.g ``"New South Wales": "Sydney"``

.. code-block:: python

    state_capitals = dict([
        ["New South Wales", "Sydney"],
        ["Victoria", "Melbourne"],
        ["Queensland", "Brisbane"]
    ])

    print(state_capitals)
    # Output is {'New South Wales': 'Sydney', 'Victoria': 'Melbourne', 'Queensland': 'Brisbane'}

.. admonition:: Tasks

    #. Create a dictionary using the dict function and a list of lists such that it maps the names of three programming languages, Python, Java, and C++, to their creators: Guido van Rossum, James Gosling, and Bjarne Stroustrup. Print the dictionary.
    #. Create a dictionary using the dict function and a list of lists such that it maps the names of three countries, China, India, and USA, to their populations in billions: 1.4, 1.4, and 0.3. Print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a dictionary using the dict function and a list of lists such that it maps the names of three programming languages, Python, Java, and C++, to their creators: Guido van Rossum, James Gosling, and Bjarne Stroustrup. Print the dictionary.

                .. code-block:: python

                    languages = dict([
                        ['Python', 'Guido van Rossum'],
                        ['Java', 'James Gosling'],
                        ['C++', 'Bjarne Stroustrup']
                    ])
                    print(languages)


            .. tab-item:: Q2

                Create a dictionary using the dict function and a list of lists such that it maps the names of three countries, China, India, and USA, to their populations in billions: 1.44, 1.39, and 0.33. Print the dictionary.

                .. code-block:: python

                    populations = dict([
                        ['China', 1.44],
                        ['India', 1.39],
                        ['USA', 0.33]
                    ])
                    print(populations)


----

Making a dictionary from a list of tuples
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Make a dictionary using the dict function.
| Pass in a list of tuples, with each tuple made up 2 elements, e.g ``("New South Wales", "Sydney")``
| The first element becomes the key and the second element becomes the value. e.g ``"New South Wales": "Sydney"``

.. code-block:: python

    capitals = dict([
        ("South Australia", "Adelaide"),
        ("Western Australia", "Perth"),
        ("Australian Capital Territory", "Canberra")
    ])
    print(capitals)
    # Output is {'South Australia': 'Adelaide', 'Western Australia': 'Perth', 'Australian Capital Territory': 'Canberra'}

.. admonition:: Tasks

    #. Create a dictionary using the dict function and a list of tuples such that it maps the names of three car brands, Toyota, BMW, and Ford, to their countries of origin: Japan, Germany, and USA. Print the dictionary.
    #. Create a dictionary using the dict function and a list of tuples such that it maps the names of three planets, Mercury, Venus, and Earth, to their average distances from the sun in million kilometers: 57.9, 108.2, and 149.6. Print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a dictionary using the dict function and a list of tuples such that it maps the names of three car brands, Toyota, BMW, and Ford, to their countries of origin: Japan, Germany, and USA. Print the dictionary.

                .. code-block:: python

                    car_brand_countries = dict([
                        ('Toyota', 'Japan'),
                        ('BMW', 'Germany'),
                        ('Ford', 'USA')
                    ])
                    print(car_brand_countries)


            .. tab-item:: Q2

                Create a dictionary using the dict function and a list of tuples such that it maps the names of three planets, Mercury, Venus, and Earth, to their average distances from the sun in million kilometers: 57.9, 108.2, and 149.6. Print the dictionary.

                .. code-block:: python

                    planet_distances_to_sun = dict([
                        ('Mercury', 57.9),
                        ('Venus', 108.2),
                        ('Earth', 149.6)
                    ])
                    print(planet_distances_to_sun)

----

Making a dictionary from 2 lists
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| 2 lists of keys and values can be combined and converted into a dictionary using several methods.

Making a dictionary from 2 lists --update
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| The update method is used to add each state key and city value.

.. code-block:: python

    states = ["Queensland", "South Australia", "Western Australia"]
    cities = ["Brisbane", "Adelaide", "Perth"]

    capitals = {}
    for i in range(len(states)):
        capitals.update({states[i]: cities[i]})

    print(capitals)
    # Output is {'Queensland': 'Brisbane', 'South Australia': 'Adelaide', 'Western Australia': 'Perth'}


.. admonition:: Tasks

    #. Create a dictionary using the update method and two lists such that it maps the names of 'Lockett', 'Coventry', and 'Dunstall', to their goals kicked: 1360, 1299, and 1254. Print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a dictionary using the update method and two lists such that it maps the names of 'Lockett', 'Coventry', and 'Dunstall', to their goals kicked: 1360, 1299, and 1254. Print the dictionary.

                .. code-block:: python

                    names = ['Lockett', 'Coventry', 'Dunstall']
                    goals = [1360, 1299, 1254]
                    goal_kickers = {}
                    for i in range(len(names)):
                        goal_kickers.update({names[i]: goals[i]})
                    print(my_dict)


Making a dictionary from 2 lists --set key value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Each state key gets its city value each time through the for loop.

.. code-block:: python

    states = ["Queensland", "South Australia", "Western Australia"]
    cities = ["Brisbane", "Adelaide", "Perth"]

    capitals = {}
    for i in range(len(states)):
        capitals[states[i]] = cities[i]
    print(capitals)
    # Output is {'Queensland': 'Brisbane', 'South Australia': 'Adelaide', 'Western Australia': 'Perth'}


.. admonition:: Tasks

    #. Create a dictionary using the update method and two lists such that it maps the names of 'Lockett', 'Coventry', and 'Dunstall', to their goals kicked: 1360, 1299, and 1254. Print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a dictionary using the update method and two lists such that it maps the names of 'Lockett', 'Coventry', and 'Dunstall', to their goals kicked: 1360, 1299, and 1254. Print the dictionary.

                .. code-block:: python

                    names = ['Lockett', 'Coventry', 'Dunstall']
                    goals = [1360, 1299, 1254]
                    goal_kickers = {}
                    for i in range(len(names)):
                        goal_kickers[names[i]] = goals[i]
                    print(goal_kickers)


Making a dictionary from 2 lists --dict and zip
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| The zip() function pairs each element from the states list with the corresponding element from the cities list.
| The result is an iterator containing these tuples: ``('Queensland', 'Brisbane'), ('South Australia', 'Adelaide'), ('Western Australia', 'Perth')``
| The dict function then converts the zip object into a dictionary.

.. code-block:: python

    states = ["Queensland", "South Australia", "Western Australia"]
    cities = ["Brisbane", "Adelaide", "Perth"]

    capitals = dict(zip(states, cities))
    print(capitals)
    # Output is {'Queensland': 'Brisbane', 'South Australia': 'Adelaide', 'Western Australia': 'Perth'}

.. admonition:: Tasks

    #. Create a dictionary using the zip function and two lists such that it maps the names of three animals, Elephant, Dog, and Cat, to their average lifespans in years: 70, 13, and 15. Print the dictionary.
    #. Create a dictionary using the zip function and two lists such that it maps the names of three cities, Tokyo, Delhi, and Shanghai, to their populations in millions: 37.4, 28.5, and 25.6. Print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a dictionary using the zip function and two lists such that it maps the names of three animals, Elephant, Dog, and Cat, to their average lifespans in years: 70, 13, and 15. Print the dictionary.

                .. code-block:: python

                    animals = ['Elephant', 'Dog', 'Cat']
                    lifespans = [70, 13, 15]
                    animal_lifespans = dict(zip(animals, lifespans))
                    print(animal_lifespans)

            .. tab-item:: Q2

                Create a dictionary using the zip function and two lists such that it maps the names of three cities, Tokyo, Delhi, and Shanghai, to their populations in millions: 37.4, 28.5, and 25.6. Print the dictionary.

                .. code-block:: python

                    cities = ['Tokyo', 'Delhi', 'Shanghai']
                    populations = [37.4, 28.5, 25.6]
                    city_populations = dict(zip(cities, populations))
                    print(city_populations)


----

Making a dictionary by dictionary comprehension from 2 lists
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The dictionary comprehension below creates a dictionary by iterating over length of the states list and using the index, i, to set the state key and city value.

.. code-block:: python

    states = ["Western Australia", "Tasmania", "Northern Territory"]
    cities = ["Perth", "Hobart", "Darwin"]

    capitals = {states[i]: cities[i] for i in range(len(states))}
    print(capitals)


.. admonition:: Tasks

    #. Create a dictionary using a dictionary comprehension via the indexes of two lists such that it maps the names of 'Lockett', 'Coventry', and 'Dunstall', to their goals kicked: 1360, 1299, and 1254. Print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a dictionary using a dictionary comprehension via the indexes of two lists such that it maps the names of 'Lockett', 'Coventry', and 'Dunstall', to their goals kicked: 1360, 1299, and 1254. Print the dictionary.

                .. code-block:: python

                    names = ['Lockett', 'Coventry', 'Dunstall']
                    goals = [1360, 1299, 1254]
                    goal_kickers = {names[i]: goals[i] for i in range(len(names))}
                    print(goal_kickers)

| The dictionary comprehension below creates a dictionary by iterating over the tuples produced by zip().
| For each tuple, the state becomes the key and city becomes the value.

.. code-block:: python

    states = ["Western Australia", "Tasmania", "Northern Territory"]
    cities = ["Perth", "Hobart", "Darwin"]

    capitals = {state: city for state, city in zip(states, cities)}
    print(capitals)

.. admonition:: Tasks

    #. Create a dictionary using dictionary comprehension and two lists such that it maps the names of three sports, Soccer, Basketball, and Baseball, to the number of players in each team: 11, 5, and 9. Print the dictionary.
    #. Create a dictionary using dictionary comprehension and two lists such that it maps the names of three countries, USA, China, and Japan, to their GDPs in trillion USD: 21.43, 14.34, and 5.08. Print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a dictionary using dictionary comprehension and two lists such that it maps the names of three sports, Soccer, Basketball, and Baseball, to the number of players in each team: 11, 5, and 9. Print the dictionary.

                .. code-block:: python

                    sports = ['Soccer', 'Basketball', 'Baseball']
                    players = [11, 5, 9]
                    sport_players = {sport: player for sport, player in zip(sports, players)}
                    print(sport_players)

            .. tab-item:: Q2

                Create a dictionary using dictionary comprehension and two lists such that it maps the names of three countries, USA, China, and Japan, to their GDPs in trillion USD: 21.43, 14.34, and 5.08. Print the dictionary.

                .. code-block:: python

                    countries = ['USA', 'China', 'Japan']
                    gdps = [21.43, 14.34, 5.08]
                    country_gdps = {country: gdp for country, gdp in zip(countries, gdps)}
                    print(country_gdps)

----

Making a dictionary from key word arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Make a dictionary using the dict function and key word arguments.
| ``a=1`` will become the key value pair ``'a': 1``

.. code-block:: python

    simple_dict = dict(a=1, b=2, c=3, d=4)
    print(simple_dict)
    # Output is {'a': 1, 'b': 2, 'c': 3, 'd': 4}

.. admonition:: Tasks

    #. Create a dictionary using keyword arguments such that it maps the names of three programming languages, Python, Java, and JavaScript, to their release years: 1991, 1995, and 1995. Print the dictionary.
    #. Create a dictionary using keyword arguments such that it maps the names of three continents, Africa, Asia, and Europe, to their areas in million square kilometers: 30.37, 44.58, and 10.18. Print the dictionary.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a dictionary using keyword arguments such that it maps the names of three programming languages, Python, Java, and JavaScript, to their release years: 1991, 1995, and 1995. Print the dictionary.

                .. code-block:: python

                    languages_release_years = dict(Python=1991, Java=1995, JavaScript=1995)
                    print(languages_release_years)
                    # Output is {'Python': 1991, 'Java': 1995, 'JavaScript': 1995}

            .. tab-item:: Q2

                Create a dictionary using keyword arguments such that it maps the names of three continents, Africa, Asia, and Europe, to their areas in million square kilometers: 30.37, 44.58, and 10.18. Print the dictionary.

                .. code-block:: python

                    continents = dict(Africa=30.37, Asia=44.58, Europe=10.18)
                    print(continents)
                    # Output is {'Africa': 30.37, 'Asia': 44.58, 'Europe': 10.18}


----


..
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



