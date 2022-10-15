==========================
Convert an image
==========================

| See: https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.convert
| See: https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes

----

Convert to greyscale
----------------------

| Use the **convert(mode='L')** method to convert an image to greyscale.

.. code-block:: python

    from PIL import Image

    with Image.open("shapes/box.png") as im:
        new_im = im.convert(mode='L')
        new_im.save("shapes/box_grey.png")

----

Convert to black and white
----------------------------

| Use the **convert(mode='1')** method to convert an image to greyscale.

.. code-block:: python

    from PIL import Image

    with Image.open("shapes/box.png") as im:
        new_im = im.convert(mode='1')
        new_im.save("shapes/box_1.png")

----


Convert to black and white
----------------------------

| Use the **convert(mode='RGB')** method to convert an image to RGB with transparent regions converted to white.

.. code-block:: python

    from PIL import Image

    with Image.open("shapes/box.png") as im:
        new_im = im.convert(mode='RGB')
        new_im.save("shapes/box_RGB.png")

