==========================
Json files
==========================

| See: https://docs.python.org/3/library/json.html#module-json
| See: https://www.youtube.com/watch?v=9N6a-VLBa2I&list=RDCMUCCezIgC97PvUuR4_gbFUs5g&start_radio=1&rv=9N6a-VLBa2I&t=1

| json files are common when working with APIs and configuration files.
| json stands for Java Script Object Notation but is independent of programming languages.

| To minify json online see: https://onlinejsontools.com/minify-json
| To produce pretty json see: https://onlinejsontools.com/prettify-json

----

Structure
---------------

| json looks like a dictionary.
| The key of "employees" has a value consisting of an array of 3 objects with keys: "firstName" and "lastName".

.. code:: 

    {"employees":
    [{"firstName":"John","lastName":"Doe","gender":"Male"},
    {"firstName":"Anna","lastName":"Smith","gender":"Female"},
    {"firstName":"Peter","lastName":"Jones","gender":"Male"}]
    }

----

loads method
------------------

| Use the loads method to convert a string to json.
| The full syntax is at: https://docs.python.org/3/library/json.html#json.loads
| Use the simple syntax:

.. py:function:: json.loads(string)

    :param string: a string containing a JSON document

    | Returns a a json object from a string

----

Loading a json string
------------------------

| The code below loads the json string, iterates through the list of employees and prints the name of each employee.


.. code-block:: python
    
    import json

    emp_str = """
    {"employees":
    [{"firstName":"John","lastName":"Doe","gender":"Male"},
    {"firstName":"Anna","lastName":"Smith","gender":"Female"},
    {"firstName":"Peter","lastName":"Jones","gender":"Male"}]
    }
    """

    data_json = json.loads(emp_str)
    for emp in data_json["employees"]:
        print(emp["firstName"],emp["lastName"])

.. code-block:: 

    John Doe
    Anna Smith
    Peter Jones

----

dumps method
------------------

| Use the dumps method to a json object to a sting.
| The full syntax is at: https://docs.python.org/3/library/json.html#json.dumps
| Use the simple syntax:

.. py:function:: json.dumps(json)

    :param json: a JSON object

    | Returns a string from a json object

| Use the syntax below for pretty printing:

.. py:function:: json.dumps(json, indent=2, sort_keys=True)

    :param json: a JSON object
    :param indent: teh number of spaces to indent
    :param sort_keys: set to True to sort the keys alphabetically

    | Returns a string from a json object 


----

Dumping json to a string
-----------------------------------------------

| The code below deletes the gender key then converts the json to a string, then prints it.

.. code-block:: python
    
    import json

    emp_str = """
    {"employees":
    [{"firstName":"John","lastName":"Doe","gender":"Male"},
    {"firstName":"Anna","lastName":"Smith","gender":"Female"},
    {"firstName":"Peter","lastName":"Jones","gender":"Male"}]
    }
    """

    # convert to json object
    data_json = json.loads(emp_str)
    # delete each firstname
    for emp in data_json["employees"]:
        del emp["firstName"]

    # convert to a string
    data_str = json.dumps(data_json)
    print(data_str)


.. code-block:: 

    {"employees": [{"firstName": "John", "lastName": "Doe"}, {"firstName": "Anna", "lastName": "Smith"}, {"firstName": "Peter", "lastName": "Jones"}]}

----

Dumping json to a string with pretty printing
-----------------------------------------------

| The code below does pretty printing via: ``data_str = json.dumps(data_json, indent=2, sort_keys=True)``

.. code-block:: python
    
    import json

    emp_str = """
    {"employees":
    [{"firstName":"John","lastName":"Doe","gender":"Male"},
    {"firstName":"Anna","lastName":"Smith","gender":"Female"},
    {"firstName":"Peter","lastName":"Jones","gender":"Male"}]
    }
    """

    # convert to json object
    data_json = json.loads(emp_str)
    # delete each firstname
    for emp in data_json["employees"]:
        del emp["firstName"]

    # convert to a string
    data_str = json.dumps(data_json, indent=2, sort_keys=True)
    print(data_str)


.. code-block:: 

    {
    "employees": [
        {
        "firstName": "John",
        "lastName": "Doe"
        },
        {
        "firstName": "Anna",
        "lastName": "Smith"
        },
        {
        "firstName": "Peter",
        "lastName": "Jones"
        }
    ]
    }

----

from files

