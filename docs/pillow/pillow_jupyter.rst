==========================
Jupyter Test
==========================

.. thebe-button:: Activate Jupyter

----

class: thebe
--------------------

.. code-block:: python
    :class: thebe

    from PIL import Image
    Image.open("images/arrows/Narrow.png")
    
    with Image.open("images/arrows/Narrow.png") as im:
        im.show()

----

.. image:: images/arrows/Narrow.png
    :scale: 100%



