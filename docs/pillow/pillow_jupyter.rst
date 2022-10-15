==========================
Pillow Jupyter
==========================

.. thebe-button:: Activate Jupyter

----

class: thebe
--------------------

.. code-block:: python
    :class: thebe

    import IPython
    url = 'https://pc-python.readthedocs.io/en/latest/_images/Narrow.png'
    IPython.display.Image(url, width = 250)

----

.. code-block:: python
    :class: thebe

    from PIL import Image
    Image.open("images/arrows/Narrow.png")

----
.. code-block:: python
    :class: thebe
    
    from PIL import Image
    from urllib.request import urlopen

    url = "https://pc-python.readthedocs.io/en/latest/_images/Narrow.png"

    Image.open(urlopen(url))
    

----

.. image:: images/arrows/Narrow.png
    :scale: 50%



