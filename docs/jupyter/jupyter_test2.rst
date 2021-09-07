==========================
Jupyter Tests2
==========================

.. code-block:: python

    def name_age_greeting(name, age):
        age += 1
        return "Hi " + name + ", you are " + str(age) + " years old"

    print(name_age_greeting("Joe", 12))


----

.. code-block:: ipython

    def name_age_greeting(name, age):
        age += 1
        return "Hi " + name + ", you are " + str(age) + " years old"

    print(name_age_greeting("Joe", 12))

----

.. code-block:: ipython

    def name_age_greeting2(name="John", age=99):
        age += 1
        return "Hi " + name + ", you are " + str(age) + " years old"

    print(name_age_greeting2())

