==========================
file conversions
==========================

Convert a nested dict to json file
-----------------------------------

| The sportsman dictionary below, with sport nested dictionaries, can be dumped to a json string, j_str, then loaded as json, j_json.
| The json, j_json, can then be dumped to a json file.

.. code-block:: python
    
    import json


    py_dict = {
        "cricket": {
            "player": "Sobers",
            "average": "57.8 runs per innings",
        },
        "AFL": {
            "player": "Locket",
            "average": "4.84 goals per game",
        }
    }

    j_str = json.dumps(py_dict, indent=4)
    j_json = json.loads(j_str)

    json_path = "files/convert_dict_json.json"
    with open(json_path, 'w') as f:
        json.dump(j_json, f, indent=4)

| The contents of the json file are below:

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

    #. Write a definition to do teh conversion from a python dictionary to a json file.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a definition to do teh conversion from a python dictionary to a json file.

                .. code-block:: python

                    py_dict = {
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

                    dict_to_json_file(py_dict, json_path)

----

csv to json
-------------

xml to json
--------------




