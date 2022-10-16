==========================
New image
==========================

| See: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.new

----

Blank new png
----------------

| The code below saves an blank png of size (256, 256).

.. code-block:: python

    from PIL import Image

    new_im = Image.new("RGBA", (256, 256))
    new_im.save("new_images/blank.png")

----

White new png
----------------

| The code below saves a white png of size (256, 256).

.. code-block:: python

    from PIL import Image

    new_im = Image.new("RGBA", (256, 256), (255, 255, 255))
    new_im.save("new_images/white.png")


.. image:: images/white.png
    :scale: 50%
    :align: center

----

Coloured new png
------------------

| The code below saves a light blue png of size (256, 256).

.. code-block:: python

    from PIL import Image

    new_im = Image.new("RGBA", (256, 256), (204, 229, 255))
    new_im.save("new_images/light_blue.png")


.. image:: images/light_blue.png
    :scale: 50%
    :align: center

----

Coloured new jpg
------------------

| The code below saves a green png of size (128, 128).

.. code-block:: python

    from PIL import Image

    new_im = Image.new("RGB", (128, 128), (0, 255, 0))
    new_im.save("new_images/green.jpg")


.. image:: images/green.jpg
    :scale: 50%
    :align: center


