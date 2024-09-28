==========================
json files
==========================

| json files are common when working with APIs and configuration, settings and preference files.
| json stands for Java Script Object Notation but is independent of programming languages.

| See: https://docs.python.org/3/library/json.html#module-json
| Corey Schafer video See: https://www.youtube.com/watch?v=9N6a-VLBa2I&list=RDCMUCCezIgC97PvUuR4_gbFUs5g&start_radio=1&rv=9N6a-VLBa2I&t=1
| Socratica video See: https://www.youtube.com/watch?v=pTT7HMqDnJw&list=RDCMUCW6TXMZ5Pq6yL6_k5NZ2e0Q&index=2


| To minify json online see: https://onlinejsontools.com/minify-json
| To produce pretty json see: https://onlinejsontools.com/prettify-json

----

Structure
---------------

| Imported json files are made up of structures like python dictionaries and lists.
| json uses key:value pairs in {} brackets.
| The simple json below looks like a python dictionary.

.. code:: 

    {"firstName":"Anna","lastName":"Smith"}

| json can use [] to make an array of values.

.. code::

    {"days30":["Apr","Jun","Sep","Nov"]}


| In the code below, the key of "employees" has a value consisting of a dictionary with 2 keys: "office_worker" and "writer".
| The "office_worker" key has a value that is an array of 2 objects, each in {}.

.. code:: 

    {
        "employees": {
            "office_worker": [
                {"firstName": "John", "lastName": "Doe", "gender": "Male"},
                {"firstName": "Peter", "lastName": "Jones", "gender": "Male"},
            ],
            "writer": {"firstName": "Anna", "lastName": "Smith", "gender": "Female"},
        }
    }


----

Loads
-------------------------------

| Use the **loads** function to convert a string to a json in the form of a dictionary.
| For conversion see: https://docs.python.org/3/library/json.html#encoders-and-decoders
| The full syntax is at: https://docs.python.org/3/library/json.html#json.loads
| Use the simple syntax:

.. py:function:: json.loads(string)

    :param string: a string containing a JSON document

    | Returns a json object from a string

----

json to dict
-------------------------------------

| The code below loads the json string, converting it to a dictionary.
| The employees are in two keys: office_worker as a list of employee dictionaries; writer as a dictionary.
| The code iterates through the list of office_worker dictionaries and prints the name of each office_worker using an f string.
| The code gets the writer dictionary and prints the name of the writer using an f string.


.. code-block:: python
    
    import json

    emp_str = """
    {
        "employees": {
            "office_worker": [
                {"firstName": "John", "lastName": "Doe", "gender": "Male"},
                {"firstName": "Peter", "lastName": "Jones", "gender": "Male"},
            ],
            "writer": {"firstName": "Anna", "lastName": "Smith", "gender": "Female"},
        }
    }
    """

    json_dict = json.loads(emp_str)
    # iterate over office_worker
    for emp in json_dict["employees"]["office_worker"]:
        print(f'{emp["firstName"]} {emp["lastName"]}')
    # writer
    emp = json_dict["employees"]["writer"]   
    print(f'{emp["firstName"]} {emp["lastName"]}')

.. code-block:: 

    John Doe
    Peter Jones
    Anna Smith

----

Dumps
-------------

| Use the dumps function to convert a json object to a string.
| The full syntax is at: https://docs.python.org/3/library/json.html#json.dumps
| Use the simple syntax:

.. py:function:: json.dumps(json)

    :param json: a JSON object

    | Returns a string from a json object

| Use the syntax below for pretty printing:

.. py:function:: json.dumps(json, indent=4)

    :param json: a JSON object
    :param indent: the number of spaces to indent

    | Returns a string from a json object using indenting.

----

Printing specific keys from json objects
-----------------------------------------

| The code below deletes the gender keys then converts the json to a string, then prints it.

.. code-block:: python
    
    import json

    emp_str = """
    {
        "employees": {
            "office_worker": [
                {"firstName": "John", "lastName": "Doe", "gender": "Male"},
                {"firstName": "Peter", "lastName": "Jones", "gender": "Male"},
            ],
            "writer": {"firstName": "Anna", "lastName": "Smith", "gender": "Female"},
        }
    }
    """

    # convert to json object
    json_dict = json.loads(emp_str)
    # iterate over list of office workers
    for emp in json_dict["employees"]["office_worker"]:
        del emp["gender"]
    # delete key for writer
    del json_dict["employees"]["writer"]["gender"]


    # convert to a string
    data_str = json.dumps(json_dict)
    print(data_str)


.. code-block:: 

    {"employees": {"office_worker": [{"firstName": "John", "lastName": "Doe"}, {"firstName": "Peter", "lastName": "Jones"}], 
    "writer": {"firstName": "Anna", "lastName": "Smith"}}}

----

Printing specific keys from json objects with indenting
--------------------------------------------------------------

| To print with indenting, in the code above, change the line ``data_str = json.dumps(json_dict)`` to ``data_str = json.dumps(json_dict, indent=4)``.
| The indented output is below.

