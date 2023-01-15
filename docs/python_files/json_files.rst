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

The full syntax is at: https://docs.python.org/3/library/json.html#json.loads

.. py:function:: json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)

Use the simple syntax:

.. py:function:: json.loads(string)

    :param string: a string containing a JSON document

    | Deserialize str**ing to a Python object


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

    data = json.loads(emp_str)
    for emp in data["employees"]:
        print(emp["firstName"],emp["lastName"])

.. code-block:: 

    John Doe
    Anna Smith
    Peter Jones

----

Dumping a json string
------------------------

| The code below 