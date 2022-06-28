==========================
Jupyter Tests2
==========================

.. thebe-button:: Activate Jupyter Thebelab

----

.. jupyter-execute::
    :class: no-copybutton

    def name_age_greeting(name, age):
        age += 1
        return "Hi " + name + ", you are " + str(age) + " years old"

    print(name_age_greeting("Joe", 12))


----

.. jupyter-execute::
    :class: no-copybutton
    
    def name_age_greeting2(name="John", age=99):
        age += 1
        return "Hi " + name + ", you are " + str(age) + " years old"

    print(name_age_greeting2())
    