.. code-block:: 

    {
        "employees": {
            "office_worker": [
                {
                    "firstName": "John",
                    "lastName": "Doe"
                },
                {
                    "firstName": "Peter",
                    "lastName": "Jones"
                }
            ],
            "writer": {
                "firstName": "Anna",
                "lastName": "Smith"
            }
        }
    }


----

Convert a dict to json
------------------------

| The cricket dictionary below, with just key value pairs, can be dumped to a json string, then loaded as json.

.. code-block:: python
    
    import json

    cricket_dict = {
            "player": "Sobers",
            "average": "57.8"
        }

    cricket_jsonstr = json.dumps(cricket_dict, indent=4)
    cricket_json = json.loads(cricket_jsonstr)
    print(f'{cricket_json["player"]} averaged {cricket_json["average"]}')

| Each value is accessed using keys. e.g. ``cricket_json["player"]`` returns "Sobers".

.. code-block:: 

    Sobers averaged 57.8

----

Convert a nested dict to json
------------------------------

| The sportsman dictionary below, with 4 sport nested dictionaries, can be dumped to a json string, then loaded as json.

.. code-block:: python
    
    import json

    spt_dict = {'cricket':{'player':'Sobers','average':'57.8 runs per innings'},
    'AFL':{'player':'Locket','average':'4.84 goals per game'},
    'soccer':{'player':'Pele','average':'0.92 goals per game'},
    'basketball':{'player':'Bryant','average':'25.0 points per game'}}

    spt_jsonstr = json.dumps(spt_dict, indent=4)
    spt_json = json.loads(spt_jsonstr)
    for sport in spt_json:
            print(f'{spt_json[sport]["player"]} averaged {spt_json[sport]["average"]}')

| Each value is accessed using nested keys. e.g. ``spt_json[sport]["player"]`` returns "Sobers" when sport is "cricket".

.. code-block:: 

    Sobers averaged 57.8 runs per innings
    Locket averaged 4.84 goals per game
    Pele averaged 0.92 goals per game
    Bryant averaged 25.0 points per game

----

Convert a nested dict to json file
-----------------------------------

| The dictionary below, with nested dictionaries, can be dumped to a json string, j_str, then loaded as json, j_json.
| The json, j_json, can then be dumped to a json file.

.. code-block:: python
    
    import json

    emp_dict = {
        "employees": {
            "office_worker": [
                {"firstName": "John", "lastName": "Doe", "gender": "Male"},
                {"firstName": "Peter", "lastName": "Jones", "gender": "Male"},
            ],
            "writer": {"firstName": "Anna", "lastName": "Smith", "gender": "Female"},
        }
    }

    j_str = json.dumps(emp_dict, indent=4)
    j_json = json.loads(j_str)

    json_path = "files/convert_dict_json.json"
    with open(json_path, 'w') as f:
        json.dump(j_json, f, indent=4)

| The contents of the json file are below.
| THe json string in the file looks just like the python dictionary.

.. code-block:: 

    {
        "employees": {
            "office_worker": [
                {
                    "firstName": "John",
                    "lastName": "Doe",
                    "gender": "Male"
                },
                {
                    "firstName": "Peter",
                    "lastName": "Jones",
                    "gender": "Male"
                }
            ],
            "writer": {
                "firstName": "Anna",
                "lastName": "Smith",
                "gender": "Female"
            }
        }
    }

----

.. admonition:: Tasks

    #. Write a definition to do the conversion from a python dictionary to a json file.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a definition to do the conversion from a python dictionary to a json file.

                .. code-block:: python

                    import json


                    def dict_to_json_file(py_dict, json_file_path):
                        j_str = json.dumps(py_dict, indent=4)
                        j_json = json.loads(j_str)
                        with open(json_file_path, 'w') as f:
                            json.dump(j_json, f, indent=4)
                        return None


                    emp_dict = {
                        "employees": {
                            "office_worker": [
                                {"firstName": "John", "lastName": "Doe", "gender": "Male"},
                                {"firstName": "Peter", "lastName": "Jones", "gender": "Male"},
                            ],
                            "writer": {"firstName": "Anna", "lastName": "Smith", "gender": "Female"},
                        }
                    }

                    json_path = "files/convert_dict_json.json"

                    dict_to_json_file(emp_dict, json_path)

----

Load
----------------------------

| Use the load function to load a file to json.
| The full syntax is at: https://docs.python.org/3/library/json.html#json.load
| Use the simple syntax:

.. py:function:: json.load(textfile)

    :param textfile: a textfile containing a JSON document

    | Returns a json object from a file.

----

Loading a json file
------------------------

| Download the test csv file :download:`afl_premiers_counts.json <files/afl_premiers_counts.json>`
| The code below loads the json file and prints it.

.. code-block:: python
    
    import json

    json_path = "files/afl_premiers_counts.json"
    with open(json_path, "r") as f:
        json_data = json.load(f)
        print(json_data)

