==========================
file conversions
==========================

Convert a nested dict to json file
-----------------------------------

| The sportsman dictionary below, with 4 sport nested dictionaries, can be dumped to a json string, then loaded as json.

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

    j_str = json.dumps(py_dict, indent=2)
    j_json = json.loads(j_str)

    json_path = "files/convert_dict_json.json"
    with open(json_path, 'w') as f2:
        json.dump(j_json, f2, indent=4)

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

Convert a nested dict to json file
-----------------------------------

.. admonition:: Tasks

    #. Write a definition 

        .. code-block:: python



    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a **Battery** class to be assigned to a variable in the **ElectricCar** class.

                .. code-block:: python

                    py_dict = {
                        "cricket": {
                            "player": "Sobers",
                            "average": "57.8 runs per innings",
                        },
                        "AFL": {
                            "player": "Locket",
                            "average": "4.84 goals per game",
                        },
                        "soccer": {
                            "player": "Pele",
                            "average": "0.92 goals per game",
                        },
                        "basketball": {
                            "player": "Bryant",
                            "average": "25.0 points per game",
                        }
                    }

                    json_path = "files/convert_dict_json.json"

                    def dict_to_json_file(py_dict, json_file_path):
                        json_str = json.dumps(py_dict, indent=2)
                        json_f = json.loads(json_str)
                        with open(json_file_path, 'w') as f2:
                            json.dump(json_f, f2, indent=2)
                        return None

                    dict_to_json_file(py_dict, json_path)


