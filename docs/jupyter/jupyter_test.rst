==========================
Jupyter Tests
==========================

.. thebe-button:: Activate Jupyter Thebelab

thebe-button
--------------------

```{thebe-button}
```
.. thebe-button::
    
----

class: thebe
--------------------

.. code-block:: python::
    :class: thebe

    def name_age_greeting(name, age):
        age += 1
        return "Hi " + name + ", you are " + str(age) + " years old"

    print(name_age_greeting("Joe", 12))


----

jupyter-execute
--------------------

.. jupyter-execute::

    def name_age_greeting2(name="John", age=99):
        age += 1
        return "Hi " + name + ", you are " + str(age) + " years old"

    print(name_age_greeting2())

----

.. math::

    ^{_{238}}_{_{92}}U \rightarrow \space ^{_{234}}_{_{90}}Th + \space ^{_{4}}_{_{2}}He


