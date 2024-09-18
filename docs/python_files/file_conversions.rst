==========================
File conversions
==========================

| For json formatting and conversions see: https://jsonformatter.org/
| For xml formatting and conversion see: https://jsonformatter.org/xml-formatter

----

Files for csv ⇔ json
------------------------

| Download the csv file :download:`months.csv <files/months.csv>`
| Download the json file :download:`months.json <files/months.json>`

----

json file to csv file
-----------------------

| json is flexible in its structure.
| Each particular json file structure will have a different conversion to csv.
| The json stucture below is based on a simplified structure as ``{mainkey:[dictionaries]}``.
| The months json follows that structrue.
| Each object in the array will become a row in csv.

.. code:: json

    {"months":
    [{"Month":"January","Abbr":"Jan","Numeric":"1"},
    ...
    {"Month":"December","Abbr":"Dec","Numeric":"12"}]
    }

| csv file contents

.. code:: 

    Month,Abbr,Numeric
    January,Jan,1
    ...
    December,Dec,12


| Some parts of the code need some explanation:

| ``j_key = list(json_data.keys())[0]`` gets the key: "months".
| ``json_data.keys()`` return a dict object withe the key.
| ``list(json_data.keys())`` converts the dict object to a list.
| ``list(json_data.keys())[0]`` gives the key value "months" which will be needed to get the fieldnames for the csv DictWriter.

| ``fieldnames = list(json_data[j_key][0].keys())`` gets the fieldnames for the csv DictWriter, where j_key is "months".
| ``json_data[j_key]`` gives the array of dictionaries for each employee. These are listed below in the [].
| ``json_data[j_key][0]`` gives the first employee dictionary: {"firstName":"John","lastName":"Doe","gender":"Male"}.
| ``json_data[j_key][0].keys()`` gives a dict keys object.
| ``list(json_data[j_key][0].keys())`` converts the dict keys object into a list.

| The dictionary elements of the json array are iterated over by: ``for row in json_data[j_key]``, where j_key is "months".

.. code-block:: python

    import json
    import csv

    json_path = "files/months.json"
    csv_path = "files/months2.csv"

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


                    json_path = "files/months.json"
                    csv_path = "files/months.csv"

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


    csv_path = "files/months.csv"
    json_path = "files/months2.json"
    json_mainkey = "months"
    json_array = []
    with open(csv_path, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
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
                                json_array.append(row)

                        json_dict = {json_mainkey: json_array}
                        with open(json_file_path, 'w', encoding='utf-8') as jsonf:
                            json_str= json.dumps(json_dict, indent=4)
                            jsonf.write(json_str)


                    csv_path = "files/months.csv"
                    json_path = "files/months.json"
                    json_mainkey = "months"
                    csv_to_json_file(csv_path, json_path, json_mainkey)

----

Files for xml ⇔ json
------------------------

| Download the months csv file :download:`employees.xml <files/employees.xml>`
| Download the months json file :download:`employees.json <files/employees.json>`

----

Module for xml conversions
----------------------------

| ``pip install xmltodict`` from the terminal first so that file converions involving xml can be done.
| See: https://pypi.org/project/xmltodict/

----

xml file to json file
--------------------------

| The function ``xml_to_json_file(xml_file_path, json_file_path)`` takes a path to an xml file and a path to a json file.
| There are two conversion steps: convert an xml string to a dictionary via ``py_dict = xmltodict.parse(xml_str)``.
| Then from a dictionary to a json file via ``json.dump(py_dict, f, indent=4)``.

.. code-block:: python

    import json
    import xmltodict


    def xml_to_json_file(xml_file_path, json_file_path):
        with open(xml_file_path) as f:
            xml_str = f.read()
        py_dict = xmltodict.parse(xml_str)
        with open(json_file_path, 'w') as f:
            json.dump(py_dict, f, indent=4)


    xml_file_path = "files/employees.xml"
    json_file_path = "files/convert_xml_to_json.json"

    xml_to_json_file(xml_file_path, json_file_path)

----

json file to xml file
-----------------------

| xmltodict needs to construct the JSON with the very first key as the root XML tag. 
| This means that there should only be a single JSON key at the root level of data.

| The function ``json_to_xml_file(json_file_path, xml_file_path)`` takes a path to a json file and a path to an xml file.
| The line ``xml_str = xmltodict.unparse(json_data, pretty=True)`` converts the json as a dictionary to an xml string.

.. code-block:: python

    import json
    import xmltodict

    def json_to_xml_file(json_file_path, xml_file_path):
        with open(json_file_path, "r") as f:
            json_dict = json.load(f)
            xml_str = xmltodict.unparse(json_dict, pretty=True)
        with open(xml_file_path, "w") as f2:
            f2.write(xml_str)


    json_file_path = "files/employees.json"
    xml_file_path = "files/convert_json_to_xml.xml"

    json_to_xml_file(json_file_path, xml_file_path)



