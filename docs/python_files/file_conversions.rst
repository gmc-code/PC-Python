==========================
file conversions
==========================

Convert a nested dict to json file
-----------------------------------

| The sportsman dictionary below, with sport nested dictionaries, can be dumped to a json string, j_str, then loaded as json, j_json.
| The json, j_json, can then be dumped to a json file.

.. code-block:: python
    
    import json

    sport_dict = {
        "cricket": {
            "player": "Sobers",
            "average": "57.8 runs per innings",
        },
        "AFL": {
            "player": "Locket",
            "average": "4.84 goals per game",
        }
    }

    j_str = json.dumps(sport_dict, indent=4)
    j_json = json.loads(j_str)

    json_path = "files/convert_dict_json.json"
    with open(json_path, 'w') as f:
        json.dump(j_json, f, indent=4)

| The contents of the json file are below.
| THe json string in the file looks just like the python dictionary.

.. code-block:: 

    {
        "cricket": {
            "player": "Sobers",
            "average": "57.8 runs per innings"
        },
        "AFL": {
            "player": "Locket",
            "average": "4.84 goals per game"
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

                    sport_dict = {
                        "cricket": {
                            "player": "Sobers",
                            "average": "57.8 runs per innings",
                        },
                        "AFL": {
                            "player": "Locket",
                            "average": "4.84 goals per game",
                        }
                    }

                    json_path = "files/convert_dict_json.json"

                    def dict_to_json_file(py_dict, json_file_path):
                        j_str = json.dumps(py_dict, indent=4)
                        j_json = json.loads(j_str)
                        with open(json_file_path, 'w') as f:
                            json.dump(j_json, f, indent=4)
                        return None

                    dict_to_json_file(sport_dict, json_path)

----

json to csv
-------------

| json is flexible in its structure.
| Each particular json file structure will have a different conversion to csv.
| The json stucture below is based on a simplified structure as ``{mainkey:[dictionaries]}``.
| The employees json follows that structrue.
| Each object in the array will become a row in csv.

.. code:: json

    {"employees":
    [{"firstName":"John","lastName":"Doe","gender":"Male"},
    {"firstName":"Anna","lastName":"Smith","gender":"Female"},
    {"firstName":"Peter","lastName":"Jones","gender":"Male"}]
    }

.. code:: CSV

    firstName	lastName	gender
    John	Doe	Male
    Anna	Smith	Female
    Peter	Jones	Male

.. code-block:: python

    import json
    import csv


    csv_path = "files/employees.csv"
    json_path = "files/employees.json"

    with open(json_path, "r") as f:
        json_data = json.load(f)

        j_key = list(json_data.keys())[0]
        fieldnames = list(json_data[j_key][0].keys())

        with open(csv_path, 'w', newline='') as new_file:
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
            csv_writer.writeheader()
            for row in json_data[j_key]:
                csv_writer.writerow(row)



csv to json
------------------

| See: https://pythonexamples.org/python-csv-to-json/
| The csv needs a header row.


----

xml to json
--------------

json to xml
--------------




