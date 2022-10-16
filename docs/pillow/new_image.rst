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


White new png
----------------

| The code below saves a white png of size (256, 256).

.. code-block:: python

    from PIL import Image

    new_im = Image.new("RGBA", (256, 256), (255, 255, 255))
    new_im.save("new_images/white.png")

