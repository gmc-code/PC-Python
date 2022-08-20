==========================
Jupyter Tests2
==========================

.. thebe-button:: Activate Jupyter Thebelab

.. code-block:: python

    def name_age_greeting1(name="John", age=99):
        age += 1
        return "Hi " + name + ", you are " + str(age) + " years old"

    print(name_age_greeting1())
    
.. jupyter-execute::

    def name_age_greeting2(name, age):
        age += 1
        return "Hi " + name + ", you are " + str(age) + " years old"

    print(name_age_greeting2("Joe", 12))

.. jupyter-execute::

    def name_age_greeting3(name="John", age=99):
        age += 1
        return "Hi " + name + ", you are " + str(age) + " years old"

    print(name_age_greeting3())
    


.. code-block:: python

    def name_age_greeting4(name="John", age=99):
        age += 1
        return "Hi " + name + ", you are " + str(age) + " years old"

    print(name_age_greeting4())
    