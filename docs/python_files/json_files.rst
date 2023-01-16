==========================
Json files
==========================

| See: https://docs.python.org/3/library/json.html#module-json
| See: https://www.youtube.com/watch?v=9N6a-VLBa2I&list=RDCMUCCezIgC97PvUuR4_gbFUs5g&start_radio=1&rv=9N6a-VLBa2I&t=1

| json files are common when working with APIs and configuration files.
| json stands for Java Script Object Notation but is independent of programming languages.

----

Structure
---------------

| json looks like a dictionary.
| The key of "employees" has a value consisting of an array of 3 objects with keys: "firstName" and "lastName".

.. code:: 

    {"employees":[
    { "firstName":"John", "lastName":"Doe" },
    { "firstName":"Anna", "lastName":"Smith" },
    { "firstName":"Peter", "lastName":"Jones" }
    ]}


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
    {"employees":[
        { "firstName":"John", "lastName":"Doe" },
        { "firstName":"Anna", "lastName":"Smith" },
        { "firstName":"Peter", "lastName":"Jones" }
    ]}
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


----

Dumping json to a string
--------------------------

| The code below first deletes the firstName key from each employee, then converts the json object to a string and prints it.

.. code-block:: python
    
    import json

    emp_str = """
    {"employees":[
        { "firstName":"John", "lastName":"Doe" },
        { "firstName":"Anna", "lastName":"Smith" },
        { "firstName":"Peter", "lastName":"Jones" }
    ]}
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

    {"employees": [{"lastName": "Doe"}, {"lastName": "Smith"}, {"lastName": "Jones"}]}

----

from files

