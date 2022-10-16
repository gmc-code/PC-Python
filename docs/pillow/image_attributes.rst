==========================
Image attributes
==========================

| See: https://pillow.readthedocs.io/en/stable/reference/Image.html#image-attributes

| The code below shows how to open an image and print out some info about it.

.. code-block:: python

    from PIL import Image

    with Image.open("test_images/Test.png") as im:
        print(im.filename, im.format, im.mode, im.size, im.width, im.height, sep=";")

    with Image.open("test_images/Test.jpg") as im:
        print(im.filename, im.format, im.mode, im.size, im.width, im.height, sep=";")

| The first printout is: test_images/Test.png;PNG;RGBA;(620, 472);620;472
| The second printout is: test_images/Test.jpg;JPEG;RGB;(620, 472);620;472

