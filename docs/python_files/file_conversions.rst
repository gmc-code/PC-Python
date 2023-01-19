==========================
File conversions
==========================

| For json formatting and conversions see: https://jsonformatter.org/
| For xml formatting and conversion see: https://jsonformatter.org/xml-formatter

----

json file to csv file
-----------------------

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


| csv file contents

.. code:: 

    firstName,lastName,gender
    John,Doe,Male
    Anna,Smith,Female
    Peter,Jones,Male


| Some parts of the code need some explanation:

| ``j_key = list(json_data.keys())[0]`` gets the key: "employees".
| ``json_data.keys()`` return a dict object withe the key.
| ``list(json_data.keys())`` converts the dict object to a list.
| ``list(json_data.keys())[0]`` gives the key value "employees" which will be needed to get the fieldnames for the csv DictWriter.

| ``fieldnames = list(json_data[j_key][0].keys())`` gets the fieldnames for the csv DictWriter, where j_key is "employees".
| ``json_data[j_key]`` gives the array of dictionaries for each employee. These are listed below in the [].
| ``json_data[j_key][0]`` gives the first employee dictionary: {"firstName":"John","lastName":"Doe","gender":"Male"}.
| ``json_data[j_key][0].keys()`` gives a dict keys object.
| ``list(json_data[j_key][0].keys())`` converts the dict keys object into a list.

| The dictionary elements of the json array are iterated over by: ``for row in json_data[j_key]``, where j_key is "employees".

.. code-block:: python

    import json
    import csv

    json_path = "files/employees.json"
    csv_path = "files/employees.csv"

    with open(json_path, "r") as f:
        json_data = json.load(f)

        j_key = list(json_data.keys())[0]
        fieldnames = list(json_data[j_key][0].keys())

        with open(csv_path, 'w', newline='') as new_file:
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for row in json_data[j_key]:
                csv_writer.writerow(row)


----


.. admonition:: Tasks

    #. Write a definition to do the conversion from a json file to a csv file.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a definition to do the conversion from a json file to a csv file.

                .. code-block:: python

                    import json
                    import csv


                    def json_to_csv_file(json_file_path, csv_file_path):
                        with open(json_file_path, "r") as f:
                            json_data = json.load(f)

                            j_key = list(json_data.keys())[0]
                            fieldnames = list(json_data[j_key][0].keys())

                            with open(csv_file_path, "w", newline="") as new_file:
                                csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
                                csv_writer.writeheader()
                                for row in json_data[j_key]:
                                    csv_writer.writerow(row)


                    json_path = "files/employees.json"
                    csv_path = "files/employees.csv"

                    json_to_csv_file(json_path, csv_path)


----

csv file to json file
---------------------------

| See: https://pythonexamples.org/python-csv-to-json/
| The csv needs a header row.
| The json will take the form of a python dictionary: ``json_dict = {json_mainkey: json_array}``
| The csv.DictReader will be used to append each row of the csv to an array, ``json_array``.


.. code-block:: python

    import csv
    import json


    csv_path = "files/employees.csv"
    json_path = "files/employees3.json"
    json_mainkey = "employees"
    json_array = []
    with open(csv_path, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row)
            json_array.append(row)

    json_dict = {json_mainkey: json_array}
    with open(json_path, 'w', encoding='utf-8') as jsonf:
        json_str= json.dumps(json_dict, indent=4)
        jsonf.write(json_str)

----


.. admonition:: Tasks

    #. Write a definition to do the conversion from a csv file to a json file.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a definition to do the conversion from a csv file to a json file.

                .. code-block:: python

                    import csv
                    import json


                    def csv_to_json_file(csv_file_path, json_file_path, json_mainkey):
                        json_array = []
                        with open(csv_file_path, 'r', newline='') as csv_file:
                            csv_reader = csv.DictReader(csv_file)
                            for row in csv_reader:
                                print(row)
                                json_array.append(row)

                        json_dict = {json_mainkey: json_array}
                        with open(json_file_path, 'w', encoding='utf-8') as jsonf:
                            json_str= json.dumps(json_dict, indent=4)
                            jsonf.write(json_str)


                    csv_path = "files/employees.csv"
                    json_path = "files/employees.json"
                    json_mainkey = "employees"
                    csv_to_json_file(csv_path, json_path, json_mainkey)

----

xml file to dict
-----------------

| ``pip install xmltodict`` from the terminal first.

| The function ``xml_to_dict(xml_file_path)`` takes a path to an xml file and returns a python dictionary.


.. code-block:: python

    # pip install xmltodict

    import json
    import xmltodict


    def xml_to_dict(xml_file_path):
        with open(xml_file_path) as f:
            xml_str = f.read()
            py_dict = xmltodict.parse(xml_str)
        return py_dict


    xml_file_path = "files/employees.xml"

    py_dict = xml_to_dict(xml_file_path)
    print(py_dict)

----

xml file to json file
--------------------------

| ``pip install xmltodict`` from the terminal first.

| The function ``xml_to_dict(xml_file_path)`` takes a path to an xml file and returns a python dictionary.
| The function ``dict_to_json_file(py_dict, json_file_path)`` takes a dictionary and a path to the json file.
| There are two conversion steps: convert xml to a dictionary then from a dictionary to json.

.. code-block:: python

    import json
    import xmltodict


    def xml_to_dict(xml_file_path):
        with open(xml_file_path) as f:
            xml_str = f.read()
            py_dict = xmltodict.parse(xml_str)
        return py_dict


    def dict_to_json_file(py_dict, json_file_path):
        j_str = json.dumps(py_dict, indent=4)
        j_json = json.loads(j_str)
        with open(json_file_path, 'w') as f:
            json.dump(j_json, f, indent=4)
        return None


    xml_file_path = "files/employees.xml"
    json_file_path = "files/convert_xml_json.json"

    py_dict = xml_to_dict(xml_file_path)
    dict_to_json_file(py_dict, json_file_path)

----

json to xml
--------------

| For  complex xml, install and use dicttoxml2. 
| See: https://pypi.org/project/dicttoxml2/#description
| See: https://dicttoxml.readthedocs.io/en/latest/user/getstarted.html

