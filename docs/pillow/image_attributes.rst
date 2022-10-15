==========================
Images attributes
==========================

| See: https://pillow.readthedocs.io/en/stable/reference/Image.html#image-attributes

| The code below shows how to open an image and print out some info about it.

.. code-block:: python

    from PIL import Image

    with Image.open("arrows/Narrow.png") as im:
        print(im.filename, im.format, im.mode, im.size, im.width, im.height)
        
| The filename is arrows/Narrow.png 
| The format is PNG
| The mode is RGBA
| The size is (500, 500)
| The width is 500
| The height is 500


PNG (500, 500) RGBA 