.. code-block:: 

    {'premiers': [{'Index': '0', 'Club': 'Essendon', 'Years': '1897-present', 'Premierships Total': '16', 'Premierships Season(s)': '1897, 1901, 1911, 1912, 1923, 1924, 1942, 1946, 1949, 1950, 1962, 1965, 1984, 1985, 1993, 2000', 'Runners-up Total': '14', 'Runners-up Season(s)': '1898, 1902, 1908, 1941, 1943, 1947, 1948, 1951, 1957, 1959, 1968, 1983, 1990, 2001'},...]}

----

Printing specific keys
------------------------

| The code below loads the json file and prints specific keys.
| The main key to the json file is "premiers". 
| This could be obtained using ``j_key = list(json_data.keys())[0]``.
| The code below prints the names of clubs with 15 or more premierships (up to 2022)
| Note that the json values are strings and numbers as strings need to be converted to ints as in: ``if int(entry["Premierships Total"]) > 9:``

.. code-block:: python
    
    import json

    json_path = "files/afl_premiers_counts.json"
    with open(json_path, "r") as f:
        json_data = json.load(f)

        for entry in json_data["premiers"]:
            if int(entry["Premierships Total"]) >= 15:
                print(f'{entry["Club"]} {entry["Premierships Total"]}')

.. code-block:: 

    Essendon 16
    Carlton 16
    Collingwood 15

----

Dump
------------------

| Use the dump method to save a json object, including a dictionary, to a file.
| The full syntax is at: https://docs.python.org/3/library/json.html#json.dump
| Use the simple syntax:

.. py:function:: json.dump(json)

    :param json: a JSON object

    | Save a json object to a file

| Use the syntax below for pretty printing:

.. py:function:: json.dump(json, indent=4)

    :param json: a JSON object
    :param indent: the number of spaces to indent

    | Save a json object to a file using indenting.

----

dump json data to a file
--------------------------

| The code below does the same processing as a previous example, but dumps the json to a file.

.. code-block:: python
    
    import json

    emp_str = """
    {
        "employees": {
            "office_worker": [
                {"firstName": "John", "lastName": "Doe", "gender": "Male"},
                {"firstName": "Peter", "lastName": "Jones", "gender": "Male"}
            ],
            "writer": {"firstName": "Anna", "lastName": "Smith", "gender": "Female"}
        }
    }
    """

    # convert to json object
    json_dict = json.loads(emp_str)
    # iterate over list of office workers
    for emp in json_dict["employees"]["office_worker"]:
        del emp["gender"]
    # delete key for writer
    del json_dict["employees"]["writer"]["gender"]

    json_path = "files/employees_names.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(json_dict, f, indent=4)


| The file, employees2.json, contents are shown below.

.. code-block:: 

    {
        "employees": {
            "office_worker": [
                {
                    "firstName": "John",
                    "lastName": "Doe"
                },
                {
                    "firstName": "Peter",
                    "lastName": "Jones"
                }
            ],
            "writer": {
                "firstName": "Anna",
                "lastName": "Smith"
            }
        }
    }

----

dump json processed file data to a file
----------------------------------------

| The code below loads a json file, processes it and dumps the json to a file.
| ``data_list = []`` holds the dictionaries for each entry that meet the criteria: ``if int(entry["Premierships Total"]) >=13:``.
| ``keys_premiers = ["Club", "Premierships Total"]`` is used to store the dictionary keys that will be kept.
| ``entry_dict = {key: entry[key] for key in keys_premiers}`` builds the dictionary using just the chosen keys in the list: keys_premiers.
| ``data = {mainkey: data_list}`` makes the json data.

.. code-block:: python
    
    import json

    json_path = "files/afl_premiers_counts.json"
    json_path2 = "files/afl_premiers_top.json"
    
    data_list = []
    keys_to_keep = ["Club", "Premierships Total"]
    mainkey = "premiers"
    with open(json_path, encoding='utf-8') as f:
        json_data = json.load(f)
        # append data 
        for entry in json_data[mainkey]:
            if int(entry["Premierships Total"]) >=13:
                entry_dict = {key: entry[key] for key in keys_to_keep}
                data_list.append(entry_dict)

    data = {mainkey: data_list}      
    # Open a json writer, and use the json.dumps() function to dump data
    with open(json_path2, 'w', encoding='utf-8') as f2:
        json.dump(data, f2, indent=4)



| The file, afl_premiers_top.json, contents are shown below.

.. code-block:: 

    {
        "premiers": [
            {
                "Club": "Collingwood",
                "Premierships Total": "16"
            },
            {
                "Club": "Essendon",
                "Premierships Total": "16"
            },
            {
                "Club": "Carlton",
                "Premierships Total": "16"
            },
            {
                "Club": "Richmond",
                "Premierships Total": "13"
            },
            {
                "Club": "Hawthorn",
                "Premierships Total": "13"
            },
            {
                "Club": "Melbourne",
                "Premierships Total": "13"
            }
        ]
    }

